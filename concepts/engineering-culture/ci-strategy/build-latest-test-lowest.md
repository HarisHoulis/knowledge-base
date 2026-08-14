---
domain: engineering-culture
subdomain: ci-strategy
concept: build-latest-test-lowest
title: Build on latest Java, test through lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
    author: "Jake Wharton"
---

# Build on latest Java, test through lowest Java

The article argues that compiling a project on every Java version in CI is wasteful because consumers only use the pre-built jar, and the build is done once. Instead, developers should compile with a single, latest Java version and use Gradle toolchains to run tests on all supported Java versions. This reduces CI burden because compilation happens once, while test execution varies across versions, ensuring compatibility without redundant builds. The approach also supports multi-release jars and is analogous to Android's pattern of high compileSdk with low minSdk and testing across intermediate versions.

- Do not build on every Java version; build once on the latest Java using cross-compilation to target the lowest supported version.
- Use Gradle toolchains to create separate test tasks (e.g., testJdk8, testJdk9) that run the test suite on each supported Java version without recompiling.
- This strategy reduces CI time while still verifying behavioral differences across Java versions, which is especially important for multi-release jars or version-sensitive APIs.