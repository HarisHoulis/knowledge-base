---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-toolchains-avoidance
title: Gradle Toolchains Are Rarely a Good Idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle Toolchains Are Rarely a Good Idea

Despite official recommendations from Gradle and Android docs, Java toolchains are often a poor choice for compilation. Jake Wharton argues that using an older JDK to target an older Java version introduces more problems than it solves. Older JDKs are more likely to have compiler bugs, especially around features introduced near their release, and they lack modern JVM optimizations like better garbage collectors and memory-efficient string representations. Additionally, older JVMs may not properly respect container resource limits unless kept up-to-date, which many developers fail to do.

The key issue is that toolchains are unnecessary for cross-compilation since JDK 9 introduced the `--release` flag, which simultaneously sets the source language version, target bytecode version, and available runtime APIs. Kotlin similarly offers `-Xjdk-release`. This makes it possible to compile for old Java versions using a modern JDK, which is faster, safer, and more container-aware. Toolchains also clutter the disk, often consuming multiple hundreds of MiB per JDK, and can require multiple vendors' JDKs for different projects.

However, toolchains are still useful in specific scenarios: running unit tests on older JVM versions to verify runtime behavior, and executing tools like Google Java Format or Error-Prone that depend on unstable JDK internals. For compilation, the article strongly recommends avoiding toolchains and using the language-specific release flags instead.

- Gradle toolchains for compilation are rarely a good idea; use modern JDKs with `--release` (Java) or `-Xjdk-release` (Kotlin).
- Old JDKs have more compiler bugs, ignore container resource limits, and take up significant disk space.
- Toolchains remain useful for testing on older JVM versions and for running tools that rely on unstable JDK internals.