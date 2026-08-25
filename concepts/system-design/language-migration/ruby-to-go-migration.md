---
domain: system-design
subdomain: language-migration
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Parse's API was originally written in Ruby on Rails, which enabled rapid early development but eventually hit hard scaling limits. The one-process-per-request model meant a fixed pool of workers, and slow requests could quickly exhaust the pool. By the end of 2012, Parse ran 200 API servers for 3000 requests per second, and deploys took 20 minutes. As traffic grew 10x, the team concluded the Rails model could not scale and an asynchronous architecture was required (Majors, 2025).

The team evaluated EventMachine, JRuby, C++, C#, and Go. EventMachine and JRuby suffered from poor async library support; C++ was harder to maintain; C# had good concurrency but poor Linux support. Go won because goroutines are lightweight, the MongoDB driver was excellent, and engineers were excited to write Go. A preliminary rewrite of the push backend from Ruby to Go increased connections per node from 250k to 1.5 million, cementing the choice (Majors, 2025).

The core API rewrite was done endpoint-by-endpoint using a shadowing system: production traffic was split between the Ruby and Go servers, and responses were diffed field-by-field. This was crucial because Rails middleware was liberal in what it accepted, so clients sent undocumented or non-RFC-compliant requests that Rails silently fixed. The Go code had to replicate quirks like doubly encoded URLs, weird content-length requirements, and mis-encoded Unicode, leading to many cranky comments referencing Ruby behavior (Majors, 2025).

The rewrite was a success. Reliability improved by an order of magnitude, and the API layer almost stopped being the cause of incidents. The asynchronous model allowed better instrumentation, a 90% reduction in API server pool size, and simpler architecture. The full integration test suite dropped from 25 minutes to 2 minutes, and a full deploy dropped from 30 minutes to 3 minutes (Majors, 2025).

- Rails' one-process-per-request model was the core scaling bottleneck; an async architecture was necessary as Parse grew 10x.
- Go was chosen over JRuby, C++, and C# due to goroutines, the MongoDB driver, and team enthusiasm.
- Shadowing production traffic and diffing Ruby vs Go responses exposed undocumented Rails behaviors that had to be replicated.
- The migration improved reliability by an order of magnitude, reduced API server pool by 90%, and cut test/deploy times dramatically.