---
domain: android-kotlin
subdomain: gradle-build
concept: avoid-gradle-toolchains-for-compilation
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle Java toolchains are rarely a good idea, despite official Gradle and Android docs recommending them. Toolchains for compilation force the use of old JDKs, which are often outdated and lack modern container resource-limit support (cgroups). Old compilers also carry bugs, such as lambda-related issues in JDK 8, that are not fixed in backports; modern JDKs compile older targets safely via the --release flag for Java and -Xjdk-release for Kotlin. Additionally, toolchains consume significant disk space and do not control the JVM running the build itself, so they offer limited cross-compilation benefit. Wharton still recommends toolchains for running JVM unit tests on supported Java versions or isolating tools that rely on internal JDK APIs, but says compilation should use the latest JDK with version flags.

- Toolchains for compilation force outdated JDKs, leading to bugs and missing resource-limit awareness.
- Java's --release and Kotlin's -Xjdk-release make cross-compiling to older bytecode easy with a modern JDK.
- Toolchains don't control the build JVM, waste disk, and are unnecessary for simple source/target compatibility.
- Use toolchains only where a specific JVM is required at runtime, e.g., testing lowest-supported Java or running JDK-internal tools.