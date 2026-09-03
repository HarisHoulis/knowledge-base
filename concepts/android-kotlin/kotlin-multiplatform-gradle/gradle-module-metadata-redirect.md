---
domain: android-kotlin
subdomain: kotlin-multiplatform-gradle
concept: gradle-module-metadata-redirect
title: Multiplatform Compose and Gradle module metadata abuse
sources:
  - title: "Multiplatform Compose and Gradle module metadata abuse"
    url: "https://jakewharton.com/multiplatform-compose-and-gradle-module-metadata-abuse/"
    author: "Jake Wharton"
---

# Multiplatform Compose and Gradle module metadata abuse

The article describes a problem encountered when using a custom multiplatform build of the Compose runtime: Android builds fail with duplicate class errors because both Redwood's Compose runtime artifact and Google's official Compose runtime artifact contain the same `androidx.compose.runtime` classes. The root cause is that different Maven coordinates let Gradle include both artifacts, and the Android D8 tool does not allow duplicate classes.

- Redwood compiles the Compose runtime for every Kotlin platform and ships it as a single Kotlin multiplatform artifact, but Android consumers can hit duplicate class errors with Google's official Compose runtime.
- Gradle Module Metadata describes platform-specific variants and can redirect resolution through `available-at`, but that mechanism cannot point to Google's artifact because Google does not ship matching module metadata.
- A workaround replaces the Android variant's `available-at` block with a `dependencies` array pointing to `androidx.compose.runtime:runtime`, using text substitution on the generated module metadata JSON.
- The same duplicate-class problem remains on JVM and web when using Compose for Desktop or Compose for Web, because Google does not yet ship a fully multiplatform Compose runtime artifact.
- The approach is hacky but intentionally fails fast if the module metadata format changes, and a Gradle issue has been filed requesting a stable public API.