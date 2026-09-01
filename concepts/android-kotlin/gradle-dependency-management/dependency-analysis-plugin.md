---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: dependency-analysis-plugin
title: Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin
sources:
  - title: "Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin"
    url: "https://www.youtube.com/watch?v=Lipf5piizZc"
    author: "Jendrik Johannes"
    date: "2023-01-09"
---

# Understanding Gradle #28 – Clean Compile Classpaths with the Dependency Analysis Plugin

This video from the Understanding Gradle series focuses on using the Dependency Analysis Plugin to keep compile classpaths clean in modular Java or Android projects. The presenter demonstrates how the plugin helps detect dependencies that are declared with the wrong scope, such as using 'api' where 'implementation' is sufficient, or vice versa. It also finds unused dependencies and missing dependency declarations that are accidentally resolved through transitive dependencies.

The plugin provides analysis tasks that inspect the project's configurations and report issues. Examples show how it flags a dependency that should be 'implementation' instead of 'api' to shrink the compile classpath, and conversely, when a library needs to be exposed via 'api' because it appears in the public API. The video also covers detecting dependencies that are only needed at runtime and should be moved to 'runtimeOnly', and how to configure the plugin to create custom post-processing tasks based on the analysis results.

A key takeaway is that by applying this plugin, developers can better enforce modularity boundaries. The compile classpath is critical for compilation, and keeping it minimal avoids leaking internal dependencies to consumers. The plugin automates the review process, making it easier to refactor and maintain clean dependency declarations in Gradle builds.

- The Dependency Analysis Plugin automatically detects issues with dependency declarations, such as wrong scope (api vs implementation), unused dependencies, and missing declarations.
- Keeping compile classpaths clean is essential for modularity: 'api' exposes dependencies to consumers, while 'implementation' keeps them internal.
- The plugin suggests moving dependencies from 'implementation' to 'api' when they appear in a module's public API, and to 'runtimeOnly' when they are only needed at runtime.
- Analysis tasks produce reports that can be used as a basis for refactoring builds, and the plugin can be configured to run custom post-processing tasks.
- The example projects are available in both Kotlin DSL and Groovy DSL on GitHub, demonstrating practical usage.