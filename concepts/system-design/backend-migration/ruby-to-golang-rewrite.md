---
domain: system-design
subdomain: backend-migration
concept: ruby-to-golang-rewrite
title: How We Migrated the Parse API From Ruby to Golang
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang

Parse initially built its API on Ruby on Rails, leveraging Ruby's speed of development and rich library ecosystem. However, as traffic grew, the one-process-per-request model of Unicorn/Rails became a scalability bottleneck: slow requests could fill the worker pool, and the fixed pool of workers couldn't handle growing concurrency efficiently. The team decided a rewrite to an asynchronous model was necessary, and after evaluating EventMachine, JRuby, C++, C#, and Go, they chose Go because of its built-in async support, lightweight goroutines, excellent MongoDB driver, and team enthusiasm [1].

- Rails' one-process-per-request model failed to scale under rapid growth, causing worker pool exhaustion and fragility.
- Go was selected over alternatives like JRuby and C# due to its native concurrency (goroutines), low memory overhead, and strong MongoDB driver.
- The team used live shadowing and response diffing to port undocumented Rails middleware behaviors (e.g., liberal input parsing) into Go without breaking production.
- The rewrite improved reliability by an order of magnitude, reduced the API server pool by ~90%, and cut deploy time from 30 to 3 minutes and full test suite from 25 to 2 minutes [1].