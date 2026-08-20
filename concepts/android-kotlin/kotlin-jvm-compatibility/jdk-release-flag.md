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

Kotlin's `jvmTarget` sets the Java bytecode version that the compiler emits, but it does not restrict the JDK APIs that can be referenced. This allows the compiler to accidentally use newer JDK methods, causing `NoSuchMethodError` at runtime on older platforms. The article illustrates this with a crash caused by JDK 21's new `List.removeFirst()` method taking precedence over Kotlin's extension function of the same name, because member functions always win over extensions.

- `jvmTarget` only affects bytecode version, not JDK API accessibility.
- JDK 21's `List.removeFirst()` overrides Kotlin's extension function due to member precedence.
- `-Xjdk-release` flag restricts the compiler to a specific JDK API level, avoiding accidental references to newer methods.
- The flag is available in Kotlin 1.7+ and is essential for cross-compilation, though not yet in Gradle DSL.