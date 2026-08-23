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

The article demonstrates how to avoid intermediate collections in Kotlin by fusing transformation and terminal operations. For example, instead of `users.map { it.name }.joinToString()`, one can write `users.joinToString() { it.name }`, which performs the mapping during string construction, eliminating the extra iterator and intermediate collection (source). Similarly, for arrays, `Array(users.size) { users[it].name }` replaces `users.map { it.name }.toTypedArray()`, and `MutableList(users.size) { ... }` offers a pre-sized list alternative.

Benchmarks provided in the article show the lambda-initialization variants are significantly faster and allocate fewer bytes. For the joinToString case, the lambda variant is roughly 42% faster and allocates 64 fewer bytes per operation; for typed arrays, the lambda is ~87% faster and allocates 80 fewer bytes. The article also cautions that this technique requires a random-access source to be efficient, and is best used where the list type is controlled, such as internal library code.

- Use `users.joinToString() { it.name }` instead of `users.map { it.name }.joinToString()` to avoid an intermediate collection.
- Use `Array(users.size) { users[it].name }` instead of `users.map { it.name }.toTypedArray()` for arrays.
- For pre-sized lists, use `MutableList(users.size) { ... }` to compute elements without intermediate collections.
- These fused operations are faster and allocate less memory, but require a random-access source list.