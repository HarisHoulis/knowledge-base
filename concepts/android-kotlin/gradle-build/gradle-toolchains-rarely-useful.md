---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-toolchains-rarely-useful
title: Gradle Toolchains Are Rarely a Good Idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle Toolchains Are Rarely a Good Idea

Java toolchains are often recommended by Gradle and Android documentation, but Jake Wharton argues they are rarely a good idea for compilation. Using a toolchain forces your build to run on an old JDK, which may not respect container resource limits, miss backported fixes, and have more compiler bugs—especially around older features like lambdas. Modern JDKs are faster, safer, and better suited for containerized CI environments (Jake Wharton, "Gradle Toolchains Are Rarely a Good Idea", https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Since JDK 9, the Java compiler supports the --release flag, which simultaneously sets source version, target bytecode version, and available runtime APIs. This makes cross-compiling to older Java versions from a modern JDK trivial, eliminating the need for old JDKs. Similarly, Kotlin provides the -Xjdk-release flag, and Android projects only need sourceCompatibility and jvmTarget. Toolchains remain useful for running JVM unit tests across multiple supported JVM versions, or for isolated tools that rely on JDK internals, but not for compilation itself.

- Java toolchains are recommended by docs but force old JDKs that are slower, less container-aware, and more bug-prone.
- Modern JDKs can cross-compile to old Java targets using --release (Java) or -Xjdk-release (Kotlin).
- Toolchains still have utility for running tests on old JVMs or isolating incompatible tools.
- For Android, specify sourceCompatibility and jvmTarget instead of using toolchains for compilation.