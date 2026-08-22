# Backend Stack: Ktor vs FastAPI for the Knowledge-Base Digest App

## Question

Which backend stack should the knowledge-base digest app use? The client is a Compose Multiplatform app (Android + iOS), the backend is a small single-user JSON API over a relational DB with full-text search for ~307 concepts, and it must run on free-tier-friendly hosting. The human is learning Kotlin/Compose Multiplatform and backend architecture **evenly**; the existing content-ingest pipeline (`kb_pipeline/`) is Python.

## Context (fixed constraints)

- Learning exercise: learn Kotlin/Compose Multiplatform **and** backend architecture evenly.
- Client: Compose Multiplatform (Android + iOS).
- Existing ingest pipeline in this repo is Python (`kb_pipeline/`).
- Single user, no scaling. Backend is a small JSON API over a relational DB with FTS for ~307 concepts.
- Must run on free-tier-friendly hosting.

## Sources

- [Ktor: Client engines (multiplatform client support)](https://ktor.io/docs/client-engines.html)
- [Ktor: Content negotiation and serialization in Ktor Server](https://ktor.io/docs/server-serialization.html)
- [Ktor: Deployment (fat JARs, Docker, containers)](https://ktor.io/docs/server-deployment.html)
- [Kotlin Multiplatform — official page (KMP as backend + client story)](https://kotlinlang.org/docs/multiplatform.html)
- [JetBrains Exposed — README (official ORM, supported databases)](https://github.com/JetBrains/Exposed)
- [Exposed source tree (exposed-core functions)](https://github.com/JetBrains/Exposed/tree/main/exposed-core/src/main/kotlin/org/jetbrains/exposed/v1/core)
- [SQLAlchemy 2.0 PostgreSQL dialect docs — Full Text Search](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)
- [PostgreSQL docs — Chapter 12: Full Text Search](https://www.postgresql.org/docs/current/textsearch-intro.html)
- [FastAPI — Features (OpenAPI, auto docs, client codegen)](https://fastapi.tiangolo.com/features/)
- [FastAPI — Deployment](https://fastapi.tiangolo.com/deployment/)
- [Railway — Pricing (free tier)](https://railway.com/pricing)
- [Fly.io — Resource Pricing (free-tier status)](https://fly.io/docs/about/pricing/)

## Findings

### 1. Multiplatform client interop — Ktor shares code; FastAPI uses codegen

The Ktor HTTP client is explicitly multiplatform: it "runs on JVM, Android, JavaScript (including WebAssembly), and Native targets," with per-platform engines (`OkHttp`/`Android` for Android, `Darwin` for iOS) and a shared-`commonMain` API. On the server, Ktor content negotiation uses `kotlinx.serialization` (`@Serializable` data classes) for JSON. The same `@Serializable` DTOs and the client API can therefore live in a KMP shared module reused by the Android and iOS clients — one data-model definition for both the app and the backend.

JetBrains' KMP page frames server-side Kotlin explicitly around Ktor: "Use a framework like Ktor to get familiar APIs not just on the server, but also on the client, and maximize the amount of code and knowledge you can reuse."

FastAPI is built on OpenAPI and JSON Schema and enables "automatic client code generation in many languages" (per FastAPI features), but this is generated code, not shared Kotlin — the DTOs are defined in Python and the client is regenerated, not shared.

### 2. Relational DB + FTS — SQLAlchemy has first-class Postgres FTS; Exposed does not

Both stacks support the relational DBs in play (Postgres/MySQL/SQLite) via mature libraries:

- **FastAPI + SQLAlchemy:** SQLAlchemy 2.0's PostgreSQL dialect documents a Full Text Search section out of the box — `match()`, plus direct use of PostgreSQL FTS functions (`to_tsvector`, `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`, `websearch_to_tsquery`, `ts_headline`) and the `TSVECTOR`/`TSQUERY` types. PostgreSQL provides FTS natively (`tsvector`/`tsquery`, stemming, stop words, ranking, phrase operators, GIN indexes).
- **Ktor + Exposed:** Exposed (JetBrains' official Kotlin SQL library) supports Postgres, MySQL, and SQLite via JDBC. However, its SQL DSL (`exposed-core`) exposes **no full-text-search API** — the function set is arrays/math/vector; there is no `tsvector`, `to_tsquery`, or FTS `match` construct. PostgreSQL FTS would require hand-written raw SQL (`exec`) outside the DSL, since Postgres' FTS is not SQL-standard and has no Exposed wrapper.

So: for "JSON API over a relational DB with FTS", FastAPI/SQLAlchemy gives FTS for free; Ktor/Exposed makes you write raw SQL for the FTS part. For ~307 concepts this is small either way, but it is a real convenience/ergonomics gap on the Ktor side.

### 3. Deployment on free-tier hosting — both fit; JAR is simpler, Python is lighter

- **Ktor:** packages as a single fat JAR or Docker image via the Ktor Gradle plugin; deployable to any cloud service that accepts a JAR or container. Single `java -jar` artifact, no runtime dependencies to install on a VPS.
- **FastAPI:** standard ASGI app run under Uvicorn (optionally with Gunicorn workers) inside a container or Python environment; a Python env/venv must exist on the host.

Free-tier providers (as of Aug 2026):

- **Railway:** Free tier is $0/month with $1/month usage credits, up to 1 vCPU / 0.5 GB per service. Both stacks fit; a JVM (Ktor) starts heavier (~150–250 MB baseline) than a Python/uvicorn process, but 0.5 GB is ample for either at single-user load.
- **Fly.io:** No free tier for new signups — pricing is pay-as-you-go (smallest shared machine ≈ $2/month; credit card required). The legacy free allowances were sunset. So Fly is not "free-tier-friendly" for a new project.
- **VPS (e.g., Hetzner/Oracle Free):** Ktor's single JAR is arguably simpler to operate (one binary vs a Python venv + ASGI process manager), though Python is lighter on RAM. Both are trivially deployable.

Conclusion: both deploy fine on Railway's free tier or a small VPS. There is no decisive hosting disadvantage for either stack.

### 4. Learning value — Ktor reinforces the Kotlin learning goal; FastAPI is a second language

The fixed constraint is learning Kotlin/Compose Multiplatform **and** backend architecture evenly:

- **Ktor** keeps the backend in the same language, toolchain (Gradle), and ecosystem as the client — coroutines, `kotlinx.serialization`, shared DTOs, and a shared HTTP stack. Backend work directly reinforces the Kotlin skills being learned for the app, and the KMP shared-code path is the natural payoff of the KMP setup.
- **FastAPI** means the backend is a second language (Python) and the client DTOs are not shared, but it reuses the human's existing Python familiarity (the `kb_pipeline/` is already Python) and has gentler backend ergonomics (Pydantic validation, auto OpenAPI docs, first-class FTS). It teaches backend architecture without adding a new language to the backend itself.

### 5. Alternatives briefly

- **Spring Boot:** same JVM/Kotlin ecosystem, production-grade, but heavyweight (large dependency tree, annotations, runtime footprint); overkill for a single-user JSON API and less aligned with "small, learnable" and free-tier RAM limits.
- **Express/Fastify (Node):** fast to build, but a third language, no shared code with the Kotlin client, and no KMP story.
- **Go:** excellent single-binary deploys and concurrency, but again a separate language with no shared code with the Kotlin client; weaker fit for the stated learning goal.

## Recommendation

Two options for the human to decide between:

1. **Ktor + Exposed + Postgres (recommended for the stated learning goal).** Keeps the entire stack in Kotlin — shared `@Serializable` DTOs and Ktor client reused by the Compose Multiplatform app, one language/toolchain to learn, and a single-JAR deploy on Railway's free tier or a VPS. Cost: PostgreSQL FTS must be written as raw SQL (Exposed has no FTS DSL).
2. **FastAPI + SQLAlchemy + Postgres (recommended if backend-architecture learning and Python reuse trump Kotlin immersion).** Matches the existing Python ingest pipeline, has first-class PostgreSQL FTS in SQLAlchemy, light RAM footprint for free-tier hosting. Cost: no KMP shared code — DTOs are Python/OpenAPI and clients are generated, not shared; backend is a second language.

If the human wants to learn Kotlin/Compose Multiplatform and backend **evenly**, **Ktor** is the stronger choice: every hour spent on the backend compounds Kotlin fluency used by the app. FastAPI is the pragmatic fallback if the human would rather keep backend work in the language they already use for the ingest pipeline and get FTS for free.
