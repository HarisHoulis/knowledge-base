---
domain: android-kotlin
subdomain: coding-style
concept: hungarian-notation
title: Just Say No to Hungarian Notation
sources:
  - title: "Just Say No to Hungarian Notation"
    url: "https://jakewharton.com/just-say-no-to-hungarian-notation/"
    author: "Jake Wharton"
---

# Just Say No to Hungarian Notation

Jake Wharton argues that Hungarian notation (prefixing fields with 'm' or 's') is an accidental and unjustified convention in Android Java development. He begins by debunking the notion that an Android Java style guide mandates its use, clarifying that the only real guide is for AOSP contributions, which does not apply to typical Android app developers or libraries.

- There is no Android Java style guide requiring Hungarian notation; AOSP style does not apply to most developers.
- The 'm'/'s' prefix encodes field visibility, which is less important in code review than type information.
- Android Studio and IntelliJ already visually distinguish static and instance fields, making prefixes redundant.
- Google's public Java style guide explicitly forbids Hungarian notation; AOSP's legacy style is not a model.
- Hungarian notation creates stale names when field type or visibility changes, e.g., static fields prefixed with 'm'.