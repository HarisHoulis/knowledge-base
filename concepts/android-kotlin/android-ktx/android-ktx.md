---
domain: android-kotlin
subdomain: android-ktx
concept: android-ktx
title: Introducing Android KTX: Even Sweeter Kotlin Development for Android
sources:
  - title: "Introducing Android KTX: Even Sweeter Kotlin Development for Android"
    url: "https://android-developers.googleblog.com/2018/02/introducing-android-ktx-even-sweeter.html"
    date: "2018-02-05"
---

# Introducing Android KTX: Even Sweeter Kotlin Development for Android

This post announces the preview of Android KTX, a set of extensions designed to make Kotlin code for Android more concise, idiomatic, and pleasant. It provides an API layer on top of both the Android framework and the Support Library. The framework portion is available on GitHub for feedback and contributions, while Support Library extensions will arrive in upcoming releases. Examples demonstrate simpler code for tasks like converting strings to URIs, editing SharedPreferences, translating paths, and setting onPreDraw callbacks.

- Android KTX offers extension functions for both the Android framework and Support Library.
- The preview is available on GitHub; APIs may change before the stable release.
- Example extensions include String.toUri(), SharedPreferences.edit {}, Path subtraction, and View.doOnPreDraw.
- Android KTX uses the new androidx package name prefix, distinguishing static libraries from platform APIs.