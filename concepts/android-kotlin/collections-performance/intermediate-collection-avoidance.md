---
domain: android-kotlin
subdomain: collections-performance
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
    author: "Jake Wharton"
---

# Intermediate collection avoidance

The article discusses avoiding intermediate collections in Kotlin by fusing operations. For example, `users.map { it.name }.joinToString()` can be replaced with `users.joinToString() { it.name }`, eliminating an extra iterator and intermediate collection. Similarly, to create arrays or pre-sized lists, use `Array(users.size) { users[it].name }` or `MutableList(users.size) { users[it].name }` instead of `map().toTypedArray()` or `map().toMutableList()`. These lambda-based initializers use indexed loops instead of iterators, reducing overhead. Benchmarks show significant performance gains: e.g., `joinToString` with lambda is ~42% faster and allocates 64 fewer bytes per operation compared to the `map` version. The author notes that these techniques require random access to the source list; they work best for internal library usage where the source structure is known, and should be avoided for linked or persistent lists where indexing is inefficient. The IDE's intention action can automatically refactor some of these patterns, making the optimization easy to discover and apply.

- Fuse collection operations to avoid intermediate collections, e.g., `users.joinToString() { it.name }` instead of `users.map { it.name }.joinToString()`.
- Use lambda-based initializers like `Array(size) { ... }` or `MutableList(size) { ... }` instead of mapping to a list and then converting or copying.
- Fused operations are faster and allocate less memory due to indexed loops without iterators or intermediate collections.
- Random access to the source list is required for efficiency; avoid these patterns for linked or persistent lists.
- IntelliJ IDEA can automatically refactor some call chains to the more efficient fused forms.