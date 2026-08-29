---
domain: engineering-culture
subdomain: gradle-build-tooling
concept: avoid-gradle-toolchains-for-compilation
title: Gradle toolchains are rarely a good idea
sources:
  - title: "Gradle toolchains are rarely a good idea"
    url: "https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/"
---

# Gradle toolchains are rarely a good idea

Despite recommendations from the Gradle and Android documentation, Java toolchains are rarely a good idea for compilation. Using an old JDK to target older Java versions forces reliance on outdated JVMs that may ignore container resource limits, contain unpatched compiler bugs, and provide no real cross-compilation benefit because modern JDKs support the --release flag (or -Xjdk-release for Kotlin) to set the source, target, and API surface simultaneously (Jake Wharton, "Gradle toolchains are rarely a good idea", https://jakewharton.com/gradle-toolchains-are-rarely-a-good-idea/).

Toolchains also clutter development environments with multiple old JDK installations, each taking hundreds of MiB, and do not control the JVM running the build itself or its plugins. They are only useful when a separate JVM is genuinely required, such as running unit tests against the lowest supported Java version or isolating tools like Google Java Format and Error-Prone that depend on unstable JDK internals. For normal Java and Kotlin compilation, prefer the modern JDK's built-in release flags.

- Old JDKs via toolchains can ignore container resource limits and have unpatched compiler bugs.
- Modern JDKs can cross-compile to older Java versions safely using --release (Java) or -Xjdk-release (Kotlin).
- Toolchains add needless disk usage and can force multiple old JDK installations.
- Toolchains remain useful for tasks that need a different JVM, like unit tests on older Java versions or JDK-internal tools.