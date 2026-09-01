---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-toolchains-rarely-a-good-idea
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that despite official recommendations from Gradle and Android documentation, Java toolchains are rarely a good idea. He illustrates with Retrofit: using a Java 8 toolchain to target Java 8 caused the published Javadoc to be built with JDK 8, which lacks the searchable Javadoc introduced in JEP 225 (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/). Old JDKs also don't respect container resource limits unless kept up-to-date with cgroup backports, and older compilers carry more bugs and performance penalties. Modern JDKs provide better memory use, faster compilation, and frequent bug fixes, making them safer even when targeting older Java versions.

- Toolchains force use of outdated JDKs, missing modern JVM performance, container-resource awareness, and compiler bug fixes.
- Since JDK 9, the `--release` flag enables cross-compilation without needing an old JDK; use `-Xjdk-release` for Kotlin.
- Toolchains still make sense for JVM unit tests that exercise runtime behavior on old versions and for tools that rely on unstable JDK internals.
- Android projects only need `sourceCompatibility` and `jvmTarget`; no toolchain is required for targeting older Java versions.