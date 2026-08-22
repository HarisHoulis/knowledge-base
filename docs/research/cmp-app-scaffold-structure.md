# CMP app scaffold structure for a new learning app (2026)

## Question

What does the Compose Multiplatform (Android + iOS) app project look like: module structure, Android + iOS target wiring, UI architecture (UDF/state hoisting), navigation, and how it consumes the backend API? Prototype the scaffold as a concrete artifact to react to. Research only — no production code.

## Context (fixed constraints)

- Single-user digest app: browse, search, read, listen (on-device TTS), track per-concept progress + resume position.
- Targets Android + iOS via Compose Multiplatform (v1, no desktop).
- Monorepo (#164): app under `app/`, backend under `backend/` — separate Gradle builds.
- **DTOs are separate per side** (per human decision, superseding the "shared DTOs" note in the map index for #164): the app declares its own `@Serializable` wire models mirroring `docs/design/api-surface.md`.
- UDF/state hoisting is mandatory per repo standards (`docs/agents/design-rules.md`).
- Agent machine (#165): GitHub-hosted `macos-latest` runner — iOS builds verify on macOS, simulator builds need no signing.
- Stack (#123): Ktor backend; app consumes the REST API via a Ktor client. TTS (#124): hand-rolled `expect`/`actual` engine in the shared module.
- UI architecture (UDF/state hoisting) — mandatory.

## Sources (primary)

- [kmp.jetbrains.com wizard](https://kmp.jetbrains.com) (live template generation via its `generateKmtProject` API, Aug 2026)
- [Kotlin/KMP-App-Template](https://github.com/Kotlin/KMP-App-Template) (shared/build.gradle.kts, gradle/libs.versions.toml)
- [JetBrains: Create your first Compose Multiplatform app](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform-create-first-app.html)
- [JetBrains: Multiplatform compatibility guide](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-compatibility-guide.html)
- [JetBrains: iOS integration methods](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-ios-integration-overview.html)
- [JetBrains: Direct integration — `embedAndSignAppleFrameworkForXcode`](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-direct-integration.html)
- [JetBrains: Multiplatform ViewModel in Compose](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-viewmodel.html)
- [Ktor: Client engines](https://ktor.io/docs/client-engines.html)
- [Ktor: Create a multiplatform application](https://ktor.io/docs/client-create-multiplatform-application.html)
- [kotlinx.serialization releases](https://github.com/Kotlin/kotlinx.serialization/releases)
- Maven Central metadata for `org.jetbrains.compose`, `io.ktor`, `org.jetbrains.kotlinx:kotlinx-serialization-json`, `org.jetbrains.androidx.lifecycle:lifecycle-viewmodel-compose`

## Findings

### 1. The official template is NOT a single `composeApp` module

The GitHub template `JetBrains/compose-multiplatform-template` is **archived** (Dec 20, 2023). The current source of truth is the **kmp.jetbrains.com wizard** plus the official **`Kotlin/KMP-App-Template`** repo. The 2026 wizard generates a multi-module layout:

- `shared` — all shared Kotlin + Compose UI (`commonMain`/`androidMain`/`iosMain` + `commonTest`/`iosTest`/`androidHostTest`; desktop/web only if selected).
- `androidApp` — thin Android application module (`com.android.application`).
- `iosApp` — separate Xcode project.

`settings.gradle.kts`: `include(":androidApp")`, `include(":shared")`. The old "single `composeApp` with android/ios source sets" layout (which the wayfinder ticket #129 framed as option A) is the deprecated template, not the current default.

The `shared` module uses the new Google **`com.android.kotlin.multiplatform.library`** plugin (not `androidTarget()`, which has been deprecated since Kotlin 2.3.0). `androidApp` uses `com.android.application`.

### 2. Pinned versions (wizard + current stable, Aug 2026)

| Component | Version |
|---|---|
| Kotlin | 2.4.10 (wizard); 2.4.20 expected Sep 2026 |
| Compose Multiplatform | 1.11.1 stable (1.12.0-rc01 in RC) |
| Compose compiler plugin | 2.4.10 (tracks Kotlin) |
| AGP | 9.0.1 (wizard); KMP-App-Template pins 9.1.0; AGP 9.x required for the new KMP library plugin |
| Gradle wrapper | 9.1.0 (AGP 9 compat range 8.5.2–9.1.0) |
| compileSdk / targetSdk | 36 |
| minSdk | 24 |
| kotlinx-serialization-json | 1.11.0 (built on Kotlin 2.3.20, backward compatible with 2.4.10) |
| serialization Gradle plugin | 2.4.10 (tracks Kotlin) |
| Ktor client | 3.5.2 |
| lifecycle-viewmodel-compose | 2.11.0 stable (wizard pins 2.11.0-beta01) |
| Material3 | 1.11.0-alpha07 (wizard default) |

### 3. iOS targets and framework wiring

- Targets declared individually: `listOf(iosArm64(), iosSimulatorArm64())`. `iosX64` only for Intel simulators (excluded — `macos-latest` is arm64). The old `ios()` shortcut DSL was removed in Kotlin 2.2.0.
- Wizard generates a **static framework** (`binaries.framework { baseName = "Shared"; isStatic = true }`).
- Integration: **direct integration** — an Xcode Run Script phase runs `./gradlew :shared:embedAndSignAppleFrameworkForXcode`; SwiftUI hosts `MainViewControllerKt.MainViewController()` (a `ComposeUIViewController`). XCFramework is only for distributing to third parties; SPM local integration also supported.
- Simulator builds run unsigned — no Apple developer account needed for verification (#165 research).

### 4. ViewModel / UDF

`org.jetbrains.androidx.lifecycle:lifecycle-viewmodel-compose` is **multiplatform and stable** (2.11.0). It is the documented UDF approach; plain state hoisting is for local UI state. Caveats on iOS (no reflection): the ViewModel must be created with an initializer — `viewModel { MyViewModel() }`; with Nav3 scoping, ViewModels attach per navigation entry via `rememberViewModelStoreNavEntryDecorator`; `viewModelScope` needs `kotlinx-coroutines-swing` on desktop only.

### 5. Ktor client

- Current: **3.5.2**.
- Engines: **Android → OkHttp** (`ktor-client-okhttp`, the official template default; CIO is the pure-Kotlin alternative, HTTP/1.1 only) · **iOS → Darwin** (`ktor-client-darwin`, NSURLSession).
- commonMain setup: `ktor-client-core` + `ktor-client-content-negotiation` + `ktor-serialization-kotlinx-json`; engine deps in `androidMain`/`iosMain`; `HttpClient { install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true; isLenient = true }) } }`.

### 6. Module structure trade-off (the ticket's Q1)

The wayfinder ticket framed it as "single `composeApp` vs `core:`-split", where the `core/model`+`core/network` split existed to host **shared DTOs**. With DTOs now separate per side, that motivation is gone. The real options:

- **(a) Wizard default**: one Kotlin module (`shared`) holding all shared code/UI, plus `androidApp` + `iosApp` shells. Feature/`core` packages inside `shared` (`data/`, `tts/`, `ui/*`).
- **(b) Old single `composeApp`**: deprecated template shape, same idea as (a) but with Android as a source set inside the shared module instead of a separate `androidApp`.
- **(c) `core:`-split**: Gradle modules per concern (`core/model`, `core/network`, `core/tts`, `feature/*`, `app`).

Trade-offs:

| | (a) wizard default | (b) single composeApp | (c) core:-split |
|---|---|---|---|
| Gradle overhead | Low (2 includes) | Lowest (1 module) | High (5+ modules, catalogs, wiring) |
| Compile-time boundaries | Package-level only | Package-level only | Enforced by Gradle |
| DTO-sharing story | N/A (DTOs separate) | N/A | Was the original motivation — dead |
| Cost of a real seam later | Split packages into modules then | Same | Pre-paid |
| Current ecosystem fit | **Wizard + template default** | Deprecated template | Now-in-Android pattern, not CMP default |

The backend research (`docs/research/backend-architecture.md`) established the same rule for the backend modulith: "let module boundaries follow real domain seams" — start with few modules, split when a seam appears. The app is a single bounded context (the digest experience) with one TTS file pair, so (a) is the honest baseline; (c) buys enforcement the codebase doesn't yet need.

### 7. Remaining ticket questions resolved by prior research

- **Navigation** → Nav3 (`navigation3-ui` 1.1.1): `sealed interface Route : NavKey`, `SavedStateConfiguration`, two entry decorators + `lifecycle-viewmodel-navigation3`. See sibling research `docs/research/cmp-navigation-nav2-vs-nav3.md`.
- **API consumption** → Ktor client behind a `ConceptRepository` interface with a fake for tests (repo testing convention: `docs/agents/testing.md`); `ServerConfig` holds the base URL; manual `@Serializable` DTOs per side, `docs/design/api-surface.md` is the contract.
- **TTS** → `expect`/`actual` `TtsEngine` in the shared module; Android stub + iOS `AVSpeechSynthesizer` sketch. See `docs/research/cmp-on-device-tts.md`.

## Verdict

**Adopt the wizard default layout**: one Kotlin Gradle module `shared` under `app/`, `androidApp` shell, `iosApp` Xcode project, feature/`core` packages inside `shared`. Split into Gradle modules only when a real seam appears (same rule as the backend modulith).

Supporting decisions:

1. **Targets** — `iosArm64()` + `iosSimulatorArm64()`, static framework, direct integration (`embedAndSignAppleFrameworkForXcode`); `iosX64` omitted.
2. **Plugins** — `com.android.kotlin.multiplatform.library` in `shared` (the `androidTarget()` path is deprecated since Kotlin 2.3.0), `com.android.application` in `androidApp`, AGP 9.x.
3. **Versions** — pin Kotlin 2.4.10, CMP 1.11.1, AGP 9.0.1, Gradle 9.1.0, Ktor 3.5.2, kotlinx-serialization 1.11.0, `lifecycle-viewmodel-compose` 2.11.0, minSdk 24 / compileSdk 36.
4. **UDF** — multiplatform ViewModel + immutable `UiState` + one-shot event channel; `viewModel { }` initializer form (iOS has no reflection).
5. **API** — Ktor client (OkHttp/Darwin) + `ContentNegotiation` behind `ConceptRepository` interface + `FakeConceptRepository`; `ServerConfig` constant; manual per-side `@Serializable` DTOs.

## Trade-offs

- **What (a) costs vs (c)**: no compile-time enforcement of the `ui` ↔ `data` boundary — a UI composable *can* import a DTO. (c) pays that cost today in Gradle boilerplate for a codebase with one bounded context and one TTS file pair; the boundary is a discipline until a second context appears. The backend research already accepted the same trade for the backend's start-2–3-modules rule.
- **What `com.android.kotlin.multiplatform.library` costs**: it is the newest piece of the toolchain (the AGP 9 + KMP library plugin migration is active churn territory). The alternative (`androidTarget()` + KMP plugin) is the older, well-trodden path but deprecated since Kotlin 2.3.0, so staying on it front-loads a migration.
- **What the wizard pins cost**: Material3 `1.11.0-alpha07` and `lifecycle-viewmodel-compose` `2.11.0-beta01` are alpha/beta artifacts the wizard ships by default; the scaffold should pin the stable Material3 (shipped with CMP 1.11.1) and `lifecycle-viewmodel-compose` 2.11.0 stable rather than inherit the wizard's pre-release pins.

## Uncertainties

- **CMP 1.12.0-rc01** is in RC — 1.11.1 is current stable; if the scaffold takes a while, re-check whether 1.12.x went stable and whether navigation/lifecycle versions it bundles changed.
- **AGP 9.x + `com.android.kotlin.multiplatform.library`** is the newest toolchain path; Gradle 9.1.0 (wizard) vs the KMP-App-Template's AGP 9.1.0 — pick one pinned pair and verify the build end-to-end on macOS before assuming it compiles.
- **Kotlin 2.4.20** (expected Sep 2026) and **2.5.0** (Dec 2026) are ahead; serialization plugin tracks the Kotlin version, so any Kotlin bump must be coordinated with the serialization plugin and CMP compatibility.
