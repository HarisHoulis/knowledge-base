---
domain: android-kotlin
subdomain: kotlin-jvm-compiler
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes a NoSuchMethodError crash caused by Kotlin's extension function resolution when compiling against a newer JDK. In JDK 21, the List interface added removeFirst() and removeLast() as member methods, which take precedence over Kotlin's extension functions of the same name. Even with Kotlin's jvmTarget set to Java 8, the bytecode version was correct, but the compiler still referenced the JDK 21 method directly, leading to the runtime failure on older Android versions.

The root cause is that jvmTarget only controls the emitted bytecode version, not the set of JDK APIs that can be referenced. The article shows how javac has a similar behavior with the -target flag, and the proper fix is to use --release or -bootclasspath. Kotlin 1.7 introduced the equivalent flag -Xjdk-release, which restricts the JDK API surface to the specified version. Using this flag changed the bytecode to call the Kotlin standard library extension function instead of the JDK member method, resolving the crash.

The article notes that Android projects using the Android plugin or Kotlin Multiplatform Android targets do not need this flag because android.jar already limits java.* APIs. Gradle toolchains also avoid the issue by compiling with an older JDK, but the article argues that toolchains are rarely a good idea because they miss out on compiler improvements.

- jvmTarget controls bytecode version, not the JDK API surface that can be referenced.
- JDK 21 added removeFirst() to List, causing Kotlin extension functions to be shadowed by member functions when compiling against JDK 21.
- Kotlin's -Xjdk-release flag restricts the JDK API to a specified version, similar to javac's --release.
- Using -Xjdk-release changed the compilation to call kotlin.collections.CollectionsKt.removeFirst, fixing the NoSuchMethodError.
- Android users don't need this flag because android.jar already limits available java.* APIs.