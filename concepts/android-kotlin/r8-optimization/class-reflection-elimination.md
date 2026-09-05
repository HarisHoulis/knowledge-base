---
domain: android-kotlin
subdomain: r8-optimization
concept: class-reflection-elimination
title: R8 Optimization: Class Reflection and Forced Inlining
sources:
  - title: "R8 Optimization: Class Reflection and Forced Inlining"
    url: "https://jakewharton.com/r8-optimization-class-reflection-and-forced-inlining/"
---

# R8 Optimization: Class Reflection and Forced Inlining

This article from the R8 optimization series shows how R8's whole-program analysis can eliminate reflection on class objects. When a class is known to have no subtypes, R8 can replace an instance call like `this.getClass()` with a `const-class` instruction for that specific class. If the resulting `Class` reference is immediately used by a method such as `getSimpleName()`, the class constant optimization from a previous post can then replace the entire sequence with a simple string literal, e.g. `"MyActivity"`.

The article illustrates this with a library method that accepts an `Activity` and infers a log name from `activity.getClass().getSimpleName()`. Because the activity parameter is not a fixed class literal, this cannot be resolved at compile time. Normally the method is too large to inline, but R8 has an unsupported, testing-only rule `-alwaysinline` that forces inlining. Moving the `getClass().getSimpleName()` calls into call sites such as `MyActivity.onCreate` allows R8 to see the actual class and ultimately replace reflection with the string constant.

The author warns that `-alwaysinline` is undocumented and unsupported: it may change or disappear, and forcing inlining can bloat bytecode unless a subsequent optimization applies. Kotlin's `inline` function modifier is mentioned as a stable alternative for Kotlin callers. The `getClass()` optimization itself saves only a few bytes, but its main value is unlocking further optimizations like string replacement.

- R8 can replace `this.getClass()` with a class literal when whole-program analysis proves no subclasses exist.
- Replacing `getClass()` enables existing class constant optimizations to turn `getSimpleName()` into a literal string.
- The R8-specific `-alwaysinline` rule can force inlining of otherwise too-large methods to expose these optimizations at call sites.
- Forced inlining is unsupported and risks bytecode bloat; Kotlin's `inline` modifier provides a stable alternative for Kotlin callers.
- The optimization saves only four bytes but is valuable because it unlocks subsequent string optimizations.