---
domain: engineering-culture
subdomain: gradle-dependency-management
concept: dependency-analysis-plugin
title: Clean Compile Classpaths with the Dependency Analysis Plugin
sources:
  - title: "Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin"
    url: "https://www.youtube.com/watch?v=Lipf5piizZc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-01-09T13:40:43+00:00"
---

# Clean Compile Classpaths with the Dependency Analysis Plugin

The video, part of the 'Understanding Gradle' series, focuses on using the Dependency Analysis plugin to keep compile classpaths clean in Java modules. It demonstrates how the plugin identifies incorrectly scoped dependencies (api vs implementation), unused dependencies, and missing dependency declarations. By applying the plugin to a Gradle project, developers can detect and fix issues that cause unnecessary dependencies to leak into consumers' compile classpaths, leading to slower builds and potential runtime conflicts.

Through examples, the video shows how changing a module's public API can require dependency scope adjustments, and how the plugin provides tasks to analyze dependency usage. It also covers configuring the plugin and custom post-processing tasks to tailor analysis to project needs. The key takeaway is that maintaining clean compile classpaths is crucial for modular Java projects, as it ensures proper encapsulation and minimizes recompilation and build times.

The video references an example project on GitHub (both Kotlin and Groovy DSL) and recommends the dependency analysis plugin for Android and Java projects. It aligns with broader engineering culture practices of proactive dependency hygiene and modular design.

- The Dependency Analysis plugin detects dependencies declared in the wrong configuration, such as api when implementation is sufficient or vice versa.
- It identifies unused dependencies that can be safely removed and missing dependencies that should be explicitly declared.
- Clean compile classpaths prevent API leakage between modules, reducing unintended coupling and build times.
- The plugin can be configured to adjust analysis scope and supports custom post-processing tasks for project-specific rules.