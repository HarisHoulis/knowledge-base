---
domain: engineering-culture
subdomain: java-build-strategy
concept: build-latest-test-lowest
title: Build on Latest Java, Test Through Lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
    author: "Jake Wharton"
---

# Build on Latest Java, Test Through Lowest Java

Jake Wharton argues that adding every new Java version to a CI build matrix is inefficient because users consume pre-built jars, not source builds. Instead, he recommends building only once on the latest Java version—leveraging Java's strong cross-compilation capabilities—and using Gradle toolchains to run the test suite on all supported lower versions. This reduces CI burden while preserving compatibility coverage.

The article explains that Gradle toolchains allow normal compilation to happen on a single JDK (the latest) while registering extra Test tasks that execute the same compiled classes on older JDKs. This way, the main and test sources are compiled only once, but tests are executed across the full supported version range. This setup is essential for multi-release jars, which require newer compilers but lower runtime testing.

This practice is also beneficial for projects that vary behavior by Java version or conditionally use newer APIs. It parallels Android development, where a high compileSdk and low minSdk are used with instrumentation tests on intermediate versions—a pattern already considered the norm. The author suggests that for purely algorithmic code, multi-version testing may not yield much, but for version-sensitive projects it is a best practice.

- Build once on the latest Java version and use cross-compilation to target the lowest supported version.
- Use Gradle toolchains to create a test task per supported Java version, reusing the compiled classes.
- This reduces CI workload compared to building and testing on every version in a matrix.
- Essential for multi-release jars and useful for code with version-dependent behavior.
- Mirrors Android's compileSdk/high and minSdk/low strategy with instrumentation tests across intermediate versions.