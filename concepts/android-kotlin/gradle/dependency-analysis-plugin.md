---
domain: android-kotlin
subdomain: gradle
concept: dependency-analysis-plugin
title: Clean Compile Classpaths with the Dependency Analysis Plugin
sources:
  - title: "Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin"
    url: "https://www.youtube.com/watch?v=Lipf5piizZc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-01-09T13:40:43+00:00"
---

# Clean Compile Classpaths with the Dependency Analysis Plugin

This video, part 3 of a series on Java modularity in Gradle, explains how the Dependency Analysis plugin helps keep module compile classpaths clean. With standard Java plugins, dependency scopes (api vs implementation) can easily become misdeclared, leading to unnecessarily large compile classpaths and broken encapsulation. The plugin provides analysis tasks that detect problematic dependency declarations.

The plugin identifies four main categories of issues: dependencies on the wrong scope (e.g., api used where implementation is sufficient, or implementation used where api is required), unused dependencies that are declared but never referenced, missing dependency declarations where a module uses types it does not directly declare, and incorrect use of runtimeOnly instead of implementation. These reports allow developers to refactor their build files to shrink compile classpaths, which improves build performance and enforces proper modular boundaries.

The video also demonstrates how to apply the plugin, configure it, and create custom post-processing tasks to act on the analysis results. It uses a multi-project example available on GitHub, showing both Kotlin and Groovy DSL setups. The overall goal is to keep compile classpaths minimal, ensuring that modules only expose what they need and resolve dependencies in a predictable manner.

- The Dependency Analysis plugin detects wrong dependency scopes (api vs implementation) and suggests corrections.
- It identifies unused dependencies that can be safely removed, reducing classpath bloat.
- It finds missing dependency declarations caused by transitive dependencies leaking through the compile classpath.
- Refactoring based on the plugin's reports shrinks compile classpaths, improving build performance and module encapsulation.
- The plugin supports configuration and custom post-processing tasks for automated dependency management.