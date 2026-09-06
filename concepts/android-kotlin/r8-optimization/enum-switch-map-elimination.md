---
domain: android-kotlin
subdomain: r8-optimization
concept: enum-switch-map-elimination
title: R8 Optimization: Enum Switch Maps
sources:
  - title: "R8 Optimization: Enum Switch Maps"
    url: "https://jakewharton.com/r8-optimization-enum-switch-maps/"
---

# R8 Optimization: Enum Switch Maps

The article explains why Java compilers do not directly switch on enum ordinals. Instead, javac generates a synthetic int[] mapping, such as `$SwitchMap$Greeting`, that translates each enum constant's ordinal into a stable one-based index used by the switch. This indirection ensures that reordering enum constants in a separately compiled source file does not change the behavior of already-compiled callers.

Kotlin's `when` expression uses a similar mechanism, generating `$WhenMappings.$EnumSwitchMapping$0` arrays. While necessary for separate compilation, this indirection is wasted in an Android application because the enum and its callers are packaged together. R8's whole-program analysis removes the map, rewrites the switch to use enum ordinals directly, and eliminates the now-unused synthetic classes. This removal is also a prerequisite for further enum optimizations like branch elimination based on constant ordinals.

- javac generates an int[] switch map that maps enum ordinals to stable case indices, preserving behavior across enum constant reordering.
- Bytecode for enum switches loads the mapping array, calls ordinal(), and then indexes into the array before branching.
- R8 removes this synthetic indirection in whole-program optimization, enabling the switch to use ordinals directly.
- Kotlin `when` uses a similarly generated `$WhenMappings` class, which R8 1.6+ can also detect and eliminate.