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

In this retrospective, Charity Majors describes the grueling two-year migration of Parse's core API from Ruby on Rails to Go. The initial choice of Rails enabled rapid iteration, but as Parse experienced hockey-stick growth, the one-process-per-request model became a critical bottleneck. Worker pools would fill with slow requests, causing outages and forcing a move to an asynchronous architecture (Majors, 2025).

- Rails' one-process-per-request model could not scale; slow requests quickly exhausted worker pools and caused reliability issues.
- Go was chosen over JRuby, C++, and C# because of its built-in async support, excellent MongoDB driver, lightweight goroutines, and team enthusiasm.
- The rewrite was done endpoint-by-endpoint using live shadowing: production traffic was split to both Ruby and Go servers, and responses were diffed field-by-field to catch subtle incompatibilities.
- Rails' 'be liberal in what you accept' philosophy forced the team to port many undocumented behaviors, leading to cranky code comments but preserving backward compatibility.
- The migration resulted in an order-of-magnitude reliability improvement, a 90% reduction in API server footprint, deploy time dropping from 30 to 3 minutes, and integration tests going from 25 to 2 minutes.