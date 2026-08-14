---
domain: system-design
subdomain: legacy-system-migration
concept: shadow-diff-migration
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "2025-07-24"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

The hardest part was replicating Rails' 'liberal in what you accept' behavior. Ruby middleware automatically cleaned up undocumented, non-RFC-compliant requests—such as doubly encoded URLs, mis-encoded Unicode, and weird HTTP bodies—so the Go code had to preserve these quirks to avoid breaking existing clients. This was painstaking work, but the payoff was immense: reliability improved by an order of magnitude, API server pool size dropped by 90%, the full integration test suite went from 25 minutes to 2 minutes, and deploys dropped from 30 minutes to 3 minutes. Majors credits the migration with making Honeycomb possible, as the shadowing and diffing workflow exposed the power of comparing responses with Scuba (Majors, 2025).

- Rails' one-process-per-request model could not scale to Parse's growth, triggering a rewrite to an asynchronous architecture.
- Go was selected over C#, C++, and JRuby due to its lightweight goroutines, superior MongoDB driver, and strong async library support.
- The team used live shadowing—running each request against both Ruby and Go servers and diffing responses—to find incompatible behaviors.
- Rails' liberal input handling forced the Go rewrite to replicate undocumented, non-RFC-compliant request parsing, leading to cranky code comments.
- The rewrite delivered 10x reliability improvement, 90% reduction in servers, and 10x faster tests and deploys.