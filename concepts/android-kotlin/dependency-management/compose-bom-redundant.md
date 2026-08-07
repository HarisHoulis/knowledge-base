---
domain: android-kotlin
subdomain: dependency-management
concept: compose-bom-redundant
title: Let's defuse the Compose BOM
sources:
  - title: "Let's defuse the Compose BOM"
    url: "https://jakewharton.com/defuse-the-compose-bom/"
    author: "Jake Wharton"
---

# Let's defuse the Compose BOM

The Compose BOM is a popular way to manage versions of Compose libraries, but Jake Wharton argues it is largely unnecessary for Gradle users. Every AndroidX library automatically bundles peer dependency constraints in its Gradle module metadata, which ensures all artifacts within a library group resolve to the same version. This built-in mechanism already prevents version mismatches without needing a BOM, as demonstrated by the metadata excerpt from foundation-layout v1.10.0.

- AndroidX libraries ship Gradle module metadata that automatically aligns all artifacts in a library group, making the BOM redundant for Gradle users.
- The Compose BOM defines only four distinct versions across five library groups, despite covering about 15 libraries.
- Version catalogs offer a modern, centralized way to manage these few versions without the extra indirection.
- The BOM's release cadence is inconsistent and its single version number hides the actual library versions, complicating bug tracking.
- Since BOM versions still participate in normal dependency resolution and can be overridden, they do not guarantee a known final version without a lock file.