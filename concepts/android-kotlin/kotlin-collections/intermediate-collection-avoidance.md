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

Kotlin's collection extension functions like `map` are convenient but can introduce intermediate collections and extra iterators, hurting performance. For example, `users.map { it.name }.joinToString()` creates an intermediate list before joining. IntelliJ IDEA offers an intention action to simplify this to `users.joinToString() { it.name }`, which fuses the transformation into the join operation, eliminating the extra collection and iterator. The resulting code is both shorter and faster, and the IDE helps discover this superior form.

A similar optimization applies to array and pre-sized list initialization. Instead of `users.map { it.name }.toTypedArray()`, you can use `Array(users.size) { users[it].name }`, which uses an indexed loop rather than an iterator and intermediate collection. Primitive variants like `IntArray` and pre-sized lists via `MutableList(users.size) { ... }` also benefit. This technique requires random-access sources; for linked or persistent lists, performance would be abysmal, so it is best used internally where the list type is controlled.

Benchmarks show significant gains: `joinToString` with a lambda runs at 73.6 ns/op vs 126.6 ns/op for the `map` version, and allocates 168 B/op vs 232 B/op. For `toTypedArray`, the lambda version runs at 10.3 ns/op vs 78.4 ns/op, allocating 40 B/op vs 120 B/op. These improvements come from avoiding iterators and intermediate collections. This strategy is also used by Compose UI's 'fast' collection functions.

- Fuse `map` with terminal operations like `joinToString` to avoid intermediate collections (e.g., `users.joinToString() { it.name }`).
- Use `Array`, `IntArray`, or `MutableList` with a lambda initializer for indexed construction instead of `map().toTypedArray()`.
- Ensure the source list supports random access; otherwise the indexed approach can degrade performance.
- Lambda-based initialization is faster and allocates less, as benchmarks show.
- IntelliJ IDEA's intention actions can guide you to these optimized forms.