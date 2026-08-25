---
domain: android-kotlin
subdomain: gradle
concept: gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Java/Gradle toolchains are rarely a good idea for compilation, despite recommendations from Gradle and Android docs. Toolchains force the use of old JDKs, which lack modern performance improvements, container resource awareness (cgroups support), and often have compiler bugs fixed only in newer versions. For example, Retrofit's Javadoc was built with JDK 8 and thus missed Javadoc search (JEP 225) and modern HTML/CSS.

Modern JDKs provide the `--release` flag for Java and `-Xjdk-release` for Kotlin, enabling cross-compilation to older targets without needing old JDKs. This approach is safer, faster, and more resource-efficient. Toolchains still have utility for running unit tests on specific JVM versions (e.g., testing lowest supported Java) and for isolating tools that rely on unstable JDK internals, but they should not be the default for compilation.

- Toolchains require old JDKs that perform worse, don't respect container limits, and have more compiler bugs.
- Use `--release` (Java) or `-Xjdk-release` (Kotlin) to target older JVMs while compiling with the latest JDK.
- Toolchains remain useful for testing on specific JVM versions and running incompatible tools via JavaExec.
- Gradle and Android docs' recommendation to always use toolchains is misleading for compilation.