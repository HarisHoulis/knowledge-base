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

The video explains how modularity in Java projects relies on keeping compile classpaths clean, and introduces the Dependency Analysis plugin for Gradle to automate this process. It demonstrates the plugin's ability to detect wrongly scoped dependencies (e.g., `api` vs `implementation`), unused dependencies, missing direct declarations, and cases where `runtimeOnly` is more appropriate. By applying the plugin to a sample project, the author shows how it generates reports and suggests fixes that help developers shrink compile classpaths and enforce proper module boundaries.

The tutorial walks through applying the plugin in a root build file, running analysis tasks, and interpreting the results. It highlights the importance of using `api` only when a dependency's types appear in the module's public API, and `implementation` otherwise. The plugin also uncovers dependencies that are declared but not used, as well as those that are used but not declared, which can lead to fragile builds. The video further explores configuring the plugin and creating custom post-processing tasks to integrate the analysis into development workflows.

Ultimately, the key takeaway is that clean compile classpaths improve build performance, reduce redundant recompilation, and make module dependencies explicit. The Dependency Analysis plugin serves as a practical tool to achieve this by providing actionable insights and automated checks. (Source: onepiece.Software by Jendrik Johannes, 2023)

- The Dependency Analysis plugin detects wrong dependency scopes, including `api` vs `implementation` and `implementation` vs `runtimeOnly`.
- It identifies unused dependencies that can be safely removed, and missing direct declarations that should be added to avoid transitive dependency issues.
- Running the plugin's analysis tasks produces reports suggesting changes to shrink compile classpaths and improve build isolation.
- The plugin can be configured to suit project needs, and supports custom post-processing tasks for tailored analysis output.
- Clean compile classpaths enforce module boundaries and reduce compile overhead in multi-module Gradle builds.