---
domain: android-kotlin
subdomain: build-tooling
concept: gradle-toolchains-not-recommended
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle Java toolchains are rarely a good idea for compilation, despite recommendations from Gradle and Android docs. Using a 10-year-old JDK to target old Java versions increases the risk of compiler bugs, ignores container resource limits, and produces outdated artifacts like non-searchable Javadoc. Modern JDKs can cross-compile perfectly using the `--release` flag (Java) or `-Xjdk-release` flag (Kotlin), which set both bytecode and API compatibility without needing an old JDK installed.

Toolchains still have utility for running JVM tests on multiple Java versions and for isolating tools that rely on unstable JDK internals. However, they should not be used for compilation because newer JDKs are faster, respect cgroups limits, and have fewer bugs. The article also notes that toolchains do not control the JVM running Gradle itself, so they don't solve all JDK compatibility issues.

- Compiling with old JDKs via toolchains is unnecessary since modern JDKs can cross-compile using `--release` (Java) or `-Xjdk-release` (Kotlin).
- Old JDKs may not honor container resource limits, can have compiler bugs, and produce outdated artifacts (e.g., non-searchable Javadoc).
- Toolchains remain useful for running JVM unit tests on multiple Java versions and for tools that require older JDK internals.
- Avoid installing multiple old JDKs for compilation; they consume disk space and provide no benefit over a modern JDK.