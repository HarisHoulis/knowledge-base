---
domain: system-design
subdomain: dependency-management
concept: dependency-analysis-plugin
title: Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin
sources:
  - title: "Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin"
    url: "https://www.youtube.com/watch?v=Lipf5piizZc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-01-09T13:40:43+00:00"
---

# Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin

In this video, Jendrik Johannes continues the series on Java modularity by demonstrating how to keep compile classpaths clean using the Dependency Analysis plugin. The video shows practical examples with Java plugins, illustrating how changing a module's public API can lead to inconsistent dependency declarations. The plugin helps detect issues like dependencies declared with the wrong scope (e.g., 'api' vs 'implementation'), unused dependencies, missing declarations, and incorrect runtime-only usage. By applying the plugin and running its analysis tasks, developers can identify these problems and refactor their build files to shrink compile classpaths, improving build performance and enforcing proper modular boundaries [1].

- The Dependency Analysis plugin detects wrong dependency scopes (e.g., api vs implementation) and flags unused or missing dependencies.
- It helps shrink compile classpaths, which is crucial for enforcing true modularity and reducing coupling between modules.
- The plugin provides analysis tasks and can be configured to support custom post-processing actions.
- The video demonstrates the plugin's use in both Kotlin DSL and Groovy DSL example projects.
- Keeping compile classpaths clean improves build performance and clarifies the public API of each module.