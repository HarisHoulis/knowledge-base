---
domain: android-kotlin
subdomain: d8-r8
concept: core-library-desugaring
title: D8 Library Desugaring
sources:
  - title: "D8 Library Desugaring"
    url: "https://jakewharton.com/d8-library-desugaring/"
---

# D8 Library Desugaring

D8's core library desugaring backports newer Java APIs (like java.time, streams, Optional) to older Android API levels, enabling developers to use them without backport libraries. The article explains that D8 already supported simple desugaring for APIs such as Objects.requireNonNull (rewritten to getClass()) and Long.hashCode (backported via generated classes). For full Java 8+ type desugaring, D8 rewrites bytecode references from java.time to j$.time and bundles an implementation from Google's desugar_jdk_libs project, a process that significantly increases APK size in debug builds but is partially mitigated by R8 minification.

- Core library desugaring rewrites Java 8+ API calls to backported implementations (j$ packages), enabling use on older Android versions.
- Simple APIs like Objects.requireNonNull and Long.hashCode have targeted desugaring mechanisms.
- Enabling coreLibraryDesugaring in AGP causes D8/R8 to add an implementation dex (via L8) and generate keep rules for accessed backported types.
- APK size increases when using desugared types; release builds with R8 help reduce the impact.
- The desugared API list includes methods from Java 7/8 and some Java 9–11 APIs.