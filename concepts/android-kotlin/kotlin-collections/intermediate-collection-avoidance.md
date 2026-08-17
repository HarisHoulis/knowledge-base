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

The article highlights how Kotlin's collection extension functions, while convenient, can create intermediate collections and iterators that hurt performance. For example, `users.map { it.name }.joinToString()` allocates an intermediate mapped list before joining, whereas `users.joinToString() { it.name }` performs the mapping during the join operation, eliminating the extra collection and iterator. Similarly, converting a collection to an array using `map().toTypedArray()` can be replaced with `Array(users.size) { users[it].name }`, and for primitive arrays `IntArray(users.size) { users[it].age }` is available. Pre-sized lists can also be initialized with `MutableList(users.size) { ... }` to avoid intermediate allocations.

The article presents benchmarks showing these lambda-initialization variants are both faster and allocate fewer bytes than the `map`-based alternatives. However, it cautions that this technique relies on random-access source lists; for linked or persistent lists, the indexed access can be abysmal. It recommends using this approach primarily when you control the source list and need efficiency, echoing the strategy used by Compose UI's similarly named 'fast' collection functions.

- Fuse operations: `joinToString(mapping)` instead of `map().joinToString()` to remove intermediate collections.
- Use `Array(size) { ... }` or `IntArray(size) { ... }` for converting collections to arrays without intermediate maps.
- Initialize pre-sized mutable lists with `MutableList(size) { ... }` for efficient element computation.
- Only apply these techniques when the source supports random access; otherwise performance deteriorates.
- Benchmarks confirm lower allocation and faster execution for the lambda-initialized variants.