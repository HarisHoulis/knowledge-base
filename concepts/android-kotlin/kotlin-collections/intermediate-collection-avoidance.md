---
domain: android-kotlin
subdomain: kotlin-collections
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
---

# Intermediate collection avoidance

Kotlin's collection extension functions like `map` create intermediate collections and iterators, which can be avoided by fusing operations. For example, `users.map { it.name }.joinToString()` can be replaced with `users.joinToString() { it.name }`, which transforms each element during string construction, eliminating the intermediate collection. IntelliJ IDEA offers a weak warning and an intention action to refactor this automatically.

- Use fused operations like `joinToString` with a transform instead of separate `map` calls to avoid intermediate collections.
- For arrays and pre-sized lists, use `Array(size) { ... }`, `IntArray(size) { ... }`, and `MutableList(size) { ... }` instead of `map` plus conversion.
- These techniques use indexed loops rather than iterators, making them faster and allocating fewer bytes, as shown in benchmarks.
- Random access to the source list is required for efficiency; avoid this pattern with non-random-access lists like linked or persistent lists.