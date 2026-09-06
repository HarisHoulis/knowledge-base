---
domain: android-kotlin
subdomain: r8-optimization
concept: method-outlining
title: R8 Optimization: Method Outlining
sources:
  - title: "R8 Optimization: Method Outlining"
    url: "https://jakewharton.com/r8-optimization-method-outlining/"
    author: "Jake Wharton"
---

# R8 Optimization: Method Outlining

Jake Wharton discusses R8's method outlining optimization, which de-duplicates repeated bytecode sequences into shared methods. The post is motivated by generated code in Moshi, where each JSON property generates `StringBuilder` code for exception messages. The author considered generating a helper method but found that duplicating the code leads to smaller APKs because R8 can outline the common sequences after whole-program analysis. In the example, two model classes with 10 properties produce 20 `StringBuilder` usages, meeting R8's threshold (at least 20 duplicates, bytecode length 3-99 bytes). R8 replaces the repeated code with calls to `GeneratedOutlineSupport.outline0`.

The article explains why this matters for generated code: manual helper methods can be larger than duplicates if there are not enough call sites; outlining automatically triggers with enough repeated patterns across the whole program. It also notes that Kotlin's `inline` functions can produce code that R8 later outlines, so `inline` should be used only for its intended benefits such as `reified` generics or avoiding lambda allocations. The next planned post in the series is about `const-class` bytecodes.

- Outlining is the opposite of inlining: it de-duplicates repeated bytecode sequences into a shared method.
- R8 only outlines sequences that are repeated at least 20 times and are between 3 and 99 bytes.
- For Moshi-style generated code, duplicating StringBuilder logic can beat manual helper methods because R8's whole-program outlining removes the duplication.
- Kotlin inline functions can generate code that R8 may outline later, so inline should be used judiciously.