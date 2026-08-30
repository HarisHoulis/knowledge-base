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

This video explains how Gradle Artifact Transforms can be used to turn legacy JAR files into Java Modules for the Java Module System (JPMS). The core challenge is that many libraries on the classpath or module path are not real modules, and simply placing them on the module path makes them automatic modules, which export all packages and derive module names from filenames—leading to fragile and opaque behavior. Artifact Transforms provide a mechanism to modify artifacts as they are resolved, allowing you to add proper module metadata or patch existing JARs before they are used as modules.

The presenter demonstrates how to implement a custom Artifact Transform in Gradle, covering how transforms are registered, triggered by attributes, and wired into dependency resolution. He also contrasts the manual approach with the Extra Java Module Info plugin, which simplifies the task by letting you declare module-info metadata for external libraries without writing transforms yourself. The summary emphasizes that Artifact Transforms are a powerful tool for modernizing Java builds and integrating legacy dependencies into a module-based architecture.

Key takeaways include the limitations of automatic modules, the mechanics of Gradle's transform registration and triggering, and the practical utility of the extra-java-module-info plugin for real-world projects.

- Artifact Transforms allow you to modify artifacts during dependency resolution, e.g., adding module-info to legacy JARs.
- Automatic modules are a quick fallback but have drawbacks: they export all packages and derive module names from file names.
- Custom transforms are implemented in Gradle and triggered by requested attributes.
- The Extra Java Module Info plugin provides a simpler, declarative way to add module metadata to non-modular libraries.
- Using transforms helps integrate legacy JARs into the Java Module System cleanly.