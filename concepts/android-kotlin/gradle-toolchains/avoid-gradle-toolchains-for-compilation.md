---
domain: android-kotlin
subdomain: gradle-toolchains
concept: avoid-gradle-toolchains-for-compilation
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

The article argues that Gradle Java toolchains, despite being recommended by Gradle and Android docs, are rarely a good idea for compilation. Using an older JDK to target an older JVM brings disadvantages: old JVMs are less likely to honor container resource limits, have more compiler bugs (especially around features like lambdas), and perform worse. Modern JDKs can cross-compile perfectly using the `--release` flag (Java) or `-Xjdk-release` (Kotlin), so there is no value in compiling with an older JDK. The author also notes toolchains force installation of multiple old JDKs, wasting disk space, and that toolchains do not control the JVM running the build or plugins.

- Use `--release` for Java and `-Xjdk-release` for Kotlin to target older APIs without needing old JDKs.
- Toolchains are still useful for running JVM unit tests on older JDKs or for tools that rely on unstable JDK internals.
- Old JVMs have more compiler bugs, worse container resource handling, and lower performance; modern JDKs are safer and faster.
- Toolchains add dependency on outdated JDKs and do not affect the Gradle daemon or plugin JVM, so they offer limited benefit.