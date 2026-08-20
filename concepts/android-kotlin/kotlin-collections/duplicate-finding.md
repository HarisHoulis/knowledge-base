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

The article explores various Kotlin approaches to find duplicate elements in an integer array. The initial map-based solution using `groupBy` and `filterValues` works but is potentially wasteful. Attempts to avoid the map using `toList() - toSet()` and `MutableList.removeAll` fail because both remove all occurrences of each element, not just the first, a behavior inherited from Java.

- `groupBy { it }.filterValues { it.size > 1 }.keys` correctly finds duplicates but may be heavy on allocations.
- `toList() - toSet()` and `MutableList.removeAll(ints.toSet())` unexpectedly remove all occurrences, not just first, due to Kotlin/Java collection semantics.
- A working alternative is `ints.toMutableList().apply { ints.toSet().forEach(::remove) }.toSet()`.
- Using `filterNot` with a bound `HashSet::add` reference elegantly finds duplicates: `ints.filterNot(HashSet<Int>()::add).toSet()`.
- The `filterNotTo` variant (`ints.filterNotTo(HashSet(), HashSet<Int>()::add)`) is both the fastest and allocates the fewest bytes in benchmarks.