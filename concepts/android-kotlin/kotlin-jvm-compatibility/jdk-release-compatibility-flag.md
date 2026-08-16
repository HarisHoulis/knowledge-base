---
domain: android-kotlin
subdomain: kotlin-jvm-compatibility
concept: jdk-release-compatibility-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

Jake Wharton describes a production crash caused by a `NoSuchMethodError` for `List.removeFirst()` on Android, even though the code used a Kotlin extension function. The root cause was that the build JDK was upgraded to 21, which added `removeFirst()` as a member method on `java.util.List`, and in Kotlin member functions always take precedence over extension functions. The `jvmTarget` setting only controls the emitted bytecode version (major version 52 for Java 8), not the set of JDK APIs that can be referenced, so the compiler still linked against the JDK 21 API.

- `jvmTarget` only affects bytecode version, not API compatibility; it does not prevent accidental use of newer JDK APIs.
- When compiling with a modern JDK, new member methods on core Java classes can silently override Kotlin extension functions, leading to runtime failures on older platforms.
- Kotlin's `-Xjdk-release` flag behaves like `javac --release`, constraining both bytecode version and available JDK APIs.
- Using `-Xjdk-release` fixes the issue by forcing resolution to the Kotlin extension function. Android developers generally don't need it because `android.jar` already limits API access.