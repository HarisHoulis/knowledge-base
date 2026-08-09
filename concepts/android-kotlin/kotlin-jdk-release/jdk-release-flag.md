---
domain: android-kotlin
subdomain: kotlin-jdk-release
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes a crash in an Android app caused by a `NoSuchMethodError` when calling `removeFirst()` on a `List`. The root cause is that JDK 21 added `removeFirst()` as a member method to the `List` interface, and Kotlin's extension functions are resolved statically, meaning the member method always wins when applicable. This happened even though the project set `jvmTarget` to 1.8, because `jvmTarget` only controls the Java bytecode version, not the set of JDK APIs that can be referenced.

The article explains that `jvmTarget` behaves like `javac`'s `-target` flag, which does not restrict API usage. The proper fix is to use Kotlin's `-Xjdk-release` flag, which acts like `javac`'s `--release` by setting both the bytecode version and the available JDK APIs. After applying this flag, the bytecode correctly calls the static Kotlin standard library helper instead of the interface method.

The article provides a Gradle configuration snippet for adding `-Xjdk-release` to the Kotlin compiler arguments, and notes that Android plugin users do not need this because the `android.jar` bootclasspath already restricts available `java.*` APIs. It also mentions that Gradle toolchains avoid the issue but have disadvantages, and that a dedicated Gradle DSL is not yet available.

- `jvmTarget` only sets the bytecode version; it does not restrict the JDK APIs you can reference.
- JDK 21 added `removeFirst()` and `removeLast()` to the `List` interface, causing Kotlin extension functions with the same name to be shadowed.
- `-Xjdk-release` is the Kotlin equivalent of `javac`'s `--release`, restricting the JDK API to the specified version.
- After using `-Xjdk-release`, the bytecode correctly invokes `kotlin.collections.CollectionsKt.removeFirst` instead of `java.util.List.removeFirst`.
- The Android plugin does not require this flag because `android.jar` already limits the `java.*` APIs to those of `compileSdk`.