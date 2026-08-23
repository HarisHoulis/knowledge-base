---
domain: android-kotlin
subdomain: gradle-toolchains
concept: gradle-toolchains-rarely-good
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle toolchains, while recommended by Gradle and Android docs, are rarely a good idea for compilation. Using an old JDK to target an older JVM brings compiler bugs, container resource limitations, and slower builds. Modern JDKs can cross-compile effectively with the `--release` flag for Java or `-Xjdk-release` for Kotlin, avoiding the need for outdated JDKs. Toolchains still have utility for running unit tests on multiple JVM versions or isolated tools that rely on unstable JDK internals.

- Avoid using Gradle toolchains for compilation; use `--release` (Java) or `-Xjdk-release` (Kotlin) with a modern JDK instead.
- Old JDKs have more compiler bugs, ignore container resource limits, and lack performance improvements.
- Toolchains can be useful for testing on lowest-supported JVM versions via `Test` tasks or for running tools like Google Java Format on an older JDK.
- Retrofit's Javadoc was built with JDK 8 via a toolchain, missing searchable Javadoc features from JDK 9+.