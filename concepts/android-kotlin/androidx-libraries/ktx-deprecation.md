---
domain: android-kotlin
subdomain: androidx-libraries
concept: ktx-deprecation
title: An update on Android KTX
sources:
  - title: "An update on Android KTX"
    url: "https://jakewharton.com/an-update-on-android-ktx/"
    author: "Jake Wharton"
    date: "2026-04-01"
---

# An update on Android KTX

The Android KTX libraries, originally launched to provide Kotlin extensions for Android APIs, are being phased out as Kotlin adoption has become widespread. All Kotlin-specific extensions have been merged directly into their respective main AndroidX libraries, making separate KTX modules obsolete. A comprehensive table lists each KTX library and the first version where it became empty (e.g., core-ktx in 1.19.0-alpha01, activity-ktx in 1.9.0). A Lint feature has been requested to warn developers when they depend on an obsolete KTX library. Developers should migrate their codebase to rely on the main libraries, which now include the Kotlin niceties natively.

- Android KTX libraries are being deprecated because their Kotlin extensions have been merged into the main AndroidX libraries.
- Each KTX module became obsolete in a specific version of the parent library; a table in the article shows these versions.
- Developers should remove KTX dependencies and update to the appropriate main library versions to get the same functionality.
- A Lint check is proposed to warn when using a KTX library that is no longer needed.
- The article acknowledges the contributions of the original authors and the community to the KTX project.