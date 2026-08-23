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

Schema changes are risky because multiple schema versions always coexist in a running system. Reasons include rolling deploys, stored data written by old code, third-party clients still using old versions, and asynchronous messages that are read later or reprocessed. Staging environments mask this version overlap because they run a single version against recent data (ByteByteGo, 2026).

Compatibility is directional: backward compatibility means new code can read old data, while forward compatibility means old code can read new data. Decoding a record uses the writer's schema and the reader's schema; fields present in data but missing in the reader are discarded, and fields in the reader but missing in the data are filled with defaults. Breaking changes include removing or renaming fields, making optional fields required, changing types, and narrowing validation. Adding a field with a default is safe, but adding a required field to a request or removing a field from a response breaks consumers (ByteByteGo, 2026).

Expand-contract migrations break breaking changes into reversible steps: add a nullable column, dual-write, backfill, switch reads, stop writing the old column, and finally drop it. Schema registries store and validate schemas centrally, catching incompatible changes at registration time. Versioning strategies differ by context: internal APIs allow coordinated breaks, public APIs require explicit versioning and deprecation windows, and event logs need schema registry enforcement with defaults on every field. Finally, deprecating unused schema elements is often skipped; field-level usage instrumentation and scheduling removal during the expansion phase help make it happen (ByteByteGo, 2026).

- Multiple schema versions always coexist; compatibility is a property of a pair of versions and the data flow direction.
- Adding a field with a default is usually non-breaking; removing or renaming a field, or making it required, breaks consumers.
- Expand-contract migrations let breaking changes be deployed in individually safe, reversible steps.
- Schema registries validate schemas against previous versions, but cannot catch semantic changes like unit shifts.
- Deprecation and removal of unused schema elements require explicit scheduling and usage measurement.