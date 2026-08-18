---
domain: engineering-culture
subdomain: ci-cd
concept: build-latest-test-lowest
title: Build on latest Java, test through lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
---

# Build on latest Java, test through lowest Java

Adding every new Java version to a CI build matrix is wasteful because users consume pre-built JARs, not source builds. Jake Wharton argues that the build should run only once on the latest Java version, leveraging its excellent cross-compilation capabilities to target the lowest supported version via `--release` or `sourceCompatibility`/`targetCompatibility` (Jake Wharton, https://jakewharton.com/build-on-latest-java-test-through-lowest-java/).

Instead of compiling multiple times, test execution should be varied across all supported Java versions. This is achieved with Gradle toolchains by registering additional `Test` tasks that use different JDK launchers while reusing the same compiled test classes. This setup reduces CI burden and ensures correctness on every supported version, especially for projects using multi-release JARs (Jake Wharton, https://jakewharton.com/build-on-latest-java-test-through-lowest-java/).

Not every project needs this, but it is a best practice for code that conditionally uses new APIs or interacts with non-public APIs. Android developers already follow this pattern with high `compileSdk` and low `minSdk` (Jake Wharton, https://jakewharton.com/build-on-latest-java-test-through-lowest-java/).

- Build only once on the latest Java version to save CI time and use current tools.
- Use Gradle toolchains to run the same test suite on every supported Java version.
- Target the lowest supported Java version via `--release` or source/target compatibility.
- This approach is essential for projects with multi-release JARs or version-dependent behavior.
- Android's compileSdk/minSdk pattern is an existing analogy.