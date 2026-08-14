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

After these failed attempts, the author resets with a partition-based approach using MutableSet.add, which returns false when an element is already in the set. This leads to a cleaner solution using `filterNot(HashSet<Int>()::add)`, which retains only elements already seen. The final refinement is `filterNotTo(HashSet(), HashSet<Int>()::add)`, which both reads well and avoids an extra toSet() call. Benchmark results show the filterNotTo variant is both the fastest and allocates the fewest bytes, offering a double win in performance.

- The map-based groupBy approach works but may be overkill for simple duplicate detection.
- Kotlin's minus operator and MutableList.removeAll both remove all occurrences of each element in the collection, not just the first.
- MutableSet.add returns false for duplicates, enabling a concise filterNot-based solution.
- Using filterNotTo with a bound HashSet::add reference is the most performant and allocation-friendly method in benchmarks.