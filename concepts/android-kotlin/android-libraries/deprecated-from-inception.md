---
domain: android-kotlin
subdomain: android-libraries
concept: deprecated-from-inception
title: Deprecated From Inception
sources:
  - title: "Deprecated From Inception"
    url: "https://jakewharton.com/deprecated-from-inception/"
---

# Deprecated From Inception

Jake Wharton argues that ActionBarSherlock, while necessary for apps with a minSdkVersion below 14, was intentionally designed from the start to be deprecated. Its API mirrors the native ActionBar classes, themes, and attributes, so when an app eventually raises its minimum API level to 14 or higher, switching from ActionBarSherlock to the native ActionBar is almost entirely mechanical, mostly import changes and replacing getSupportActionBar with getActionBar.

- Apps with minSdkVersion below 14 should use ActionBarSherlock to avoid boilerplate.
- The library's API is intentionally compatible with the native ActionBar to ease future migration.
- Switching from ActionBarSherlock to native ActionBar at API 14 can be almost fully scripted.
- Google's action bar backport announcement was criticized as too late and potentially wasteful engineering effort.
- Libraries should ideally be small and modular, but ActionBarSherlock's design trades that for drop-in replaceability.