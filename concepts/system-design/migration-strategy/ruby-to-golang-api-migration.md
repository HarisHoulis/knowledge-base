---
domain: system-design
subdomain: migration-strategy
concept: ruby-to-golang-api-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The article recounts Parse's two-year rewrite of its core API from Ruby on Rails to Go, driven by the fundamental scaling limits of Rails' one-process-per-request model. As traffic grew, slow requests could saturate the fixed worker pool, causing outages and requiring constant human intervention. The team evaluated alternatives including EventMachine, JRuby, C++, C#, and Go, ultimately choosing Go for its lightweight goroutines, strong MongoDB driver, and developer enthusiasm (Majors, 2025).

- Rails' one-process-per-request model could not scale with Parse's hockey-stick growth; async was necessary.
- Go was chosen over C# and other alternatives for its goroutine lightweight concurrency, excellent MongoDB driver, and team enthusiasm.
- Shadowing production traffic and diffing Ruby vs Go responses was key to catching undocumented Rails middleware behaviors.
- The rewrite improved reliability by 10x, cut API server pool by ~90%, and reduced test/deploy times dramatically.
- The async model enabled better instrumentation and simplified architecture, reducing ops burnout.