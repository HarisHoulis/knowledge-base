---
domain: system-design
subdomain: data contracts
concept: schema-evolution
title: Schema Evolution: Changing the Contract Without Breaking What Runs
sources:
  - title: "Schema Evolution: Changing the Contract Without Breaking What Runs"
    url: "https://blog.bytebytego.com/p/schema-evolution-changing-the-contract"
    author: "ByteByteGo"
    date: "Thu, 20 Aug 2026 15:32:18 GMT"
---

# Schema Evolution: Changing the Contract Without Breaking What Runs

Schema changes are notoriously difficult because multiple schema versions are always in play simultaneously. This is not just a deployment-window artifact: rolling deploys, stored data, third-party clients, and asynchronous messages create permanent version overlap. Consequently, compatibility is a pairwise property: backward compatibility lets new code read old data, while forward compatibility lets old code read new data. The choice of guarantee determines safe deployment ordering and whether producers or consumers can move first (ByteByteGo, 2026).

Decoding a record requires resolving two schemas: the writer's and the reader's. Fields absent from the reader's schema are discarded, while fields missing from the data are filled with defaults. Adding an optional field with a default is usually safe; deleting, renaming (for name-based formats), making a field required, changing its type/cardinality, or narrowing validation are breaking. Notably, input vs. output contracts break in opposite directions: adding a required input field breaks callers, while removing an output field breaks consumers (ByteByteGo, 2026).

Breaking changes can be executed safely using expand-contract migrations: add a nullable column, dual-write, backfill, verify, switch reads, switch writes, then drop the old column. Each step must be individually deployable and reversible. Schema registries automate compatibility checks at registration time, catching violations before production, though they cannot detect semantic changes like unit changes. Versioning strategies differ by context: internal APIs allow coordinated breaking changes, public APIs and mobile clients require explicit versioning and long deprecation windows, while databases and event logs need additive evolution or registry enforcement (ByteByteGo, 2026).

Deprecation and removal are often neglected because they produce no visible improvement and have asymmetric risk. Field-level and endpoint-level usage instrumentation, agreeing on removal dates during expansion, and treating removal as part of the original work can make cleanup a reality. The article emphasizes that schema evolution is fundamentally about managing the overlapping lifetimes of producers and consumers (ByteByteGo, 2026).

- Multiple schema versions always coexist due to rolling deploys, stored data, third-party clients, and async messages; compatibility is a pairwise property of producer/consumer versions.
- Safe changes are additive (optional fields with defaults, new endpoints, wider input), while breaking changes remove or redefine fields or make previously valid inputs invalid.
- Expand-contract migrations decompose breaking changes into individually safe, reversible steps: expand, dual-write, backfill, switch reads, switch writes, drop old.
- Schema registries catch incompatible changes at registration time, but cannot detect semantic changes like unit changes; naming fields with units helps.
- Versioning strategies vary: internal APIs can coordinate breaking changes, public APIs and mobile clients need explicit versions and long deprecation windows, and databases/event logs require additive evolution or registry enforcement.