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

Jake Wharton explores various Kotlin approaches to finding duplicate integers in an array, highlighting subtle pitfalls in collection operations. He initially used `groupBy`, which works but is memory-wasteful. Attempts to subtract a `Set` from a `List` using `toList() - toSet()` unexpectedly return an empty list because the `minus` operator removes all occurrences of each element, not just the first. Similarly, `MutableList.removeAll(ints.toSet())` also removes all occurrences, contradicting the behavior of `MutableList.remove`, which only removes the first occurrence. This asymmetry is inherited from Java's `Collection.removeAll` (Jake Wharton, "Perils of duplicate finding").

- The `minus` operator and `removeAll` remove all occurrences of each specified element, making them unsuitable for finding duplicates by removing first occurrences.
- `MutableList.remove` removes only the first occurrence, but there is no convenient function to remove first occurrences of each element from a supplied collection.
- A robust and readable solution uses `filterNot` with a bound reference to `HashSet::add`, keeping elements whose set addition returns false (i.e., already seen).
- The `filterNotTo` variant, which supplies a destination set, is both the fastest and allocates the least memory in benchmarks.
- When using collection operators, be aware of surprising semantics inherited from Java and choose functional alternatives like `filterNot` to avoid hidden bugs.