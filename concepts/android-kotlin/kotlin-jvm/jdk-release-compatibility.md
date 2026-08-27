---
domain: android-kotlin
subdomain: kotlin-jvm
concept: jdk-release-compatibility
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

Kotlin's `jvmTarget` setting controls the emitted Java bytecode version, but it does not restrict which JDK APIs the compiler can reference. The article demonstrates this with a `NoSuchMethodError` caused by JDK 21 adding `removeFirst()` to the `List` interface. Because Kotlin's extension function resolution gives priority to member functions, the new JDK method silently shadowed the standard library's `removeFirst()` extension, producing bytecode that calls the interface method directly. This fails on older Android runtimes where that method does not exist.

The author explains that Kotlin's `-Xjdk-release` flag (analogous to `javac --release`) restricts the JDK API surface to a specific version during compilation. Adding this flag changes the compiled bytecode from an `invokeinterface` call to `List.removeFirst()` to an `invokestatic` call to `CollectionsKt.removeFirst()`, resolving the issue. The article notes that Android projects are already protected by using `android.jar` as the bootclasspath, but JVM and multiplatform JVM targets should use `-Xjdk-release`. There is no Gradle DSL yet, though a YouTrack issue tracks this feature.

- `jvmTarget` only sets bytecode version, not the JDK API level, so code can silently reference newer JDK methods.
- JDK 21 added member `removeFirst()`/`removeLast()` to `List`, causing Kotlin extensions to be shadowed and resulting in `NoSuchMethodError` on older runtimes.
- Kotlin's `-Xjdk-release` flag restricts the JDK API to a specified version, similar to `javac --release`.
- Android projects using `android.jar` already have API restrictions; JVM and multiplatform JVM targets need `-Xjdk-release` manually.
- There is no Gradle DSL for this flag yet, tracked in KT-49746.