---
domain: python-backend
subdomain: sqlite-tools
concept: table-transform
title: sqlite-utils 4.2
sources:
  - title: "sqlite-utils 4.2"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
    author: "Simon Willison"
    date: "2026-08-13"
---

# sqlite-utils 4.2

sqlite-utils 4.2 is a release focused on enhancing the table.transform() feature, which enables complex ALTER TABLE operations by creating a fresh table, copying data, and swapping it in. This release significantly expands the range of schema definitions that transform() can preserve, including check constraints, unique constraints, and column comments. Additionally, new introspection properties for check constraints have been added, and numerous smaller improvements are included. The release incorporates contributions from several community members. A crashing bug was later discovered in 4.2 and fixed in 4.2.1.

- table.transform() now preserves check constraints, unique constraints, and column comments.
- New introspection properties for check constraints are added.
- Includes contributions from multiple community contributors.
- A crashing bug in 4.2 was fixed in 4.2.1.