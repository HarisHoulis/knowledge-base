---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-finding
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
---

# Perils of duplicate finding

The article explores different ways to find duplicate integers in a Kotlin array, starting with a straightforward groupBy approach but then investigating more efficient or concise alternatives. Several pitfalls are highlighted: the `minus` operator and `MutableList.removeAll` both remove all occurrences of the supplied elements, not just the first, which leads to incorrect results when trying to remove one copy of each value. This behavior is inherited from Java's Collection.removeAll.

- The `minus` operator on collections removes all occurrences of each element in the subtracted collection, not just one per element.
- `MutableList.removeAll` also removes all occurrences, while `MutableList.remove` removes only the first occurrence, creating a subtle asymmetry.
- Using `filterNot` with a bound `HashSet::add` reference elegantly filters out elements that have been seen before, yielding duplicates.
- The `filterNotTo` variant is the fastest and allocates the fewest bytes according to the provided benchmarks, making it the recommended approach.