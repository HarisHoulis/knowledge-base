---
domain: android-kotlin
subdomain: jdk-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

The article describes a production crash caused by JDK 21's new member function `List.removeFirst()`, which silently shadowed the Kotlin extension function of the same name. The app was built with JDK 21 but targeted Java 8 bytecode (`jvmTarget` = 1.8), leading to a `NoSuchMethodError` at runtime on older Android versions. The author clarifies that the `jvmTarget` setting only controls the emitted bytecode version, not the set of JDK APIs that can be referenced from the compiler's bootclasspath. This is analogous to `javac`'s `-target` flag, which similarly permits referencing newer APIs unless the bootclasspath is explicitly set.

The solution is Kotlin's `-Xjdk-release` flag, introduced in Kotlin 1.7, which acts like `javac`'s `--release` by automatically restricting the JDK API surface to the specified version. After enabling the flag, the bytecode invocation changes from a virtual interface call to a static call to the Kotlin standard library's `CollectionsKt.removeFirst`, restoring correct behavior. The article shows how to configure this flag in Gradle for Kotlin JVM and multiplatform targets, notes that Android projects using `android.jar` are already protected, and mentions that no Gradle DSL exists yet (KT-49746 tracks it). It also advises against Gradle toolchains as an alternative, since they force using an old JDK and miss compiler improvements.

- `jvmTarget` controls bytecode version but not API availability; newer JDK methods can still be referenced.
- JDK 21's `List.removeFirst()` member shadows Kotlin's extension function, causing a `NoSuchMethodError` on older runtimes.
- Use `-Xjdk-release` in `kotlinOptions.freeCompilerArgs` to enforce JDK API compatibility.
- Android builds are safe because `android.jar` limits available `java.*` APIs to `compileSdk`.
- Gradle toolchains are not recommended; they use an old JDK and forfeit compiler improvements.