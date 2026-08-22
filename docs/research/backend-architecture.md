# Backend architecture for the Ktor digest app (2026)

## Investigation Date

2026-08-22

## Question

Which backend architecture should a **Ktor + Exposed + Postgres single-user REST backend** use, to stay scalable and maintainable over a long learning project — **without sharing DTOs with the Compose Multiplatform app** and **without a single "god" package** (one package holding everything, which the human rejected as a Single-Responsibility violation)?

Settled context this research rests on: stack decision (#123) is Ktor + Exposed + Postgres [prior research: `docs/research/backend-stack-ktor-vs-fastapi.md`]; hosting is Neon (Postgres) + a Hetzner VPS [prior research: `docs/research/hosting-free-tier-options.md`]; the repo is a monorepo (#164) with the app under `app/` and the backend under `backend/` as separate Gradle builds [sibling research: `docs/research/agent-machine-options.md`]. The human explicitly rejected (a) sharing DTOs between backend and app and (b) a "presentation-data-domain" layer split for the backend, and rejected a single god package.

Candidates compared: (1) layered/onion/clean, (2) hexagonal/ports-and-adapters, (3) modular monolith (Gradle modules per bounded context, one Ktor app) — the leading candidate — (4) feature packages inside one module (baseline), plus Ktor-idiomatic guidance on DI, Exposed placement, testing seams, and the serialization/error boundary.

## Sources

- [S1] Ktor docs — Application structure (Ktor) — https://ktor.io/docs/server-application-structure.html
- [S2] Ktor docs — Modules (Ktor) — https://ktor.io/docs/server-modules.html
- [S3] Ktor docs — Dependency injection (Ktor) — https://ktor.io/docs/server-dependency-injection.html
- [S4] Ktor docs — Dependency registration (Ktor) — https://ktor.io/docs/server-di-dependency-registration.html
- [S5] Ktor docs — Dependency resolution (Ktor) — https://ktor.io/docs/server-di-dependency-resolution.html
- [S6] Ktor docs — Testing with dependency injection (Ktor) — https://ktor.io/docs/server-di-testing.html
- [S7] Ktor docs — Configure the DI plugin (Ktor) — https://ktor.io/docs/server-di-configuration.html
- [S8] Ktor docs — Integrate a database with Kotlin, Ktor, and Exposed (Ktor) — https://ktor.io/docs/server-integrate-database.html
- [S9] Ktor docs — Testing in Ktor Server (Ktor) — https://ktor.io/docs/server-testing.html
- [S10] Ktor docs — Content negotiation and serialization in Ktor Server (Ktor) — https://ktor.io/docs/server-serialization.html
- [S11] Ktor docs — Status pages (Ktor) — https://ktor.io/docs/server-status-pages.html
- [S12] Ktor docs — Routing organization (Ktor) — https://ktor.io/docs/server-routing-organization.html
- [S13] Exposed README (JetBrains) — https://github.com/JetBrains/Exposed
- [S14] Exposed docs — Working with Transactions (JetBrains) — https://www.jetbrains.com/help/exposed/transactions.html
- [S15] Kotlin docs — Serialization (JetBrains) — https://kotlinlang.org/docs/serialization.html
- [S16] Gradle docs — Multi-Project Builds (Gradle) — https://docs.gradle.org/current/userguide/multi_project_builds.html
- [S17] Cockburn, "Hexagonal (Ports & Adapters) Architecture" (Alistair Cockburn, 2005) — https://alistair.cockburn.us/hexagonal-architecture/
- [S18] Martin, "The Clean Architecture" (Robert C. Martin, 2012) — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
- [S19] Ktor Chat sample — modular full-stack Ktor app (Ktor) — https://github.com/ktorio/ktor-chat
- [S20] Ktor DDD example (Anton Arhipov; referenced by Ktor docs, archived Aug 2026) — https://github.com/antonarhipov/ktor-ddd-example
- [S21] Koin docs — Ktor quickstart (Koin/Kotzilla) — https://insert-koin.io/docs/quickstart/ktor/

## Findings

### 1. Ktor is deliberately unopinionated, but its own docs enumerate the full spectrum of structures — including the "modulith"

The official Application structure page states outright: "While Ktor is intentionally unopinionated, there are common patterns and best practices that help keep your application modular, testable, and easy to extend" [S1]. It then enumerates, in one primary source, every candidate in this research question:

- **Default single-module** (the `start.ktor.io` generator layout): "Although suitable for small applications, this structure does not scale well as the project grows" [S1].
- **Layered**: `config/`, `plugins/`, `controller/`, `service/`, `repository/`, `domain/`, `dto/` packages [S1].
- **Modular architecture**: multiple Gradle modules (`db/core`, `db/postgres`, `db/mongo`, `server/core`, `server/banking`), where "the banking module does not compile against any database implementation. It only depends on `db/core`, keeping the domain separate from infrastructure details" [S1].
- **Feature-based modules**: `customer/` and `order/` each containing `CustomerRoutes.kt`/`CustomerService.kt`/`CustomerDto.kt` [S1].
- **DDD**: a `domain/` layer "independent of Ktor" with entities, value objects, aggregates, repository *interfaces* owned by the domain, and services — routes live in a separate `server/` layer that wires `ExposedCustomerRepository` into `CustomerService` [S1].
- **Microservice-oriented** and **"Modulith deployment"**: "multiple Gradle modules representing services can be packaged independently but deployed together in a single Ktor application. This approach is commonly referred to as a modulith. Each Gradle module remains internally isolated and exposes an application module that can be loaded through configuration" via `ktor.application.modules` [S1].

Ktor's own guidance is size-scoped: "Small services often work well with only a few modules and simple dependency injection. Medium-sized applications typically benefit from a consistent feature-based structure… Large or domain-heavy systems can adopt a domain-driven approach" [S1]. The structures "are not mutually exclusive" — e.g. "feature-based organization within a domain-driven architecture" [S1].

The modular architecture maps onto Ktor's core idiom: a Ktor *module* is an extension function on `Application` that "sets up routes, installs plugins, and configures services"; "Dependencies are typically injected at module boundaries" (`fun Application.customerModule(customerService: CustomerService)`), and a module function can also receive its dependencies as parameters (the simplest documented approach, "works well for small or medium applications") or pull them from `Application.attributes` (a type-safe map) or from a DI container [S1][S2]. Modules can load concurrently via `ktor.application.startup = concurrent` [S2].

### 2. Candidate 1 — Layered / onion / clean architecture maps cleanly onto Ktor idioms but is the heaviest option

Ktor's docs describe the layered structure as "common in enterprise applications and provides a clear starting point for maintainable code" [S1]. The onion/clean variants are pattern-originator territory: Clean Architecture's governing rule is **The Dependency Rule** — "source code dependencies can only point *inwards*… Nothing in an inner circle can know anything at all about something in an outer circle," with databases and web frameworks relegated to the outermost ring and data crossing boundaries "in the form that is most convenient for the inner circle" (never DB row structures) [S18]. Clean/hexagonal/onion "all have the same objective, which is the separation of concerns" via layers [S18].

How that maps onto Ktor: the framework itself is the outer ring (routing + ContentNegotiation + StatusPages are "details"); domain entities and use cases are inner rings that never import `io.ktor.*` or `org.jetbrains.exposed.*`; the interface-adapters ring owns the `@Serializable` DTOs and repository implementations [S1][S18]. Ktor's own DDD section is exactly this shape — `domain/` holds `Customer`, `CustomerRepository` (interface), `CustomerService`; `server/` holds `CustomerRoutes.kt` and the `Application.kt` that instantiates `ExposedCustomerRepository` [S1]. Ktor points to a standalone DDD example that "demonstrating DDD principles for structuring Ktor applications" with per-domain `CustomerRepository.kt`/`CustomerService.kt`/`CustomerRoutes.kt` [S20].

**Trade-offs**: strict clean/onion demands explicit boundary machinery — output ports, interface adapters, and mapping objects at every ring crossing ("We usually resolve this apparent contradiction by using the Dependency Inversion Principle… arrange interfaces and inheritance relationships such that the source code dependencies oppose the flow of control," [S18]). For a single-user CRUD API this is ceremony the human already rejected in the "presentation-data-domain" variant; Ktor docs reserve full DDD for "large or domain-heavy systems" [S1]. The durable part of the idea — *domain code does not depend on the framework or the DB* — is cheap and is preserved by every candidate below via the repository-interface seam.

### 3. Candidate 2 — Hexagonal / ports-and-adapters: the same seam discipline, Ktor-native

The original pattern is Cockburn's 2005 paper: the application sits at the center; every external actor (UI, database, test harness) talks to it through a **port** (a purposeful API) via a substitutable **adapter**; its stated intent is to "create your application to work without either a UI or a database so you can run automated regression-tests against the application," with an in-memory "mock" database as a first-class adapter for the data port [S17]. The "rule to obey is that code pertaining to the *inside* part should not leak into the *outside* part" [S17]. Cockburn is explicit that the number of ports is "largely a matter of taste" (two to four typical) and that the pattern "can be configured to run decoupled from external databases using an in-memory oracle, or *mock*, database replacement" [S17].

In Ktor terms, the driving adapter is the routing layer and the driven adapters are the persistence implementations: Ktor's official DB tutorial is a textbook ports-and-adapters example — a `TaskRepository` *interface* with a `FakeTaskRepository` (in-memory) and a `PostgresTaskRepository` (Exposed) implementation, swapped purely by changing which implementation is registered for the interface, "because you are injecting the dependency through the interface, the switch in implementation is transparent to the code for managing routes" [S8]. Ktor's DDD section makes the same move (`CustomerRepository` interface in domain, Exposed implementation in the app wiring) [S1].

**Trade-offs**: hexagonal gives the testability payoff (no DB in route tests) with the same interface seam as a plain layered approach, but its formal vocabulary (ports/adapters/hexagons, primary vs secondary) adds naming ceremony without new capability for a single-context CRUD service. It is best understood as the *discipline* behind candidate 4/3, not a separate structure to bolt on [S17][S8].

### 4. Candidate 3 — Modular monolith ("modulith"): the documented scalable Ktor structure, and a first-class fit for this monorepo

This is the candidate Ktor itself documents and endorses for growth, and it directly satisfies both of the human's rejections:

- **No god package.** Gradle multi-project builds exist precisely to "split… projects into smaller, focused modules that are built, tested, and released together… while keeping each module logically isolated" [S16]. A Ktor modulith is "multiple Gradle modules representing services… packaged independently but deployed together in a single Ktor application," each module exposing an `Application` extension function loaded through `ktor.application.modules` [S1]. Ktor's example shows the boundary-enforcement trick: a `server/banking` module depends on `db/core` (interfaces) and only at runtime on `db/postgres` via `runtimeOnly`, so "the banking module does not compile against any database implementation" [S1]. Reference implementations to crib from: **Ktor Chat**, the official "large, full-stack" Ktor+Exposed+Compose sample, is structured as `core` (domain data objects, interfaces, exceptions), `server/common`, `server/rest`, `server/admin`, `db` (exposed database schema types and repository implementations), and `client`, which its README calls "an inversion of control for a full-stack Kotlin application, with a nod to architectures like Onion, Hexagonal, or Clean" [S19]. For this app (concepts + progress + auth), the shape is: one `backend:app` assembly module (plugins, DI wiring, module registration) plus one Gradle module per bounded context, each holding its own routes, service, repository interface + Exposed implementation, and wire DTOs [S1][S19].
- **No shared DTOs.** Since the app (`app/`) and backend (`backend/`) are already separate Gradle builds in the monorepo [sibling research], nothing forces a shared DTO module; each backend module owns its own `@Serializable` wire models (see Finding 8).

Gradle mechanics are plain and settled: all subprojects live under one `settings.gradle.kts` via `include(...)`; a project dependency like `implementation(project(":backend:concepts"))` affects both build order and classpath; project paths use colons for nesting [S16]. Ktor module loading from config means the assembly module stays thin: `ktor.application.modules: [com.example.concepts.conceptsModule, com.example.progress.progressModule]` [S2][S1].

**Trade-offs**: multi-module means more Gradle files and slower configuration-time; the payoff (compile-time isolation, per-module `runtimeOnly` DB deps, independent testability "by instantiating modules in isolation" [S1]) only matters once the codebase actually has more than one context. Start small — 2–3 modules — and let module boundaries follow real domain seams (this matches the repo's own architectural rule that modularisation is a first-class structural concern, `docs/agents/architectural-rules.md`).

### 5. Candidate 4 — Feature packages inside one module: the honest baseline

Ktor docs describe the feature-based structure as the sweet spot for "medium-sized applications": "Each feature becomes a self-contained module, containing its routes, services, data transfer objects (DTOs) and domain logic" — where "module" here means a Ktor `Application` module (a package of extension functions), not a Gradle module [S1]. "This structure scales well in medium-to-large monoliths or when splitting individual features into microservices later. Each feature can be migrated or versioned independently" [S1]. Routing organization docs likewise recommend, as projects grow, "grouping by domain or feature" with each feature holding only its own routing code [S12].

**Trade-offs**: inside a single Gradle module, the "god package" risk the human rejected returns gradually — nothing enforces the package boundaries, and cross-feature imports compile freely. It is the correct *internal organizing style* (Ktor docs themselves suggest "feature-based organization within a domain-driven architecture" [S1]) but a weak *top-level* structure for a learning project whose stated goal is "scalable and easily-maintainable." The cleanest reading: **feature packages are what goes inside each modulith Gradle module**, not a substitute for the modulith.

### 6. DI for Ktor: first-party `ktor-server-di` exists and is the default the docs teach; Koin is a third-party option; manual wiring is the documented fallback

Ktor 3.x ships a **built-in DI plugin** (`io.ktor:ktor-server-di`) — "Ktor includes a dependency injection (DI) plugin that lets you register services and configuration objects once and access them throughout your application… The plugin integrates with the Ktor application lifecycle and supports scoping, structured configuration, and automatic resource management" [S3]. Primary-source capabilities:

- **Registration**: `dependencies { provide<TaskRepository> { PostgresTaskRepository() } }` (lambda, constructor reference, class reference, or function reference); named providers via `provide("default") { … }` resolved with `@Named`; configuration-file registration under `ktor.application.dependencies` [S4].
- **Resolution**: `dependencies.resolve<T>()` or delegated `val service: GreetingService by dependencies`; injection into module functions by parameter ("Ktor will resolve these dependencies from the DI container based on type matching"); `@Property("database.connectionUrl")` injects config values; async/suspending providers [S5]. Because `dependencies.resolve()` is suspend, the config module must be `suspend` [S8].
- **Testing**: `testApplication { application { dependencies.provide<MyService> { MockService() } … } }` overrides production deps; "In test environments, the DI plugin uses `IgnoreConflicts` by default," so test overrides don't error [S6][S7].
- **Scoping**: the plugin "supports scoping" and configurable key-matching/conflict policies (`ktor.di.keyMapping`, `ktor.di.conflictPolicy`) [S3][S7].

Ktor's official Ktor+Exposed tutorial uses this plugin end-to-end — registering `FakeTaskRepository` then `PostgresTaskRepository` for the `TaskRepository` interface, resolving it inside the serialization module, and overriding it in tests [S8]. The alternative containers: **Koin** is a third-party (Kotzilla) DI framework with a Ktor integration (`koin-ktor`, installed via `install(Koin) { modules(appModule) }` inside `Application.main()`) [S21]; it is a legitimate choice but now redundant on the server, where the first-party plugin covers registration, resolution, config injection, scoping, lifecycle, and test overriding [S3]–[S7]. Manual wiring remains fully documented: passing dependencies as module-function parameters is "the simplest way… works well for small or medium applications and keeps dependencies clear" (with the caveat that "modules become tightly coupled at compile time and cannot be easily swapped at runtime"), and `Application.attributes` gives a type-safe keyed map "without… direct references between modules" [S2].

**Recommendation direction for this repo**: use Ktor's built-in `ktor-server-di` (it is the default the official tutorial teaches, removes a dependency, and covers the fake-vs-real repository swap and test overrides [S8][S6]); keep Koin in mind only if the app ever needs a shared multiplatform DI layer (it does not, since DTOs are not shared and the app is a separate build [S21][sibling research]).

### 7. Exposed placement, transactions, and the repository seam

**What Exposed is**: "a lightweight SQL library on top of a database connectivity driver for the Kotlin programming language, with support for both JDBC and R2DBC" offering "two approaches for database access: a typesafe SQL-wrapping DSL and a lightweight DAO API" [S13]. Modules: `exposed-core` (DSL), `exposed-dao` (DAO, "only compatible with `exposed-jdbc`"), `exposed-jdbc`, `exposed-r2dbc`, plus extensions (`exposed-java-time`, `exposed-kotlin-datetime`, `exposed-json`, `exposed-migration-*`) [S13]. So the backend needs at minimum `exposed-core` + `exposed-jdbc` (and `exposed-dao` only if using the DAO style; the Ktor tutorial uses both, with DAO [S8]).

**Transactions**: "CRUD operations in Exposed must be called from within a transaction" [S14]. `transaction {}` runs synchronously on the calling thread ("they might block other parts of your application if not managed carefully"); the coroutine-friendly variants are `suspendTransaction()` from both `exposed-r2dbc` and `exposed-jdbc` [S14]. Ktor's official pattern for a coroutine server is a helper that switches to `Dispatchers.IO` and opens a top-level suspend transaction per repository call:

```kotlin
suspend fun <T> withTransaction(block: suspend JdbcTransaction.() -> T): T =
    withContext(Dispatchers.IO) { inTopLevelSuspendTransaction { block() } }
```

used as `override suspend fun allTasks(): List<Task> = withTransaction { TaskDAO.all().map(::daoToModel) }` [S8]. That is the key transaction-scope decision: **one transaction per repository method call, not one per HTTP request** — the Ktor tutorial wraps each repository method in its own `withTransaction` [S8], and Exposed's nesting semantics (nested `transaction {}` shares the parent's transaction resources by default; independent nesting requires `useNestedTransactions = true` and uses SAVEPOINTs, which "may affect performance") make per-call transactions the predictable choice [S14].

**Not leaking Exposed into routes**: in the tutorial, routes see only the `TaskRepository` interface returning plain `Task` models; `TaskTable`, `TaskDAO`, and the `daoToModel` mapper live in a separate `db` package; the DAO entity type never crosses into route code [S8]. Ktor's DDD section codifies it as a rule: "Repositories abstract persistence and expose operations for retrieving or saving aggregates. Their implementations live in the infrastructure layer, but the interfaces belong to the domain" [S1]. Ktor Chat pushes it to module granularity — a dedicated `db` module holds "exposed database schema types and repository implementations," and `core` holds the domain interfaces [S19]. In a modulith, the same rule applies per module: `repository` interface + domain model in the module's API surface, Exposed `Table`/`DAO`/mapper in the module's internals [S1][S8].

### 8. Testing seams: routes without a DB, and fakeable repositories

Ktor's testing engine runs calls "directly without starting a real web server or binding to sockets" via `testApplication {}`, with a preconfigured HTTP client for asserting status/body, explicit module loading (`application { … }`), per-test `routing {}`, and `externalServices {}` to mock external hosts [S9]. Combined with the DI plugin, the official tutorial tests routes against an in-memory repository with zero DB and zero sockets:

```kotlin
suspend fun Application.configureTestApp() {
    dependencies { provide<TaskRepository> { FakeTaskRepository() } }
    configureSerialization(); configureStatusPages(); configureRouting()
}
class ServerTest {
    @Test fun newTasksCanBeAdded() = testApplication {
        application { configureTestApp() }
        // client.post("/tasks") … assert status + list contents
    }
}
```

[ S8][S6]. The three seams that make this work: (1) `suspend` repository interface methods, so fakes are trivial and real implementations can hop dispatchers; (2) DI registration by interface, so "many different implementations can be injected" (Ktor's own words) — production registers `PostgresTaskRepository`, tests register `FakeTaskRepository`; (3) domain/service code depending on the repository interface, never on Exposed [S8][S1]. For pure unit tests of service logic, the same interface means fakes without any Ktor machinery — matching this repo's existing convention of injected callables over mocking (repo doc `docs/agents/testing.md`).

### 9. Serialization boundary and wire DTOs (when DTOs are not shared with the app)

The wire boundary is Ktor's `ContentNegotiation` + `kotlinx.serialization`: install the plugin, `json()` (configurable via `JsonBuilder`, e.g. `ignoreUnknownKeys`), receive with `call.receive<T>()` and respond with `call.respond(obj)`, where `T` is a `@Serializable` data class [S10]. kotlinx.serialization supports "all platforms, including JVM, JavaScript, and Native"; JSON is the **stable** format library (CBOR/ProtoBuf/etc. are experimental) and `@Serializable` classes are fully supported [S15].

When DTOs are **not** shared with the app — the human's constraint — the consequences are mild and Ktor's docs already describe the split: the layered structure explicitly distinguishes `domain/` ("Domain models and aggregates") from `dto/` ("Data transfer objects") [S1]. The per-module shape is: `@Serializable` wire DTOs live in the feature module's API surface (used by routes), domain models stay serialization-free, and a mapper converts between them at the route/service boundary (the tutorial's `daoToModel` is the persistence-side example of the same idea [S8]). Exposed rows/DAOs never cross into routes (Finding 7), so the JSON surface is fully controlled by `@Serializable` DTOs [S10][S8]. Since the app is a separate Gradle build, "not shared" is the *default*, not something to engineer around — each side declares its own wire model, and the API contract is the JSON shape (which this repo already spec'd in `docs/design/api-surface.md`).

**Error handling at the same boundary**: the `StatusPages` plugin maps thrown exceptions and status codes to responses — `exception<Throwable> { call, cause -> … }`, plus `status(...)` and `statusFile(...)` handlers [S11]. Ktor's tutorial shows the boundary working with serialization: bad JSON surfaces as `JsonConvertException`, caught in the route and answered `400 BadRequest`; a duplicate-task `IllegalStateException` becomes `400`; missing resources become `404` [S8]. The pattern that keeps the boundary clean: domain/repository failures throw typed exceptions; StatusPages converts them to HTTP responses, so routes stay thin and wire formats (including the DTO shape and error body) are decided in exactly one place [S11][S8].

### 10. Synthesis against the constraints

| Constraint | What wins | Source |
|---|---|---|
| No god package | Modulith (Gradle modules per context); packages enforce nothing, Gradle enforces everything | [S1][S16] |
| No shared DTOs | Per-module `@Serializable` DTOs; separate `app/` and `backend/` builds make sharing opt-in | [S1][S10], sibling research |
| No presentation-data-domain layers | Feature-style organization *inside* each module (routes+service+repo interface+DTO+domain together); the only hard seam is repository-interface ↔ Exposed impl | [S1][S8] |
| Scalable / maintainable over years | Modulith scales by adding a module; Ktor docs say single-module "does not scale well" | [S1] |
| Testable without DB | Repository interface + DI plugin + `testApplication` + fakes | [S8][S6][S9] |
| Small learning surface | Start with 2–3 modules; "small services… only a few modules and simple dependency injection" | [S1][S16] |

## Recommendation

**Adopt the modular monolith ("modulith") as the backend architecture: one Gradle build under `backend/` with a thin assembly module plus one Gradle module per bounded context (start with `concepts`, `progress` — mirroring the settled API surface), each module organized feature-style (routes, service, repository interface, Exposed implementation, wire DTOs, domain model in one place) and all loaded into a single Ktor application via `ktor.application.modules`.**

Supporting decisions, from the primary sources:

1. **Structure** — modulith, per Ktor's own documentation of the pattern [S1]; mechanics per Gradle's multi-project docs [S16]; structure cribbed from the official Ktor Chat sample (`core`/`server/*`/`db` split) [S19].
2. **DI** — Ktor's built-in `ktor-server-di` plugin: register repository implementations and services, resolve by interface, override in tests. This is what Ktor's official Ktor+Exposed tutorial teaches and removes the need for a third-party container [S3][S8][S6][S21].
3. **Persistence** — Exposed (`exposed-core` + `exposed-jdbc`, + `exposed-dao` only if DAO style) behind a `suspend` repository interface; per-repository-call `withTransaction` with `Dispatchers.IO` + `inTopLevelSuspendTransaction` [S13][S14][S8]; Exposed `Table`/`DAO`/mappers confined to the module internals, never in routes [S8][S1].
4. **Wire boundary** — `ContentNegotiation` + kotlinx.serialization with per-module `@Serializable` DTOs mapped to/from domain models; `StatusPages` as the single exception→HTTP boundary [S10][S11][S8].
5. **Testing** — `testApplication` + fake repositories registered via the DI plugin; integration tests against real Postgres stay out of default runs, consistent with repo conventions [S9][S6].

## Trade-offs

- **What it costs to pick the modulith**: Gradle multi-module boilerplate (settings file, per-module build files, version catalog) is a fixed overhead the single-module baseline (candidate 4) doesn't pay [S16]. For a genuinely tiny codebase the feature-package baseline is cheaper *now*; the modulith pays off the moment a second domain appears, because Gradle (not willpower) enforces the no-god-package and no-cross-import boundaries [S16][S1]. Mitigation: start with exactly two domain modules plus the assembly module, and add modules only when a real seam shows up.
- **What strict layering/clean/hexagonal costs**: explicit boundary objects and DIP machinery at every ring crossing (output ports, mappers, adapter interfaces) [S18] — ceremony the human already rejected. The modulith keeps the *valuable* part (domain and repository interfaces independent of Ktor and Exposed, per Ktor's DDD section [S1] and the tutorial's interface-injection [S8]) without adopting the full onion.
- **What the built-in DI plugin costs**: it is a new first-party surface, so it is younger than Koin; Koin's Ktor integration is mature and documented [S21]. The risk is low — the plugin's registration/resolution/testing API is small and Ktor's official tutorial uses it as the default [S8][S3].
- **Per-call vs per-request transactions**: per-repository-call transactions (the tutorial's pattern) are simple and correct for a single-user app, but a multi-step service that must be atomic needs an explicit outer transaction — Exposed's nested-transaction sharing semantics make that possible, and independent nesting via SAVEPOINT costs performance [S14].
- **Not sharing DTOs costs**: duplicated model definitions (app-side and backend-side) and hand-maintained mapping, instead of one shared `@Serializable` model. The prior research recommended shared DTOs [prior research: `backend-stack-ktor-vs-fastapi.md`]; the human rejected that, and the separate `app/`/`backend/` Gradle builds make the duplication explicit and cheap to maintain [sibling research].

## Open questions

1. **Exposed DAO vs DSL for this project.** The README documents both approaches and the DAO is JDBC-only [S13]; the Ktor tutorial uses DAO [S8]. The decision (DAO entities vs pure DSL `ResultRow` + mappers) affects how much mapping code the repository layer carries — worth a ticket but not an architecture blocker.
2. **Maturity of `ktor-server-di`.** The docs present it as standard (registration, resolution, config, scoping, lifecycle, test override) [S3]–[S7], but it is the youngest piece of the stack; if it proves unstable in practice, the documented fallback is dependency-as-module-parameter or `Application.attributes`, both still first-party [S2].
3. **Where raw Postgres FTS lives.** The prior stack decision noted Exposed exposes no FTS DSL, so PostgreSQL full-text search needs hand-written SQL inside the repository layer [prior research: `backend-stack-ktor-vs-fastapi.md`]. The modulith isolates that to the relevant module's repository internals — no new architecture needed, but the FTS implementation itself is a separate decision.
4. **Module granularity for auth.** Authentication is a cross-cutting concern (JWT/API-key for the phone app + the ingest CI job); Ktor Chat puts admin/auth in its own `server/admin` module [S19]. Decide whether auth is a third module or lives in the assembly module.
