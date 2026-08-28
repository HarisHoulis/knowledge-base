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

Kotlin's collection extension functions like `map` are convenient but can create intermediate collections and extra iterators, harming performance. Jake Wharton highlights how IntelliJ IDEA offers an intention action to fuse operations, e.g., replacing `users.map { it.name }.joinToString()` with `users.joinToString() { it.name }`, which eliminates the intermediate list and iterator, producing shorter and faster code.

Similarly, when converting a list to an array or a pre-sized list, using lambda-based initializers like `Array(users.size) { users[it].name }` or `MutableList(users.size) { users[it].name }` avoids intermediate collections and use indexed loops. Benchmarks show significant speedups and reduced allocations. However, this technique requires the source to support random access; using it for linked or persistent lists can be abysmal.

- Use fused operations like `joinToString { }` to avoid intermediate collections from `map`.
- For arrays and pre-sized lists, use lambda initializers like `Array(size) { ... }` instead of `map().toTypedArray()`.
- Lambda initializers use indexed loops, improving speed and reducing allocations.
- Only apply this pattern when the source list supports random access.
- IntelliJ IDEA can auto-refactor to these more efficient forms.