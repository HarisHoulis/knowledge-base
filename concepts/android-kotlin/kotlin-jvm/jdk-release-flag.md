---
domain: android-kotlin
subdomain: kotlin-jvm
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes a production crash caused by a `NoSuchMethodError` on `List.removeFirst()`. The Kotlin code was relying on a Kotlin extension function, but after upgrading the build JDK to 21, the new member function `removeFirst()` added to the `List` interface by JDK's sequenced collections took precedence, because member functions always win over extension functions. This illustrates a subtle cross-compilation hazard when building with a newer JDK against an older target.

The author explains that setting Kotlin's `jvmTarget` to Java 8 only controls the emitted bytecode version, not the set of JDK APIs that can be referenced. Inspecting the compiled class showed major version 52 (Java 8) but still an `invokeinterface` directly calling `java.util.List.removeFirst()`. This is the same behavior as `javac -target` without a bootclasspath, which can lead to references to APIs unavailable on the runtime.

The solution is `-Xjdk-release`, a Kotlin compiler flag introduced in Kotlin 1.7 that works like `javac --release`. It restricts the JDK API surface to the specified version, causing the extension function to resolve to the Kotlin standard library static helper instead of the JDK member. The article notes that Android plugin users don't need this flag because `android.jar` already limits the available `java.*` APIs, and that no Gradle DSL exists yet (tracked in KT-49746).

- `jvmTarget` only sets bytecode version, not the JDK API level, so newer JDK methods can be accidentally referenced.
- New JDK member functions shadow Kotlin extension functions, leading to `NoSuchMethodError` on older runtimes.
- Use `-Xjdk-release` to align the JDK API with the target bytecode version, similar to `javac --release`.
- The Kotlin Android plugin is already safe because `android.jar` restricts accessible APIs.
- Gradle toolchains avoid the issue but force using an ancient JDK, losing compiler improvements.