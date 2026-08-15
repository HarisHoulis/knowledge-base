---
domain: python-backend
subdomain: database-utilities
concept: alchemy-utils
title: alchemy-utils 0.1a0
sources:
  - title: "alchemy-utils 0.1a0"
    url: "https://simonwillison.net/2026/Aug/12/alchemy-utils/"
    date: "2026-08-12T19:51:30+00:00"
---

# alchemy-utils 0.1a0

The post announces the alpha release of alchemy-utils, a new Python library that aims to provide the same core API as sqlite-utils but backed by SQLAlchemy for multiple database engines [1]. The project was created as a research spike with the help of Codex and GPT-5.6 Sol Ultra, using a test-driven approach against PostgreSQL, SQLite, and DuckDB [1].

The post demonstrates practical CLI usage, such as listing rows from a local PostgreSQL table and inserting a CSV of San Francisco trees into DuckDB with automatic schema detection. It also notes that an initial slow insert was optimized, reducing runtime from nearly an hour to about 35 seconds [1].

- alchemy-utils is a database-agnostic reimplementation of sqlite-utils, built on SQLAlchemy.
- Supports multiple database engines including PostgreSQL, SQLite, and DuckDB.
- Developed with AI coding agents (Codex and GPT-5.6 Sol Ultra) using TDD and uv.
- Provides a CLI for common operations like `rows` and `insert`.
- Released as an early alpha (0.1a0).