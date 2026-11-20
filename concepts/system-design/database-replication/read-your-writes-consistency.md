---
domain: system-design
subdomain: database-replication
concept: read-your-writes-consistency
title: PostgreSQL 19 Adds WAIT FOR LSN for Read-Your-Writes Consistency on Standbys
sources:
  - title: "PostgreSQL 19 Released"
    url: "https://simonwillison.net/2026/Nov/19/postgresql-19/"
    author: "Simon Willison"
    date: "2026-11-19"
---

# PostgreSQL 19 Adds WAIT FOR LSN for Read-Your-Writes Consistency on Standbys

PostgreSQL 19 introduces the WAIT FOR LSN command, which lets a session on a read replica wait until the standby has replayed the write-ahead log up to a given log sequence number (LSN) before running a query. This gives applications that route reads to standbys "read-your-writes" consistency, so a user can read data they just wrote on the primary (Simon Willison, 2026-11-19).

The practical pattern is to capture the LSN after a write with pg_current_wal_insert_lsn(), store it (for example in a signed cookie), and on a later request issue WAIT FOR LSN '<lsn>' WITH (TIMEOUT '0.1s') before reading from the replica. The timeout is optional but causes an error if the replica fails to catch up in time.

Willison notes he first saw this pattern in Wikipedia's MediaWiki, which hand-rolled an equivalent against MySQL replication by saving the primary binlog position in the session and waiting for the replica to catch up before reads. MediaWiki now uses MySQL's WAIT_FOR_EXECUTED_GTID_SET() with a fallback to SOURCE_POS_WAIT().

- PostgreSQL 19's WAIT FOR LSN lets standby sessions wait for WAL replay up to a specific LSN before querying, enabling read-your-writes consistency.
- Capture the LSN with pg_current_wal_insert_lsn() after a write, persist it (e.g., signed cookie), and wait on it before the next read.
- An optional TIMEOUT raises an error if the replica doesn't catch up in time.
- The pattern mirrors MediaWiki's hand-rolled MySQL replication lag handling, now built into PostgreSQL.