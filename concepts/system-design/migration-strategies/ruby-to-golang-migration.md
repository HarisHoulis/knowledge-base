---
domain: system-design
subdomain: migration-strategies
concept: ruby-to-golang-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors' retrospective discusses Parse's two-year migration from Ruby on Rails to Golang. The original Rails setup scaled poorly due to the one-process-per-request model, causing worker pool saturation, long deploys, and reliability issues as traffic grew. After evaluating EventMachine, JRuby, C++, C#, and Go, Parse chose Go for its built-in async support, efficient goroutines, and strong MongoDB driver. The rewrite proceeded endpoint-by-endpoint using shadowing (splitting traffic and diffing responses) to catch behavioral mismatches, revealing how Rails' permissive HTTP handling masked undocumented and non-RFC-compliant requests that Go rejected.

- Rails' one-process-per-request model capped scalability and caused cascading failures under load, driving the need for an async runtime.
- Go won over C# and other alternatives due to its lightweight goroutines, excellent MongoDB driver, and developer enthusiasm.
- Live shadowing and differential response comparison were essential for safely rewriting Rails' 'liberal' request handling without breaking existing clients.
- The rewrite improved reliability by an order of magnitude, reduced API server pool by ~90%, cut full API deploy time from 30 to 3 minutes, and trimmed integration test time from 25 to 2 minutes.