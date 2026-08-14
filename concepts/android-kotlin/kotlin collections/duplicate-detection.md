---
domain: android-kotlin
subdomain: kotlin collections
concept: duplicate-detection
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of duplicate finding

Jake Wharton's article 'Perils of duplicate finding' explores pitfalls in Kotlin collection operations when identifying duplicate integers. The naive use of `ints.toList() - ints.toSet()` returns an empty list because Kotlin's `minus` operator removes all occurrences of each element in the set, not just one per element. Similarly, `MutableList.removeAll(ints.toSet())` also removes all occurrences due to behavior inherited from Java, despite `MutableList.remove` only removing the first occurrence. This subtle asymmetry can lead to incorrect duplicate-detection code.

To correctly get duplicates, the article recommends tracking seen elements with a `HashSet`. Using `filterNot(HashSet<Int>()::add)` keeps only elements whose `add` returns false, meaning they were already seen. The `filterNotTo(HashSet(), HashSet<Int>()::add)` variant is both concise and performant, as benchmarks show it slots ~40 ns/op with fewest allocations. The article emphasizes that while the map-based `groupBy` approach is straightforward, these alternatives avoid intermediate maps and improve readability and efficiency.

- `Iterable.minus(Collection)` and `MutableList.removeAll(Collection)` remove all occurrences of each element, not just the first, leading to empty results when used for duplicate detection.
- `MutableList.remove(element)` does remove only the first occurrence, but removing each unique element via `forEach` is awkward and still not the most efficient.
- Using `HashSet::add` as a predicate with `filterNot` is a clean way to keep only repeated elements.
- `filterNotTo(HashSet(), HashSet<Int>()::add)` is the fastest and most allocation-friendly option among those benchmarked.