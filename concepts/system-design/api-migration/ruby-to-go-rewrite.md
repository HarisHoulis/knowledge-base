---
domain: system-design
subdomain: api-migration
concept: ruby-to-go-rewrite
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors recounts Parse's two-year rewrite of its core API from Ruby on Rails to Go. The initial choice of Rails allowed rapid iteration, but as traffic grew, the one-process-per-request model became a bottleneck: slow requests could exhaust the worker pool faster than auto-scaling could react, and the team realized the model would not scale to 10x their size. After evaluating EventMachine, JRuby, C++, C#, and Go, they chose Go because of its built-in async primitives, lightweight goroutines, excellent MongoDB driver, and developer enthusiasm. A first migration of the push backend from EventMachine to Go increased connection capacity from 250k to 1.5 million connections per node (Majors, 2025).

- Rails' one-process-per-request model doesn't scale when slow requests fill the worker pool; an async model is required for large-scale APIs.
- Go was chosen over C# and other async options because of its lightweight goroutines, strong MongoDB driver, and developer enthusiasm.
- Migrating the push backend first demonstrated Go's efficiency: 250k to 1.5 million connections per node.
- Shadowing production traffic and diffing responses between Ruby and Go was essential for catching undocumented Rails behaviors.
- The rewrite improved reliability by an order of magnitude, cut API server pool by 90%, and drastically reduced deploy and test times.