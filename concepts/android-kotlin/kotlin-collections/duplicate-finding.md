---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-finding
title: Perils of Duplicate Finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of Duplicate Finding

The article explores various Kotlin approaches to find duplicate elements in an integer array, starting with a straightforward `groupBy` method that produces a set of duplicated values. The author then attempts more concise alternatives, but discovers surprising behavior in Kotlin's collection API: the `minus` operator and `MutableList.removeAll` both remove all occurrences of each specified element, not just the first, contrary to what one might expect from the `remove` method. This subtlety originates from Java's `Collection.removeAll` semantics. After several incorrect attempts, the author settles on a functional approach using `filterNot` with a bound `HashSet` reference, and then refines it further to `filterNotTo(HashSet(), HashSet<Int>()::add)`, which both reads cleanly and performs best in benchmarks. The key lesson is to understand API semantics deeply and to leverage Kotlin's standard library extensions, especially the `To`-suffixed variants, for efficient and idiomatic code.

- Kotlin's `minus` operator and `MutableList.removeAll` remove all occurrences of elements, not just the first, which can lead to incorrect duplicate detection.
- A concise correct solution uses `ints.filterNot(HashSet<Int>()::add)` to keep only elements already seen.
- For better performance and lower allocations, use `filterNotTo(HashSet(), HashSet<Int>()::add)`.
- Always verify collection operation semantics, especially when inheriting behavior from Java.