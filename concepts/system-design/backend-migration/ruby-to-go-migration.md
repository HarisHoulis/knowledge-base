---
domain: system-design
subdomain: backend-migration
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang

The rewrite paid off significantly: reliability improved by an order of magnitude, API server pool size dropped by about 90%, full integration test time fell from 25 to 2 minutes, and deploys from 30 to 3 minutes. The async model also enabled better instrumentation and simpler architecture, reducing operational burnout and improving customer co-tenancy (Majors, 2025).

- Rails' one-process-per-request model could not scale with Parse's hockey-stick growth, motivating a move to an asynchronous architecture.
- Go was selected over C# and other options due to its low-level concurrency (goroutines), the MongoDB driver, and lightweight per-connection memory use.
- The most challenging part was porting undocumented Rails behaviors, such as accepting non-RFC-compliant requests, which was solved by shadowing production traffic and diffing Ruby vs Go responses.
- The rewrite resulted in an order-of-magnitude reliability improvement, 90% fewer API servers, and dramatic reductions in test and deployment times.
- The process also highlighted the power of differential analysis tools like Scuba, turning the team onto observability practices that later influenced Honeycomb.