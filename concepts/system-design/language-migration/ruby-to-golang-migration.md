---
domain: system-design
subdomain: language-migration
concept: ruby-to-golang-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors recounts the grueling two-year rewrite of Parse's core API from Ruby on Rails to Golang. The initial Ruby stack served 3000 requests per second across 200 API servers, but the one-process-per-request model began to fail under hockey-stick growth. Slow requests filled the worker pool, causing cascading outages, and the team realized the architecture could not scale to 10x. They evaluated EventMachine, JRuby, C++, C#, and Go, ultimately choosing Go for its built-in async support, lightweight goroutines, excellent MongoDB driver, and team enthusiasm (Charity Majors, 2025).

The migration was done endpoint by endpoint using a live shadowing system: incoming production traffic was split and run against both Ruby and Go servers, then responses were diffed field-by-field using Scuba. This revealed the hardest part of the rewrite: porting all the undocumented and non-RFC-compliant behaviors that Rails middleware silently cleaned up, such as doubly encoded URLs, mis-encoded Unicode, and horrible oauth misuse. The Go codebase ended up peppered with cranky comments documenting Ruby-specific quirks (Charity Majors, 2025).

The rewrite paid off enormously. Reliability improved by an order of magnitude, the API server pool shrank by 90%, and deploy time dropped from 30 minutes to 3 minutes thanks to graceful restarts. The integration test suite went from 25 minutes to 2 minutes. The team no longer got paged weekly for API outages, and co-tenancy issues became isolated to single apps. Majors even suggests that without this rewrite, Honeycomb might never have existed, because the diffing workflow sparked their obsession with powerful observability tools (Charity Majors, 2025).

- Ruby on Rails' one-process-per-request model could not scale to Parse's growth; asynchronous processing was required.
- Go was chosen over alternatives like C#, JVM, and C++ due to its concurrency primitives, MongoDB driver, low memory footprint, and team excitement.
- A live shadowing system that diffed responses between Ruby and Go servers was critical for catching breaking changes from Rails' liberal HTTP handling.
- The migration improved reliability by an order of magnitude, cut API server needs by 90%, and reduced deploy/test times dramatically.