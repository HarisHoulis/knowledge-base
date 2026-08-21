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

The article describes a production crash caused by a `NoSuchMethodError` when calling `removeFirst()` on a `List`. The issue arose after upgrading the build JDK to 21, which added `removeFirst()` as a member function to the `List` interface. In Kotlin, member functions take precedence over extension functions, so the previously resolved Kotlin extension function `kotlin.collections.removeFirst` was silently replaced by the JDK 21 member method, breaking compatibility with older Android versions ([source](https://jakewharton.com/kotlins-jdk-release-compatibility-flag/)).

Setting `jvmTarget` to 1.8 only controls the bytecode version, not the JDK API surface used during compilation. The article demonstrates with `javap` that the classfile version was 52 (Java 8) but the bytecode still referenced `java/util/List.removeFirst()`. This mirrors `javac`'s behavior, where `-target` alone does not restrict API usage; `javac` uses `--release` to properly bind against the older JDK APIs. Kotlin's equivalent is `-Xjdk-release`, introduced in Kotlin 1.7, which should be set to the minimum supported Java version ([source](https://jakewharton.com/kotlins-jdk-release-compatibility-flag/)).

The article shows how adding `-Xjdk-release=1.8` to Kotlin compiler arguments changes the bytecode to call the static extension helper `CollectionsKt.removeFirst` instead of the interface method. Users of the Kotlin Android plugin or Android multiplatform targets do not need this flag because `android.jar` already restricts `java.*` APIs to the `compileSdk` level. The flag has no official Gradle DSL yet, but progress is tracked in [KT-49746](https://youtrack.jetbrains.com/issue/KT-49746/Support-Xjdk-release-in-gradle-toolchain).

- Kotlin extension functions are overridden by same-signature member functions added in newer JDKs, causing binary incompatibility.
- `jvmTarget` only sets bytecode version, not the JDK API level; `-Xjdk-release` is needed for proper cross-compilation.
- `-Xjdk-release` behaves like `javac`'s `--release`, combining source/target compatibility with a restricted bootclasspath.
- Android developers using `android.jar` already have API restriction, so they don't need this flag.
- No Gradle DSL yet; use `kotlinOptions.freeCompilerArgs` to add `-Xjdk-release`.