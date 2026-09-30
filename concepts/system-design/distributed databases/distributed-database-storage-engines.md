---
domain: system-design
subdomain: distributed databases
concept: distributed-database-storage-engines
title: Distributed Databases with Peter Mattis
sources:
  - title: "Distributed databases with Peter Mattis"
    url: "https://newsletter.pragmaticengineer.com/p/distributed-databases-with-peter"
    author: "Gergely Orosz"
    date: "2026-09-30"
---

# Distributed Databases with Peter Mattis

Peter Mattis — co-founder and CTO of Cockroach Labs, original creator of GIMP, and former Google engineer on Gmail and distributed storage — walks through his path from open source to Google to building a distributed database, and how AI has brought him back to writing code (Pragmatic Engineer podcast). His early career included nearly declining Sergey Brin's Google offer over the commute, and nearly shelving GIMP weeks before launch after seeing a pre-announcement of a more ambitious competitor. His takeaway: "There's always going to be someone else working on your idea... assume that dozens of people have the same idea you have, but most won't ship it."

The episode traces a recurring data-structure theme: B-trees powered Gmail's thread and unread-count tracking, and later a std::map replacement Mattis wrote at Google (the red-black tree's two-pointers-per-node made it large and cache-unfriendly, whereas a B-tree exploited spatial locality). He did similar work on Go's map with a Swiss Table implementation that later landed in the Go library. As he puts it, if you squint hard, everything in distributed databases and storage starts looking like a B-tree — the subject of the paper "The Ubiquitous B-Tree." At Google, he also worked on Colossus, which pioneered Reed–Solomon erasure coding in a distributed file system, reducing storage overhead by 33% while increasing redundancy.

On CockroachDB's design: Colossus was append-only, so Spanner (built on top of it) inherited that constraint, which rules out B-trees (they need file mutation) and favors log-structured merge trees that append writes to a log for durability. Google popularized LSMs with LevelDB; RocksDB forked it and was CockroachDB's early storage engine until Mattis wrote and open sourced Pebble in 2019, now CockroachDB's engine. For consensus, CockroachDB uses three replicas by default (up to five for some system tables), because one replica can't recover from a crash and two can't tell whether the other received the last write — more replicas mean higher latency.

A substantial thread covers AI and engineering practice: Mattis is reviewing less code and predicts "we're materially going to stop looking at the code in the same way we don't look at assembly anymore." Non-engineers at Cockroach Labs built roughly 1,000 internal apps in a couple of months on an internal app-building platform ("an internal Lovable"), surprising the engineering team. He says flow still exists with AI but feels different — "a bit less intense, but you're managing more things cognitively," like a professor with a swarm of research assistants running many experiments in parallel.

- B-trees recur throughout Mattis's work — Gmail's thread tracking, his std::map replacement at Google, and CockroachDB's range index; he replaced red-black-tree-based std::map with a faster, smaller B-tree and later did a Swiss Table implementation for Go's map that landed in the Go library.
- Append-only storage (Colossus, and therefore Spanner) rules out B-trees and favors log-structured merge trees; CockroachDB used RocksDB before Mattis wrote Pebble in 2019, now its storage engine.
- CockroachDB defaults to three replicas for consensus: one can't recover from a crash, and with two neither knows if the other received the last write; more replicas increase latency.
- Mattis predicts code review as practiced today will largely stop — "we're materially going to stop looking at the code in the same way we don't look at assembly anymore."
- Non-engineers at Cockroach Labs built ~1,000 internal apps in a couple of months on an internal app-building platform, mirroring how OpenAI's non-engineers shifted most token spend from ChatGPT to Codex within four months.