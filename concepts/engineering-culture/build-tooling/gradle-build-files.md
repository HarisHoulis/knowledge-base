---
domain: engineering-culture
subdomain: build-tooling
concept: gradle-build-files
title: Understanding Gradle #02 – The Build Files
sources:
  - title: "Understanding Gradle #02 – The Build Files"
    url: "https://www.youtube.com/watch?v=OKjE_Lt_66U"
    author: "Jendrik Johannes"
    date: "2021-08-15T18:38:32+00:00"
---

# Understanding Gradle #02 – The Build Files

In this video, Jendrik Johannes explains the purpose and structure of Gradle build files, which are the central configuration scripts in a Gradle project. The key idea is that every subproject should have an empty build file to start, and meaning is added incrementally through plugins, extensions, and dependencies (Jendrik Johannes, 2021).

A build file gains meaning when a plugin is applied, such as the 'java' plugin, which gives the subproject standard tasks and conventions. Plugin-specific details are then configured through an extension, like the 'java' extension, allowing customization of source compatibility or other options. Dependencies are declared separately, either between subprojects or as external components, to define the project's classpath and module relationships (Jendrik Johannes, 2021).

The video emphasizes a clean and modular build setup: keep build files minimal, apply plugins for behavior, use extensions for configuration, and declare dependencies explicitly. This approach makes builds easier to understand and maintain, especially in multi-project builds (Jendrik Johannes, 2021).

- Each subproject should start with an empty build file; meaning is added by applying plugins.
- Plugins provide default tasks and conventions; extensions allow fine-grained configuration of plugin behavior.
- Dependencies are declared explicitly, either between subprojects or as external components, to define the project's relationships.
- Keeping build files minimal and focused improves maintainability and readability.