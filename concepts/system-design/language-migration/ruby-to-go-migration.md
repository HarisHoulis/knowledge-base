---
domain: system-design
subdomain: language-migration
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24T02:14:45Z"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

This article recounts Parse's two-year migration from Ruby on Rails to Go, driven by the scaling limitations of the one-process-per-request model. Ruby allowed rapid initial development, but as traffic grew, the fixed worker pool became a bottleneck, causing slow requests to fill the pool and making deployments painful. After evaluating EventMachine, JRuby, C++, C#, and Go, the team chose Go for its lightweight goroutines, excellent MongoDB driver, and strong developer appeal ([source](https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected)).

The hardest part of the rewrite was maintaining backward compatibility with Rails' permissive HTTP handling. Rails accepted undocumented and non-RFC-compliant requests, so the team had to port these quirks to Go, adding comments to explain each oddity. They used a live shadowing system: running each request against both Go and Ruby servers in production and diffing the responses field by field. This tooling-influenced approach later inspired the creation of Honeycomb ([source](https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected)).

The rewrite yielded dramatic improvements: reliability improved by an order of magnitude, the API server pool shrank by 90%, the integration test suite dropped from 25 minutes to 2 minutes, and full deploys from 30 minutes to 3 minutes. The async model also enabled better instrumentation and simplified the architecture. The author credits the migration as essential to Honeycomb's origins ([source](https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected)).

- Ruby on Rails' one-process-per-request model became a scalability bottleneck as traffic grew, motivating the move to an async language.
- Comparing Go and Ruby responses in production via a shadowing system was key to preserving undocumented Rails behaviors.
- Go's lightweight goroutines and strong MongoDB driver made it the preferred choice over C# and other alternatives.
- The migration improved reliability by 10x, cut API server count by 90%, and drastically reduced deploy and test times.
- The rewrite was a grueling two-year effort that the author credits with enabling Honeycomb's creation.