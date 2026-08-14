---
domain: android-kotlin
subdomain: kotlin-jvm-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes a production crash caused by `NoSuchMethodError` when calling `removeFirst()` on a `List`. The code was written in Kotlin using an extension function, but after upgrading the build JDK to 21, the new `List.removeFirst()` member method shadowed the extension because member functions always win. The `jvmTarget` set to 1.8 was insufficient—it only controls bytecode version, not available JDK APIs. 

Kotlin 1.7 introduced `-Xjdk-release`, which acts like `javac`'s `--release` flag, restricting the API surface to a specific JDK version. By adding `-Xjdk-release=1.8` to the compiler arguments, the extension function resolves to the Kotlin standard library static method instead of the JDK member, fixing the crash. The article notes that Android targets don't need this because `android.jar` already constrains the `java.*` APIs, and that Gradle toolchains avoid the issue but have other drawbacks.

- -Xjdk-release prevents accidental use of newer JDK APIs when targeting older bytecode.
- jvmTarget only sets bytecode version; it does not limit the JDK API surface.
- The flag is needed for Kotlin JVM and multiplatform JVM targets, but not Android targets.
- Gradle toolchains sidestep the issue but sacrifice modern compiler improvements.