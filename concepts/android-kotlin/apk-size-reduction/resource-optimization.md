---
domain: android-kotlin
subdomain: apk-size-reduction
concept: resource-optimization
title: Smaller APKs with resource optimization
sources:
  - title: "Smaller APKs with resource optimization"
    url: "https://jakewharton.com/smaller-apks-with-resource-optimization/"
    author: "Jake Wharton"
---

# Smaller APKs with resource optimization

Jake Wharton explains how Android APKs store resource file paths and names multiple times: in the zip entry headers, directory records, the resources.arsc database, classes.dex, and (for V1-signed APKs) the signing manifest. A minimal APK test shows the full resource path appears three times and the bare resource name appears twice in an unsigned APK.

Android Gradle Plugin 4.2 introduces `android.enableResourceOptimizations=true`, which runs `aapt optimize` on merged resources and resources.arsc for release builds. It shortens resource file names and paths inside the APK, e.g., `res/layout/home_view.xml` becomes `res/eA.xml`, while leaving resource entries unchanged. Real-world tests show APK size reductions of 0.76% for Plaid, 2.0% for SeriesGuide, and 2.0% for Tivi, with larger relative gains when V1 signing is used because resource paths appear in the manifest. The feature is easy to enable and applies regardless of `minifyEnabled`.

- Resource file paths and names are duplicated inside an APK, making path length a meaningful contributor to size.
- AGP 4.2's `android.enableResourceOptimizations=true` enables resource path shortening automatically for release builds.
- Empirical savings on real apps range from 0.76% to 2.0%, depending on resource count and other APK components.
- V1 signing makes resource optimization even more impactful because file paths are stored in the manifest.
- Enabling the flag in `gradle.properties` is a zero-effort way to reduce APK size.