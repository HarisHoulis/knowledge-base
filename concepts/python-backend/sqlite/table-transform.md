---
domain: python-backend
subdomain: sqlite
concept: table-transform
title: sqlite-utils 4.2
sources:
  - title: "sqlite-utils 4.2"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
    date: "2026-08-13T20:11:29+00:00"
---

# sqlite-utils 4.2

sqlite-utils 4.2 focuses on improving the table.transform() feature, which enables complex ALTER TABLE operations by creating a fresh table, copying data across, and then replacing the original (source: https://simonwillison.net/2026/Aug/13/sqlite-utils/). This release expands support for preserving edge-case schema definitions during transformation, including check constraints, unique constraints, and column comments. It also introduces new introspection properties for inspecting check constraints, alongside a variety of smaller changes. The release includes contributions from multiple community members. Shortly after publication, a crashing bug was discovered in 4.2 and fixed in 4.2.1, highlighting the importance of rapid patch releases.

- table.transform() now preserves check constraints, unique constraints, and column comments.
- New introspection properties allow programmatic access to check constraints.
- Release includes contributions from Bunlong Heng, ethanhawkes-gif, Rami Abdelrazzaq, nyxst4ck, and ikatyal2110.
- A crashing bug in 4.2 was fixed in 4.2.1.