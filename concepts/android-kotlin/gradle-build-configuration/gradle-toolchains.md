---
domain: android-kotlin
subdomain: gradle-build-configuration
concept: gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle toolchains, despite being recommended by Gradle and Android docs, are rarely a good idea for compilation. Building with old JDKs to target older Java versions is unnecessary because modern JDKs can cross-compile using the `--release` flag (Java) or `-Xjdk-release` (Kotlin), while providing better performance, container resource awareness, and fewer compiler bugs (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Using an old JDK for compilation also forces developers to install and maintain outdated JDKs, which consume significant disk space and may not respect system resource limits. Old compiler versions have known bugs, especially around features like lambdas, and lack the performance improvements of newer JVMs. The toolchain mechanism itself does not control the JVM running the build or plugins, so it does not address minimum requirement issues (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

However, toolchains still have legitimate use cases: running unit tests on the lowest supported JVM and isolating tools that rely on unstable JDK internals, such as Google Java Format or Error-Prone. The article recommends using `--release` for Java, `-Xjdk-release` for Kotlin, and `sourceCompatibility`/`jvmTarget` for Android, while reserving toolchains for these non-compilation scenarios (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

- Modern JDKs can target older Java versions via `--release` or `-Xjdk-release`, so old JDKs are not needed for cross-compilation.
- Old JDKs are slower, have more compiler bugs, and ignore container resource limits, making them inferior for compilation.
- Toolchains still make sense for running JVM unit tests on older Java versions and for tools that depend on internal JDK APIs.
- Despite official recommendations, toolchains are not the default choice for Java/Kotlin compilation.