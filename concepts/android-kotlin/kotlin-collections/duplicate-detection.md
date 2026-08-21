---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-detection
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of duplicate finding

The article ultimately recommends a more idiomatic and efficient solution using `filterNotTo` with a bound `HashSet::add` reference. This approach correctly collects duplicates in one pass, is visually concise, and benchmarks fastest with lowest allocation (39.9 ns/op, 432 B/op). The key insight is that `MutableSet.add` returns false for already-seen elements, making it a natural predicate for filtering duplicates.

- Kotlin's `minus` and `removeAll` remove all occurrences of elements, not just the first, which can break duplicate-finding logic.
- Use `MutableSet.add` as a predicate: it returns true the first time a value is seen and false for subsequent duplicates.
- `filterNot` with a bound `HashSet::add` provides a readable one-liner for finding duplicates.
- `filterNotTo` is the most efficient variant, minimizing both time and memory allocations.