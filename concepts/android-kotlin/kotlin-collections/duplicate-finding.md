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

The article explores various Kotlin approaches to find duplicate elements in an integer array, highlighting surprising behaviors and performance tradeoffs. Jake Wharton starts with a map-based approach (groupBy + filterValues) that works but feels wasteful, then attempts more concise alternatives. The first attempt, `ints.toList() - ints.toSet()`, fails because Kotlin's `minus` operator removes all occurrences of each element in the collection argument, not just one per element. Similarly, `MutableList.removeAll` also removes all occurrences, inheriting Java's `removeAll` semantics, making it unsuitable for removing only the first occurrence of each duplicate.

- Kotlin's `minus` operator and `removeAll` remove all occurrences of elements in the supplied collection, not just the first occurrence.
- Using `MutableSet.add` as a filter predicate can efficiently identify duplicates: elements where `add` returns false are duplicates.
- The `filterNotTo` variant with a bound `HashSet::add` reference is both the fastest and allocates the fewest bytes in benchmarks.