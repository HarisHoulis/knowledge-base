---
domain: android-kotlin
subdomain: performance
concept: divide-vs-shift
title: Which is better on Android: divide by 2 or shift by 1?
sources:
  - title: "Which is better on Android: divide by 2 or shift by 1?"
    url: "https://jakewharton.com/which-is-better-on-android-divide-by-two-or-shift-by-one/"
    author: "Jake Wharton"
---

# Which is better on Android: divide by 2 or shift by 1?

The article investigates whether using bitwise shifts instead of multiplication or division by powers of two improves performance on Android. Jake Wharton traces code through javac/kotlinc, D8/R8, and ART compilers. He shows that javac and kotlinc produce identical bytecode for multiply and shift-left, while divide and shift-right remain distinct due to Java's semantics for negative division. D8 and R8 preserve these operations in Dalvik bytecode without optimizing them.

ART, however, compiles `value * 2` and `value << 1` to exactly the same native code (shl/lsls), and deduplicates them. Division by 2 is compiled to an arithmetic shift right with extra instructions to handle negative values, unlike a plain shift right. This means replacing `value * 2` with `value << 1` offers no benefit, and benchmarks on a Pixel 3 show division and shift differ by only ~1 ns (4 ns vs 3 ns), effectively no difference. The author concludes to reserve shifts for bitwise operations and use arithmetic operators for clarity.

- javac/kotlinc, D8, and R8 do not optimize multiply/divide by 2 into shifts in Dalvik bytecode.
- ART compiles `value * 2` and `value << 1` to identical native code, so there is no performance reason to prefer shifts for multiplication.
- `value / 2` compiles to a shift-right plus extra instructions to handle negative numbers, unlike `value >> 1` which is a plain shift.
- Benchmarks show division and shift differ by ~1 ns (4 ns vs 3 ns) on a Pixel 3, i.e., effectively no difference.
- Reserve shifts for bitwise operations; use arithmetic operators for clarity.