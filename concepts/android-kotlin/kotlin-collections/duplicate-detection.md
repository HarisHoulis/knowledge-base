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

Jake Wharton explores how to correctly find duplicate elements in a Kotlin collection, contrasting multiple approaches. He starts with a map-based groupBy solution that works but feels wasteful, then tries several alternatives, revealing surprising behaviors in Kotlin's collection operators. The minus operator removes all occurrences of each element in the set, not just the first, and MutableList.removeAll similarly removes all occurrences, whereas MutableList.remove only removes the first. These subtle asymmetries lead to incorrect results until he finds a functional idiom using a bound function reference to a HashSet's add method with filterNot. The final version, filterNotTo(HashSet(), HashSet<Int>()::add), is both concise and the most performant in microbenchmarks, allocating the fewest bytes.

- Kotlin's minus operator on a list and set removes all occurrences of each set element, yielding an empty list for duplicate-finding.
- MutableList.removeAll removes all occurrences, while MutableList.remove only removes the first occurrence—a surprising asymmetry.
- Using filterNot with a bound HashSet.add reference elegantly keeps only elements that have already been seen.
- filterNotTo(HashSet(), HashSet<Int>()::add) is the fastest and most allocation-friendly approach in microbenchmarks.