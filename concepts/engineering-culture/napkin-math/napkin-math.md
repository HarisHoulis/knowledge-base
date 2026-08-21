---
domain: engineering-culture
subdomain: napkin-math
concept: napkin-math
title: Pushing software engineering limits with “napkin math”
sources:
  - title: "Pushing software engineering limits with “napkin math”"
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "Tue, 21 Jul 2026 16:52:07 GMT"
---

# Pushing software engineering limits with “napkin math”

The article profiles Simon Eskildsen, co-founder and CEO of turbopuffer, and his use of “napkin math” to challenge engineering assumptions and optimize systems. Simon, a self-taught engineer who skipped college, learned algorithmic thinking through the International Olympiad for Informatics (IOI) and later spent nearly a decade at Shopify building infrastructure. His key practice is maintaining a table of approximate hardware costs and performance numbers (e.g., $2 per gigabyte of memory, $0.02 per gigabyte of S3) and memorizing them with flashcards, enabling quick mental estimates to validate or refute design decisions (Orosz, 2026).

- Napkin math is the practice of using approximate, memorized numbers for hardware costs and performance to quickly sanity-check engineering decisions.
- Simon Eskildsen built a GitHub table of ~50 key numbers and used flashcards to memorize them, making back-of-envelope calculations fast and accurate.
- This approach can debunk flawed benchmarks, as when a 10-second database query was shown to theoretically take 10 milliseconds, exposing inefficiency.
- Long tenure at Shopify taught Simon that simple solutions often outlast large, complex ones, and contributed to creating toxiproxy for resilience testing.
- At turbopuffer, napkin math showed that search solutions were drastically overpriced relative to theoretical limits, leading to a disruptive new product.