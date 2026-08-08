---
domain: android-kotlin
subdomain: code-simplification
concept: legacy-file-migration
title: Kotlin Refactoring - Simplifying
sources:
  - title: "Kotlin Refactoring - Simplifying"
    url: "https://www.youtube.com/watch?v=XAvcwwPzzsc"
    author: "Pairing with Duncan"
    date: "2022-02-03T11:06:24+00:00"
---

# Kotlin Refactoring - Simplifying

The video covers a refactoring session in a Kotlin project called Gilded Rose. Previously, the code supported reading a 'last modified' date from a stock list file with a backwards-compatible fallback: if the date was missing, it would infer today's date. However, the code never actually saved this date back to the file in production, so the fallback path remained in active use. The first step is to fix this by saving the inferred date when the file is loaded, then deploying to production. After confirming the production file now includes the last modified date, the team can remove the legacy compatibility paths and simplify the code. The transcript demonstrates deleting obsolete test helpers, removing default parameters, and using `Instant.EPOCH` as a natural fallback for the genuinely empty-file case. The overall approach is to migrate production data first, then strip out the now-unnecessary backward-compatibility logic, making the code cleaner and easier to maintain.

- Upgrade production data before removing legacy code paths: save the inferred last modified date during a normal load, then deploy to ensure the file format is permanent.
- Remove obsolete methods and parameters once compatibility is no longer needed, such as the 'loadLegacyFile' method and the default last modified parameter.
- Use `Instant.EPOCH` as a sensible fallback for empty files instead of propagating a configurable default date.
- Run all tests after each refactoring step to verify behavior is preserved.