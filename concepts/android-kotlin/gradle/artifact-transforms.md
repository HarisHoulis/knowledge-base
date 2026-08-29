---
domain: android-kotlin
subdomain: gradle
concept: artifact-transforms
title: Understanding Gradle #32 – Artifact Transforms
sources:
  - title: "Understanding Gradle #32 – Artifact Transforms"
    url: "https://www.youtube.com/watch?v=T9U0BOlVc-c"
    author: "Jendrik Johannes"
    date: "2023-04-28"
---

# Understanding Gradle #32 – Artifact Transforms

The video explains how Gradle's Artifact Transforms can convert legacy JAR files into Java Modules. When a library is not a real Java module, it can be placed on the module path as an automatic module, but this has limitations: automatic modules export all packages and require care with dependencies. The video demonstrates how to use Artifact Transforms to enhance JARs by adding module metadata, effectively turning old JARs into 'clean' Java modules (Jendrik Johannes, 2023).

- Artifact Transforms allow on-the-fly transformation of dependencies, such as turning JARs into Java Modules during resolution.
- Automatic Modules are a workaround but have issues with encapsulation and dependency management.
- A custom transform can be implemented by registering a TransformAction and specifying attributes that trigger it.
- The extra-java-module-info plugin simplifies adding module information to existing JARs.
- Artifact Transforms avoid permanently modifying JARs in the repository.