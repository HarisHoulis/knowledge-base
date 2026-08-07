---
domain: android-kotlin
subdomain: androidx-ktx
concept: ktx-sunset
title: An update on Android KTX
sources:
  - title: "An update on Android KTX"
    url: "https://jakewharton.com/an-update-on-android-ktx/"
    author: "Jake Wharton"
    date: "2026-04-01"
---

# An update on Android KTX

Android KTX libraries are being wound down because Kotlin adoption has been so successful that all Kotlin extensions have been merged directly into their respective main AndroidX libraries. This marks the end of the separate `-ktx` modules that were introduced eight years ago to add Kotlin niceties to the Android platform (Jake Wharton, https://jakewharton.com/an-update-on-android-ktx/).

- Android KTX extension libraries are being discontinued because Kotlin extensions have been merged into the main AndroidX libraries.
- The table lists each `-ktx` module and the version where it became empty/obsolete; many are alpha versions pending stable release.
- A Lint feature request has been filed to warn developers when they declare an obsolete KTX library.
- The KTX libraries were successful because Kotlin adoption was so widespread that they became redundant.
- Jake Wharton, the original creator, also led the final elimination, with contributions from ~157 people.