---
domain: python-backend
subdomain: sqlite
concept: sqlite3-rsync
title: sqlite3_rsync: Database Remote-Copy Tool For SQLite
sources:
  - title: "sqlite3_rsync: Database Remote-Copy Tool For SQLite"
    url: "https://simonwillison.net/2026/Nov/26/sqlite3-rsync/"
    author: "Simon Willison"
    date: "2026-11-26"
---

# sqlite3_rsync: Database Remote-Copy Tool For SQLite

sqlite3_rsync is a tool for copying a snapshot of a SQLite database over an SSH connection to another machine, without first creating a full local duplicate. Normally, snapshot copies require the backup API or VACUUM INTO, both of which need enough disk space to hold a complete copy—a problem on small instances where the database already uses more than half the available disk (https://www.sqlite.org/rsync.html).

The tool also synchronizes an existing copy of a database without re-transmitting the entire thing over the network, working similarly to regular rsync. The replica sends cryptographic hashes for pages or groups of pages to the origin side; the origin returns page content that differs, or requests finer-grain hashes if a multi-page hash does not match. If the two sides start out vastly different, total bandwidth can exceed the database size due to hash-exchange overhead, but the excess is only a few percent at most.

Simon Willison notes he had already written about this application of sqlite3_rsync back in October 2024, when the tool was first released (https://simonwillison.net/2024/Oct/4/sqlite-rsync/).

- sqlite3_rsync copies a SQLite snapshot over SSH without needing a full local duplicate, unlike the backup API or VACUUM INTO.
- It syncs existing copies efficiently by exchanging cryptographic page hashes rather than retransmitting the whole database.
- When origin and replica differ greatly, bandwidth overhead from hash exchange is only a few percent above database size.