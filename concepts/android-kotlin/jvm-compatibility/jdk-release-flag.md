---
domain: android-kotlin
subdomain: jvm-compatibility
concept: jdk-release-flag
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
    author: "Jake Wharton"
---

# Kotlin's JDK release compatibility flag

The article explains a production crash caused by a `NoSuchMethodError` for `List.removeFirst()`. The issue arose because the code was compiled with JDK 21, where `List` gained a member method `removeFirst()`. In Kotlin, extension functions are statically resolved, but member functions always win if they match. Thus, the Kotlin stdlib's `removeFirst()` extension was ignored, and the compiler emitted a direct interface call to the JDK 21 method, which is absent on older Android versions.

Setting `jvmTarget` to 1.8 only controls the bytecode version, not the JDK API available at compile time. The article demonstrates that the classfile major version was 52 (Java 8), yet the bytecode still referenced the JDK 21 method. This mirrors `javac`'s `-target` flag, which also requires `-bootclasspath` or `--release` to constrain API usage. Kotlin 1.7 introduced `-Xjdk-release`, which acts like `javac --release` and restricts the JDK API to the specified version. Using it changed the bytecode to call the Kotlin stdlib's static helper instead of the interface method, fixing the crash.

The article notes that the flag is essential for Kotlin JVM and multiplatform JVM targets to ensure compatibility with a minimum JVM. Android users typically don't need it because `android.jar` as the bootclasspath limits `java.*` APIs to the `compileSdk`. There is no official Gradle DSL for the flag yet, tracked in KT-49746. Toolchains are an alternative but require running an ancient JDK, which is generally discouraged.

- Kotlin extension functions are only used when no matching member function exists; JDK 21's new `List.removeFirst()` member overrides the stdlib extension.
- `jvmTarget` only sets bytecode version and does not restrict the JDK API that can be referenced, leading to crashes on older platforms.
- The `-Xjdk-release` flag in Kotlin 1.7+ acts like `javac --release`, restricting the JDK API and ensuring correct extension resolution.
- Android projects are protected by their `compileSdk` android.jar bootclasspath, but JVM and multiplatform targets need `-Xjdk-release` for cross-compilation safety.
- Gradle toolchains avoid the issue by using an actual old JDK, but miss modern compiler improvements; a Gradle DSL for the flag is pending (KT-49746).