---
domain: system-design
subdomain: backend-migration
concept: ruby-to-golang-migration
title: How We Migrated the Parse API From Ruby to Golang
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang

The article is a retrospective by Charity Majors about the grueling two-year rewrite of Parse's core API from Ruby on Rails to Golang. Initially, Ruby enabled rapid iteration, but as Parse experienced hockey-stick growth, the one-process-per-request model of Rails proved unscalable. The fixed worker pool would fill with slow requests, causing cascading failures and requiring massive over-provisioning. The team realized they needed an asynchronous model and evaluated several options, ultimately choosing Go over JRuby, C++, and C# due to its built-in concurrency primitives, lightweight goroutines, excellent MongoDB driver, and team enthusiasm.

- Ruby on Rails allowed fast initial development but its one-process-per-request model became a critical bottleneck as traffic grew, leading to worker pool saturation and fragility.
- Go was chosen after evaluating JRuby, C++, and C# because it offered native async operations, lightweight goroutines, a superior MongoDB driver, and a more productive developer experience.
- The hardest challenge was preserving backward compatibility with undocumented and non-RFC-compliant requests that Rails middleware silently accepted; the team used live shadowing and response diffing to identify behavioral mismatches.
- The rewrite yielded an order-of-magnitude reliability improvement, a 90% reduction in API server pool size, test suite time dropping from 25 to 2 minutes, and deploy time from 30 to 3 minutes.
- The experience with diffing production traffic and the need for powerful observability tools directly inspired the creation of Honeycomb.