# Which database should hold the concepts for the app?

Question: the KB's concepts move from the filesystem tree (ADR-0001, now to be superseded) into a **canonical** database that is written by the GitHub Actions daily-ingest pipeline and read by the phone app through the backend API. Hosting is already settled as either Supabase Free (managed Postgres + auto REST) or Neon Free + own API on a small Hetzner VPS; the backend stack is settled as Ktor + Exposed + Postgres or FastAPI + SQLAlchemy + Postgres. Given those constraints, which engine holds concepts, and how is full-text search satisfied?

## Recommendation

**Use PostgreSQL with its native full-text search (`tsvector`/`tsquery`), hosted as managed Postgres — Supabase Free by default, Neon Free as the named alternative.**

Both settled hosting options are already Postgres-compatible and both settled backend stacks already assume Postgres, so the storage layer is Postgres either way. The FTS requirement is satisfied by the engine itself (native, GIN-indexed, stemmed, relevance-ranked), which means **no separate search infrastructure is added**. The only real decision inside Postgres is *which managed host*, and that decision is reversible without touching the DB layer.

- **Supabase Free** is the default because it is the lowest-ops path: managed Postgres plus an auto-generated REST API (PostgREST) the phone can use directly, native Postgres FTS, and a free tier (500 MB) that is ~1000× the projected dataset. Its two quirks are its deciding negatives: free projects **pause after 1 week of inactivity**, and free-tier direct connections are **IPv6-only** (IPv4 clients — i.e. GitHub Actions runners — must connect through the shared pooler).
- **Neon Free** is the alternative and wins whenever we build the own-API path anyway (Ktor/FastAPI on the VPS), or when we want neither quirk: Neon never pauses on inactivity (computes scale to zero after 5 minutes and auto-resume on connection) and its connection endpoints are reachable over IPv4 as well as IPv6. Same 0.5 GB storage allowance, 100 CU-hours/month of compute — far more than a single-user daily ingest needs.
- **Self-hosted Postgres on the Hetzner VPS** is technically possible (identical FTS) but only if we want to own backups, upgrades, and security on a second box — the very ops burden the settled hosting decision removed. Not recommended.

**SQLite + FTS5 is not viable as the canonical networked store.** It is file-based and single-writer, so the "phone app AND CI both write over the network" requirement forces it to live inside the backend process; the backend then becomes the canonical writer and must expose an HTTP write surface for the ingest — the DB is no longer canonical, and the deployment is more complex than the already-settled managed-Postgres path. It would win only if the product pivoted to an offline/local-first app with SQLite embedded in the app itself.

**Everything else is ruled out by the settled constraints** (see "Ruled out" below): non-relational engines (MongoDB, DynamoDB) contradict the settled relational/Postgres path and add a second data model with no benefit at ~307 concepts; vector search (pgvector, Qdrant) answers a different question than lexical FTS over English prose — and pgvector is an extension on the *same* Postgres if semantic search is ever wanted later.

### Assessment against the settled constraints

| Criterion | Postgres + native FTS (Supabase/Neon) | SQLite + FTS5 (embedded in backend) | MongoDB / DynamoDB / vector |
|---|---|---|---|
| Canonical write: app + CI both write/read over network | ✅ Native, both hosts accept network connections | ❌ File-based; must write *through* backend, backend becomes canonical | ❌ Non-relational model breaks settled path |
| FTS quality for English prose | ✅ Stemmed (`tsvector`/Snowball), stop words, phrase search, `ts_rank`/`ts_rank_cd` ranking | ✅ Porter stemmer + `bm25()` ranking — comparable quality | ❌ No native lexical FTS (needs separate search system) |
| BE-stack library support | ✅ First-class in both: SQLAlchemy documents a full FTS surface; Exposed via raw SQL (`exec()`) | ⚠️ Works, but not the settled stack's target | ⚠️ Third-party glue, off-path |
| Free-tier fit | ✅ 500 MB / 0.5 GB ≫ ~80K words; compute trivial | ✅ (file) | ⚠️ / No |
| Ops burden | ✅ Near-zero (managed) | ⚠️ Must run/maintain a backend to host the file | ❌ Extra service or non-relational schema |
| Learning value | ✅ Transferable Postgres/SQL skills | ⚠️ Lower | ❌ Off-path |

---

## Option 1: PostgreSQL + native full-text search (managed)

**Capabilities.** Postgres FTS preprocesses documents into `tsvector` (normalized *lexemes*, stop words removed, positional info kept) and queries into `tsquery`, matched with the `@@` operator; helper functions `to_tsvector`, `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery` build both. Built-in configurations cover many languages (English included), with Snowball-stemmer and Ispell dictionaries, thesaurus and stop-word support; results can be sorted by relevance, including proximity ranking. GIN indexes accelerate search. This is all core engine functionality — nothing to install, and identical on Supabase, Neon, or a self-hosted VPS.

**Reachability / canonical write.** Both settled hosts are networked services:
- **Supabase** connects via standard Postgres connection strings; free-tier *direct* connections are IPv6-only, and the shared pooler (Supavisor) is IPv4 on every tier — so IPv4 clients such as CI runners use the pooler. There is also an auto-generated REST API for the phone.
- **Neon** connects via standard Postgres connection strings (SSL required), reachable over IPv4 and IPv6, and speaks the standard Postgres wire protocol so any Postgres client works.

The ingest pipeline (which already owns fetch + LLM + audit logic) simply replaces its `writer.py` file-writes with parameterized inserts; the app reads via the backend API (or Supabase REST directly). Postgres' single-writer guarantees apply at the DB level, so both writers coordinate through normal transactions.

**BE-stack library support.**
- **SQLAlchemy (fallback stack):** the PostgreSQL dialect documents a first-class FTS surface — `Operators.match()` (emits `text @@ plainto_tsquery('…')`) for simple cases, and the `func` namespace pre-typed with `to_tsvector`, `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`, `websearch_to_tsquery`, `ts_headline`, plus the `TSVECTOR` type and `regconfig` support.
- **Exposed (primary stack):** no FTS-specific DSL is documented; the documented mechanism for database-specific SQL is `Transaction.exec()` for raw strings. FTS queries are therefore hand-written `exec()` SQL (parameterized `?` placeholders are supported). This is a modest, contained cost, not a blocker.

**Free-tier fit.** Supabase Free: 500 MB database, unlimited API requests, 2 active projects, **projects pause after 1 week of inactivity**. Neon Free: 0.5 GB storage, 100 CU-hours/project/month, 5 GB egress, **scale-to-zero after 5 min inactivity (auto-resumes)**; exceeding compute/egress suspends compute until the next cycle, exceeding storage blocks writes. Both are far beyond a single-user KB (~307 concepts, ~80K words — order 1 MB of body text), and a once-daily ingest keeps Supabase well inside its activity window.

**Ops burden.** Near-zero: backups, TLS, and patching are the vendor's. The one manual operational risk is Supabase's 1-week-inactivity pause (resume is a dashboard action), which only bites if the daily ingest ever stops for a week; Neon's scale-to-zero avoids even that.

## Option 2: SQLite + FTS5

**Capabilities.** FTS5 is a mature full-text engine: `MATCH` queries, `ORDER BY rank` with the built-in `bm25()` ranking function, the `porter` tokenizer for English stemming, phrase/NEAR/prefix/boolean queries, and `highlight()`/`snippet()`. For English prose its quality is comparable to Postgres FTS.

**Why it cannot be the canonical store here.** SQLite's own guidance is decisive: "If there are many client programs sending SQL to the same database over a network, then use a client/server database engine instead of SQLite", and its checklist's first question is "Is the data separated from the application by a network? → choose client/server." SQLite is a single-writer-per-file engine. The settled architecture has two *independent* writers (the phone app via the backend, and the GitHub Actions ingest) separated from the data by a network. To satisfy that, the `.db` file must be embedded on the backend host, the backend becomes the only process that can write, and the ingest must reach it through an HTTP write endpoint rather than a DB connection. The DB then has no canonical identity of its own — the backend does. It would win only in an offline/local-first design where SQLite is embedded in the mobile app itself.

**Other costs.** It adds a backend-owned write API that the settled Postgres path does not need, and it is off the already-settled Postgres-compatible hosting and backend path. Nothing about FTS5 quality justifies that.

## Ruled out (brief)

- **MongoDB / DynamoDB.** Non-relational engines contradict the settled relational/Postgres path (constraints 1–2) and would add a second data model with no benefit at 307 concepts; neither satisfies the English-FTS requirement from the engine alone.
- **Vector search (pgvector / Qdrant).** The requirement is lexical FTS over English prose, which Postgres FTS answers directly; pgvector does semantic similarity and is explicitly designed to *combine* with Postgres FTS (hybrid search), not replace it. pgvector is a Postgres extension available on both managed hosts, so it can be enabled later on the same database if semantic search is ever wanted — it is an upgrade path, not an alternative. Qdrant would be a separate service, i.e. strictly more infrastructure.

---

## Sources

### PostgreSQL — native full-text search

**PostgreSQL 18 docs, "Introduction to Full Text Search".** Establishes the whole capability set: FTS "identifies natural-language documents that satisfy a query, and optionally sort[s] them by relevance"; regex/LIKE lack "linguistic support" and "provide no ordering (ranking)"; preprocessing parses tokens, normalizes to lexemes (lowercasing, suffix removal) and removes stop words; `tsvector`/`tsquery` types with the `@@` match operator; query builders `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`; "predefined configurations for many languages"; Snowball-stemmer, Ispell, thesaurus, and stop-word dictionaries; proximity-based ranking; and "full text searches can be accelerated using indexes" (GIN/GiST, §12.9).
https://www.postgresql.org/docs/current/textsearch-intro.html

### SQLAlchemy — Postgres FTS support

**SQLAlchemy 2.0 docs, "PostgreSQL dialect — Full Text Search".** Documents the Python-side FTS surface: `Operators.match()` "is hardcoded to generate an expression using the `@@` operator in conjunction with the `plainto_tsquery()` PostgreSQL function"; the `func` namespace "is augmented by the PostgreSQL dialect to set up correct argument and return types for most full text search functions" — `to_tsvector`, `to_tsquery`, `plainto_tsquery`, `phraseto_tsquery`, `websearch_to_tsquery`, `ts_headline` — with the `TSVECTOR` type and `regconfig` selection for index-aware searches.
https://docs.sqlalchemy.org/en/20/dialects/postgresql.html

### Exposed — no FTS DSL; raw SQL path

**JetBrains/Exposed README.** Position: "a lightweight SQL library on top of a database connectivity driver", DSL + DAO APIs; supported databases include Postgres and SQLite. No full-text-search module or API is listed among the documented modules.
https://github.com/JetBrains/Exposed

**Exposed docs, "Working with SQL Strings"** (docs source in the Exposed repo). "Using an SQL string to perform a database operation is possible from inside a transaction block with `.exec()` … which may be useful when specific database commands are required"; parameterized SQL uses `?` placeholders; statement-type overrides exist. This is the documented mechanism for database-specific SQL such as Postgres FTS. (A search of the docs' `Working-with-SQL-Strings.md`, `SQL-Functions.md`, and `DSL-Querying-data.topic` returns no `tsvector`/`tsquery`/FTS-specific API.)
https://github.com/JetBrains/Exposed/blob/main/documentation-website/Writerside/topics/Working-with-SQL-Strings.md

### Supabase Free — limits and connectivity

**Supabase pricing.** Free plan: $0/month, "500 MB database size (Shared CPU • 500 MB RAM)", "Unlimited API requests", "Free projects are paused after 1 week of inactivity", "Limit of 2 active projects". Managed Postgres, auto REST, community support.
https://supabase.com/pricing

**Supabase docs, "Connect to your database".** Direct connection `db.[project].supabase.co:5432` is "on IPv6, or on IPv4 if the project has the IPv4 add-on"; the shared pooler (Supavisor) "is IPv4-only on every project tier". Confirms the connection-string/network modes a CI runner would use.
https://supabase.com/docs/guides/database/connecting-to-postgres

### Neon Free — limits and connectivity

**Neon docs, "Plans".** Free plan: $0/month, 0.5 GB storage/project, 100 CU-hours/project/month, up to 2 CU autoscaling, 5 GB egress, scale-to-zero "After 5 min" (always enabled, cannot disable); running out of compute/egress suspends compute until the next billing period, exceeding the storage cap fails writes; 1-day monitoring retention, community support.
https://neon.tech/docs/introduction/plans

**Neon docs, "Connect from any application".** Standard Postgres connection strings over the public internet (SSL required); "Neon speaks the standard Postgres wire protocol, so any Postgres client works: pg, psycopg2, psql, Prisma, Drizzle, SQLAlchemy, and others"; AWS-hosted projects support both IPv4 and IPv6.
https://neon.tech/docs/connect/connect-from-any-app

### SQLite — FTS5 and the network caveat

**SQLite docs, "FTS5 Extension".** Capability set: virtual-table FTS with `MATCH`, `ORDER BY rank`, built-in `bm25()` ranking, the `porter` tokenizer ("designed for use with English language terms") implementing the Porter stemming algorithm, default `unicode61` tokenizer, phrase/prefix/NEAR/boolean queries, and `highlight()`/`snippet()` auxiliary functions.
https://www.sqlite.org/fts5.html

**SQLite docs, "Appropriate Uses For SQLite".** "SQLite does not compete with client/server databases"; under client/server applications: "If there are many client programs sending SQL to the same database over a network, then use a client/server database engine instead of SQLite … A good rule of thumb is to avoid using SQLite in situations where the same database will be accessed directly (without an intervening application server) and simultaneously from many computers over a network." The checklist's first question is "Is the data separated from the application by a network? → choose client/server." It also documents the legitimate "server-side database" pattern (SQLite embedded in an application server) — the shape this architecture would have to take, at the cost of the backend becoming the canonical writer. Also: "SQLite only supports one writer at a time per database file."
https://www.sqlite.org/whentouse.html

### Vector search — hybrid with FTS, on the same Postgres

**pgvector README.** "Open-source vector similarity search for Postgres"; HNSW/IVFFlat approximate indexes; "Hybrid Search: Use together with Postgres full-text search … ORDER BY ts_rank_cd(textsearch, query)" — i.e. vector search *combines with*, rather than replaces, Postgres FTS; installation notes list managed hosted providers (Supabase, Neon among them).
https://github.com/pgvector/pgvector

### Settled constraints (grounding, not external docs)

**ADR-0001** (`docs/adr/0001-filesystem-tree-over-database.md`) — the decision this supersedes: filesystem tree with `grep` search, no database. The supersession itself is the reason the canonical-write requirement exists.

**CONTEXT.md** — domain model (Concept/Domain/Subdomain), the Daily Ingest workflow writing through the pipeline, and the ~single-user scale this research optimizes for.
