# Which local store for the CMP app (content cache + progress outbox)?

## Question

The app posture is fixed as **cache-on-read with queued-sync** (ticket #191): every opened concept is stored locally (concept detail + list-row metadata), and progress writes queue to an append-only outbox that is flushed to the idempotent `PUT /concepts/{id}/progress` when connectivity returns. Pick the cross-platform local store for the `shared` module of a Compose Multiplatform app (Android + iOS), choosing between **SQLDelight** (native SQL, Kotlin Multiplatform, typed queries, transactions) and the alternatives (**Realm/Kotlin Multiplatform**, **file-based serialized blobs**, and — for completeness — **Room KMP**). This research reports facts only; the decision falls out in the follow-up grilling ticket.

## Context (fixed constraints)

- CMP app scaffold (`prototype/cmp-app-scaffold`): single Kotlin module `app/shared` using the `com.android.kotlin.multiplatform.library` plugin (AGP 9.1.0), targets `iosArm64()` + `iosSimulatorArm64()` (static framework, direct integration) plus Android (minSdk 24, compileSdk 37). Kotlin 2.4.10, Compose Multiplatform 1.11.1, AGP 9.x, Gradle 9.1.0. Deps already present: Ktor client 3.5.2 (OkHttp/Darwin), kotlinx-serialization-json 1.11.0, kotlinx-coroutines-core 1.11.0, lifecycle-viewmodel 2.11.0 (see `app/build-logic/src/main/kotlin/kb.shared.gradle.kts`).
- API seam (#129): `ConceptRepository` interface over `KbApi`. Operations: `domains()`, `concepts(...)`, `concept(id)` (returns `ConceptDetail` with markdown `body`), `search(...)`, `writeProgress(id, ProgressWrite)`. DTOs are `@Serializable` kotlinx-serialization classes (`Dtos.kt`).
- Offline posture (#191 resolution): cache-on-read — detail + list-row metadata persisted on open; offline Browse prunes the tree to cached entries; offline Search is a **title scan over cached concepts (no local FTS)**; progress outbox flushed to the idempotent PUT; freshness = fresh-on-open re-fetch when `body_updated_at` changed. **The progress + cache update is one atomic unit** (an outbox write must never partially persist).
- Corpus: a few hundred small cached rows at most; an append-only outbox. (The canonical server DB holds ~307 concepts per `docs/research/database-choice.md`; the repo's `concepts/` tree holds 786 `.md` files, ~3.1 MB, but only *opened* concepts land in the cache.)
- Repo convention: prefer native framework utilities over new third-party packages; a store is the deliberate, ticket-sanctioned exception. Design rules in `docs/agents/design-rules.md`.

## Sources

### SQLDelight

- [SQLDelight releases (GitHub)](https://github.com/sqldelight/sqldelight/releases) — 2.3.2 (2026-03-16, latest), 2.2.1 (2025-11-13), 2.1.0 (2025-05-16); 2.3.2 notes: "Full compatibility with Android Gradle Plugin 9.0's new DSL (#6140)", "Fix compatibility with Android Gradle Plugin's built-in Kotlin (#6139)", "Android Driver: increase Android minSdk to 23", runtime `SuspendingTransacter.TransactionDispatcher`.
- [SQLDelight docs — Overview (2.1.0)](https://sqldelight.github.io/sqldelight/2.1.0/) — supported dialects/platforms matrix (SQLite: Android, Native (iOS/macOS/Linux/Windows), JVM, JS, "Multiplatform").
- [SQLDelight docs — Getting Started, SQLite Multiplatform](https://sqldelight.github.io/sqldelight/2.1.0/multiplatform_sqlite/) — Gradle plugin, `.sq` files under `src/main/sqldelight`, `Database`/`Schema` generation, per-platform driver coordinates (`android-driver`, `native-driver`, `sqlite-driver`).
- [SQLDelight docs — Getting Started, Kotlin/Native](https://sqldelight.github.io/sqldelight/2.1.0/native_sqlite/) — "Since SQLDelight 2.0, the Native driver only supports Kotlin/Native's new memory manager"; reader connection pools (`maxReaderConnections`).
- [SQLDelight docs — Transactions](https://sqldelight.github.io/sqldelight/2.1.0/multiplatform_sqlite/transactions/) — `transaction {}`, `transactionWithResult {}`, rollback, afterCommit/afterRollback callbacks.
- [SQLDelight docs — Migrations](https://sqldelight.github.io/sqldelight/2.1.0/multiplatform_sqlite/migrations/) — `.sqm` files, `verifySqlDelightMigration`, schema `.db` export, code migrations via `Schema.migrate(..., AfterVersion)`.
- [SQLDelight docs — Gradle](https://sqldelight.github.io/sqldelight/2.1.0/multiplatform_sqlite/gradle/) — `linkSqlite` property ("for a static framework, this flag has no effect. The XCode build ... should add `-lsqlite3` to the linker flags"), dialects, `generateAsync`, `deriveSchemaFromMigrations`.
- [SQLDelight 2.x API — Transacter](https://sqldelight.github.io/sqldelight/2.1.0/2.x/runtime/app.cash.sqldelight/-transacter/index.html) — blocking `transaction`/`transactionWithResult`; `SuspendingTransacter` suspend variants (same package).
- [SQLDelight 2.x API — native-driver / NativeSqliteDriver](https://sqldelight.github.io/sqldelight/2.1.0/2.x/drivers/native-driver/app.cash.sqldelight.driver.native/-native-sqlite-driver/index.html) — constructor takes a `DatabaseManager`/`DatabaseConfiguration` (from SQLiter) or `(schema, name)`; reader pool + transaction pool, default 1 connection each; thread-aligned transactions ("you cannot operate on a single transaction from multiple threads"); `wrapConnection` for SQLiter connections.
- [SQLDelight 2.x API — android-driver / AndroidSqliteDriver](https://sqldelight.github.io/sqldelight/2.1.0/2.x/drivers/android-driver/app.cash.sqldelight.driver.android/-android-sqlite-driver/index.html) — `(schema, context, name, factory, callback, cacheSize, useNoBackupDirectory, windowSizeBytes)` over `androidx.sqlite.db.SupportSQLiteOpenHelper`.
- [SQLDelight 2.x API — coroutines-extensions](https://sqldelight.github.io/sqldelight/2.1.0/2.x/extensions/coroutines-extensions/app.cash.sqldelight.coroutines/index.html) — only Flow mapping functions (`asFlow`, `mapToList`, `mapToOne`, ...) in 2.x; the 1.x `transactionWithContext` coroutine-transaction API is **gone** in 2.x.
- [PR #6140 — Enable lazy configuration of SQLDelight tasks](https://github.com/sqldelight/sqldelight/pull/6140) — "Make AGP configuration lazy using `onVariants`, and enable newDsl flag in tests"; closes #5989 "Migrate from old DSL variant API to new DSL variant API". Follow-up comment thread documents AGP 8.9–8.11 generated-source-wiring bugs and that "AGP 9.0 (built-in Kotlin) makes `variant.sources.kotlin` the canonical path".
- [Issue #6078 — KotlinSourceSet with name 'main' not found with AGP9](https://github.com/sqldelight/sqldelight/issues/6078) — SQLDelight 2.2.1 failed on AGP 9 (new DSL / built-in Kotlin); fixed in the 2.3.x line.
- [Issue #6270 — target generated code for a Kotlin language version](https://github.com/sqldelight/sqldelight/issues/6270) — open request from a user on Kotlin 2.4 (functional, asking for a codegen nicety).
- [SQLDelight 2.3.2 `gradle/libs.versions.toml`](https://raw.githubusercontent.com/sqldelight/sqldelight/2.3.2/gradle/libs.versions.toml) — built against Kotlin **2.3.10**, AGP **9.1.0**, SQLiter **1.3.3**, `androidx.sqlite` **2.6.2**, minSdk 23; `sqliter = co.touchlab:sqliter-driver`, `stately-concurrency 2.1.0`.
- [SQLDelight 2.3.2 `drivers/native-driver/build.gradle`](https://raw.githubusercontent.com/sqldelight/sqldelight/2.3.2/drivers/native-driver/build.gradle) — native-driver target list includes `iosArm64()`, `iosSimulatorArm64()` (and macos/linux/watchos/tvos/mingw); commonMain deps: runtime + `stately-concurrency` + `sqliter`.
- [SQLDelight 2.3.2 `drivers/android-driver/build.gradle`](https://raw.githubusercontent.com/sqldelight/sqldelight/2.3.2/drivers/android-driver/build.gradle) — Android driver depends on `androidx.sqlite:sqlite` (api) + `androidx.sqlite:sqlite-framework`.
- [SQLiter (Touchlab)](https://github.com/touchlab/SQLiter) — "Minimal sqlite for Kotlin multiplatform"; "SQLiter powers the SQLDelight library on native clients"; coordinates `co.touchlab:sqliter-driver`.
- [Maven Central metadata: `app.cash.sqldelight:runtime`](https://repo1.maven.org/maven2/app/cash/sqldelight/runtime/maven-metadata.xml) — latest release 2.3.2.

### Realm / Atlas Device SDK

- [MongoDB docs — Atlas Device SDKs Deprecation](https://www.mongodb.com/docs/atlas/device-sdks/deprecation/) — "As of September 2024, Atlas Device SDKs are deprecated. Atlas Device SDKs will reach end-of-life and be removed on **September 30, 2025**." On-device database "will continue to exist as an open source project"; Device Sync and the sync wire protocol are deprecated and removed; community branches exist per SDK.
- [MongoDB docs — Atlas Device SDK landing](https://www.mongodb.com/docs/atlas/device-sdks/) — "Atlas Device SDKs are deprecated."
- [realm/realm-kotlin README](https://github.com/realm/realm-kotlin) — banner: "We announced the deprecation of Atlas Device Sync + Realm SDKs in September 2024... For a version of Realm Kotlin without sync features, install version `3.0.0+` or see the `community` git branch." Also: the 2.3.0 compatibility matrix (Kotlin 2.0.20+, Gradle 7.2–8.5, new memory model only).
- [realm/realm-kotlin CHANGELOG](https://raw.githubusercontent.com/realm/realm-kotlin/master/CHANGELOG.md) — 3.0.0 (post-deprecation, no-sync line): "compatible with Kotlin 2.0.20 and above", "Minimum Gradle version: 7.2", "Minimum Android Gradle Plugin version: 7.1.3"; file format v24. Repo `pushed_at` 2025-10-31 (last activity).
- [Maven Central: `io.realm.kotlin:library-base`](https://repo1.maven.org/maven2/io/realm/kotlin/library-base/maven-metadata.xml) — latest release 3.0.0.

### File-based serialized blobs

- [Okio (GitHub)](https://github.com/lysine-dev/okio) — "A modern I/O library for Android, Java, and Kotlin Multiplatform"; multiplatform `okio.FileSystem` (commonMain API; `okio.FileSystem.SYSTEM`).
- [Okio FileSystem.kt (source)](https://github.com/lysine-dev/okio/blob/main/okio/src/commonMain/kotlin/okio/FileSystem.kt) — `abstract fun atomicMove(source: Path, target: Path)`, `createDirectories`, `list`, etc.
- [Maven Central: `com.squareup.okio:okio`](https://repo1.maven.org/maven2/com/squareup/okio/okio/maven-metadata.xml) — latest 3.18.1; [3.18.1 Gradle module metadata](https://repo1.maven.org/maven2/com/squareup/okio/okio/3.18.1/okio-3.18.1.module) confirms `iosArm64` and `iosSimulatorArm64` variants.
- kotlinx-serialization-json 1.11.0 is already a scaffold dependency (`kb.shared.gradle.kts`); kotlinx-serialization supports Kotlin/Native iOS targets.
- [SQLite docs — Appropriate Uses For SQLite](https://www.sqlite.org/whentouse.html) (context for what file-level atomicity does/does not buy; single-writer, ACID is engine-level, not cross-file).

### Room (AndroidX)

- [Room release notes (Android Developers)](https://developer.android.com/jetpack/androidx/releases/room) — "Version 2.7.0 April 9, 2025: Room has been refactored to become a Kotlin Multiplatform (KMP) library. Current supported platforms are Android, iOS, JVM (Desktop), native Mac and native Linux." 2.8.0 (2025-09-10) adds `room-sqlite-wrapper`; requires KSP (KSP2 recommended on Kotlin 2.0+).
- [Set up Room database for KMP (Android Developers)](https://developer.android.com/kotlin/multiplatform/room) — current docs (Room **3.0.1**, `androidx.room3:room3-runtime`): Room Gradle plugin (`androidx.room3`) + KSP per-target configs (`kspAndroid`, `kspIosArm64`, `kspIosSimulatorArm64`, ...) + `androidx.sqlite:sqlite-bundled`; iOS framework requires `-lsqlite3` linker opt.
- [Google Maven group index `androidx.room3`](https://dl.google.com/dl/android/maven2/androidx/room3/group-index.xml) — artifacts confirm KMP structure: `room3-common-iosarm64`, `room3-common-iossimulatorarm64`, `room3-runtime-android`, `room3-migration-*`, `room3-testing-*`, etc.
- [Android-KMP plugin docs (com.android.kotlin.multiplatform.library)](https://developer.android.com/kotlin/multiplatform/plugin) — the new plugin is "the officially supported tool for adding an Android target to a Kotlin Multiplatform (KMP) library module"; old `com.android.library`-based KMP is deprecated in AGP 9.0 (Q4 2025) and targeted for removal in AGP 10.0 (H2 2026).
- [KSP issue #2476 — Support `com.android.kotlin.multiplatform.library`](https://github.com/google/ksp/issues/2476) — open (created 2025-05-29); KSP did not support the new Android-KMP plugin; comments (Dec 2025) report working setups with KSP 2.3.4 + Kotlin 2.3.0 + AGP 9.0-rc01 and lingering gaps (`kspCommonMainMetadata` unavailable).
- [KSP releases](https://github.com/google/ksp/releases) — 2.3.10 (2026-08-03), 2.3.10 fixes include "Fix R-class resolution in KSP when AGP 9 built-in Kotlin is enabled".

### AndroidX SQLite KMP (low-level binding)

- [SQLite release notes (Android Developers)](https://developer.android.com/jetpack/androidx/releases/sqlite) — "Version 2.5.0 April 9, 2025: Kotlin Multi-Platform (KMP) Support... `androidx.sqlite:sqlite-framework` offers implementation of the interfaces for Android and iOS natively, while `androidx.sqlite:sqlite-bundled` offers an implementation that uses SQLite compiled from source." 2.6.0 (2025-09-10) adds watchOS/tvOS KMP targets and raises minSdk to 23.

## Findings

### 1. SQLDelight

#### 1.1 Versions, platforms, Kotlin/Native support

- Latest stable is **2.3.2** (2026-03-16; 2.3.0/2.3.1 were skipped for publication issues) — confirmed on Maven Central (`app.cash.sqldelight:runtime` latest = 2.3.2) and the GitHub releases page.
- SQLDelight 2.x is a Kotlin Multiplatform library with a per-platform driver per target: `android-driver` (Android JVM), `native-driver` (iOS/macOS/Linux/Windows/watchOS/tvOS Kotlin/Native), `sqlite-driver`/`jdbc-driver` (JVM), web-worker driver (JS/Wasm). The docs' platform matrix lists SQLite on **Android, Native (iOS, macOS, Linux, Windows), JVM, JS, and "Multiplatform"**.
- The native-driver's declared targets at 2.3.2 include **`iosArm64()` and `iosSimulatorArm64()`** (both of the scaffold's iOS targets) — verified in the driver's `build.gradle`.
- Since SQLDelight 2.0 the native driver supports **only Kotlin/Native's new memory manager** — which is the only memory manager in Kotlin 2.4.x, so this is satisfied automatically.
- The 2.1.0 docs pages are the current doc set; the GitHub releases page shows 2.3.2 as the latest tag. The 2.3.2 build is compiled against **Kotlin 2.3.10** and **AGP 9.1.0**; the scaffold uses Kotlin 2.4.10 / AGP 9.1.0. Kotlin klibs are consumable by newer compilers (library built with an older Kotlin works in a newer toolchain), and the open issue #6270 records a user running SQLDelight on Kotlin 2.4 without a compat complaint (the request is a codegen annotation nicety, not a break).

#### 1.2 Driver stack: what sits under the native and Android drivers

- The native-driver in 2.x is **built on SQLiter** (`co.touchlab:sqliter-driver` 1.3.3, plus `stately-concurrency`): "SQLiter powers the SQLDelight library on native clients." The `NativeSqliteDriver` constructor at 2.1.0+ takes `(DatabaseConfiguration | DatabaseManager | (schema, name), maxReaderConnections = 1)`, with a `wrapConnection` helper for SQLiter's `DatabaseConnection`.
- The `NativeSqliteDriver` maintains **two connection pools: a reader pool and a transaction pool, each defaulting to 1 connection**; `maxReaderConnections` raises the reader pool. All writes and everything inside a transaction uses the single transaction-pool connection.
- **Threading/alignment caveat (this is the modern form of the old "single connection / backgroundDispatcher" guidance):** "Aligning a transaction to a thread means you cannot operate on a single transaction from multiple threads"; the docs recommend keeping transactions inside the `transaction {}` lambda scope. On iOS there is no thread pooling in native coroutines today, so this is a discipline constraint, not a platform blocker. The 1.x-era `backgroundDispatcher` parameter no longer exists; it was replaced by the SQLiter-backed configuration and the reader/transaction pools.
- The Android driver wraps Android's `SupportSQLiteOpenHelper` (`androidx.sqlite.db`), i.e. the platform SQLite; 2.3.x bumps its minSdk to 23 (scaffold minSdk is 24, so fine). Its `build.gradle` lists `androidx.sqlite:sqlite` (KMP API) and `androidx.sqlite:sqlite-framework` as dependencies.
- **Static-framework integration note for this scaffold:** the `linkSqlite` Gradle property only affects dynamic frameworks. Because the scaffold builds a **static** framework (`isStatic = true`), the iOS app's Xcode project must add `-lsqlite3` to its linker flags (or link the `sqlite3` CocoaPod). This is a small, explicit Xcode-side wiring step.

#### 1.3 Transactions / atomicity

- 2.x provides **real SQLite ACID transactions** through the runtime `Transacter`: blocking `transaction {}` / `transactionWithResult {}` (commonMain, thread-confined), plus suspend `SuspendingTransacter.transaction {}` / `transactionWithResult {}` for coroutine call sites. The 2.3.2 release added `SuspendingTransacter.TransactionDispatcher` for controlling the transaction's `CoroutineContext`.
- Rollback is automatic on exception; explicit `rollback()` and `afterCommit`/`afterRollback` hooks exist.
- **The 1.x `transactionWithContext`/`transactWithContext` coroutine APIs are gone** — the 2.x `coroutines-extensions` artifact only carries Flow mapping (`asFlow`, `mapToList`, ...). In 2.x a transaction is either the blocking `transaction {}` or the suspend `SuspendingTransacter.transaction {}` on the runtime.
- Consequence for the outbox requirement: a single `transaction {}` can write the progress-outbox row **and** the cache row as one atomic commit — exactly the "progress + cache update is the unit" requirement. Nested/child transactions and `noEnclosing` semantics exist.
- SQLite itself is ACID and single-writer-per-file; SQLDelight compiles to SQLite `BEGIN`/`COMMIT` semantics on every driver.

#### 1.4 Read shape / queries

- Typed queries are generated from labeled statements in `.sq` files: `selectAll`, parameterized `insert`, `update`, and any `SELECT` mapping to the scaffold's needs (concept detail by id, list rows by domain/subdomain with progress columns, title scan for offline search).
- Offline title scan is a plain indexed `SELECT ... WHERE title LIKE ?` / `instr()` query over the cached concepts table — no FTS required by the posture; a plain index on `title` suffices and a few hundred rows is trivially fast even as a scan.
- Query results can be consumed as `Flow` via the coroutines-extensions (`asFlow().mapToList(dispatcher)`) for reactive UI state on both Android and iOS.
- Schema is validated at compile time (`.sq` files are parsed/type-checked during the build; the IntelliJ/Android Studio plugin adds autocomplete and refactoring).

#### 1.5 Build weight / setup friction / migrations

- Requires the **Gradle plugin** `app.cash.sqldelight` (applied in the `shared` module), `.sq` files under `src/commonMain/sqldelight` (default `srcDirs`), and per-platform driver deps (`android-driver` in `androidMain`, `native-driver` in `iosMain`).
- Generates a `Database` class + `Schema` object + per-file `XQueries` objects at build time.
- **Migrations** are `.sqm` files (named `<from-version>.sqm`), run by `Database.Schema.migrate()`; optional `verifySqlDelightMigration` + `schemaOutputDirectory` export to generate a baseline `.db` and CI-verify that migrations reproduce the latest schema. For a first release the schema can ship with version 1 and no migration files at all.
- Dialect is auto-selected for Android by `minSdk`, defaults to SQLite 3.18 otherwise; newer dialects (`sqlite-3-38-dialect`, etc.) are available as dependencies.
- Runtime deps pulled in: `runtime`, the chosen driver, and transitively SQLiter + stately on native, `androidx.sqlite` on Android. No KSP, no annotation processing.
- One caveat surfaced in the field: on AGP versions 8.9–8.11 the generated-source wiring broke (fixed upstream in AGP 8.12; documented in the #6140 thread); the scaffold's AGP 9.1.0 is on the supported path ("AGP 9.0 (built-in Kotlin) makes `variant.sources.kotlin` the canonical path").

#### 1.6 Gradle plugin × AGP 9 / new Android-KMP plugin / Kotlin 2.4

- SQLDelight ≤ 2.2.1 **fails on AGP 9** with the new DSL (`KotlinSourceSet with name 'main' not found` — issue #6078). The 2.3.x line is the first compatible line: 2.3.2's release notes state "Full compatibility with Android Gradle Plugin 9.0's new DSL" (PR #6140: AGP configuration made lazy via `onVariants`, `newDsl` flag enabled in tests) and "Fix compatibility with Android Gradle Plugin's built-in Kotlin" (#6139).
- This matters directly for the scaffold: `com.android.kotlin.multiplatform.library` **is** the AGP-9-era Android-KMP plugin (the officially supported way to add Android to a KMP library module), so SQLDelight **2.3.x is the required line**; 2.1.0/2.2.1 should not be used with this toolchain.
- SQLDelight's own build uses AGP 9.1.0 and Kotlin 2.3.10 at 2.3.2; master CI tracks newer AGP (9.3.x) and merges Kotlin 2.4.0-pre-release dependency bumps. Kotlin 2.4.10 consumption is untested-by-CI but consistent with Kotlin's klib backward-compatibility and the open #6270 (a Kotlin 2.4 user, functional).

#### 1.7 Integration with the `ConceptRepository`/`KbApi` seam

- The store slots in behind the seam exactly as the posture intends: `ConceptRepository` implementations delegate reads to the cache when offline and to `KbApi` when online; `concept(id)` "open" persists `ConceptDetail` + list-row metadata inside one transaction; `writeProgress(id, write)` appends to the outbox table inside the same transaction that updates the local cache/progress row.
- DTOs (`@Serializable`) and SQLDelight's generated row types are distinct; the repository maps between them (a thin adapter layer). The generated types can also be declared with `@Serializable` if desired, but nothing forces it.
- No conflict with the existing expect/actual seam (`createHttpClient()`); the store adds its own tiny expect/actual factory (`expect class DriverFactory` per the official docs) for `AndroidSqliteDriver` (needs a `Context`) vs `NativeSqliteDriver`.

### 2. Realm / MongoDB Atlas Device SDK for Kotlin

#### 2.1 Status: deprecated and past its end-of-life

- **MongoDB deprecated the Atlas Device SDKs in September 2024, with end-of-life on September 30, 2025** — the deprecation page is unambiguous: "Atlas Device SDKs will reach end-of-life and be removed on September 30, 2025." The MongoB docs landing page carries the same banner.
- **The sync layer is gone**: "Atlas Device Sync is deprecated... apps built using Sync need to move to an alternative solution or remove Sync before September 30, 2025." App Services Authentication, the sync wire protocol, and Data Access Permissions are deprecated alongside it.
- The on-device database **continues as an open-source project**, not a MongoDB product: the Kotlin SDK's README instructs users to install **`3.0.0+`** (the no-sync line) or use the `community` branch; Maven Central confirms `io.realm.kotlin:library-base` latest is **3.0.0**. The repo's last push was 2025-10-31 — effectively dormant since the deprecation.

#### 2.2 Compatibility with this scaffold

- Realm's own compatibility matrix (2.3.0) documents Kotlin 2.0.20+, **Gradle 7.2–8.5**, new memory model only. The 3.0.0 changelog documents "Kotlin 2.0.20 and above", "Minimum Gradle version: 7.2", "Minimum Android Gradle Plugin version: 7.1.3" — **no statement anywhere about Gradle 9.x, AGP 9.0+, or the `com.android.kotlin.multiplatform.library` plugin**, all of which this scaffold uses. The project that would have to test that is dormant.
- Realm requires its own **Gradle plugin (`io.realm.kotlin`)** plus a **compiler plugin** and bundled native (realm-core) libraries — significant build weight; it also has its own object model (`RealmObject` subclasses), separate from the scaffold's `@Serializable` DTOs.

#### 2.3 Transactions / queries (factual, for completeness)

- Realm has real transactions: `realm.write {}` / `realm.writeBlocking {}` (both atomic, coroutine and blocking forms), with the whole transaction committing or rolling back — so outbox+cache atomicity is achievable.
- Query language is Realm Query Language (NSPredicate-like): `realm.query<Concept>("title BEGINSWITH $0", ...)`, plus `asFlow()` observation. Indexes exist (`@Index`). No FTS in the base SDK.

### 3. File-based serialized blobs (kotlinx-serialization + okio)

- **Setup weight is near zero**: kotlinx-serialization-json 1.11.0 is already a dependency; adding `com.squareup.okio:okio:3.18.1` (a pure-KMP commonMain `FileSystem` with `iosArm64`/`iosSimulatorArm64` variants confirmed in its Gradle module metadata) gives `FileSystem.SYSTEM` read/write on both platforms. No Gradle plugin, no generated code, no schema.
- **Atomicity is the weak point.** `FileSystem.atomicMove(source, target)` gives single-file atomic replace (temp-write + rename), which is fine for one document but **cannot make two files (cache row + outbox row) commit atomically**. If the process dies between the cache write and the outbox write, the outbox entry is lost or duplicated — exactly the partial-persist failure the posture forbids. There is no transaction primitive.
- **No query capability.** The offline title scan becomes "load the whole index/cache file, deserialize the full list, filter in memory." At a few hundred rows that is genuinely cheap (sub-millisecond deserialization of a few hundred small JSON objects), so this is not a performance argument — it is a code-shape argument (a hand-rolled index file, manual write scheduling, no declarative queries).
- **No schema/migration story** (schema is whatever the JSON shapes say; evolution is a manual migration-in-code chore).
- Concurrency: two writers (main thread + outbox flusher) need a mutex/dispatcher guard; SQLite gives this for free.

### 4. Room (AndroidX) — the ticket's premise is outdated, but the blocker has moved

- **Factual correction to the ticket's premise**: Room has been a KMP library since **2.7.0 (April 2025)** — "Current supported platforms are Android, iOS, JVM (Desktop), native Mac and native Linux" (official release notes). It does compile in a KMP `shared` module, so "Room does not compile in KMP" is no longer true; the seam argument alone does not disqualify it.
- The current Room line is **Room 3.x** (`androidx.room3:room3-runtime:3.0.1`), with a dedicated Gradle plugin (`androidx.room3`), **KSP** codegen per target (`kspAndroid`, `kspIosArm64`, `kspIosSimulatorArm64`, ...), **schema export**, and a required `SQLiteDriver` from the AndroidX SQLite KMP stack (`androidx.sqlite:sqlite-bundled` recommended). iOS additionally needs `-lsqlite3` link flags.
- **The real blocker for this scaffold is KSP × the new Android-KMP plugin**: KSP's support for `com.android.kotlin.multiplatform.library` is the subject of **open issue google/ksp#2476** (May 2025). Community reports (Dec 2025) show working setups on KSP 2.3.4 + AGP 9.0-rc01 with per-target `kspAndroid` configs, plus known gaps (`kspCommonMainMetadata` missing), and KSP 2.3.10 (Aug 2026) continues to fix "AGP 9 built-in Kotlin" interop. So Room on this toolchain is *possible in principle, unverified in the exact combination (Kotlin 2.4.10 + AGP 9.1.0 + KSP + Room 3.0.1), and heavier* (Gradle plugin + KSP + schema export) than SQLDelight. Room 2.7/2.8 predate the AGP-9 era and are the wrong reference.

### 5. Other KMP SQLite bindings (brief)

- **SQLiter** (`co.touchlab:sqliter-driver`) — a minimal raw-SQLite driver for Kotlin/Native; it is a building block (it *powers* SQLDelight's native driver) rather than an app-facing store. Using it directly means writing your own query layer; no typed queries, no migrations. Only relevant as SQLDelight's engine, not a candidate in its own right.
- **`androidx.sqlite` KMP** (`androidx.sqlite:sqlite-framework` / `sqlite-bundled`) — the AndroidX low-level `SQLiteDriver`/`SQLiteConnection`/`SQLiteStatement` API for Android + iOS (KMP since 2.5.0, April 2025; 2.6.0 raised minSdk to 23). It is the layer Room sits on and the layer SQLDelight's Android driver wraps. As a direct choice it is a raw SQL API: real transactions via the `SQLiteConnection`/transaction API and the engine's ACID guarantees, but no typed queries, no `.sq` compile-time checking, no migration tooling.
- `sqldelight-native-driver` / `androidx.sqlite.kmp` / other third-party bindings: not assessed beyond the above; SQLDelight's own native driver IS the maintained native binding.

### 6. Does the corpus justify SQL at all?

- The cache is a few hundred small rows (titles, slugs, a progress tuple, plus a markdown `body` per opened concept) and an append-only outbox. That is **far below any scale where SQLite indexing or query planning matters**; a file-based store would be fast enough (a few hundred small JSON documents deserialize in well under a millisecond).
- The deciding factors are therefore **not performance**: they are (a) **atomicity of the outbox+cache unit** — real only in SQL/Realm, not in file-based blobs; (b) **query ergonomics** (indexed/declarative title scan vs. load-and-filter); and (c) **maintenance story** (schema + migration tooling vs. hand-rolled files). SQLite (via SQLDelight) provides all three as library features; the file-based approach provides none of them for free and pushes the discipline into app code. Realm provided them too, but its project is EOL'd and dormant.

## Verdict (facts, not a decision)

| Criterion | SQLDelight (2.3.2) | Realm KMP | File-based (okio + kotlinx-serialization) | Room KMP (3.0.1) |
|---|---|---|---|---|
| Compiles in CMP `shared` for Android + iOS (K/N arm64) | ✅ `android-driver` + `native-driver`, `iosArm64`/`iosSimulatorArm64` listed; requires 2.3.x for AGP 9 new DSL | ⚠️ KMP targets exist, but project is deprecated/EOL (Sept 2025) and dormant; no AGP 9 / Gradle 9 / new Android-KMP plugin evidence | ✅ Pure Kotlin (okio 3.18.1 commonMain) | ⚠️ KMP since 2.7.0 (Android/iOS/JVM/Mac/Linux); current 3.x line; blocked/unverified by open KSP × new Android-KMP plugin issue |
| Real transactions (outbox+cache atomic) | ✅ SQLite ACID via `transaction {}` / `SuspendingTransacter.transaction {}` | ✅ `realm.writeBlocking {}` (project EOL) | ❌ None; temp-write+rename is single-file only | ✅ SQLite via AndroidX SQLite driver |
| Read shape (detail/list rows, indexed title scan) | ✅ Typed `.sq` queries, indexes, Flow | ✅ RQL queries + Flow | ❌ Load-all + in-memory filter | ✅ DAO queries |
| Build weight / setup friction | Gradle plugin + `.sq` files + per-target driver dep; migrations via `.sqm`; iOS static framework needs `-lsqlite3` in Xcode | Own Gradle plugin + compiler plugin + bundled native libs; schema-first object model | ~zero; one dependency (okio) | Gradle plugin + KSP per target + schema export + SQLite driver; heaviest |
| Integration with `ConceptRepository`/`KbApi` seam | Store sits behind the seam; thin DTO↔row adapter; expect/actual `DriverFactory` | Object model conflicts with `@Serializable` DTOs | Trivial (serialize DTOs directly) | DAO layer on top; DTO↔entity mapping |
| Maintenance / longevity | Actively maintained (releases 2025–2026) | **EOL Sept 2025**; open-source continuation with no visible activity since Oct 2025 | No schema/migration tooling (manual) | Active (AndroidX), but iOS+KMP still settling; KSP coupling |

None of the three viable families is ruled out on compatibility alone at the "does it compile" bar — but the compatibility, atomicity, and read-shape rows above separate them factually. The call itself is left to the grilling ticket.

## Trade-offs

- **SQLDelight** buys real ACID transactions, typed/compile-checked queries, and a migration story at the cost of a Gradle plugin, `.sq`/`.sqm` files, generated code, a per-platform driver dependency, an iOS `-lsqlite3` Xcode linker flag, and (2.x-specific) a blocking-`transaction {}`/suspend-`SuspendingTransacter` split to keep straight. Version must be ≥ 2.3.0 for the scaffold's AGP 9.1 toolchain.
- **File-based blobs** buy near-zero setup and zero generated code, and are genuinely sufficient at this corpus size — but they cannot make the outbox+cache write atomic, cannot answer a query without loading and filtering everything, and delegate schema evolution to app code. The atomicity gap is the posture's hard requirement, not a nicety.
- **Realm** bought a polished object store with real transactions, but as a *product* it is dead: EOL was September 30, 2025; the only supported line is the open-source 3.0.0 no-sync release from a repo with no commits since late 2025, with no documented support for this scaffold's Gradle 9 / AGP 9 / new Android-KMP plugin toolchain. Any compatibility risk taken on a dormant dependency is a long-tail risk.
- **Room** is the "Android default" but its KMP path is the newest and heaviest here (Gradle plugin + KSP + schema export + bundled SQLite), and it depends on KSP's still-open support for the exact Android-KMP plugin this scaffold uses.

## Uncertainties

- **SQLDelight × Kotlin 2.4.10 / AGP 9.1 / Gradle 9.1 exact-triple verification**: SQLDelight 2.3.2 is built with Kotlin 2.3.10 and AGP 9.1.0 and explicitly claims AGP 9 new-DSL compatibility; master CI tracks newer AGP/Kotlin. But there is no CI statement covering the exact Kotlin 2.4.10 + AGP 9.1.0 + `com.android.kotlin.multiplatform.library` combination, and no documented proof that the SQLDelight plugin's `onVariants`-based Android wiring covers the new plugin's `androidLibrary` target specifically (the 2.3.x notes address "AGP 9's new DSL" and "built-in Kotlin" broadly). A 30-minute compile smoke test in the scaffold is the cheap de-risking step.
- **KSP × Room on the new Android-KMP plugin**: open issue google/ksp#2476; community setups work on slightly older versions, but the exact KSP + Kotlin 2.4.10 + Room 3.0.1 + AGP 9.1.0 combination is unverified.
- **Realm 3.0.0 line**: whether the no-sync 3.0.0 release (or the `community` branch) builds under Gradle 9.1/AGP 9.1 was not verified (no CI evidence exists to check); the repo has been inactive since 2025-10-31.
- **SQLDelight generated-code language level**: open issue #6270 asks for control over the generated code's Kotlin language version when consuming from Kotlin 2.4; current codegen targets the compiler's defaults. Cosmetic, but unverified for 2.4.
- **Original MongoDB announcement URL**: the authoritative primary source used here is the MongoDB docs deprecation page (and the realm-kotlin README banner); the specific September 2024 blog post URL could not be resolved (404) and is not cited.
- **Corpus figure**: the "few hundred" cached-rows bound comes from the map/prior research (~307 concepts on the server); the actual offline cache will be strictly smaller (only opened concepts), which only strengthens the file-based option's adequacy on raw scale.
