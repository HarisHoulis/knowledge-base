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

Jake Wharton describes a `NoSuchMethodError` on Android caused by Kotlin's `removeFirst()` extension function being shadowed by a new member method added to `List` in JDK 21. The code was compiled with `jvmTarget` set to 1.8, but as the article explains, the Java bytecode version is independent of the set of JDK APIs you can reference. Thus, even with a Java 8 classfile target, the Kotlin compiler can emit calls to APIs introduced in later JDKs, leading to runtime crashes on older platforms. He compares this to `javac`'s `-target` flag, which has the same limitation and can be addressed via the `--release` flag that automatically sets source, target, and bootclasspath together. Kotlin 1.7 introduced `-Xjdk-release` to provide equivalent behavior for Kotlin/JVM compilation. Configuring this flag changes the bytecode to invoke the static extension function `CollectionsKt.removeFirst` instead of the interface method, avoiding the unavailable API. The article recommends using `-Xjdk-release` for Kotlin JVM and multiplatform JVM targets, while noting that Android users are already protected by `android.jar` acting as the bootclasspath and Android Lint. There is no Gradle DSL yet, tracked in KT-49746, and Gradle toolchains are not recommended because they use old JDKs and miss compiler improvements.

- `jvmTarget` only sets bytecode version, not the JDK API level; it does not prevent references to newer JDK methods.
- New member functions on JDK classes can silently override Kotlin extension functions, e.g., `List.removeFirst()` in JDK 21.
- Kotlin's `-Xjdk-release` flag (like javac's `--release`) restricts the compiler to APIs available in the specified JDK version.
- Applying `-Xjdk-release` changes the bytecode to call the static Kotlin extension helper instead of the JDK interface method.
- Android plugin users don't need this flag because `android.jar` already limits Java APIs; a Gradle DSL is still pending in KT-49746.