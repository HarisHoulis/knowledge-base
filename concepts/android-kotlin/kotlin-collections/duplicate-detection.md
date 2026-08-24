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

In this article, Jake Wharton explores how to find duplicate elements in an integer array using Kotlin. He first presents a straightforward groupBy approach that prints [1, 3] but finds it wasteful. This leads to an investigation of Kotlin collection operations, where he discovers surprising behaviors in the minus operator and MutableList.removeAll, both of which remove all occurrences of elements rather than just the first. These misconceptions initially produce incorrect empty outputs [1].

- Kotlin's minus operator and removeAll remove all occurrences of each element in the supplied collection, not just the first occurrence, which can lead to unexpected results.
- The correct manual approach is to use a MutableList and remove the first occurrence of each element via remove, or more elegantly use a bound function reference like filterNot(HashSet<Int>()::add).
- The filterNotTo variant (e.g., ints.filterNotTo(HashSet(), HashSet<Int>()::add)) is both concise and the fastest, allocating the fewest bytes in benchmarks.