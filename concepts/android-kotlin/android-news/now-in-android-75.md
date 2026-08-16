---
domain: android-kotlin
subdomain: android-news
concept: now-in-android-75
title: Now in Android #75
sources:
  - title: "Now in Android #75"
    url: "https://medium.com/androiddevelopers/now-in-android-75-e4bbe977d33f"
    author: "Manuel Vivo"
    date: "2023-01-18"
---

# Now in Android #75

The first Now in Android episode of 2023 highlights a new stable release of Android Studio, featuring improvements to Compose Preview auto-updates, layout inspector recomposition counts, visual XML linting for Views, sync performance with parallel project imports, SDK Index integration, a new logcat, resizable emulators, and physical device mirroring. AndroidX releases include stable AppCompat 1.6.0 (Android 13 per-language preferences and predictive back) and Room 2.5.0 (converted runtime to Kotlin, Upsert annotation, and room-paging support for RxJava/Guava). Lifecycle 2.6.0-alpha04 removes the experimental annotation from collectAsStateWithLifecycle and deprecates pausing dispatcher and launchWhenX APIs. New libraries include androidx.credentials for password/passkey sign-in, and privacy sandbox libraries adservices and sdkruntime.

Articles cover adding a domain layer to the Now in Android app, extending the Android SDK to backport features like the photo picker, building media apps for Wear OS with the Wear media toolkit, migrating from TextureView to SurfaceView for HDR playback, and using new stylus low latency libraries (low latency graphics and motion prediction). Videos address paywall conversion optimization, push notification engagement, CameraX concepts, a FLEDGE API sample, and the Attribution Reporting API. The Android Developers Backstage podcast discusses Kotlin Multiplatform and the K2 frontend.

- Android Studio stable includes enhanced Compose tooling, new logcat, and better sync performance.
- AppCompat 1.6.0 and Room 2.5.0 graduated to stable with notable features.
- New AndroidX libraries target credentials and privacy sandbox APIs.
- Recommended architecture guidance suggests adding a domain layer for readability and scalability.
- Privacy Sandbox APIs (FLEDGE, Attribution Reporting) are introduced with sample implementations.