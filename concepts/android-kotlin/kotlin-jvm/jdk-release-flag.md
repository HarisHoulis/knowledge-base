---
domain: android-kotlin
subdomain: kotlin-jvm
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes a runtime crash (`NoSuchMethodError`) caused by a Kotlin extension function being shadowed by a new JDK member function. When the build JDK was bumped to 21, the `List` interface gained `removeFirst()` and `removeLast()` as member methods, which took precedence over Kotlin's `kotlin.collections.removeFirst()` extension function. This led to the JVM bytecode invoking the member function, causing a crash on older Android versions that lack this API.

- Setting `jvmTarget` only controls the bytecode version, not the set of available JDK APIs, so references to newer methods can still slip in.
- JDK 21 added `removeFirst()` and `removeLast()` to `List`, overriding Kotlin's extension functions and causing `NoSuchMethodError` at runtime on older platforms.
- Kotlin's `-Xjdk-release` flag (introduced in Kotlin 1.7) acts like `javac --release`, restricting the JDK API surface to a specific version.
- After enabling `-Xjdk-release`, the compiler resolves `removeFirst` to the Kotlin stdlib static helper, fixing the crash.
- Android projects don't need this because `android.jar` already limits `java.*` APIs, but plain Kotlin/JVM and multiplatform JVM targets benefit from it.