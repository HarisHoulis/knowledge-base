---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-finding
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of duplicate finding

In his article "Perils of duplicate finding" (https://jakewharton.com/perils-of-duplicate-finding/), Jake Wharton explores several Kotlin approaches to detect duplicate integers in an array. The initial map-based solution using `groupBy` and `filterValues` works but feels wasteful. Replacing it with the `minus` operator (`ints.toList() - ints.toSet()`) surprisingly returns an empty list because Kotlin's `minus` removes all occurrences of each element in the set, not just one. Similarly, `MutableList.removeAll(ints.toSet())` also removes every occurrence, despite `remove` only removing the first, a subtle asymmetry inherited from Java's `Collection.removeAll`.

The article then demonstrates progressively better approaches. Using `MutableList.remove` in a `forEach` finally yields the duplicated values but requires extra conversion to a set. A partition-based solution with `HashSet.add` works correctly but is visually clunky. The cleanest and most efficient solution uses `filterNotTo(HashSet(), HashSet<Int>()::add)`, which leverages a bound function reference to `add` and keeps only elements that are already in the set. This approach is not only readable but also the fastest and least allocation-heavy in benchmarks.

Key takeaways include understanding the surprising behavior of collection `minus` and `removeAll`, recognizing the asymmetry in `remove` vs `removeAll`, and preferring `filterNotTo` with a bound `HashSet::add` reference for duplicate detection in terms of both clarity and performance.

- Kotlin's `minus` operator on collections removes all occurrences of each specified element, so `ints.toList() - ints.toSet()` always yields an empty list.
- `MutableList.removeAll` removes all occurrences of each element, while `remove` removes only the first; this asymmetry is inherited from Java.
- To find duplicates, use `ints.filterNotTo(HashSet(), HashSet<Int>()::add)`, which is both concise and the fastest in benchmarks.
- Alternative `filterNot(HashSet<Int>()::add).toSet()` works correctly but allocates more bytes than `filterNotTo`.