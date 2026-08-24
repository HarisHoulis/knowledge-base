---
domain: system-design
subdomain: backend-migration
concept: shadow-traffic-diffing
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors resurrected a 2015 post about Parse's two-year rewrite of its core API from Ruby on Rails to Go. The original motivations were scalability: Rails' one-process-per-request model caused worker pools to fill up with slow requests, and as Parse experienced hockey-stick growth, this became unsustainable. The team evaluated options like JRuby, C++, C#, and Go, ultimately choosing Go because of its built-in async support, lightweight goroutines, excellent MongoDB driver, and ease of recruiting engineers.

The hardest part was preserving backward compatibility, since Rails middleware was extremely liberal in what it accepted—handling undocumented or non-RFC-compliant requests implicitly. To catch behavioral differences, the team ran incoming traffic against both Ruby and Go servers in parallel and diffed responses field by field. This shadowing technique was enabled by Scuba and became a turning point for observing system behavior.

The rewrite paid off: reliability improved by an order of magnitude, API server pool size dropped by about 90%, full deploy time dropped from 30 to 3 minutes, and integration test time dropped from 25 to 2 minutes. The codebase was cleaned of magical gems, and the ops team no longer faced weekly Ruby API outages. Majors credits this migration with ultimately leading to Honeycomb's creation, as the diffing tooling revealed the power of querying individual request/response pairs.

- Rails' one-process-per-request model cannot scale to high concurrency; async models like Go's goroutines are a better fit.
- A live shadowing system that diffs responses between old and new implementations is critical for safely migrating a production API.
- Rails middleware silently accepts non-RFC-compliant requests, so any rewrite must port those undocumented behaviors to avoid breakage.
- Go rewrite improved reliability by an order of magnitude, cut API server count by ~90%, and reduced deploy/test times dramatically.
- The experience of diffing individual responses inspired the creation of Honeycomb.