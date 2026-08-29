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

The article explores efficient ways to find duplicate integers in a Kotlin array. Initial approaches using `toList() - toSet()` and `removeAll(toSet())` surprisingly return an empty list because Kotlin's `minus` operator and `MutableList.removeAll` remove all occurrences of each element, not just the first. This behavior is inherited from Java's `Collection.removeAll`, making it a subtle pitfall for developers expecting list-like removal semantics.

The author then iterates through several correct solutions, including using `MutableList.remove` in a loop, which works but is verbose. A cleaner functional approach uses `partition` with a `HashSet` to separate seen and duplicate elements, but the most idiomatic and readable solution is `filterNot` with a bound method reference to a `HashSet`'s `add` function, keeping only elements already seen. Further refinement with `filterNotTo` avoids an intermediate collection, directly populating the result set.

Benchmarks show that `filterNotTo` is both the fastest and allocates the fewest bytes, making it the optimal choice even when performance matters. The article highlights the importance of understanding collection operation semantics and leveraging Kotlin's standard library functions for concise, efficient code.

- Kotlin's `minus` operator on collections removes all occurrences of given elements, which can silently produce empty lists when used for duplicate detection.
- `MutableList.removeAll` behaves similarly, removing all occurrences of each element, unlike `remove` which removes only the first.
- A reliable and readable approach uses `filterNot(HashSet()::add)` to keep elements that have already been seen.
- `filterNotTo(HashSet(), HashSet()::add)` improves both performance and memory allocation by avoiding intermediate collections.