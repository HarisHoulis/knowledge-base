---
domain: android-kotlin
subdomain: dependency-management
concept: play-services-unbundling
title: Play Services 5.0 Is A Monolith Abomination
sources:
  - title: "Play Services 5.0 Is A Monolith Abomination"
    url: "https://jakewharton.com/play-services-is-a-monolith/"
    author: "Jake Wharton"
---

# Play Services 5.0 Is A Monolith Abomination

Google Play Services 5.0 is a monolithic library that contributes over twenty thousand methods to an Android app, consuming nearly one-third of the 64K dex method limit. This is a serious problem for developers who are already wary of libraries like Guava, which contributes roughly 14k methods. The author argues that unlike Guava, Play Services contains many disparate features that share little in common except being from Google, making it a strong candidate for modularization (Jake Wharton, "Play Services 5.0 Is A Monolith Abomination", https://jakewharton.com/play-services-is-a-monolith/).

The post suggests that Google should unbundle Play Services into small, modular artifacts. Developers could then declare only the components they need, such as ads, analytics, or games, either via Gradle dependencies or a dedicated plugin DSL. The author rejects ProGuard as an answer because stripping unused code on release builds does not justify shipping large chunks of unused code in dependencies, nor does it help development build speed. The post includes detailed method-count breakdowns by package and dependency graphs to illustrate how easily the library could be partitioned.

By pointing out the inflated method count and the unrelated internal packages, the author makes a clear case for more granular dependency management on Android, anticipating the later official split of Google Play Services into separate artifacts.

- Google Play Services 5.0 adds over 20,000 DEX methods, consuming about one-third of the 64K method limit on Android.
- Unlike Guava, Play Services' features are disparate and could be easily partitioned into modular libraries.
- The author recommends declaring only needed components (e.g., ads, analytics, games) as separate dependencies, or using a plugin DSL, instead of including the entire monolith.
- ProGuard is not an acceptable justification for shipping unused code, as it only helps release builds and not development workflows.