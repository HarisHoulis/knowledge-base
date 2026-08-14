---
domain: python-backend
subdomain: database-utilities
concept: alchemy-utils
title: alchemy-utils 0.1a0
sources:
  - title: "alchemy-utils 0.1a0"
    url: "https://simonwillison.net/2026/Aug/12/alchemy-utils/"
    author: "Simon Willison"
    date: "2026-08-12"
---

# alchemy-utils 0.1a0

Simon Willison announces the alpha release of alchemy-utils, a database-agnostic Python library and CLI utility inspired by his earlier sqlite-utils. The project was prototyped as a 'shower project' using coding agents Codex and GPT-5.6 Sol Ultra, with the goal of mirroring the core sqlite-utils API—insert, upsert, insert_all, upsert_all, create, update, and table introspection—but backed by SQLAlchemy to support multiple database engines. The prototype was tested against PostgreSQL, SQLite, and DuckDB, and the development followed red/green TDD with pytest, using uv for project initialization.

The article demonstrates two practical usage examples: listing rows from a PostgreSQL table with 'alchemy-utils rows', and inserting a large CSV of San Francisco trees into a DuckDB database with automatic schema creation. The author notes that the initial CSV insertion took nearly an hour, but after having Codex optimize the code, it was reduced to around 35 seconds. The alpha release is available on GitHub, and the post includes a link to the release and a gist with the prompts used.

- alchemy-utils is a new alpha library that replicates sqlite-utils' core API using SQLAlchemy, enabling support for PostgreSQL, SQLite, DuckDB, and other engines.
- The project was created with the help of AI coding agents (Codex and GPT-5.6 Sol Ultra) in a research spike, with iterative prompts and frequent commits.
- It provides a CLI for database operations, such as 'rows' to list table rows and 'insert' to load CSV data with automatic schema creation.
- Performance optimization was done via AI-assisted refactoring, drastically reducing the time to load a large CSV into DuckDB from nearly an hour to ~35 seconds.