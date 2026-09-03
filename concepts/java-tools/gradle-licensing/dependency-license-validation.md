---
domain: java-tools
subdomain: gradle-licensing
concept: dependency-license-validation
title: Gradle Dependency License Validation
sources:
  - title: "Gradle dependency license validation"
    url: "https://code.cash.app/gradle-dependency-license-validation"
    author: "Jake Wharton"
---

# Gradle Dependency License Validation

Cash App's Android app displayed a screen listing open source libraries and their licenses, but it had to be updated manually and often became stale or incomplete. During a hack week, Jake Wharton sought to automate the discovery of libraries and licenses while preserving the existing UI, because existing Gradle plugins typically generate HTML pages unsuitable for the app's requirements. The solution leverages the SPDX License List to normalize license names and URLs to short SPDX identifiers like Apache-2.0, addressing mapping and normalization problems when raw license data varies. Once normalized, an allow-list of SPDX identifiers can be used to fail the build if a disallowed license is detected. The normalized data can also be serialized as JSON for direct inclusion or further processing in the open source screen. This functionality was released as the Gradle plugin Licensee, which works for any Gradle-based project and supports edge cases such as internal dependencies, commercial SDKs, and non-standard licenses (source: https://code.cash.app/gradle-dependency-license-validation).

- Manual license list updates are error-prone and can become stale.
- SPDX License List maps varied license names/URLs to short standard identifiers.
- An allow-list of SPDX identifiers can enforce approved licenses at build time.
- Normalized license data can be serialized as JSON for flexible UI use.
- The Licensee Gradle plugin automates this for any Gradle project, not just Android.