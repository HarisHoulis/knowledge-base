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

sqlite-utils 4.2 enhances the table.transform() feature, which enables complex ALTER TABLE operations by creating a fresh table, copying data, and then swapping it in place. The update preserves a broader range of edge-case schema definitions during transformation, including check constraints, unique constraints, and column comments. This improvement addresses previous limitations where such schema details were lost when transforming tables.

The release also adds new introspection properties for check constraints, giving developers programmatic access to these schema definitions. It includes contributions from multiple community members and various smaller changes. Notably, version 4.2 itself contained a crashing bug that was later fixed in 4.2.1, so users are advised to use the latest patch release.

- table.transform() now preserves check constraints, unique constraints, and column comments when recreating tables.
- New introspection properties are available for accessing check constraints programmatically.
- The release includes community contributions and numerous minor improvements.
- A crashing bug in 4.2 was fixed in 4.2.1, making the patch release the recommended version.