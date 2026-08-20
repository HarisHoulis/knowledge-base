---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

The article argues that Gradle Java toolchains are rarely a good idea for compilation, despite recommendations from Gradle and Android docs. Using an old JDK via a toolchain to target older Java versions brings outdated JVMs that ignore container resource limits, have more compiler bugs (especially around lambdas), and lack performance improvements from modern JVMs. Since JDK 9, the `--release` flag lets the current JDK cross-compile to older Java versions while correctly limiting APIs, making old JDKs unnecessary for compilation. Kotlin should use `-Xjdk-release` instead. (Source: https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/)

- Toolchains for compilation are unnecessary because `--release` (Java) and `-Xjdk-release` (Kotlin) support cross-compilation with a modern JDK.
- Old JDKs used by toolchains may be outdated, ignore container resource limits, and contain more compiler bugs.
- Toolchains remain useful for running unit tests against older JVM versions and for JavaExec tasks that rely on unstable JDK internals.
- For Android, specify `sourceCompatibility` (Java) and `jvmTarget` (Kotlin) instead of using toolchains.