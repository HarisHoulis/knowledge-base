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

The article explores different Kotlin approaches to finding duplicate integers in an array, highlighting subtle pitfalls in collection operations. The naive approach of subtracting a set from a list (`ints.toList() - ints.toSet()`) yields an empty list because Kotlin's `minus` operator removes all occurrences of each element in the collection, not just the first. Similarly, `MutableList.removeAll` also removes all occurrences, contrary to what `remove` does, leading to unexpected results. The author eventually arrives at a concise and efficient solution using `filterNotTo` with a bound `HashSet::add` reference, which keeps elements that were already seen. The article also notes that these behaviors are inherited from Java and emphasizes the importance of understanding collection semantics.

- Kotlin's `minus` operator and `MutableList.removeAll` remove all occurrences, not just the first, causing naive duplicate-finding attempts to fail.
- A correct approach uses a `HashSet` to track seen elements: `filterNotTo(HashSet(), HashSet<Int>()::add)` keeps only duplicates.
- Bound function references like `HashSet<Int>()::add` allow concise inline stateful predicates.
- The `filterNotTo` variant is both the fastest and most memory-efficient among the tested alternatives.