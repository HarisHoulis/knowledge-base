---
domain: android-kotlin
subdomain: r8-optimizations
concept: staticization
title: R8 Optimization: Staticization
sources:
  - title: "R8 Optimization: Staticization"
    url: "https://jakewharton.com/r8-optimization-staticization/"
    author: "Jake Wharton"
---

# R8 Optimization: Staticization

R8 is the optimizing version of D8, the Android dexer. It parses Java bytecode into an intermediate representation, applies optimization passes, and then writes Dalvik bytecode. This post examines the staticization optimization, which converts instance methods that do not actually need an instance into static methods. Kotlin companion objects are compiled to a separate nested `Companion` class plus a singleton field on the enclosing class, adding binary size, class-loading time, memory pressure, and slower virtual calls. R8 recognizes this Kotlin-specific bytecode pattern, moves companion methods onto the enclosing class as static methods, and removes the `Companion` class and singleton field entirely, as shown in the provided bytecode examples.

- Staticization makes instance methods static when the receiver is not actually used.
- R8 specifically understands Kotlin companion object bytecode: it moves methods to the enclosing class and eliminates the `Companion` class and singleton field.
- Kotlin call sites (e.g., `Greeter.Companion.hello()`) are rewritten to static calls like `Greeter.hello()`.
- The optimization still occurs when `@JvmStatic` is used, eventually removing the companion class.
- It also applies to Kotlin `object`s and Java singleton classes, reducing binary size, class loading, memory pressure, and virtual call overhead.