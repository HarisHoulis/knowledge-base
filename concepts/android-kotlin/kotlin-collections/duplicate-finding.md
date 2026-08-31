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

Jake Wharton explores various Kotlin approaches to finding duplicate integers in a collection. The straightforward map-based solution works but feels wasteful. Attempts using `toList() - toSet()` and `removeAll` yield empty results because Kotlin's `minus` and `removeAll` remove all occurrences of each element, not just the first. This surprising asymmetry, inherited from Java, leads to incorrect behavior. A cleaner approach uses `MutableSet.add` as a predicate with `filterNot`, keeping elements already seen. The most concise and efficient version uses `filterNotTo` with a destination set, which is both fastest and allocates the fewest bytes in benchmarks.

- Kotlin's `minus` and `removeAll` remove all occurrences of an element, not just the first, which can cause unexpected empty results.
- Using `HashSet::add` as a predicate in `filterNot` effectively tracks seen values and retains duplicates.
- `filterNotTo(HashSet(), HashSet<Int>()::add)` is the most elegant and performant solution in the article.
- The `filterNotTo` variant outperforms other methods both in speed and memory allocation.