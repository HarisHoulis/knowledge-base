---
domain: system-design
subdomain: backend-migration
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

This retrospective chronicles Parse's two-year rewrite of its core API from Ruby on Rails to Go, driven by the fundamental scaling limits of Rails' one-process-per-request model. As traffic and app count 10x'd, worker pools filled with slow requests, making the system fragile and operations burnout-inducing. The team realized an asynchronous model was essential and evaluated EventMachine, JRuby, C++, C#, and Go, ultimately choosing Go for its lightweight goroutines, excellent MongoDB driver, and developer enthusiasm (Charity Majors, 2025).

The hardest part was preserving Rails' "liberal in what you accept" HTTP middleware behavior, which tolerated undocumented and non-RFC-compliant requests. To avoid breaking production, they built a live shadowing system that ran each request against both the Ruby and Go API servers and diffed the responses field-by-field using Scuba. This workflow not only exposed subtle incompatibilities but also demonstrated the power of rich, queryable comparison tools, which later influenced Honeycomb's founding (Majors, 2025).

The rewrite delivered dramatic improvements: reliability improved by an order of magnitude, the API server pool shrank by ~90%, full integration test time dropped from 25 minutes to 2 minutes, and deployments from 30 to 3 minutes. The new async model also enabled comprehensive instrumentation and simplified the architecture by removing isolated Rails server silos (Majors, 2025).

- Rails' one-process-per-request model could not scale with Parse's hockey-stick growth, leading to the need for an asynchronous architecture.
- Go was chosen over C#, Java, and C++ due to its built-in concurrency, superior MongoDB driver, and team excitement.
- Replicating Rails' permissive request handling required a live shadowing system that diffed Ruby and Go responses for every production request.
- The rewrite improved reliability by an order of magnitude, cut the API server fleet by ~90%, and drastically reduced test and deploy times.
- The experience with diffing and querying response-level data directly inspired the creation of Honeycomb.