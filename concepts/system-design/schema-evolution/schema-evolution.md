---
domain: system-design
subdomain: schema-evolution
concept: schema-evolution
title: Schema Evolution: Changing the Contract Without Breaking What Runs
sources:
  - title: "Schema Evolution: Changing the Contract Without Breaking What Runs"
    url: "https://blog.bytebytego.com/p/schema-evolution-changing-the-contract"
    author: "ByteByteGo"
    date: "Thu, 20 Aug 2026 15:32:18 GMT"
---

# Schema Evolution: Changing the Contract Without Breaking What Runs

Schema changes are notoriously difficult because multiple schema versions are always in play simultaneously. The article explains that version overlap arises not only from rolling deploys but also from stored historical data, third-party clients, and asynchronous messages, making version coexistence a permanent feature. Staging environments fail to catch issues because they run only one version against fresh test data, whereas production runs multiple versions against the same storage and queues. (ByteByteGo, 2026)

Compatibility is directional and defined by the pair of producer and consumer versions. New code reading old data requires backward compatibility, while old code reading new data requires forward compatibility. The decoding process uses two schemas: the writer's schema and the reader's schema, with rules for discarding unknown fields and substituting defaults for missing ones. Field identity also matters—JSON and Avro match by name, so a rename is a breaking change, while Protobuf matches by number and allows renames without breaking messages, but reusing a number can cause silent corruption. (ByteByteGo, 2026)

Breaking changes include deleting or renaming fields, making optional fields required, changing types or cardinality, narrowing validation, and changing units or meaning under the same name. Expand-contract migrations break such changes into individually safe deployment steps, typically involving adding a nullable column, dual-writing, backfilling, and eventually dropping the old column. Schema registries centralize schema storage and automatically check compatibility at registration time, but they cannot catch semantic changes like unit changes, which is why naming fields with units is recommended. (ByteByteGo, 2026)

Versioning strategy depends on how much control a team has over readers and how long old data survives. Internal APIs can coordinate breaking changes, public APIs need explicit versions and deprecation windows, and event logs benefit from registry enforcement and defaults. The article contrasts explicit versioning with additive-only evolution and notes that deprecation is frequently skipped due to lack of observable benefit and missing usage instrumentation. Practical mitigations include measuring field-level usage, scheduling removal during the initial migration, and treating removal as part of the original work. (ByteByteGo, 2026)

- More than one schema version is always active due to rolling deploys, stored data, third-party clients, and async messages, making version overlap permanent.
- Compatibility is directional: backward compatibility means new code reads old data, while forward compatibility means old code reads new data; decoding relies on writer and reader schemas with default substitution.
- safe changes include adding optional fields with defaults, adding new endpoints/tables, and broadening input; breaking changes include removing fields, making optional fields required, and changing types or units.
- Expand-contract migrations sequence breaking schema changes into safe, reversible steps; schema registries automate compatibility checks but cannot detect semantic changes like unit shifts.
- Deprecation timelines are often skipped; measuring usage, scheduling removal upfront, and treating removal as part of the original work can increase the chance of actual cleanup.