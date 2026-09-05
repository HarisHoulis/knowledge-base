---
domain: android-kotlin
subdomain: d8-optimizations
concept: d8-local-optimizations
title: D8 Optimizations
sources:
  - title: "D8 Optimizations"
    url: "https://jakewharton.com/d8-optimizations/"
    author: "Jake Wharton"
---

# D8 Optimizations

D8, Android's Java-to-Dalvik bytecode compiler, performs local optimizations within a single method body in addition to its well-known Java 8+ backporting and bug-workaround capabilities. One optimization rewrites switch statements into if/else chains when doing so reduces overall bytecode size. For example, a packed-switch with associated data can be larger than a series of conditional jumps when there are few cases or non-contiguous values. D8 computes the cost of both forms and selects the smaller one.

D8 also constant-folds method calls on constant strings and constant-sized arrays. For strings, it evaluates methods such as length(), startsWith(), endsWith(), contains(), equals(), hashCode(), substring(), trim(), and many others at compile time when the receiver is a known constant. This is safe because String is a final class with well-defined behavior. Similarly, when an array is created in the same method with a constant size, D8 replaces array-length lookups with the same constant register used to allocate the array, eliminating the array-length instruction.

These optimizations are intentionally conservative and must not change program behavior. Since they are limited to a single method body, their standalone impact is small, but they multiply in effectiveness when R8 performs whole-program inlining and other global optimizations.

- D8 rewrites switch statements to if/else conditionals when it yields smaller Dalvik bytecode than packed-switch.
- D8 evaluates many String method calls at compile time when the receiver is a constant string.
- D8 replaces array.length on a locally-created array with the constant size used to allocate it.
- All D8 optimizations are local to a method body and have no externally-visible runtime effect.