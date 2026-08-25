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

The article (source: https://jakewharton.com/perils-of-duplicate-finding/) explores different Kotlin approaches to finding duplicate elements in a list, starting with a groupBy-based solution. It then investigates alternatives like `toList() - toSet()` and `removeAll`, which surprisingly remove all occurrences rather than just the first, leading to incorrect results. The author demonstrates unexpected behavior in Kotlin's collection operators, inherited from Java, and iteratively refines to a correct solution using a `HashSet` as a bound function reference.

- Kotlin's minus operator and `MutableList.removeAll` remove all occurrences, making them unsuitable for duplicate detection.
- `MutableList.remove` removes only the first occurrence, but there is no built-in to remove first occurrences of each element in a collection.
- A clean and idiomatic solution is `ints.filterNotTo(HashSet(), HashSet<Int>()::add)`, which keeps duplicates.
- The `filterNotTo` version is both the fastest and allocates the fewest bytes in benchmarks.