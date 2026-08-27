---
domain: android-kotlin
subdomain: gradle
concept: artifact-transforms
title: Understanding Gradle #32 – Artifact Transforms
sources:
  - title: "Understanding Gradle #32 – Artifact Transforms"
    url: "https://www.youtube.com/watch?v=T9U0BOlVc-c"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-04-28T08:11:15+00:00"
---

# Understanding Gradle #32 – Artifact Transforms

This video explains how to use Gradle Artifact Transforms to convert legacy JAR files into proper Java modules for the Java Module System (JPMS). Without transformations, putting an ordinary JAR on the module path causes it to be treated as an automatic module, which derives its module name from the file name and exports all packages by default. This can lead to issues such as unclear module names and accidental exposure of internal packages.

Artifact Transforms allow Gradle to modify dependency artifacts during dependency resolution, before they are placed on the module path or classpath. The video walks through the implementation and registration of a custom artifact transform that injects module metadata (e.g., module names or module-info descriptors) into existing JARs. It also demonstrates how transforms are triggered based on request attributes, enabling modular builds without requiring every library to be re-packaged.

A practical solution is the 'extra-java-module-info' plugin, which provides a ready-made artifact transform for adding module descriptors to non-modular JARs. The video emphasizes how this technique improves reliability and maintainability when working with third-party libraries in a modular Java project.

- Artifact transforms rewrite dependency artifacts during resolution, enabling modification without altering original binaries.
- Old JARs become automatic modules on the module path, leading to auto-generated names and implicit exports of all packages.
- Custom transforms can inject module-info.class or module name metadata to create explicit modules from plain JARs.
- Transforms are triggered by attribute requests, like requiring a module name attribute during dependency resolution.
- The extra-java-module-info plugin offers a simpler, reusable implementation for adding module metadata.