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

Jake Wharton describes a production crash caused by `NoSuchMethodError: List.removeFirst()` on Android. The Kotlin code used `removeFirst()` as an extension function from `kotlin.collections`, but after upgrading the build JDK to 21, the new `removeFirst()` member method on `java.util.List` took precedence per Kotlin's extension resolution rules. Setting `jvmTarget` to 1.8 only controls the emitted bytecode version, not the JDK API surface, so the compiler still emitted a direct interface call to the JDK 21 method (Jake Wharton, https://jakewharton.com/kotlins-jdk-release-compatibility-flag/).

The fix is the Kotlin compiler flag `-Xjdk-release`, which behaves like `javac --release` by restricting the available JDK APIs to the specified version. With this flag, `removeFirst()` resolves to the static `CollectionsKt.removeFirst` helper instead of the missing interface method. The article notes that Android projects using the Android plugin are already protected because `android.jar` limits `java.*` APIs, but Kotlin JVM and multiplatform JVM target users should apply this flag manually. It also advises against Gradle toolchains as a workaround, since they force the use of an old JDK compiler and lose modern compiler improvements.

- `jvmTarget` only sets the bytecode version, not the JDK API surface; new JDK methods can still be referenced.
- Kotlin extension functions are shadowed by member functions with the same signature, which can break older runtimes.
- Use `-Xjdk-release=<version>` to restrict JDK APIs during Kotlin/JVM compilation.
- Android plugin users are safe because `android.jar` already limits the API surface.
- Gradle toolchains avoid the issue but at the cost of using outdated compiler versions.