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

Kotlin's collection extension functions make data transformation easy, but chaining functions like `map` and `joinToString` creates intermediate collections and extra iterators that waste memory and CPU. The article shows that IDE warnings can guide developers to fused operations, such as `users.joinToString() { it.name }`, which performs the mapping during string construction and eliminates the intermediate collection entirely.

For array or pre-sized list creation, the same principle applies. Instead of `users.map { it.name }.toTypedArray()`, using `Array(users.size) { users[it].name }` substitutes an indexed loop for the iterator and intermediate collection. This pattern is also available for primitive arrays (e.g., `IntArray`, `DoubleArray`) and `MutableList` initializers, enabling efficient element derivation from a source with random access.

Benchmarks included in the article show significant improvements: the fused lambda forms are faster and allocate fewer bytes. However, this technique relies on random-access sources; using a linked or persistent list would degrade performance. Therefore, it is most appropriate in internal library code where the source list is controlled.

- Use `joinToString` with a transform lambda to avoid intermediate `map` collections.
- Initialize arrays and pre-sized lists with lambda-based constructors like `Array(size) { ... }` to use indexed loops.
- Only apply the indexed-loop pattern when the source supports random access, or performance will suffer.
- The fused operations are both shorter and faster, and benchmarks show lower memory allocation.