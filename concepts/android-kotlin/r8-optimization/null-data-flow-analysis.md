---
domain: android-kotlin
subdomain: r8-optimization
concept: null-data-flow-analysis
title: R8 Optimization: Null Data Flow Analysis (Part 1)
sources:
  - title: "R8 Optimization: Null Data Flow Analysis (Part 1)"
    url: "https://jakewharton.com/r8-optimization-null-data-flow-analysis-part-1/"
    author: "Jake Wharton"
---

# R8 Optimization: Null Data Flow Analysis (Part 1)

The post also compares behavior across tools. The same IR is shared by D8, so even without R8's inlining optimizations, D8 eliminates trivially true/false conditionals from Java source directly, whereas the legacy `dx` tool retains them because its IR lacks nullability information (source). This illustrates that modern Android tooling significantly improves bytecode quality through data flow analysis.

- R8's IR uses SSA form, enabling null data flow analysis across inlined code.
- After inlining a `coalesce` function, R8 can prove certain null checks are always true or false and remove dead branches.
- D8 alone also performs this dead code elimination for conditionals directly present in source, unlike the legacy `dx` tool.
- The resulting Dalvik bytecode matches hand-optimized source with zero conditionals.