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

Schema changes are inherently difficult because multiple schema versions coexist at any time, not just during deployments. Rolling deploys, stored data, third-party clients, and asynchronous messages all contribute to version overlap, which staging environments fail to replicate. As a result, data written under one schema version is frequently read under a different version, causing failures that are not caught in preview environments (ByteByteGo, 2026).

Compatibility must be assessed in both directions: backward compatibility (new code reads old data) and forward compatibility (old code reads new data). Decoding relies on two schemas: the writer's and the reader's. A field in the data but missing from the reader's schema is discarded; a field in the reader's schema but missing from the data is populated with a default. Adding an optional field with a default is safe, while renaming or removing fields, changing types, narrowing validation, or changing units under the same name can break consumers. Interestingly, input and output contracts break in opposite directions: adding a field to a request is breaking, while removing a field from a response is breaking (ByteByteGo, 2026).

Breaking changes can be introduced safely through expand-contract migrations, which sequence a change into individually deployable steps: add new nullable column, dual-write, backfill, verify, switch reads, stop writes, drop old. Schema registries enforce compatibility by checking proposed schemas against previous versions at registration time, catching incompatible changes early. However, automated checks cannot catch semantic changes like units changing from cents to dollars, so naming fields with units and adding new fields is a common defense. Versioning strategies vary by context: internal services can coordinate breaking changes, public APIs need formal versioning and deprecation windows, and event logs benefit from registry enforcement and defaults on every field (ByteByteGo, 2026).

Deprecation and removal of old schema elements are often skipped because they produce no visible improvement and carry asymmetric risk. To make removal feasible, teams should instrument field- and endpoint-level usage, agree on removal dates during the expansion phase, and treat removal as part of the original work rather than a follow-up ticket (ByteByteGo, 2026).

- Multiple schema versions are always in play due to rolling deploys, stored data, third-party clients, and async messages; staging cannot catch version-overlap issues.
- Safety of a schema change depends on compatibility direction and resolution rules: adding a field with a default is safe, while removal, rename (by name), type change, or narrowing validation often breaks consumers.
- Breaking changes can be deployed safely using expand-contract migrations: add nullable column, dual-write, backfill, verify, switch reads, stop writes, drop old.
- Schema registries catch incompatible changes at registration time, but cannot detect semantic changes like unit changes; use unit-suffixed field names and add new fields instead of redefining old ones.
- Versioning strategy depends on control over consumers and data longevity; deprecation requires explicit scheduling and usage instrumentation to actually happen.