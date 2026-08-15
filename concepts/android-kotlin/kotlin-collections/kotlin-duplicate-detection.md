---
domain: android-kotlin
subdomain: kotlin-collections
concept: kotlin-duplicate-detection
title: Perils of duplicate finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of duplicate finding

A correct and efficient solution uses `filterNot` with a bound reference to `HashSet::add`. The `add` function returns `true` the first time an element is seen and `false` for duplicates, so `filterNot` keeps only the duplicates. The final refinement uses `filterNotTo(HashSet(), HashSet<Int>()::add)`, which both filters and collects into a set in one pass. Benchmarks show this is the fastest and least allocating approach among the tried alternatives (Jake Wharton, "Perils of duplicate finding").

- Kotlin's `minus` operator and `removeAll` remove all occurrences of elements, not just the first, which breaks intuitive duplicate removal.
- Using `MutableList.remove` inside `forEach` works but is verbose and inefficient.
- `filterNot(HashSet<Int>()::add)` leverages the boolean return of `set.add` to keep only duplicate elements.
- `filterNotTo(HashSet(), HashSet<Int>()::add)` is the most efficient and readable version, avoiding extra intermediate collections.