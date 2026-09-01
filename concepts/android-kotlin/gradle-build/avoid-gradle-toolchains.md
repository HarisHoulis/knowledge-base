---
domain: android-kotlin
subdomain: gradle-build
concept: avoid-gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

The article argues that Gradle toolchains, despite being recommended by Gradle and Android docs, are rarely a good idea for compilation. Toolchains force the use of old JDKs, which may be outdated, perform poorly in containerized environments, and have more compiler bugs. Newer JDKs can cross-compile to older targets via the `--release` flag (Java) or `-Xjdk-release` (Kotlin), making old JDKs unnecessary for compilation [source](https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Toolchains also consume significant disk space and do not control the JDK used to run the Gradle build itself. However, toolchains still have utility for running unit tests against older JVM versions or for JVM-based tools that depend on unstable internals. The recommendation is to use toolchains only for such cases, not for compilation [source](https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

- Prefer the `--release` (Java) or `-Xjdk-release` (Kotlin) flags over toolchains for cross-compilation.
- Old JDKs are often outdated, ignore container limits, and have more compiler bugs.
- Toolchains can still be used for JVM unit tests and incompatible tools like Error-Prone or Google Java Format.
- Toolchains do not control the JDK running the Gradle build itself and waste disk space.