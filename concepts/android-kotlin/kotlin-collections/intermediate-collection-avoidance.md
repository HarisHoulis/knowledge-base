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

Kotlin's collection extension functions make transformations easy but can create intermediate collections. For example, `users.map { it.name }.joinToString()` produces an intermediate list of names before joining. IntelliJ IDEA offers a warning and intention action to simplify the chain to `users.joinToString() { it.name }`, mapping during string construction and eliminating the extra iterator and collection (Jake Wharton, Intermediate collection avoidance).

Similar fused operations include initializing arrays or pre-sized lists with a lambda: `Array(users.size) { users[it].name }` instead of `users.map { it.name }.toTypedArray()`, and `IntArray(users.size) { users[it].age }` for primitive arrays. This trades the iterator and intermediate collection for an indexed loop, which is more efficient but requires random-access lists to avoid abysmal performance (Jake Wharton, Intermediate collection avoidance).

Benchmarks show that lambda-initialized variants are faster (e.g., 10.3 ns/op vs 78.4 ns/op for toTypedArray) and allocate fewer bytes (40 vs 120 B/op). Kotlin's zero-overhead functions keep code concise while performance is improved (Jake Wharton, Intermediate collection avoidance).

- Use fused operations like `joinToString { }` to avoid intermediate collections.
- Prefer `Array(size) { ... }` or `MutableList(size) { ... }` over `map().toTypedArray()` for initialization.
- These techniques rely on random access; avoid for non-random-access lists.
- Benchmarks show significant speed and allocation improvements.