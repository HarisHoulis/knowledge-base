---
domain: system-design
subdomain: data-contracts
concept: schema-evolution
title: Schema Evolution: Changing the Contract Without Breaking What Runs
sources:
  - title: "Schema Evolution: Changing the Contract Without Breaking What Runs"
    url: "https://blog.bytebytego.com/p/schema-evolution-changing-the-contract"
    author: "ByteByteGo"
    date: "2026-08-20"
---

# Schema Evolution: Changing the Contract Without Breaking What Runs

The article explains that schema changes are difficult because multiple schema versions always coexist in a running system. This overlap arises from rolling deploys, stored data written by old code, third-party clients still using old API versions, and asynchronous messages that can be read later or reprocessed. Only rolling deploys are temporary; the other causes make version overlap a permanent feature (ByteByteGo, 2026).

- Schema compatibility is directional: backward compatibility means new code reads old data, while forward compatibility means old code reads new data.
- Adding a field with a default is safe because readers substitute the default for missing data; removing fields, making optional fields required, or changing a field's type/meaning breaks consumers.
- Expand-contract migrations decompose breaking changes into safe steps: add, dual-write, backfill, verify, switch reads, switch writes, then drop the old column.
- Schema registries catch incompatible changes at registration time, but they cannot detect semantic changes like unit changes.
- Versioning strategies depend on control and data lifetime: internal APIs can coordinate, public APIs need explicit versions, and event logs need defaults and registry enforcement.