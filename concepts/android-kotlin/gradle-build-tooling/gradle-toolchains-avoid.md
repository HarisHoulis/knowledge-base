---
domain: android-kotlin
subdomain: gradle-build-tooling
concept: gradle-toolchains-avoid
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle toolchains are rarely a good idea for compilation, despite recommendations from Gradle and Android documentation. Using an old JDK as a toolchain leads to outdated compilers that lack container resource-limit support, contain unfixed bugs, and are slower than modern JDKs. As an example, Retrofit's Javadoc was built with JDK 8 and therefore missed searchable Javadoc introduced in JDK 9. Modern JDKs can cross-compile to older targets using the `--release` flag (Java) or `-Xjdk-release` flag (Kotlin), making old JDKs unnecessary for compilation. Toolchains also consume significant disk space and do not control the JVM running the build itself. However, toolchains still have utility for running unit tests on older JVM versions and for isolating tools that depend on JDK internals, such as Google Java Format or Error-Prone.

- Don't use Gradle toolchains for compilation; use `--release` for Java and `-Xjdk-release` for Kotlin.
- Old JDKs often lack container-aware resource limits, have more compiler bugs, and build slower than modern JDKs.
- Modern JDKs accurately cross-compile to older Java versions, so there is no need to install and use old JDKs for compilation.
- Toolchains are still useful for running unit tests on the lowest supported JVM and for tools that rely on unstable JDK internals.
- For Android, specifying `sourceCompatibility` and `jvmTarget` is sufficient; `targetCompatibility` is not needed.