---
domain: android-kotlin
subdomain: kotlin-jvm-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

The article describes a crash caused by `NoSuchMethodError` when calling `removeFirst()` on a `List`. The code was written in Kotlin and appeared to use the Kotlin extension function `removeFirst`, but after upgrading the build JDK to 21, the `List` interface gained a new member method `removeFirst()` as part of sequenced collections. Because member functions always win over extension functions, the Kotlin extension was shadowed, and the compiled code attempted to invoke the JDK 21 interface method at runtime, which does not exist on older Android or JVM versions.

- Kotlin's `jvmTarget` only controls the bytecode version, not the set of JDK APIs the compiled code can reference, so it does not prevent accidental usage of newer JDK methods.
- The `-Xjdk-release` flag for `kotlinc` behaves like `javac`'s `--release`, restricting the JDK API surface to the specified version and preventing such compatibility issues.
- Using `-Xjdk-release` makes Kotlin resolve `removeFirst` to the stdlib extension function instead of the JDK 21 member method.
- Android Kotlin users generally do not need this flag because `android.jar` already limits the available `java.*` APIs to the `compileSdk` and Android Lint enforces minSdk compatibility.
- There is no Gradle DSL for `-Xjdk-release` yet; it is tracked in issue KT-49746.