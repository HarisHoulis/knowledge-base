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

The article discusses how Kotlin collection extension functions can be written in a more efficient form by avoiding intermediate collections. For example, `users.map { it.name }.joinToString()` can be replaced with `users.joinToString() { it.name }`, which fuses the mapping into the join operation and eliminates the additional iterator and intermediate collection. IntelliJ IDEA provides a weak warning and an intention action to perform this refactoring automatically (https://jakewharton.com/intermediate-collection-avoidance/).

Similar fused operations exist for array and pre-sized list initialization. Instead of `users.map { it.name }.toTypedArray()`, one can use `Array(users.size) { users[it].name }`, trading the intermediate iterator and collection for an indexed loop. Primitive array versions like `IntArray(users.size) { users[it].age }` are also available, and `MutableList(users.size) { users[it].name }` works for lists. These lambda-accepting initializers are useful for setting default values, computing elements from the index, or deriving data from another source (https://jakewharton.com/intermediate-collection-avoidance/).

Benchmarks in the article show significant improvements: for `joinToString`, allocation drops from 232 B/op to 168 B/op and time from ~126 ns to ~74 ns; for `toTypedArray`, allocation drops from 120 B to 40 B and time from ~78 ns to ~10 ns. However, the article cautions that these techniques rely on random-access lists; using them on linked, persistent, or otherwise non-random-access structures would result in abysmal performance. Therefore, they are best suited for internal library usage where the original list type is controlled (https://jakewharton.com/intermediate-collection-avoidance/).

- Prefer fused functions like `joinToString(transform)` over `map(...).joinToString()` to eliminate intermediate collections.
- Use `Array(size) { ... }`, `IntArray(size) { ... }`, and `MutableList(size) { ... }` for efficient initialization via indexed loops.
- These optimizations only improve performance when the source list supports random access; avoid for linked or persistent lists.
- IntelliJ IDEA can automatically refactor some of these patterns via intention actions.