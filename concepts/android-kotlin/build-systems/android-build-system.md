---
domain: android-kotlin
subdomain: build-systems
concept: android-build-system
title: The Android Build System Is Broken
sources:
  - title: "The Android Build System Is Broken"
    url: "https://jakewharton.com/the-android-build-system-is-broken/"
    author: "Jake Wharton"
---

# The Android Build System Is Broken

The article argues that Android does not truly have a build system, but rather a scripting language forced into XML, a default configuration attempting to cover all use cases, and an IDE whose configuration has marginal integration. This setup breaks down in complex projects with multiple modules, nested library dependencies, and overlapping jar dependencies, leaving developers to fend for themselves (Jake Wharton, "The Android Build System Is Broken").

The author outlines what a proper build system should provide: the ability to dynamically configure variants, to include or exclude files, to generate sources, and to handle complex dependencies without rigid constraints. While Maven and IntelliJ IDEA are cited as closer to these ideals, they are not perfect. The article criticizes Google for advocating ant and the Eclipse plugin, which are inadequate for modern Android development, and concludes that developers deserve a build system with the same attention to detail as the OS and debugging tools.

- Android's build tooling is described as a scripting language in XML, not a real build system.
- Complex multi-module and multi-dependency projects are poorly served by ant and Eclipse.
- A build system should empower, enable, and be dynamic, not constrain or restrict.
- Google's support for ant and Eclipse is seen as a problem, while Maven/IntelliJ are better but still imperfect.