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

The article, authored by Jake Wharton, discusses how Kotlin's collection extension functions, while concise, often create intermediate collections. The example of mapping users to names and joining into a string triggers an IDE warning suggesting a fused form: `users.joinToString() { it.name }`. This eliminates the intermediate collection and iterator from the `map` call, resulting in code that is both shorter and faster.

The author then extends the principle to array and pre-sized list initialization. Instead of `users.map { it.name }.toTypedArray()`, you can use `Array(users.size) { users[it].name }`. Similarly, `IntArray` and `MutableList` variants exist. These forms use indexed loops rather than iterators and intermediate collections, making them more efficient.

The article includes benchmark results comparing the two approaches for joining strings and converting to typed arrays. The fused lambda versions show significantly lower latency and allocations, e.g., `NamesJoinToString.lambda` at ~73.6 ns/op vs `map` at ~126.6 ns/op, and allocates 168 B/op vs 232 B/op. However, the author cautions that these techniques rely on random-access sources; using them on non-random-access collections like linked lists can degrade performance, so they are best used internally where you control the source list.

- Kotlin's `map` followed by `joinToString` creates an intermediate collection; fusing via `joinToString { }` eliminates it.
- Use `Array(size) { }` or `MutableList(size) { }` to initialize collections directly, avoiding intermediate collections.
- Benchmarks show the lambda-based versions are faster and allocate less.
- These fused operations require random-access sources to be efficient.