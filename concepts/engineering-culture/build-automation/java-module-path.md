---
domain: engineering-culture
subdomain: build-automation
concept: java-module-path
title: Understanding Gradle #31 – The Module Path
sources:
  - title: "Understanding Gradle #31 – The Module Path"
    url: "https://www.youtube.com/watch?v=X9u1taDwLSA"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-03-07"
---

# Understanding Gradle #31 – The Module Path

In this video, Jendrik Johannes explains the Java Module System (JPMS/Jigsaw) and its integration with Gradle. The central idea is the contrast between the classpath and the module path. On the classpath, multiple versions of the same class can coexist and conflicts are silently resolved by the first match, whereas the module path requires unique module names and reports conflicts at runtime or compile time. This makes the module path stricter and more predictable for large applications. The video demonstrates how to use javac and java with the module path, showing a minimal module-info.java that declares module dependencies with requires and exposes packages with exports. It also covers how Gradle builds modular Java applications, noting that dependency management (versions, coordinates) is still Gradle's responsibility, while the module declarations in module-info.java define the modular structure. A key challenge is redundancy: dependencies must be declared in both Gradle and module-info.java. To address this, the java-module-dependencies plugin is introduced, which allows referring to modules by their names and automatically maps them to Maven coordinates, streamlining version management and reducing duplication.

- The module path enforces unique module names and detects conflicts, unlike the classpath which silently resolves duplicate classes.
- module-info.java uses 'requires' for module dependencies and 'exports' for exposing packages to other modules.
- Gradle continues to handle dependency resolution and versioning; module-info.java only expresses the module-level contract.
- The java-module-dependencies plugin eliminates redundant dependency declarations by mapping module names to Maven coordinates.
- Running a modular application with Gradle requires configuring the JavaExec task to use the module path.