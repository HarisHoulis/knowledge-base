---
domain: android-kotlin
subdomain: r8-optimization
concept: class-constant-operations
title: R8 Optimization: Class Constant Operations
sources:
  - title: "R8 Optimization: Class Constant Operations"
    url: "https://jakewharton.com/r8-optimization-class-constant-operations/"
    author: "Jake Wharton"
---

# R8 Optimization: Class Constant Operations

R8, Android's optimizer, can evaluate certain class operations at compile-time because class references are present in bytecode. As demonstrated with `MyClass.class.getSimpleName()`, R8 replaces such calls with the resulting string literal, turning a static field initialization that would run when the class loads into a direct constant. This removes the need for the `<clinit>` method and allows the constant to be inlined at usage sites, eliminating runtime overhead for patterns like log tags that use class names.

- R8 can replace `MyClass.class.getSimpleName()` (and `getName()`/`getCanonicalName()`) with the compile-time string literal when the class is known, eliminating runtime reflection and the static initializer.
- The optimization interacts correctly with obfuscation: R8 defers the substitution until after the class receives its final obfuscated name, so runtime behavior remains consistent.
- To avoid bloat in the dex string pool, the optimization is currently limited to top-level types; nested/anonymous types are excluded.
- Kotlin's reified generic type parameters combined with inline functions guarantee class literal references, enabling R8 to apply this optimization more broadly.
- If further optimizations (like class merging) change the effective class name, R8 adjusts the string accordingly, preserving correctness.