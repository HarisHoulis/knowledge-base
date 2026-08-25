---
domain: system-design
subdomain: data-contracts
concept: schema-evolution
title: Schema Evolution: Changing the Contract Without Breaking What Runs
sources:
  - title: "Schema Evolution: Changing the Contract Without Breaking What Runs"
    url: "https://blog.bytebytego.com/p/schema-evolution-changing-the-contract"
    author: "ByteByteGo"
    date: "Thu, 20 Aug 2026 15:32:18 GMT"
---

# Schema Evolution: Changing the Contract Without Breaking What Runs

Schema changes are inherently risky because multiple schema versions are always in play simultaneously. Rolling deploys, stored data, third-party clients, and asynchronous messages mean old and new code read and write the same data long after a migration. This makes version overlap a permanent feature, not just a release-time concern, and explains why staging rarely exposes schema-related issues. Compatibility depends on the direction of data access: backward compatibility lets new code read old data, while forward compatibility lets old code read new data. The decoder resolves differences by discarding unknown fields and substituting defaults for missing ones, which is why adding a field with a default is usually safe and renaming or removing a field can break consumers.

- Multiple schema versions coexist due to rolling deploys, historical data, old clients, and queued messages, making overlap permanent.
- Compatibility is directional: backward (new reads old) vs. forward (old reads new) determines safe deployment order.
- Adding a field with a default is safe; removing, renaming, or redefining a field breaks consumers depending on the field matching method.
- Expand-contract migrations decompose breaking changes into individually safe steps, with dual writes and backfills.
- Schema registries catch incompatible changes at registration time, but cannot detect semantic changes like unit shifts.