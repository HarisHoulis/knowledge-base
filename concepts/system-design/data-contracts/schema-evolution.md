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

Schema changes are deceptively risky because multiple schema versions are always in play at the same time. Rolling deploys, stored data, third-party clients, and asynchronous messages mean old and new code read and write the same data concurrently, so version overlap is a permanent feature rather than a deployment-window issue. This explains why migrations that pass staging can still cause production failures, and why better deployment tooling cannot fully solve the problem (ByteByteGo).

Compatibility is directional and must be considered for each producer–consumer pair. Backward compatibility (new code reads old data) lets consumers be upgraded first, while forward compatibility (old code reads new data) lets producers go first. Decoding relies on the writer’s schema and the reader’s schema, with fields missing from the reader filled by defaults and unrecognized fields discarded. Adding a field with a default is generally safe, while deleting or renaming a field (in name-based formats like JSON/Avro) is breaking, as are type changes and narrowing validation. Input and output contracts break in opposite directions: adding a required request field breaks callers, adding a response field is safe (ByteByteGo).

For breaking changes, expand-and-contract migrations decompose the change into safe, individually deployable steps: expand with a nullable column, dual-write and backfill, then switch reads, switch writes, and drop the old column. Schema registries centralize schema versions, embed identifiers in messages, and reject incompatible changes at registration time—catching issues before production. Versioning strategies vary by context: internal APIs can coordinate breaks, public APIs need explicit versions and deprecation windows, and event logs benefit from registry enforcement and defaults on every field. Successful deprecation requires instrumentation, scheduled removal dates, and treating removal as part of the original work, since skipping it leaves no failing signal (ByteByteGo).

- Version overlap is permanent due to rolling deploys, stored data, third-party clients, and async messages—so schema evolution must be handled as an ongoing constraint.
- Compatibility is directional: backward (new code reads old data) and forward (old code reads new data) dictate the safe deployment order of producers and consumers.
- Adding a field with a default is safe; removing or renaming fields (in name-based formats), changing types, and narrowing validation break consumers.
- Expand-contract migrations decompose breaking changes into reversible steps, and schema registries validate changes before they reach production.
- Deprecation requires explicit instrumentation, scheduled removal dates, and treating cleanup as part of the original work to actually happen.