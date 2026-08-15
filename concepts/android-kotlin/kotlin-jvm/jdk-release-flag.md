---
domain: android-kotlin
subdomain: kotlin-jvm
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

The article describes a runtime crash (`NoSuchMethodError`) caused by Kotlin's extension function `removeFirst()` being shadowed by a new member function on `List` added in JDK 21. The author explains that setting Kotlin's `jvmTarget` to 1.8 only changes the emitted bytecode version (major version 52) and does not constrain the Java API that can be referenced. This mirrors `javac`'s `-target` flag, which requires `--release` or `-bootclasspath` to also limit API access. Kotlin 1.7 introduced the `-Xjdk-release` flag to act like `javac`'s `--release`, restricting compilation to a specific JDK API. With `-Xjdk-release=1.8`, the compiler correctly resolves `removeFirst()` to the static Kotlin stdlib extension instead of the JDK interface method. For Android, this is unnecessary because `android.jar` already limits the available APIs, but for Kotlin/JVM targets it is essential. There is no Gradle DSL for this yet, but it is tracked in [KT-49746](https://youtrack.jetbrains.com/issue/KT-49746/Support-Xjdk-release-in-gradle-toolchain). [source](https://jakewharton.com/kotlins-jdk-release-compatibility-flag/)

- `jvmTarget` only controls bytecode version, not the Java API surface you can reference, so newer JDK methods can leak in.
- Kotlin member functions always win over extension functions, so new JDK 21 `List.removeFirst()` overrode the stdlib extension.
- Use `-Xjdk-release=<version>` (similar to `javac --release`) to constrain both bytecode and API references for Kotlin/JVM targets.
- Android targets don't need this because `android.jar` already restricts the API to the `compileSdk` level.