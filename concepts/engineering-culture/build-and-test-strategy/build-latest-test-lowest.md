---
domain: engineering-culture
subdomain: build-and-test-strategy
concept: build-latest-test-lowest
title: Build on latest Java, test through lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
    author: "Jake Wharton"
---

# Build on latest Java, test through lowest Java

The author argues against the common practice of adding every new Java version to the CI build matrix. Since users consume pre-built JARs rather than building the project themselves, compiling on every version is unnecessary. The recommended approach is to build only once on the latest Java version, which provides the best tooling and cross-compilation capabilities, while targeting the lowest supported Java version via the `--release` flag or source/target compatibility settings.

To retain broad test coverage, Gradle toolchains can be used to execute the same compiled test classes on every supported Java version. This is achieved by registering additional `Test` tasks that use a specific toolchain language version, while copying the classpath and test classes from the main `test` task. This setup reduces CI workload by compiling only once but still verifies behavior across all supported JDKs.

The approach is particularly essential for projects using multi-release JARs, where compilation with newer versions but testing through a lower bound is required. The author also notes that Android developers already follow this principle by keeping `compileSdk` high and `minSdk` low, while testing on intermediate versions.

- Build the project once on the latest Java version, not on every version, because users consume pre-built artifacts.
- Use the `--release` flag or source/target compatibility to target the lowest supported Java version during compilation.
- Leverage Gradle toolchains to run the same compiled test suite on every supported JDK version without recompiling.
- This strategy reduces CI burden while maintaining compatibility checks, and is critical for multi-release JARs.
- Android developers already follow this pattern with high `compileSdk` and low `minSdk`.