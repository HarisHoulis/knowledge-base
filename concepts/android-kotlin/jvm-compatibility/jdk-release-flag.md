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

The article describes a production crash caused by Kotlin's jvmTarget setting not preventing references to newer JDK APIs. A NoSuchMethodError occurred because JDK 21 added removeFirst() as a member method on List, which then shadowed the Kotlin extension function of the same name. Although the class file was compiled to Java 8 bytecode (major version 52), the compiler still resolved the call to the JDK 21 interface method, leading to runtime failure on older Android devices [source].

Kotlin's jvmTarget only controls the emitted bytecode version, not the set of JDK APIs available at compile time. This is equivalent to javac's -target flag. The solution is the -Xjdk-release flag introduced in Kotlin 1.7, which acts like javac's --release by simultaneously setting source, target, and the JDK API surface. After enabling the flag, the bytecode correctly calls the Kotlin standard library helper instead of the missing List.removeFirst() method [source].

The article notes that Android plugin users do not need this flag because the android.jar already limits java.* APIs to compileSdk, and Gradle toolchains avoid the problem by using an old JDK, but at the cost of missing modern compiler improvements. A Gradle DSL for -Xjdk-release is still being tracked in KT-49746 [source].

- Kotlin's jvmTarget only changes bytecode version, not the JDK APIs you can reference.
- JDK 21 added removeFirst() to List, shadowing the Kotlin extension function and causing crashes on older platforms.
- Use -Xjdk-release=<version> to restrict the JDK API surface alongside the target bytecode version.
- Android projects with android.jar as bootclasspath are already protected and do not need this flag.
- Gradle toolchains solve the issue but sacrifice modern compiler improvements.