---
domain: android-kotlin
subdomain: gradle-build
concept: artifact-transforms
title: Understanding Gradle #32 – Artifact Transforms
sources:
  - title: "Understanding Gradle #32 – Artifact Transforms"
    url: "https://www.youtube.com/watch?v=T9U0BOlVc-c"
    author: "Jendrik Johannes"
    date: "2023-04-28T08:11:15+00:00"
---

# Understanding Gradle #32 – Artifact Transforms

Gradle's Artifact Transforms provide a way to modify dependencies before they are used, which is particularly useful for converting legacy JARs into proper Java modules. The video explains how automatic modules work and why they are insufficient for many cases, since they export all packages and rely on filename-based module names (Jendrik Johannes, 2023). By implementing an Artifact Transform, developers can enhance JARs by e.g. adding module information, thus improving modularity.

Artifact Transforms are triggered based on attributes and registered in Gradle's build scripts. The video demonstrates the implementation, covering how to define the transform and ensure it runs when artifacts are consumed. This allows integrating non-modular libraries into a modular project without manual workarounds.

The extra-java-module-info plugin from GradleX is showcased as a practical implementation of this concept, enabling developers to add module-info to jars via simple configuration. This solves the pain points described earlier, making it easier to use the Java Module System with existing libraries.

- Automatic modules are a stopgap that often break due to too-broad exports and implicit dependencies.
- Artifact Transforms enable on-the-fly modification of jar files before they enter a build configuration.
- Transforms are registered and activated via attributes, both in the build script and on the dependency side.
- The extra-java-module-info plugin automates the enhancement of jars to be proper Java modules.