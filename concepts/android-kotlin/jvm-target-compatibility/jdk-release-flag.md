---
domain: android-kotlin
subdomain: jvm-target-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

A production Android app crashed with `NoSuchMethodError` because Kotlin's `removeFirst()` extension function was shadowed by a new member method added to `java.util.List` in JDK 21. The crash occurred after bumping the build JDK to 21, even though the Kotlin `jvmTarget` was set to 1.8. The article explains that `jvmTarget` only controls the emitted Java bytecode version, not the set of JDK APIs that can be referenced (Jake Wharton, https://jakewharton.com/kotlins-jdk-release-compatibility-flag/).

Kotlin's `-Xjdk-release` flag, introduced in Kotlin 1.7, prevents accidental use of newer JDK APIs by restricting the available `java.*` APIs to the specified release, much like `javac`'s `--release` flag. Adding `-Xjdk-release=1.8` to the compiler arguments changes the bytecode from invoking `List.removeFirst()` as an interface method to invoking the static helper `kotlin.collections.CollectionsKt.removeFirst()`, fixing the crash (Jake Wharton, https://jakewharton.com/kotlins-jdk-release-compatibility-flag/).

The article notes that Android plugin users do not need this flag because `android.jar` already limits the available Java APIs to those of the `compileSdk`, and Android Lint enforces `minSdk` compatibility. There is currently no Gradle DSL for `-Xjdk-release`, but it is tracked in JetBrains issue KT-49746 (Jake Wharton, https://jakewharton.com/kotlins-jdk-release-compatibility-flag/).

- JDK 21's new `List.removeFirst()` member method silently overrode Kotlin's extension function, causing a runtime `NoSuchMethodError` on Android.
- `jvmTarget` controls bytecode version, but does not restrict the JDK APIs against which the code is compiled.
- Kotlin's `-Xjdk-release` flag enforces API compatibility with a specific JDK version, analogous to `javac --release`.
- Android projects using `android.jar` as bootclasspath already receive this protection and don't need the flag.