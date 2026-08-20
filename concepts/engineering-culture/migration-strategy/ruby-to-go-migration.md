---
domain: engineering-culture
subdomain: migration-strategy
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors revisits her retrospective on Parse's two-year rewrite of its core API from Ruby on Rails to Go. The migration was driven by Rails' one-process-per-request model, which could not handle Parse's hockey-stick growth: slow requests would fill the worker pool, requiring excessive servers and causing reliability issues. The team evaluated async alternatives and chose Go for its lightweight goroutines, superior MongoDB driver, and developer enthusiasm (Majors, 2025).

The hardest part was preserving backward compatibility with Rails' liberal request handling, which accepted undocumented and non-RFC-compliant HTTP. To catch behavioral differences, they used a shadowing system that ran requests against both Ruby and Go servers and diffed responses field by field. This tooling philosophy later influenced Honeycomb (Majors, 2025).

The rewrite ultimately improved reliability by an order of magnitude, cut the API server pool by about 90%, reduced full deploy time from 30 to 3 minutes, and trimmed integration test time from 25 to 2 minutes. The experience highlighted the importance of async models, rigorous differential testing, and the hidden costs of framework magic (Majors, 2025).

- Rails' one-process-per-request model failed to scale as traffic grew; async concurrency was necessary.
- Go was chosen over C#, C++, and JRuby due to its lightweight goroutines, MongoDB driver, and developer appeal.
- Live shadowing with response diffing was essential to catch undocumented behaviors from Rails middleware.
- The rewrite improved reliability by an order of magnitude and reduced server needs by ~90%.
- Team culture and tooling lessons directly influenced the author's later work at Honeycomb.