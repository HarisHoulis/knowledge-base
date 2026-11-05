---
domain: system-design
subdomain: source-control-infrastructure
concept: client-server-source-control
title: How Anthropic Redesigned Source Control with Scion
sources:
  - title: "How Anthropic Redesigned Source Control"
    url: "https://blog.bytebytego.com/p/how-anthropic-redesigned-source-control"
    author: "ByteByteGo"
    date: "2026-11-04"
---

# How Anthropic Redesigned Source Control with Scion

Anthropic's coding agents generate code faster than its Git-based infrastructure can support it. Merged changes grew from roughly 2,500 per day in May 2026 to over 30,000 per day by September, the main branch history is close to 100 GB, and CI performs about 25 million checkouts per day. A naive transfer of a compressed working copy per checkout would generate over 600 PB of traffic daily, so the system must both accept changes quickly and distribute code to huge numbers of consumers.

Git's local independence became a liability for this workload. Anthropic tried shallow clones, sparse checkouts, partial clones, internal mirrors, and repository seeds, at peak operating several hundred internal mirrors that had to be kept in sync, while seeds went stale and partial-data clients struggled with history queries. Scion instead makes the server responsible for repository operations: it answers history queries, computes diffs, creates commits, and performs merges and rebases, while the client (scn) keeps a limited cache and prepares files on disk. There is no separate push step, and no fully materialized repository on any single server.

Changes are recorded as changesets: durable records of files changed relative to the first parent, with references to contents, parent info, and author details. Metadata lives in Spanner, compressed file contents in cloud object storage, and the root tree is derived by the server. Content-addressing makes objects immutable, so caches need no freshness checks. Scaling combines shared source control APIs with a cache hierarchy: jobs talk to a node-local scion-daemon, misses go to the regional scion-cache, and only then to authoritative servers, with all layers sharing the same object-request interface to contain failures.

The team of seven built both Scion and the Antique code review tool. Developers rated Claude as better at writing code than themselves but remained critical for understanding inter-system components and design trade-offs, often steering Claude away from certain paths. Claude's speed also made Scion one of the most well-tested codebases the team has produced.

- Git's self-contained clones and mirror/seed workarounds couldn't keep up with ~30,000 merges per day and ~25 million CI checkouts per day
- Scion moves history, diff, commit, merge, and rebase operations to a distributed server, eliminating the separate push step
- Changesets record changed files relative to the first parent, with metadata in Spanner and contents in object storage
- Content-addressed immutable objects enable shared caching across a daemon, regional cache, and authoritative server hierarchy
- A seven-person team built Scion and Antique, with developers focusing on system-level design and trade-offs while Claude wrote most of the code