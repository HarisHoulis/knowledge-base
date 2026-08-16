---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that, despite Gradle and Android documentation recommending Java toolchains, they are rarely a good idea for compilation. He cites a recent Retrofit release where using a JDK 8 toolchain caused non-searchable Javadoc, missing out on JEP 225 improvements available since JDK 9 (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/). 

Toolchains force the use of old JDKs, which lack recent container resource-limit support, contain unfixed compiler bugs, and are slower than modern JDKs. Modern JDKs can cross-compile effectively using the `--release` flag for Java or `-Xjdk-release` for Kotlin, making old toolchains unnecessary for compilation. 

Wharton still finds toolchains useful for running unit tests against old JVMs to verify runtime behavior, and for isolating tools like Google Java Format or Error-Prone that depend on unstable JDK internals. But for compilation, he recommends avoiding toolchains entirely and using the appropriate compatibility flags.

- Avoid Gradle toolchains for compilation; use the `--release` flag (Java) or `-Xjdk-release` (Kotlin) instead.
- Old JDKs lack container resource-limit support, have more compiler bugs, and miss modern Javadoc improvements.
- Toolchains remain useful for running tests on old JVMs and for isolating incompatible tools.
- For Android, set `sourceCompatibility` and `jvmTarget` rather than using toolchains.