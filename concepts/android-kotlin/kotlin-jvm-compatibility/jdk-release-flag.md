---
domain: android-kotlin
subdomain: kotlin-jvm-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
    date: "2024-03-15"
---

# Kotlin's JDK release compatibility flag

The Kotlin JVM compiler's `jvmTarget` only controls the bytecode version, not the set of JDK APIs you can reference. This means compiling with a newer JDK can accidentally resolve Kotlin extension functions to new member functions on JDK classes, causing `NoSuchMethodError` at runtime on older platforms. The article illustrates this with a crash caused by `List.removeFirst()` introduced in JDK 21, where the extension function lost to the member function.

- Setting `jvmTarget` (or Java compatibility) does not restrict JDK API usage; it only changes the emitted bytecode version.
- Kotlin extension functions are resolved statically, and a member function with the same signature always wins, so new JDK members can silently override extension behavior.
- The `-Xjdk-release` compiler flag (similar to `javac --release`) restricts the JDK API surface to the specified version, fixing such issues.
- Android users generally don't need this because `android.jar` already limits available `java.*` APIs, but JVM/multiplatform users should use it.