---
domain: system-design
subdomain: backend-migration
concept: shadow-diff-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The article recounts Parse's two-year rewrite of its core API from Ruby on Rails to Go, driven by the fundamental scaling limitations of Rails' one-process-per-request model. As Parse grew, worker pools filled with slow requests, deploys took 20-30 minutes, and reliability suffered. The team concluded that an asynchronous concurrency model was necessary (Majors, 2025).

After evaluating EventMachine, JRuby, C++, C#, and Go, they chose Go for its lightweight goroutines, strong MongoDB driver, and engineering enthusiasm. The migration was performed endpoint-by-endpoint using a live shadowing system: production traffic was split and run against both Ruby and Go servers, with responses diffed field-by-field using Scuba. This exposed Rails' "liberal in what you accept" middleware behaviors that had to be deliberately ported to Go (Majors, 2025).

The rewrite yielded dramatic improvements: reliability improved by an order of magnitude, API server pool shrank by 90%, deployment time dropped from 30 to 3 minutes, and the full integration test suite dropped from 25 to 2 minutes. The team also gained better observability and simplified the architecture. Majors reflects that the rewrite was worth the grueling effort, and might have been essential to Honeycomb's origin (Majors, 2025).

- Rails' one-process-per-request model couldn't handle Parse's hockey-stick growth; an async model was required.
- Live shadowing with response diffing (using Scuba) was critical to catch undocumented Rails behaviors.
- Go won over alternatives due to lightweight goroutines, excellent MongoDB driver, and team enthusiasm.
- Results: 10x reliability improvement, 90% reduction in API servers, 10x faster deploys and integration tests.