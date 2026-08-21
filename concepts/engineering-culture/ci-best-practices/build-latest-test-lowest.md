---
domain: engineering-culture
subdomain: ci-best-practices
concept: build-latest-test-lowest
title: Build on Latest Java, Test Through Lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
    author: "Jake Wharton"
---

# Build on Latest Java, Test Through Lowest Java

The article criticizes the common practice of adding every new Java version to a CI build matrix. Building on each version is wasteful because users consume pre-built artifacts, not source builds. Instead, the author recommends building once on the latest Java version, leveraging its excellent cross-compilation capabilities, while targeting the lowest supported version via the `--release` flag or source/target compatibility settings.

- Building on every JDK version is unnecessary; consumers use pre-built jars.
- Use Gradle toolchains to compile once on the latest JDK but run tests on all supported JDKs.
- This reduces CI workload while preserving test coverage across versions.
- Critical for multi-release jars or code that changes behavior based on Java version.
- Android developers already apply this pattern with compileSdk/minSdk and instrumentation tests.