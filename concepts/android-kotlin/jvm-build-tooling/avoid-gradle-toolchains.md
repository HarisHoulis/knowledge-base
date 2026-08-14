---
domain: android-kotlin
subdomain: jvm-build-tooling
concept: avoid-gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that despite Gradle and Android documentation recommending Java toolchains, they are rarely a good idea for compilation. He cites Retrofit's toolchain use causing its Javadoc to be built with JDK 8, losing searchable Javadoc features introduced in JEP 225 with JDK 9. Old JDKs also fail to properly honor container resource limits and have more compiler bugs, especially around features like lambdas introduced near their release.

Modern JDKs can cross-compile effectively using the `--release` flag for Java or `-Xjdk-release` for Kotlin, removing the need to compile with an older JDK. Newer compilers benefit from JVM improvements such as faster execution, better memory handling, and fewer bugs. Toolchains also waste disk space with multiple large JDK installs and do not control the JVM running the Gradle build itself.

Toolchains still have utility for running JVM unit tests across different Java versions, as Retrofit does, and for tools like Google Java Format or Error-Prone that depend on unstable JDK internals. For Android projects, specifying `sourceCompatibility` and `jvmTarget` is sufficient instead of using a toolchain.

- Toolchains are recommended by Gradle and Android docs but are rarely a good idea for compilation.
- Using an old JDK via toolchains can produce outdated artifacts (e.g., non-searchable Javadoc) and inherits old JVM bugs and poor container resource awareness.
- Modern JDKs can cross-compile to older targets with `--release` (Java) or `-Xjdk-release` (Kotlin), so old JDKs are unnecessary for compilation.
- Toolchains are still useful for running tests on multiple JVM versions and for isolating tools that require older JDKs.
- For Android, set `sourceCompatibility` and `jvmTarget` instead of relying on toolchains.