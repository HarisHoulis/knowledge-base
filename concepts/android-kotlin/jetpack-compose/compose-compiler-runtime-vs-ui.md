---
domain: android-kotlin
subdomain: jetpack-compose
concept: compose-compiler-runtime-vs-ui
title: A Jetpack Compose by any other name
sources:
  - title: "A Jetpack Compose by any other name"
    url: "https://jakewharton.com/a-jetpack-compose-by-any-other-name/"
    author: "Jake Wharton"
---

# A Jetpack Compose by any other name

The article argues that Jetpack Compose is actually two separate efforts: the Compose compiler/runtime, a general-purpose tool for managing trees of nodes of any type, and Compose UI, a UI toolkit built on top of those trees. While historically these two projects became linked, the separation still exists and has become more defined. The author, Jake Wharton, reveals that he has three projects that use only the compiler/runtime and not Compose UI, and that the umbrella name 'Compose' makes this distinction unnecessarily confusing [source: https://jakewharton.com/a-jetpack-compose-by-any-other-name/].

The conflation of the two parts under one name creates two problems: specificity and pigeonholing. When people say 'Compose', they almost always mean Compose UI, making discussions imprecise. Moreover, because the UI toolkit dominates the name, the general-purpose compiler/runtime's potential is overlooked. The author notes that the compiler/runtime supports more platforms and targets than Compose UI, including JVM servers and non-browser JS engines, yet these use cases receive little attention. He calls for Google to rename the compiler/runtime to something like 'Evergreen', 'Juliet', or 'Crane' so that it can stand on its own, separate from the Compose UI toolkit [source: https://jakewharton.com/a-jetpack-compose-by-any-other-name/].

- Compose compiler/runtime is a general-purpose node-tree management tool, distinct from the Compose UI toolkit built on top of it.
- Using the single name 'Compose' for both causes imprecision and suggests the core is only for UI.
- The core supports more platforms/targets than Compose UI (e.g., JVM servers, JS engines), demonstrating its broader applicability.
- The article pleads with Google to give the compiler/runtime a distinct name so it can gain recognition.