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

Jake Wharton argues that Gradle toolchains are rarely a good idea for compilation, despite recommendations from Gradle and Android docs. He explains that using an older JDK to target an older JVM is unnecessary since JDK 9 introduced the `--release` flag, which sets source version, target bytecode, and runtime API in one go. Compiling with the latest JDK using `--release` (Java) or `-Xjdk-release` (Kotlin) avoids the need for multiple old JDK installations and yields better performance, fewer compiler bugs, and proper container resource awareness. He also notes that toolchains do not control the JVM running the build itself, so they don't solve any JVM-level constraints for plugins.

- Prefer `--release` for Java and `-Xjdk-release` for Kotlin instead of toolchains to cross-compile to older JVM versions.
- Modern JDKs are faster, have fewer compiler bugs, and respect container resource limits better than outdated JDKs.
- Toolchains are still useful for running JVM unit tests against older JVM versions or for incompatible tools via `JavaExec`.
- Avoid forcing installation of multiple old JDKs; they waste disk space and complicate the build environment.