---
domain: python-backend
subdomain: sqlite-tools
concept: sqlite-utils-4-2
title: sqlite-utils 4.2
sources:
  - title: "sqlite-utils 4.2"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
    date: "2026-08-13T20:11:29+00:00"
  - title: "sqlite-utils 4.2 release"
    url: "https://github.com/simonw/sqlite-utils/releases/tag/4.2"
    author: "Simon Willison"
    date: "2026-08-13"
  - title: "Crashing bug issue #842"
    url: "https://github.com/simonw/sqlite-utils/issues/842"
  - title: "sqlite-utils changelog"
    url: "https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-2-1"
    author: "Simon Willison"
    date: "2026-08-13"
---

# sqlite-utils 4.2

sqlite-utils 4.2 was released, with a focus on enhancing the table.transform() feature, which enables complex ALTER TABLE operations by creating a new table, copying data, and swapping it in. This release significantly expands the preservation of edge-case schema definitions, including check constraints, unique constraints, and column comments, making transforms more robust for production schemas ([source](https://simonwillison.net/2026/Aug/13/sqlite-utils/)).

The release also adds new introspection properties for check constraints, allowing developers to inspect these constraints programmatically. Numerous smaller improvements and community contributions are included, from contributors such as Bunlong Heng, ethanhawkes-gif, Rami Abdelrazzaq, nyxst4ck, and ikatyal2110 ([source](https://simonwillison.net/2026/Aug/13/sqlite-utils/)).

Shortly after release, a crashing bug was discovered and fixed in version 4.2.1, highlighting the practical caveat that even well-tested tools can have immediate regressions ([source](https://github.com/simonw/sqlite-utils/issues/842)).

- table.transform() now preserves check constraints, unique constraints, and column comments.
- New introspection properties for check constraints were added.
- The release includes contributions from multiple community members.
- A crashing bug was found post-release, fixed in 4.2.1.
- sqlite-utils 4.2 is a significant update for complex schema migrations.