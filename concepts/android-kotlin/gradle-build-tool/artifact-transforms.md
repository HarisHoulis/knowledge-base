---
domain: android-kotlin
subdomain: gradle-build-tool
concept: artifact-transforms
title: Understanding Gradle #32 – Artifact Transforms
sources:
  - title: "Understanding Gradle #32 – Artifact Transforms"
    url: "https://www.youtube.com/watch?v=T9U0BOlVc-c"
    author: "Jendrik Johannes"
    date: "2023-04-28"
---

# Understanding Gradle #32 – Artifact Transforms

The video explains how to use Artifact Transforms in Gradle to convert legacy JAR files into proper Java Modules. Java's Module System requires a module-info descriptor, but many libraries are still shipped as plain JARs. Automatic modules offer a temporary workaround, but they have drawbacks such as exposing all packages and unstable module names (Jendrik Johannes, 2023).

- Automatic modules allow plain JARs on the module path but cause issues like broad package exports and implicit module names.
- Artifact Transforms let Gradle modify dependency artifacts during resolution, enabling the injection of module-info into old JARs.
- Transforms are triggered by specific attributes requested during dependency resolution, allowing customized module metadata.
- The extra-java-module-info plugin simplifies this process by providing a convenient DSL to add module-info to third-party libraries.