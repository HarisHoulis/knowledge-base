---
domain: system-design
subdomain: backend-migration
concept: ruby-to-go-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The article recounts Parse's migration from a Ruby on Rails API to Golang. As traffic grew, the one-process-per-request model of Rails became a scaling bottleneck—slow requests could fill the worker pool faster than auto-scaling could react. The team decided on an asynchronous model and evaluated options like EventMachine, JRuby, C++, C#, and Go. They chose Go because of its lightweight goroutines, the excellent MongoDB Go driver, and team enthusiasm (Majors, 2025).

The migration was performed endpoint-by-endpoint using a live shadowing system: both Ruby and Go servers handled production traffic, and responses were diffed field-by-field using Scuba. This allowed them to catch behavioral mismatches. The hardest part was replicating Rails' liberal acceptance of non-RFC-compliant requests, such as doubly encoded URLs and weird headers, requiring careful porting of undocumented behaviors (Majors, 2025).

The rewrite was highly successful: reliability improved by an order of magnitude, the API server pool shrank by 90%, deploy time dropped from 30 to 3 minutes, and integration test time dropped from 25 to 2 minutes. It also reduced operational burnout and made the codebase cleaner (Majors, 2025).

- Rails' one-process-per-request model does not scale to high concurrency; an asynchronous model is necessary.
- Go was chosen over C# for its lightweight goroutines, best-in-class MongoDB driver, and developer enthusiasm.
- Live shadowing—running both old and new servers and diffing responses—enabled safe migration.
- Replicating Rails' permissive HTTP handling was a major challenge, requiring porting undocumented behaviors.
- The migration improved reliability by 10x and drastically reduced infrastructure and deployment times.