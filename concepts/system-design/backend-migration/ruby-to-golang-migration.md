---
domain: system-design
subdomain: backend-migration
concept: ruby-to-golang-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors details the two-year rewrite of Parse's core API from Ruby on Rails to Go. The original Rails setup used a one-process-per-request model with a fixed pool of Unicorn workers, which became a bottleneck as traffic exploded. Slow requests could fill the entire worker pool faster than auto-scaling could react, causing frequent outages and forcing the team to consider a fundamentally asynchronous architecture (Majors, 2025).

The team evaluated several async options, including EventMachine, JRuby, C++, and C#, but ultimately chose Go because of its built-in concurrency primitive (goroutines), superior MongoDB driver, and ease of recruiting. The hardest part was preserving backward compatibility with Rails' 'be liberal in what you accept' philosophy. They used a live shadowing system: running each request against both the Go and Ruby servers backed by separate MongoDB replicas, then diffing responses field by field. This approach, powered by Scuba, caught undocumented behaviors and non-RFC-compliant requests that Rails had silently accepted (Majors, 2025).

The rewrite drastically improved reliability: API-layer incidents dropped to nearly zero, server pool size shrank by ~90%, full deploy time dropped from 30 to 3 minutes, and the integration test suite fell from 25 to 2 minutes. The async model also made it possible to instrument everything without blocking operations, simplifying the architecture and improving co-tenancy for customers (Majors, 2025).

- Rails' one-process-per-request model couldn't scale as Parse 10x'd in traffic, leading to worker pool exhaustion and outages.
- Go was chosen over JRuby, C++, and C# for its lightweight goroutines, strong MongoDB support, and developer enthusiasm.
- The migration used live shadowing and response diffing to ensure the Go API matched all of Rails' undocumented compatible behaviors.
- The rewrite improved reliability by an order of magnitude, cut server pool size by ~90%, and reduced deploy time from 30 to 3 minutes.