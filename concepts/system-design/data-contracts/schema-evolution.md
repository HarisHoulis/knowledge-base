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

Schema changes are difficult because multiple versions of code and data coexist in any running system. The article explains that rolling deploys, stored data, third-party clients, and asynchronous messages ensure version overlap is permanent, not just a deployment window issue. Compatibility must be understood as a property of pairs of versions: backward compatibility lets new code read old data, while forward compatibility lets old code read new data. These directions determine safe deployment ordering, and decoding relies on two schemas: the writer's and the reader's, with rules for missing or extra fields (ByteByteGo, 2026).

Breaking changes fall into categories: removing something a reader depends on (e.g., deleting or renaming a field, making an optional field required) or redefining a field’s meaning or type. Adding optional fields with defaults is generally safe, but the safety of adding fields to APIs depends on direction: requests and responses break oppositely. For breaking changes, expand-contract migrations decompose the change into individually safe steps: expand with new nullable fields, dual-write, backfill, verify, switch reads, switch writes, then drop the old schema. Schema registries automate compatibility checks by storing schemas and rejecting incompatible changes at registration time, but they cannot catch semantic changes like unit changes (ByteByteGo, 2026).

Versioning strategies differ by context: internal APIs allow coordinated breaking changes, public APIs need explicit versions and deprecation windows, mobile clients require long-term server compatibility, relational databases mandate expand-contract, and event logs benefit from registry enforcement and defaults. Finally, deprecation timelines are often skipped because removal has no visible benefit and risks breaking things, so field-level usage instrumentation and scheduling removal as part of the original work are recommended. The article emphasizes that schema evolution is a permanent feature of distributed systems, and safe changes require planning for version overlap and using the right compatibility guarantees (ByteByteGo, 2026).

- Multiple schema versions always coexist due to rolling deploys, stored data, third-party clients, and async messages; this makes schema evolution a permanent concern.
- Backward compatibility (new code reads old data) vs. forward compatibility (old code reads new data) dictates deployment order: consumers first for backward, producers first for forward.
- Adding fields with defaults is safe; renaming, deleting, changing types, or narrowing validation breaks consumers when the reader depends on the old contract.
- Expand-contract migrations break breaking changes into safe steps (add nullable, dual-write, backfill, verify, switch reads, switch writes, drop old) to allow rollback at each stage.
- Schema registries catch incompatibilities early, but cannot detect semantic changes like unit changes; deprecation removal should be instrumented and scheduled upfront.