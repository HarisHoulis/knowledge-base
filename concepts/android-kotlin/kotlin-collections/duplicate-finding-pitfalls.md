---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-finding-pitfalls
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
---

# Perils of duplicate finding

The article explores several Kotlin approaches to finding duplicate integers in a list, highlighting surprising behaviors in standard library collection operations. Using `ints.groupBy { it }.filterValues { it.size > 1 }.keys` works but is wasteful. Attempts like `ints.toList() - ints.toSet()` and `mutableList.removeAll(ints.toSet())` unexpectedly return empty lists because both the `minus` operator and `removeAll` remove all occurrences of the supplied elements, not just the first (source: https://jakewharton.com/perils-of-duplicate-finding/). This behavior is inherited from Java's `Collection.removeAll`.

A correct but verbose approach uses `MutableList.remove` inside a loop. More elegant solutions leverage `MutableSet.add`'s boolean return to partition or filter seen values. The final recommended approach is `ints.filterNotTo(HashSet(), HashSet<Int>()::add)`, which is concise, readable, and benchmarked as the fastest with fewest allocations (source: https://jakewharton.com/perils-of-duplicate-finding/).

- Kotlin's `minus` operator on a List and Set removes all occurrences of each element in the set, so `list - set` always yields an empty list for duplicate detection.
- `MutableList.removeAll` also removes all occurrences, unlike `MutableList.remove`, which removes only the first occurrence; this asymmetry is inherited from Java.
- A reliable and efficient duplicate filter is `filterNotTo(HashSet(), HashSet<Int>()::add)`, which leverages the bound `MutableSet.add` reference to keep only previously seen elements.
- Benchmarks show `filterNotTo` is about 2.4x faster and allocates ~44% fewer bytes than the naive `groupBy` approach.