---
domain: system-design
subdomain: api-evolution
concept: api-impact-analysis
title: Netflix Builds Quasar to Measure the Blast Radius of Library API Changes
sources:
  - title: "Netflix Builds Quasar to Measure the Blast Radius of Library API Changes"
    url: "https://www.infoq.com/news/2026/11/netflix-quasar-api-impact/"
    author: "Leela Kumili"
    date: "2026-11-27"
---

# Netflix Builds Quasar to Measure the Blast Radius of Library API Changes

Netflix developed Quasar, an internal tool that combines semantic code indexing with API comparisons to identify which downstream consumers are affected by changes to a library's API. Rather than relying on textual search, Quasar traces actual API references across repositories, giving maintainers a concrete view of the blast radius of a change.

The tooling is built on SCIP for semantic code indexing, with index data stored in Amazon S3 and queried via Athena. This lets maintainers assess migration impact and make informed release decisions before shipping breaking changes.

Netflix is also exploring agent-assisted consumer migrations, extending the workflow from impact detection toward automated remediation.

- Quasar combines semantic code indexing and API comparisons to find downstream consumers of changed library APIs
- It uses SCIP for indexing, with data in S3 and queried through Athena
- The goal is to assess migration impact and inform release decisions
- Netflix is exploring agent-assisted consumer migrations