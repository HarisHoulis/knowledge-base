---
domain: system-design
subdomain: schema-management
concept: schema-evolution
title: Schema Evolution: Changing the Contract Without Breaking What Runs
sources:
  - title: "Schema Evolution: Changing the Contract Without Breaking What Runs"
    url: "https://blog.bytebytego.com/p/schema-evolution-changing-the-contract"
    author: "ByteByteGo"
    date: "2026-08-20"
---

# Schema Evolution: Changing the Contract Without Breaking What Runs

Schema changes are difficult because multiple versions of a schema are always in play simultaneously. Version overlap arises from rolling deploys, stored data written by older code, third-party clients that refuse to upgrade, and asynchronous messages that are written and read at different times. Only the first is temporary; the rest make compatibility a permanent concern. Schema evolution is therefore about supporting both backward compatibility (new code reads old data) and forward compatibility (old code reads new data), which in turn determines safe deployment order (ByteByteGo, 2026).

Decoding a record always involves two schemas: the one used to write the data and the one the reader was compiled against. Fields missing from either side are either discarded or filled with a default, making additive changes with defaults safe. In contrast, removing or renaming fields, making optional fields required, changing types or cardinality, narrowing validation, or changing units under the same name breaks consumers. Even adding enum values can break consumers with exhaustive branches. Breaking changes require an expand-contract migration, where each step is independently deployable: add a nullable column, dual-write, backfill, verify, switch reads, then writes, and finally drop the old column. Schema registries can enforce compatibility rules at registration time and catch obvious breaking changes early, but they cannot detect semantic changes like unit changes (ByteByteGo, 2026).

Versioning strategies differ by context. Internal APIs allow coordinated breaking changes, while public APIs and mobile clients need explicit versions and long deprecation windows. Relational databases demand expand-contract migrations because all historical rows remain readable. Event logs benefit from schema registries and declared defaults. Finally, removing deprecated schema elements is often skipped because it yields no visible improvement and requires field-level usage data. Instrumentation, scheduling removal dates during design, and treating removal as part of the original work are practical remedies (ByteByteGo, 2026).

- Schema version overlap is permanent, driven by stored data, third-party clients, and asynchronous messages, not just rolling deploys.
- Safe schema changes include adding optional fields with defaults, adding new endpoints/tables/topics, and accepting broader input; breaking changes include removing/renaming fields, making optionals required, changing types, narrowing validation, and changing units.
- Breaking changes should be implemented as expand-contract migrations so each step is reversible and deployable independently.
- Schema registries catch structural incompatibilities early but cannot catch semantic or meaning-changing alterations.
- Deprecation and removal of old schema elements requires explicit instrumentation and scheduling, otherwise dead fields and endpoints persist indefinitely.