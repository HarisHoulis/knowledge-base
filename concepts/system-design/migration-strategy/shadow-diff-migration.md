---
domain: system-design
subdomain: migration-strategy
concept: shadow-diff-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The article recounts Parse's two-year rewrite of its core API from Ruby on Rails to Golang. The initial Rails stack worked well at small scale but hit a wall as traffic grew: the one-process-per-request model caused worker pools to fill with slow requests and made autoscaling ineffective. The team evaluated EventMachine, JRuby, C++, C#, and Go, ultimately choosing Go for its lightweight goroutines, excellent MongoDB driver, and better recruiting appeal. A key part of the migration was a live shadowing system that sent production traffic to both Ruby and Go servers and diffed the responses, which exposed countless undocumented Rails behaviors that had to be reimplemented in Go.

- Ruby on Rails one-process-per-request model became a scalability bottleneck as Parse experienced hockey-stick growth.
- Go was chosen over C# and other options due to its built-in async model, lightweight goroutines, and superior MongoDB driver.
- The team used live shadowing: run each request against both Ruby and Go servers, then diff responses field-by-field to find behavioral mismatches.
- Replicating Rails' liberal input handling (non-RFC compliant requests, weird encodings) was the hardest part of the rewrite.
- The rewrite improved reliability by an order of magnitude, cut API server pool by ~90%, reduced deploy time from 30 to 3 minutes, and simplified the architecture.