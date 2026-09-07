---
domain: android-kotlin
subdomain: java-modernization-and-desugaring
concept: java-9-12-android-support
title: Android's Java 9, 10, 11, and 12 Support
sources:
  - title: "Android's Java 9, 10, 11, and 12 Support"
    url: "https://jakewharton.com/androids-java-9-10-11-and-12-support/"
    author: "Jake Wharton"
---

# Android's Java 9, 10, 11, and 12 Support

This article is part of a series on D8 and R8, Android's dexer and optimizer, and continues the exploration of Android's Java support beyond Java 8. Jake Wharton examines the language features introduced in Java 9 through Java 12 and evaluates whether they can be used in Android development. He finds that most new language features are implemented entirely in the Java compiler, producing bytecode that D8 can dex without issue. For instance, Java 9's try-with-resources on effectively-final variables and the anonymous diamond operator require no desugaring. However, Java 9's private interface methods rely on D8's existing desugaring machinery for static/default methods, and on API 24+ ART natively supports private interface members.

- Java 9 language features such as try-with-resources on effectively-final variables and anonymous diamond operator work on all Android API levels because they are purely javac features.
- Java 9's private interface methods are desugared by D8 for pre-API 24 devices, but ART natively supports them starting at API 24.
- Java 9's string concatenation bytecode uses invokedynamic; D8 desugars this back to StringBuilder operations, preserving compatibility across all API levels.
- Java 10's `var` and Java 11's lambda parameter `var` are compiler-only features, so they are immediately usable in Android without special desugaring.
- APIs from Java 9-11, such as collection factories and the new HTTP client, are not yet part of the Android SDK, and while some may be desugared in the future, the large HTTP client's inclusion is uncertain.