---
domain: android-kotlin
subdomain: kotlin-collections
concept: intermediate-collection-avoidance
title: Intermediate Collection Avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
    author: "Jake Wharton"
---

# Intermediate Collection Avoidance

Jake Wharton discusses how Kotlin's standard collection functions like `map` can create intermediate collections and iterators that are unnecessary. He demonstrates that the IDE's "weak warning" can refactor `users.map { it.name }.joinToString()` into the more efficient `users.joinToString() { it.name }`, which fuses the mapping into the joining operation and eliminates the intermediate collection and iterator. This is both shorter and faster, and the IDE helps discover this superior form (Jake Wharton, Intermediate collection avoidance).

Wharton also highlights similar fused operations for array and pre-sized list initialization using lambda initializers, such as `Array(users.size) { users[it].name }` instead of `users.map { it.name }.toTypedArray()`, and `MutableList(users.size) { users[it].name }` for pre-sized lists. These alternatives trade the intermediate iterator and collection for indexed loops, which are more efficient. Benchmarks show significant improvements: for converting names to typed arrays, the lambda variant ran in 10.326 ns/op versus 78.444 ns/op for the map version and allocated fewer bytes. However, Wharton cautions that this technique only works well when the source list supports random access; for linked or persistent lists, performance will be abysmal, so it is best used for internal library code where the list type is controlled.

- The IntelliJ IDEA weak warning can auto-refactor chained collection calls like `map` followed by `joinToString` into a fused form that eliminates intermediate collections and iterators.
- For creating arrays or pre-sized lists, using a lambda initializer (e.g., `Array(size) { ... }`) is faster and allocates less than `map` followed by `toTypedArray()` or similar.
- Primitive array variants like `IntArray` are also available for performance-sensitive code.
- These optimizations rely on random access; when the source list is linked or persistent, the indexed loop approach can be much slower.
- Benchmarks confirm the lambda initialization approach is both faster and more memory-efficient than the intermediate-collection approach.