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

The article discusses how Kotlin's collection extension functions, while convenient, can create intermediate collections and iterators. For example, `users.map { it.name }.joinToString()` first builds a list of names before joining. IntelliJ IDEA offers a weak warning and an intention action to simplify this to `users.joinToString() { it.name }`, which fuses the transformation into the joining operation, eliminating the intermediate collection and iterator. This results in code that is both shorter and faster, and the IDE helps developers discover this superior form.

Similar fused operations are available for array and pre-sized list initialization. Instead of `users.map { it.name }.toTypedArray()`, one can use `Array(users.size) { users[it].name }`, which uses an indexed loop rather than an iterator and intermediate collection. Primitive array versions such as `IntArray` are also available. For mutable lists, `MutableList(users.size) { ... }` provides an analogous lambda-based initializer that can compute elements based on the index or derive data from another source.

A key caveat is that when deriving data from another list, the source must support random access to actually be more efficient. Linked or persistent lists would perform abysmally, so this technique is best for internal library usage where the original list is controlled. Benchmarks in the article show that the lambda initialization variants are significantly faster and allocate fewer bytes due to the absence of iterators and intermediate collections.

- Fusing intermediate map with terminal operations like joinToString avoids extra iterators and collections.
- IntelliJ IDEA's weak warnings and intention actions can automatically refactor to more efficient fused calls.
- Array(users.size) { ... } and MutableList(users.size) { ... } provide indexed-loop initialization, avoiding intermediate collections.
- These techniques require random-access sources; they degrade on linked or persistent lists.
- Benchmarks show notable speed improvements and reduced memory allocation for lambda-based variants.