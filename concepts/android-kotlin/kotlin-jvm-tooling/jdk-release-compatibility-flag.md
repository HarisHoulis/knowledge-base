---
domain: android-kotlin
subdomain: kotlin-jvm-tooling
concept: jdk-release-compatibility-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

A Kotlin/Android project crashed with `NoSuchMethodError` because `List.removeFirst()` was called directly on the `java.util.List` interface. This happened after the build JDK was upgraded to 21, where `List` gained a member `removeFirst()`. The Kotlin code originally used the Kotlin extension function `kotlin.collections.removeFirst()`, but member functions always win over extensions, so the new JDK member took precedence (Jake Wharton, "Kotlin's JDK release compatibility flag").

The project had configured Kotlin's `jvmTarget` and Java compatibility to 1.8, but this only controls the emitted bytecode version, not the set of JDK APIs that can be referenced. Java's `javac -target` has the same limitation, and `javac --release` was introduced to also lock the boot classpath. Kotlin 1.7 added the analogous `-Xjdk-release` flag, which sets the JDK API surface alongside the bytecode target (Jake Wharton, "Kotlin's JDK release compatibility flag").

Adding `-Xjdk-release=1.8` to Kotlin compiler arguments changed the bytecode from `invokeinterface java/util/List.removeFirst` to `invokestatic kotlin/collections/CollectionsKt.removeFirst`, correctly resolving to the extension function. This flag is needed for Kotlin JVM and multiplatform JVM targets; Kotlin Android plugin users do not need it because `android.jar` already constrains `java.*` APIs to the `compileSdk`. There is no dedicated Gradle DSL yet, and the article notes that Gradle toolchains avoid the issue only by using an ancient JDK, which has downsides (Jake Wharton, "Kotlin's JDK release compatibility flag").

- Raising the build JDK can introduce new member functions that shadow Kotlin extensions, causing runtime errors like `NoSuchMethodError`.
- `jvmTarget` only controls bytecode version, not the JDK API surface; use Kotlin's `-Xjdk-release` to align the API with the target bytecode.
- `-Xjdk-release` is the Kotlin equivalent of `javac --release` and fixes references to JDK APIs that are newer than the target.
- Kotlin Android projects are already protected by `android.jar`, but JVM and multiplatform targets should explicitly use `-Xjdk-release`.