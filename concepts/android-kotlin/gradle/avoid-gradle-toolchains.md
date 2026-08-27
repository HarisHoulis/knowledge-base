---
domain: android-kotlin
subdomain: gradle
concept: avoid-gradle-toolchains
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
    author: "Jake Wharton"
---

# Gradle toolchains are rarely a good idea

Jake Wharton argues that Gradle toolchains are rarely a good idea despite the Gradle and Android docs recommending them. He highlights that toolchains force the build to use old JDKs, which leads to outdated Javadoc, JVMs that don't honor container resource limits, and a higher risk of compiler bugs. For example, Retrofit's Javadoc built with JDK 8 is not searchable because that feature arrived in JDK 9 via JEP 225 (Jake Wharton, https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

- Toolchains for compilation force outdated JDKs, causing missing Javadoc search features, container resource issues, and compiler bugs.
- Modern JDKs can cross-compile to older Java versions using --release (Java) or -Xjdk-release (Kotlin), making old JDKs unnecessary for compilation.
- Toolchains remain useful for running tests on older JVMs and for tools that rely on unstable JDK internals.
- Avoid toolchains for compilation; use sourceCompatibility/jvmTarget when targeting Android.