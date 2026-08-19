---
domain: android-kotlin
subdomain: gradle-build
concept: avoid-gradle-toolchains
title: Gradle Toolchains Are Rarely a Good Idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle Toolchains Are Rarely a Good Idea

Jake Wharton argues that Gradle toolchains are rarely a good idea, despite being recommended by Gradle and Android documentation. He explains that toolchains force the use of old JDKs, which lack important features like searchable Javadoc (JEP 225), have poorer container resource awareness, contain more compiler bugs, and are slower. Modern JDKs can cross-compile to older Java versions using the `--release` flag (for Java) or `-Xjdk-release` flag (for Kotlin), making toolchains unnecessary for compilation. (Source: Jake Wharton, jakewharton.com)

- Use `--release` for Java and `-Xjdk-release` for Kotlin instead of toolchains for compilation.
- Old JDKs used by toolchains miss modern Javadoc features, container resource limits, and bug fixes.
- Toolchains are still useful for running unit tests on older JVMs or isolating incompatible tools via JavaExec.
- For Android, just set sourceCompatibility and jvmTarget; you don't need a toolchain.