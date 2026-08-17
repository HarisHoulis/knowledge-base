---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-detection
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
---

# Perils of duplicate finding

The article explores several approaches to finding duplicate integers in a Kotlin array, illustrating common pitfalls with collection operators. Initially, using `groupBy` works but is considered wasteful. Attempts using `toList() - toSet()` and `MutableList.removeAll` surprisingly yield empty results because the `minus` operator and `removeAll` remove all occurrences of each element, not just the first. This behavior is inherited from Java's `Collection.removeAll` and is often counterintuitive.

The author then tries `MutableList.remove` with a `forEach` which works but is visually awkward. A more elegant solution uses `partition` with a `HashSet` to separate seen and duplicate elements, but the best approach is a simple `filterNotTo(HashSet(), HashSet<Int>()::add)`, which is both concise and efficient. Benchmarking shows `filterNotTo` is fastest and allocates the least memory among the viable options.

- The `minus` operator and `removeAll` remove all occurrences of elements, not just the first, leading to surprising results.
- `filterNot` with a bound `HashSet::add` reference is a clean way to collect duplicates, keeping elements where `add` returns false.
- `filterNotTo(HashSet(), HashSet<Int>()::add)` is the most efficient variant, with best performance and lowest allocation.
- Kotlin's collection behavior often mirrors Java, so understanding the underlying Java semantics is essential.