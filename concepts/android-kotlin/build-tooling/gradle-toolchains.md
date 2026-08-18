---
domain: android-kotlin
subdomain: build-tooling
concept: gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle toolchains are rarely a good idea for compilation, despite being recommended by Gradle and Android docs. Using a Java 8 toolchain for Retrofit produced non-searchable Javadoc, illustrating how old JDKs stagnate and miss modern improvements (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/). Old JVMs can also ignore container resource limits, have more compiler bugs, and are slower than modern JDKs.

Modern JDKs support the --release flag for Java and -Xjdk-release for Kotlin, making it possible to cross-compile to older Java versions without needing an old JDK. Toolchains still have value for running unit tests across JVM versions and for isolating tools that rely on unstable JDK internals, but for compilation they are unnecessary. For Android builds, only sourceCompatibility/jvmTarget are needed.

- Don't use Gradle toolchains for compilation; use --release for Java and -Xjdk-release for Kotlin.
- Old JDKs have more compiler bugs, lack container resource awareness, and generate slower builds.
- Toolchains remain useful for unit tests that must run on multiple JVM versions.
- For Android, set sourceCompatibility and jvmTarget instead of toolchains.