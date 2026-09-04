---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: memory-model-testing
title: Litmus-Testing Kotlin's Many Memory Models
sources:
  - title: "Litmus-Testing Kotlin's Many Memory Models"
    url: "https://jakewharton.com/litmus-testing-kotlins-many-memory-models/"
---

# Litmus-Testing Kotlin's Many Memory Models

The article explains that Kotlin's compiler backends have different memory models: JavaScript is single-threaded, the JVM is permissive, and Kotlin/Native enforces runtime-checked invariants. These differences affect even single-threaded data structures, because Kotlin/Native restricts top-level val access to the main thread unless annotated appropriately.

During porting of AndroidX collections to Kotlin multiplatform, the author encountered the same issue that affected ArrayDeque: a shared, empty array was implemented as a top-level val but lacked the @SharedImmutable annotation, causing failures when accessed on a background thread. The fix is to run tests on both the main thread and a background thread, using the Kotlin/Native Worker API.

For multiplatform code, the author suggests an expect/actual `threadedTest` function: native implementation runs the body twice (main and background), while JS and JVM simply inline it away, since those memory models do not treat the main thread specially. The article concludes by linking to a feature request for a built-in mechanism to apply this pattern class-wide.

- Kotlin/Native enforces stricter memory model rules than JVM or JS, especially around top-level val access from background threads.
- Shared immutable empty arrays in collection implementations must be annotated with @SharedImmutable for cross-thread accessibility.
- Writing tests that run on both the main thread and a background thread catches these Kotlin/Native-specific bugs.
- The expect/actual mechanism allows common test code to invoke a threaded test helper; native uses Worker, JS/JVM skip redundant execution.