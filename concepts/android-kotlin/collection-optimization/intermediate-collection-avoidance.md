---
domain: android-kotlin
subdomain: collection-optimization
concept: intermediate-collection-avoidance
title: Intermediate collection avoidance
sources:
  - title: "Intermediate collection avoidance"
    url: "https://jakewharton.com/intermediate-collection-avoidance/"
---

# Intermediate collection avoidance

The article explains how to avoid intermediate collections in Kotlin by fusing collection operations. For example, instead of using `map` followed by `joinToString`, you can call `joinToString` with a transform lambda, which eliminates the intermediate list and iterator. This results in both shorter and faster code, and IntelliJ IDEA warns you to simplify such call chains.

- Use `joinToString()` with a transform lambda instead of `map().joinToString()` to reduce overhead.
- Use lambda-based initializers like `Array(size) { ... }` or `MutableList(size) { ... }` to create collections without intermediate maps.
- Benchmarks show these fused versions are faster and allocate fewer bytes.
- The technique is only efficient when the source list supports random access; for linked or persistent lists, performance degrades.