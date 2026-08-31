---
domain: system-design
subdomain: backend-migration
concept: api-rewrite-shadowing
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The article recounts Parse's migration of its core API from Ruby on Rails to Go, driven by scaling limitations of the one-process-per-request model. As traffic grew, the fixed worker pool became a bottleneck, causing deployments to take 20 minutes and requiring 200 API servers to serve only 3,000 RPS. The team realized an asynchronous model was necessary and evaluated EventMachine, JRuby, C++, C#, and Go, ultimately choosing Go for its goroutines, excellent MongoDB driver, and recruitment appeal (Majors, 2025).

The migration itself was executed endpoint-by-endpoint using a shadowing system: incoming production traffic was split and run against both a Go and Ruby API server, with responses diffed field-by-field using Scuba. This caught subtle incompatibilities arising from Rails' liberal input handling, such as non-RFC-compliant URLs, weird content-lengths, and mis-encoded Unicode. The Go codebase was peppered with comments documenting these quirks, preserving backward compatibility (Majors, 2025).

The rewrite yielded dramatic improvements: reliability improved by an order of magnitude, API server pool size dropped by 90%, full integration test suite time fell from 25 minutes to 2 minutes, and deploys went from 30 minutes to 3 minutes with graceful restarts. The article credits the team and notes that the experience heavily influenced the creation of Honeycomb (Majors, 2025).

- Ruby on Rails' one-process-per-request model could not scale to Parse's hockey-stick growth, leading to worker pool exhaustion and slow deploys.
- Go was chosen over alternatives like C# and JRuby due to its efficient goroutines, strong MongoDB driver, and cultural fit.
- Safe rewriting was achieved via live shadowing of production traffic and diffing Go vs Ruby responses on a field-by-field basis.
- Rails' 'liberal in what you accept' middleware required porting many undocumented behaviors and quirks to Go.
- The migration cut API server needs by 90%, test suite time from 25 to 2 minutes, and deploy time from 30 to 3 minutes while improving reliability.