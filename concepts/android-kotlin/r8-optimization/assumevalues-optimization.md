---
domain: android-kotlin
subdomain: r8-optimization
concept: assumevalues-optimization
title: R8 Optimization: Value Assumption
sources:
  - title: "R8 Optimization: Value Assumption"
    url: "https://jakewharton.com/r8-optimization-value-assumption/"
    author: "Jake Wharton"
---

# R8 Optimization: Value Assumption

R8's data-flow analysis can track nullability of variables and eliminate impossible conditionals. This article introduces the `-assumevalues` flag, an R8-specific configuration that extends this range tracking to other types, such as integers. By telling R8 that a field read or method return will always produce a value within a specified range, R8 can determine that certain checks are always true or false and remove them via dead-code elimination.

The principal real-world use case is `Build.VERSION.SDK_INT`. Because AndroidX and other libraries contain hundreds of version checks to support old API levels, specifying an app's minimum SDK lets R8 strip compatibility branches that will never execute. For example, with a minimum SDK of 21 and `-assumevalues class android.os.Build$VERSION { int SDK_INT return 21..2147483647; }`, a helper like `setElevation` collapses into a direct call to the framework method.

A key caveat is that even after eliminating the conditional, R8 deliberately keeps the field read or method call because it may have side effects — a field read can trigger class loading with static initializers. To also remove that read, `-assumenosideeffects` must be used when the developer can safely assert no side effects. The flag is powerful but requires correct assumptions about the program's runtime values.

- `-assumevalues` lets R8 perform constant folding on integer ranges, not just nullability.
- Using it with `Build.VERSION.SDK_INT` and your app's minimum SDK removes impossible Android compatibility branches in libraries and your own code.
- R8 keeps the guarded field read/method call unless `-assumenosideeffects` is specified, to preserve side-effect semantics.
- The optimization helps reduce APK size and method count by eliminating dead code in AndroidX compatibility classes.