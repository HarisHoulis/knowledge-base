---
domain: android-kotlin
subdomain: jvm-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

The article describes an Android crash caused by a `NoSuchMethodError` when calling `List.removeFirst()`. The code used Kotlin's extension function `removeFirst()`, but after upgrading the build JDK to 21, the JDK's new member method `removeFirst()` on `List` took precedence over the extension, as per Kotlin's rule that member functions always win over extensions. This happened despite setting `jvmTarget` to 1.8, because `jvmTarget` only controls the emitted bytecode version and does not restrict the set of JDK APIs available during compilation.

The author explains that `javac` has a similar limitation with `-target`, historically solved with `-bootclasspath` and later with the `--release` flag. Kotlin 1.7 introduced an equivalent flag, `-Xjdk-release`, which restricts the JDK API surface to the specified version. Configuring this flag causes the Kotlin compiler to resolve `removeFirst()` to the static extension function in `kotlin.collections.CollectionsKt` instead of the JDK member method, producing compatible bytecode. The article notes that Android users are already protected by using `android.jar` as the bootclasspath, and that there is no Gradle DSL yet but it is tracked in KT-49746.

- `jvmTarget` only sets the bytecode version, not the JDK API level, so newer JDK members can shadow Kotlin extensions and cause `NoSuchMethodError`.
- Kotlin's `-Xjdk-release` flag behaves like `javac --release`, restricting the available JDK APIs to the target version.
- Using `-Xjdk-release` ensures extension functions are resolved to the Kotlin standard library when a newer JDK adds colliding member methods.
- Android projects are less affected because `android.jar` limits accessible `java.*` APIs, but Kotlin JVM and multiplatform JVM targets should adopt this flag.
- There is no Gradle DSL for `-Xjdk-release` yet; it is tracked in JetBrains issue KT-49746.