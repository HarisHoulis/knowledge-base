---
domain: android-kotlin
subdomain: kotlin-collections
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
    author: "Jake Wharton"
---

# Intermediate collection avoidance

The article from Jake Wharton shows how to avoid intermediate collections in Kotlin collection chains. For example, `users.map { it.name }.joinToString()` can be replaced with `users.joinToString() { it.name }`, which is shorter and faster because the mapping happens during string construction, eliminating an extra iterator and intermediate list. The IntelliJ IDEA weak warning suggests this simplification.

Similar fused operations exist for arrays and pre-sized lists. Instead of `users.map { it.name }.toTypedArray()`, one can use `Array(users.size) { users[it].name }`, and for a list, `MutableList(users.size) { users[it].name }`. These use indexed loops instead of an iterator and intermediate collection, reducing overhead.

The author cautions that these techniques are only efficient when the source list supports random access; for linked or persistent lists, performance degrades. Therefore, they are best used in internal library code where the list type is controlled. Benchmarks in the article show significant speedups and reduced allocations for the lambda initializer variants compared to the `map`-based approaches.

- Use `joinToString { }` with a transformation lambda instead of `map` then `joinToString()` to avoid an intermediate collection.
- For arrays, use `Array(size) { ... }` or primitive variants (e.g., `IntArray`) instead of `map` and `toTypedArray()`.
- For pre-sized lists, use `MutableList(size) { ... }` to initialize elements from an index or another random-access source.
- These optimizations require random access to the source list; avoid them for linked or persistent structures.
- Benchmarks show lambda initialization is faster and yields lower memory allocation than `map` followed by conversion.