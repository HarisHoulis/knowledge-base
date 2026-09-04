---
domain: android-kotlin
subdomain: d8-dexer
concept: d8-assertions-optimization
title: D8 Optimization: Assertions
sources:
  - title: "D8 Optimization: Assertions"
    url: "https://jakewharton.com/d8-optimization-assertions/"
    author: "Jake Wharton"
---

# D8 Optimization: Assertions

Java's `assert` keyword is used to check invariants—conditions that should always be true. On Android, assertions have traditionally been disabled because the VM is forked from a shared zygote process. As a result, D8 previously eliminated all assertion checks from bytecode, treating the enabled-check as always false in release builds. This made `assert` effectively unusable on Android, despite its value for testing invariants (Jake Wharton, "D8 Optimization: Assertions", https://jakewharton.com/d8-optimization-assertions/).

With AGP 4.1, D8 changes this behavior by computing the assertion-enabled check at compile-time based on whether the build is debuggable. For debug variants, D8 replaces the enabled-check with `true`, preserving the invariant check and message expression in the bytecode. This allows developers to verify invariants at runtime during development while keeping release builds lean by eliminating all assertion overhead. The optimization leverages SSA form to remove both the assertion condition and the accompanying message expression when assertions are disabled, as confirmed by dexdump output (Jake Wharton, "D8 Optimization: Assertions", https://jakewharton.com/d8-optimization-assertions/).

The post notes that Kotlin's `assert()` function has a different semantic behavior and is not yet recognized by D8 for this optimization, although a feature request remains open. This D8 optimization is method-local and distinct from some R8 optimizations, reinforcing the shift toward making `assert` useful in Android debug builds (Jake Wharton, "D8 Optimization: Assertions", https://jakewharton.com/d8-optimization-assertions/).

- Android's D8 traditionally removed all Java assertions because the runtime has them disabled.
- D8 in AGP 4.1 now uses the debuggable flag to decide at compile time whether to enable assertion checks.
- Debug builds retain the invariant check, while release builds eliminate it entirely.
- This makes Java's assert useful for validating invariants in Android debug builds.
- Kotlin's assert() function is not yet optimized by D8.