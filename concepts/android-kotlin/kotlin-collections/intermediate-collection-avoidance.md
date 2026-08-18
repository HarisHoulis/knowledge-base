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

Kotlin's collection extension functions like `map` create intermediate collections that can be avoided by fusing operations. For example, `users.map { it.name }.joinToString()` can be rewritten as `users.joinToString() { it.name }`, which eliminates the extra iterator and intermediate collection, making the code both shorter and faster (Jake Wharton, Intermediate collection avoidance). Similarly, converting a mapped list to an array with `users.map { it.name }.toTypedArray()` can be replaced by `Array(users.size) { users[it].name }`, which uses an indexed loop instead of an iterator and intermediate collection. Primitive variants like `IntArray` are also available for performance-sensitive code (Jake Wharton, Intermediate collection avoidance).

- Use fused operations like `joinToString { transform }` to avoid intermediate collections from `map`.
- Initialize arrays and pre-sized lists with lambda-accepting constructors (`Array(size) { ... }`, `MutableList(size) { ... }`) to compute elements efficiently.
- The technique relies on random access to the source; avoid it if the source is a linked or persistent list.
- Benchmarks demonstrate significant speed improvements and reduced memory allocation compared to manual `map` chains.