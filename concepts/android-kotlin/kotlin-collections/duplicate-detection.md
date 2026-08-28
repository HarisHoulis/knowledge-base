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

The article explores various Kotlin approaches to find duplicate elements in a list, starting with a straightforward `groupBy` method that works but is inefficient. The author then attempts more clever solutions using collection operators, uncovering subtle behavior differences. The `minus` operator and `removeAll` both remove all occurrences of each element, while `remove` only removes the first, leading to incorrect results. The article demonstrates a concise correct solution using `filterNot` with a bound `HashSet::add` reference, and further improves it with `filterNotTo` to avoid intermediate collections. Benchmarks show that `filterNotTo` is both the fastest and allocates the fewest bytes, making it the best choice.

- The naive `groupBy` solution correctly finds duplicates but is wasteful in time and memory.
- `minus` and `removeAll` remove all occurrences of elements, not just the first, which is surprising when used for duplicate detection.
- `filterNot(HashSet::add)` provides a concise and correct way to find duplicates by keeping elements already seen.
- `filterNotTo(HashSet(), HashSet::add)` is the most efficient approach, both in speed and allocation.