---
domain: python-backend
subdomain: database-tooling
concept: alchemy-utils
title: alchemy-utils 0.1a0: A Database-Agnostic sqlite-utils
sources:
  - title: "alchemy-utils 0.1a0"
    url: "https://simonwillison.net/2026/Aug/12/alchemy-utils/"
    author: "Simon Willison"
    date: "2026-08-12"
---

# alchemy-utils 0.1a0: A Database-Agnostic sqlite-utils

Simon Willison released alchemy-utils 0.1a0, a prototype library and CLI that replicates the core API of sqlite-utils (insert, upsert, insert_all, upsert_all, create, update, and table introspection) but is backed by SQLAlchemy, making it work across multiple database engines including PostgreSQL, SQLite, and DuckDB. The project was developed as a rapid AI-assisted coding experiment, using Codex and GPT-5.6 Sol Ultra to build the initial prototype from a few prompts, then iterating with test-driven development. The release includes examples of querying a PostgreSQL database and inserting a large CSV into DuckDB, with performance improvements reducing execution time from nearly an hour to around 35 seconds after optimization.

- alchemy-utils is a new library providing a SQLAlchemy-backed, database-agnostic version of sqlite-utils.
- It supports PostgreSQL, SQLite, and DuckDB through SQLAlchemy engines.
- The core API includes insert, upsert, insert_all, upsert_all, create, update, and table introspection.
- The prototype was built quickly using AI coding agents (Codex and GPT-5.6 Sol Ultra) with a research spike and TDD.
- A large CSV import into DuckDB was optimized from ~1 hour to ~35 seconds using AI-suggested changes.