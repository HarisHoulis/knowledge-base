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

Kotlin's collection extension functions like `map` are convenient but can create intermediate collections and extra iteration. Jake Wharton discusses how IDEs and manual refactoring can eliminate these overheads by fusing operations. For example, `users.map { it.name }.joinToString()` can be replaced with `users.joinToString() { it.name }`, which transforms each element during string construction, removing the intermediate list and iterator. Similarly, `users.map { it.name }.toTypedArray()` can be replaced with `Array(users.size) { users[it].name }`, and pre-sized lists can use `MutableList(users.size) { ... }` to avoid extra allocations. These approaches use indexed loops instead of iterators, resulting in significant performance improvements and lower memory allocation. However, the author cautions that random access is required for efficient indexed loops, making this technique best suited for internal use with known list implementations.

- Fuse map with terminal operations like joinToString to avoid intermediate collections and extra iterations.
- Use Array(size) and MutableList(size) initializers with a lambda to compute elements directly, reducing overhead.
- Benchmarks show lambda initialization variants are faster and allocate fewer bytes due to indexed loops and no intermediate collection.
- These techniques require random access; avoid using them on lists with non-random-access performance (e.g., linked lists).