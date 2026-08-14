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

The sqlite-utils 4.2 release focuses on enhancing the table.transform() feature, which enables complex ALTER TABLE operations by creating a fresh table, copying data across, and then dropping and replacing the original table. This approach allows for schema changes that SQLite's native ALTER TABLE cannot directly handle. According to the [release announcement](https://simonwillison.net/2026/Aug/13/sqlite-utils/), the updated transform() now preserves a much broader set of edge-case schema definitions, including check constraints, unique constraints, and even column comments.

Additionally, the release introduces new [introspection properties](https://sqlite-utils.datasette.io/en/stable/python-api.html#checks) for check constraints, making it easier to inspect and work with these schema elements programmatically. The release includes contributions from several external developers: Bunlong Heng, ethanhawkes-gif, Rami Abdelrazzaq, nyxst4ck, and ikatyal2110. It was later discovered that version 4.2 contained a crashing bug, which was promptly fixed in the follow-up release 4.2.1.

- table.transform() now preserves check constraints, unique constraints, and column comments during table rebuilds.
- The transform() method enables complex schema changes by recreating the table and copying data.
- New introspection properties were added for check constraints.
- The release incorporates contributions from five external contributors.
- A crashing bug in 4.2 was fixed in the subsequent 4.2.1 release.