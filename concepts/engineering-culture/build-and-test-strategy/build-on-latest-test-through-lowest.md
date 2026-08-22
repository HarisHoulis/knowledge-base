---
domain: engineering-culture
subdomain: build-and-test-strategy
concept: build-on-latest-test-through-lowest
title: Build on latest Java, test through lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
    author: "Jake Wharton"
---

# Build on latest Java, test through lowest Java

The article argues that the common practice of running the entire CI build and test suite on every supported Java version is wasteful because users do not build the project from source; they consume pre-built jars. Instead, you should build only once on the latest Java version, which has excellent cross-compilation support via the `--release` flag or Gradle's `sourceCompatibility`/`targetCompatibility` settings, and then use Gradle toolchains to run the test suite on every supported Java version. This reduces CI burden significantly while still verifying compatibility across versions.

The recommended setup keeps the normal `test` task running on the compile JDK and adds a separate `testJdk<version>` task for each older version, all wired into `check`. This is especially important for multi-release jars, where sources must be compiled with newer Java but tested against a lower version bound. The article also notes that Android developers already follow this pattern with high `compileSdk`, low `minSdk`, and testing on intermediate versions, showing that the principle is widely applicable.

- Building on every Java version is pointless because consumers use pre-built jars, not source builds.
- Use Gradle toolchains to compile once on the latest Java and test on all supported versions.
- Cross-compilation via `--release` or Gradle's compatibility options targets the oldest supported Java while using the latest compiler.
- This setup is essential for multi-release jars that require compiling with newer Java but testing through a lower version bound.
- If your code doesn't vary with Java version, multi-version testing may not be needed.