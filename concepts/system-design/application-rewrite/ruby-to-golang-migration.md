---
domain: system-design
subdomain: application-rewrite
concept: ruby-to-golang-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

In this retrospective, Charity Majors recounts Parse's two-year rewrite of its core API from Ruby on Rails to Go. The primary motivation was scalability: Rails' one-process-per-request model caused worker pools to fill with slow requests, making it impossible to handle rapid growth. After evaluating EventMachine, JRuby, C++, C#, and Go, Parse chose Go for its built-in async concurrency, lightweight goroutines, and superior MongoDB driver. The rewrite was grueling due to Rails' 'liberal in what you accept' HTTP processing, which silently handled malformed and undocumented requests. To preserve backward compatibility, the team developed a live shadowing system that ran production traffic against both Ruby and Go servers and diffed responses field-by-field, using Scuba for deep analysis. This approach was instrumental in catching subtle behavioral mismatches. The effort paid off: reliability improved by an order of magnitude, the API server pool shrank by ~90%, deploy time dropped from 30 to 3 minutes, and integration test time from 25 to 2 minutes. The rewrite also reduced ops burnout and simplified the architecture. The original post was published on blog.parse.com in June 2015 and resurrected by Majors in July 2025.

- Rails' one-process-per-request model hit hard scaling limits as Parse's traffic multiplied, causing worker pool exhaustion and fragility.
- Go was selected over C# and other options due to its lightweight goroutines, strong MongoDB driver, and developer enthusiasm.
- A live shadowing system that compared Ruby and Go API responses was crucial for discovering and porting undocumented Rails middleware behaviors.
- The rewrite delivered an order-of-magnitude reliability improvement, a 90% reduction in API server footprint, and dramatically faster deploys and tests.
- Instrumentation and observability tools like Scuba were essential for validating the migration, a lesson that later influenced Honeycomb.