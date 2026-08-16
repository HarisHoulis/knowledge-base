---
domain: android-kotlin
subdomain: kotlin-collections
concept: duplicate-detection
title: Perils of Duplicate Finding
sources:
  - title: "Perils of duplicate finding"
    url: "https://jakewharton.com/perils-of-duplicate-finding/"
    author: "Jake Wharton"
---

# Perils of Duplicate Finding

The article explores several Kotlin approaches to finding duplicate integers in a list, highlighting surprising behaviors in standard library functions. The naive `list - set` approach fails because `Iterable.minus` removes all occurrences of each element in the collection, not just the first. Similarly, `MutableList.removeAll` also removes all occurrences, despite `MutableList.remove` only removing the first occurrence—an asymmetry inherited from Java's `Collection.removeAll`. A correct and idiomatic solution uses `filterNot` with a bound reference to `HashSet::add`, keeping elements that have already been seen. Adding the `To` variant `filterNotTo` into a pre-allocated `HashSet` yields the most concise and efficient version, both in speed and memory allocation.

- Kotlin's `minus` operator on a collection removes all matching elements, making `toList() - toSet()` always return an empty list for duplicates.
- `MutableList.removeAll` also removes all occurrences, contrary to the single-element `remove` semantics, a behavior inherited from Java.
- Using `filterNot(HashSet<T>()::add)` correctly identifies duplicates by keeping elements whose set addition returns false.
- The `filterNotTo` variant is both the cleanest and the fastest, with the lowest byte allocation in benchmarks.
- Always verify collection operator semantics; naming can be misleading (e.g., `removeAll` does not mean 'remove one of each').