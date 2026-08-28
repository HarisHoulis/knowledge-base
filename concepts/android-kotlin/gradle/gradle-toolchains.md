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

Jake Wharton argues that Gradle toolchains are usually the wrong choice for compilation, despite recommendations from Gradle and Android docs. Toolchains force the build to use old JDKs, which may not respect container resource limits, contain unfixed compiler bugs, and waste disk space with multiple large JDK installations. Modern JDKs are faster and include backported fixes, so compiling with an old JDK to target an older Java version is unnecessary.

- Use the --release flag (Java) or -Xjdk-release (Kotlin) instead of toolchains for cross-compilation to older Java versions.
- Old JDKs ignore container resource limits and contain compiler bugs that are not backported.
- Toolchains remain useful for running unit tests on old JVM versions and for isolating tools like google-java-format or Error-Prone.
- For Android, specify sourceCompatibility and jvmTarget rather than using a toolchain.