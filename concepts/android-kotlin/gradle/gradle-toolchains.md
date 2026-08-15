---
domain: android-kotlin
subdomain: gradle
concept: gradle-toolchains
title: Gradle Toolchains Are Rarely a Good Idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle Toolchains Are Rarely a Good Idea

Jake Wharton argues that despite Gradle and Android documentation recommending Java toolchains, they are rarely a good idea for compilation. He cites a Retrofit release where toolchains caused Javadoc to be built with JDK 8, resulting in non-searchable docs, and notes that modern JDKs can cross-compile to older targets without needing an old JDK installed.

The main problems with using old JDKs via toolchains are that old JVM versions often lack container-aware resource handling, contain compiler bugs (especially around older features like lambdas), and miss performance improvements. Additionally, keeping multiple old JDKs installed consumes significant disk space. Toolchains also only apply to tasks that spawn a new JVM—not the Gradle build or plugins—so they do not enforce a true minimum JDK for the build environment.

Toolchains still have valid use cases, such as running unit tests on the lowest supported Java version (e.g., Retrofit) or isolating incompatible tools like Google Java Format and Error-Prone. For compilation, Wharton recommends using the `--release` flag for Java and `-Xjdk-release` for Kotlin, or just `sourceCompatibility`/`jvmTarget` for Android targets.

- Use `--release` for Java and `-Xjdk-release` for Kotlin instead of toolchains for cross-compilation.
- Old JDKs are slower, buggier, and less container-aware than modern ones, even when targeting older bytecode.
- Gradle toolchains only affect tasks that spawn a new JVM, not the build or its plugins.
- Toolchains remain useful for running tests on older JVMs and for isolating incompatible tools.