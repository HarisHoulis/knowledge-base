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

Kotlin's collection extension functions make it easy to chain operations, but this can create intermediate collections that waste time and memory. For example, `users.map { it.name }.joinToString()` first builds a new list of names, then iterates that list to produce a string. The IDE's intention action suggests fusing these operations into `users.joinToString() { it.name }`, which maps each element directly during string construction, eliminating the intermediate list and iterator (Jake Wharton, https://jakewharton.com/intermediate-collection-avoidance/).

The same strategy applies to array and pre-sized list initialization. Instead of `users.map { it.name }.toTypedArray()`, one can use `Array(users.size) { users[it].name }`. This uses an indexed loop rather than an iterator and intermediate collection, and primitive array variants like `IntArray` are available. For pre-sized lists, `MutableList(users.size) { users[it].name }` works similarly, allowing element initialization based on index or another source.

These fused forms are both shorter and faster, as benchmark results show: `joinToString` with a lambda runs in 73.6 ns/op vs 126.6 ns/op for `map` followed by `joinToString`, and allocated 168 B/op vs 232 B/op. The array initializer is even more dramatic: 10.3 ns/op vs 78.4 ns/op, with 40 B/op vs 120 B/op. However, the author cautions that this technique relies on random access to the source; using it with linked or persistent lists will degrade performance, so it is best suited for internal code with controlled inputs.

- Fuse operations like `map` and `joinToString` to avoid intermediate collections; e.g., `users.joinToString() { it.name }`.
- Use lambda-based initializers `Array(size) { ... }` and `MutableList(size) { ... }` to create arrays and lists without intermediate `map` results.
- These forms use indexed loops instead of iterators, making them faster and more memory-efficient.
- Only apply when the source supports random access; linked or persistent lists will suffer poor performance.