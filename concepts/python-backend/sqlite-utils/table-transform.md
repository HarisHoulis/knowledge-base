---
domain: python-backend
subdomain: sqlite-utils
concept: table-transform
title: sqlite-utils 4.2
sources:
  - title: "sqlite-utils 4.2"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
    date: "2026-08-13T20:11:29+00:00"
---

# sqlite-utils 4.2

sqlite-utils 4.2 is a release of the Python utility library for SQLite, announced on Simon Willison's blog. The main focus is on the table.transform() feature, which enables complex ALTER TABLE operations by creating a new table, copying data into it, and then replacing the original. This release significantly improves transform() by preserving a wider range of edge-case schema definitions, including check constraints, unique constraints, and column comments. It also introduces new introspection properties for check constraints, allowing users to programmatically inspect these constraints. The release includes contributions from multiple external contributors. However, a crashing bug was later discovered, which was fixed in version 4.2.1.

- table.transform() supports complex alter table operations by recreating the table and copying data.
- Transformations now preserve check constraints, unique constraints, and column comments.
- New introspection properties were added for check constraints.
- The release includes contributions from several community members.
- Version 4.2 had a crashing bug that was fixed in 4.2.1.