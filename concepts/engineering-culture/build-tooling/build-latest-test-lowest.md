---
domain: engineering-culture
subdomain: build-tooling
concept: build-latest-test-lowest
title: Build on latest Java, test through lowest Java
sources:
  - title: "Build on latest Java, test through lowest Java"
    url: "https://jakewharton.com/build-on-latest-java-test-through-lowest-java/"
---

# Build on latest Java, test through lowest Java

The article argues that adding every new Java version to a CI matrix is unnecessary because users do not build the project from source; they consume the pre-built JAR. Instead, you should build once on the latest Java version, which also provides access to the newest tooling, and use Java's cross-compilation capabilities to target the lowest supported version via the `--release` flag or `sourceCompatibility`/`targetCompatibility`.

- Build on a single, latest Java version in CI rather than building on every version.
- Use Gradle toolchains to create test tasks that run the test suite on each supported JDK.
- Target the lowest supported Java version with `--release` or source/target compatibility.
- Hooking these test tasks into `check` ensures compatibility across all supported versions without duplicating compilation.
- This strategy is particularly important for multi-release JARs, though not every project needs it.