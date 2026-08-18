---
domain: engineering-culture
subdomain: migration-retrospective
concept: ruby-to-golang-rewrite
title: How We Migrated the Parse API From Ruby to Golang (Resurrected)
sources:
  - title: "How We Migrated the Parse API From Ruby to Golang (Resurrected)"
    url: "https://charity.wtf/p/how-we-migrated-the-parse-api-from-ruby-to-golang-resurrected"
    author: "Charity Majors"
    date: "Thu, 24 Jul 2025 02:14:45 GMT"
---

# How We Migrated the Parse API From Ruby to Golang (Resurrected)

Charity Majors resurrected her 2015 retrospective on Parse's two-year rewrite from Ruby on Rails to Go. The original post described how Rails' one-process-per-request model began to fail as Parse experienced hockey-stick growth: slow requests could fill the fixed worker pool, causing cascading outages that required manual paging and remediation. The team concluded that moving to an asynchronous model was necessary for future scale and evaluated EventMachine, JRuby, C++, C#, and Go before choosing Go. Key drivers included Go's lightweight goroutines, the superior MongoDB Go driver, and the team's enthusiasm for the language [1].

The rewrite was painful because Rails' middleware was 'liberal in what you accept', so many client requests were undocumented or non-RFC compliant yet worked against Ruby. The Go API initially broke on these edge cases. To manage this, the team shadowed production traffic by running requests against both Go and Ruby servers behind the same load balancer and diffing responses field by field. This diffing workflow, powered by Scuba, became crucial for uncovering behavioral mismatches and ultimately influenced the creation of Honeycomb [1].

The rewrite paid off with an order-of-magnitude reliability improvement, a ~90% reduction in the API server pool, and simpler architecture. The full integration test suite dropped from 25 minutes to 2 minutes, and deployments from 30 minutes to 3 minutes due to graceful restarts. The codebase became cleaner, with many magical gems and implicit assumptions removed, and the ops team no longer suffered from frequent Ruby-related outages [1].

- Rails' one-process-per-request model couldn't scale to Parse's growth; async was mandatory.
- Go was chosen over C# and other alternatives due to lightweight goroutines, the MongoDB driver, and recruiting appeal.
- Shadowing production traffic and diffing responses was key to handling Rails' permissive HTTP parsing.
- Results: 10x reliability improvement, 90% fewer API servers, test suite from 25 to 2 minutes, deploys from 30 to 3 minutes.