---
domain: android-kotlin
subdomain: gradle-build-tooling
concept: avoid-gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Gradle and Android documentation recommend Java toolchains for cross-compilation, but Jake Wharton argues they are rarely a good idea. Toolchains force the use of old JDKs that lack container resource-limit support, compiler bug fixes, and JVM performance improvements. Modern JDKs can cross-compile to older releases using the `--release` flag for Java or `-Xjdk-release` for Kotlin, making old JDKs unnecessary for compilation (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Old JVMs are less aware of container resource limits, and even backported fixes require keeping JDK 8/11 up to date, which is often neglected. Compiling with an old JDK also risks hitting compiler bugs around older features, such as lambdas in Java 8. As an example, Retrofit's Javadoc was built with JDK 8 via a toolchain, making it non-searchable; switching to a modern JDK would give all Javadoc advancements from the last 10 years (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Toolchains still have utility for non-compilation tasks: running unit tests on older JVM versions to verify runtime behavior, and isolating tools that rely on unstable JDK internals, like Google Java Format or Error-Prone, via `JavaExec`. But for compilation, use `--release` or `-Xjdk-release` instead, and reserve toolchains for tests or incompatible tools (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

- Toolchains are recommended by Gradle/Android docs but are rarely a good idea for compilation.
- Use `--release` for Java and `-Xjdk-release` for Kotlin to target older JDKs with a modern JDK.
- Old JDKs miss container-aware resource limits, compiler bug fixes, and JVM performance improvements.
- Toolchains are still useful for running tests on older JVM versions or isolating incompatible tools.
- Toolchains do not control the Gradle build JVM and consume significant disk space.