---
domain: android-kotlin
subdomain: r8-optimization
concept: enum-ordinal-name-optimization
title: R8 Optimization: Enum Ordinals and Names
sources:
  - title: "R8 Optimization: Enum Ordinals and Names"
    url: "https://jakewharton.com/r8-optimization-enum-ordinals-and-names/"
---

# R8 Optimization: Enum Ordinals and Names

This article from Jake Wharton's series on D8 and R8 explains two small but effective optimizations R8 performs on Java/Kotlin enums. When an enum constant is statically known (e.g., via sget-object) and flows into a call to ordinal(), R8 replaces the constant lookup and the ordinal() call with the fixed integer ordinal value. This is particularly useful for switch statements over enums, which internally call ordinal(), because the resulting constant can then enable branch elimination to remove all but the relevant switch case.

Similarly, R8 detects when a statically known enum constant flows into a call to name(). In that case, it replaces the lookup and method call with a string constant equal to the constant's declared name. Since these strings already exist in the dex constant pool (as the enum constant names), no extra string allocation cost is incurred. The optimization also applies to toString() when the enum does not override it, because the default implementation returns name(). These optimizations may not be dramatic on their own, but they unlock further compile-time analysis such as string constant operations and branch elimination. The author also notes that he personally contributed these optimizations to R8.

- R8 replaces a statically known enum constant followed by ordinal() with the constant's integer ordinal value.
- Because Java switch statements on enums compile to ordinal() calls, this optimization can enable branch elimination in switch expressions.
- R8 replaces a statically known enum constant followed by name() with a string constant equal to the enum constant name.
- When toString() is not overridden, it behaves like name() and is optimized the same way.
- These optimizations are small but work together with other R8 passes to produce more compact and efficient bytecode.