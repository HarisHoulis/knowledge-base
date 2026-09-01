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

Schema changes are deceptively risky because multiple schema versions are always in play. Rolling deploys, long-lived stored data, third-party clients, and asynchronous messages ensure that data written under one schema is read under another. Staging environments rarely expose these issues because they run a single version against recent test data, so failures often appear only after production deployment (ByteByteGo, "Schema Evolution"). Compatibility must be considered as a property of version pairs and data access direction: backward compatibility means new code can read old data, while forward compatibility means old code can read new data. These directions determine safe deployment order (ByteByteGo, "Schema Evolution").

Decoding relies on two rules: unknown fields are discarded, and missing fields are filled with defaults. Adding a field with a default is usually safe, but renames or type changes can break consumers depending on the serialization format (e.g., name-based vs. number-based field identity). Breaking changes cluster into removals of something readers depend on and redefinitions of existing fields. Input and output contracts break in opposite directions: adding a required field to a request is breaking, while removing a response field is breaking. Expand-contract migrations decompose breaking changes into individually safe steps, such as adding a nullable column, dual-writing, backfilling, and finally dropping the old column (ByteByteGo, "Schema Evolution").

Schema registries centralize schema versions and reject incompatible registrations before production, shifting failures to the producer's deployment. However, they cannot catch semantic changes like unit changes. Versioning strategies vary by context: internal APIs can coordinate breaking changes, public APIs need explicit versions and deprecation windows, mobile clients require long-term server-side compatibility, and event logs benefit from registry enforcement. Deprecation timelines are often neglected because removal yields no visible improvement and carries asymmetric risk, but field-level usage instrumentation and scheduled removal can help (ByteByteGo, "Schema Evolution").

- Version overlap is permanent: rolling deploys, stored data, third-party clients, and async messages force multiple schema versions to coexist.
- Backward compatibility (new code reads old data) requires consumers first; forward compatibility (old code reads new data) allows producers first.
- Expand-contract migrations turn breaking changes into a sequence of safe, reversible steps with a defined rollback boundary.
- Schema registries enforce compatibility checks before deployment but cannot detect semantic breaks like unit changes.
- Input contracts break when fields are added (required) or made mandatory; output contracts break when fields are removed or renamed.