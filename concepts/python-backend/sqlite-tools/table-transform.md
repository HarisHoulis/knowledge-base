---
domain: python-backend
subdomain: sqlite-tools
concept: table-transform
title: sqlite-utils 4.2
sources:
  - title: "sqlite-utils 4.2"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
    date: "2026-08-13"
---

# sqlite-utils 4.2

sqlite-utils 4.2 significantly improves the table.transform() feature, which handles complex ALTER TABLE operations by creating a fresh table, copying data, and replacing the old one. The update preserves a much larger array of edge-case schema definitions, including check constraints, unique constraints, and column comments. It also adds new introspection properties for check constraints and includes various smaller enhancements. The release incorporates contributions from multiple community members, though a crashing bug was later discovered and fixed in version 4.2.1.

- table.transform() now preserves check constraints, unique constraints, and column comments when transforming tables.
- New introspection properties for check constraints were added.
- Numerous smaller changes and community contributions are included, with 4.2.1 fixing a crashing bug in 4.2.