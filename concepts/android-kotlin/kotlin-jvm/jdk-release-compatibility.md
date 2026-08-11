---
domain: android-kotlin
subdomain: kotlin-jvm
concept: jdk-release-compatibility
title: Kotlin's JDK release compatibility flag
sources:
  - title: "Kotlin's JDK release compatibility flag"
    url: "https://jakewharton.com/kotlins-jdk-release-compatibility-flag/"
---

# Kotlin's JDK release compatibility flag

The article describes an Android app crash caused by a NoSuchMethodError when calling List.removeFirst(). The offending code used Kotlin's extension function removeFirst, but JDK 21 added a member function with the same name to List. Since Kotlin extensions are statically resolved and member functions always win, the compiler emitted a call to the interface method, leading to a runtime failure on older Android versions. This happened even though the project set jvmTarget to 1.8, because that flag only controls the emitted bytecode version, not the JDK API references (source: https://jakewharton.com/kotlins-jdk-release-compatibility-flag/).

- jvmTarget sets bytecode version but not API compatibility; new JDK members can shadow Kotlin extension functions.
- Use -Xjdk-release (available since Kotlin 1.7) to restrict JDK API usage, similar to javac's --release.
- The flag is essential for JVM and Kotlin Multiplatform targets; Android projects are already protected by android.jar.
- No official Gradle DSL exists for -Xjdk-release yet.