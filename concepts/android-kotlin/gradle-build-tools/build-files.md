---
domain: android-kotlin
subdomain: gradle-build-tools
concept: build-files
title: Understanding Gradle #02 – The Build Files
sources:
  - title: "Understanding Gradle #02 – The Build Files"
    url: "https://www.youtube.com/watch?v=OKjE_Lt_66U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:38:32+00:00"
---

# Understanding Gradle #02 – The Build Files

In this video, Jendrik Johannes explains the role of build files in Gradle, which are the central configuration scripts for any project. An empty build file can be added to each subproject, but it only becomes useful when a plugin is applied. Plugins give the subproject meaning by adding tasks and conventions, such as the Java plugin which makes it a Java project. (Johannes, 2021)

Plugin behavior is further refined through extensions. For instance, the Java extension allows configuring properties like source compatibility. Additionally, the dependencies block is where project dependencies are declared, covering both external components and inter-subproject dependencies. This structure makes build files the primary place for configuring and customizing Gradle builds. (Johannes, 2021)

- Build files are the central configuration scripts for Gradle projects.
- Each subproject can have an empty build file; it gains purpose only when a plugin is applied.
- Plugins add tasks and conventions, e.g., the Java plugin turns a subproject into a Java project.
- Plugin behavior is configured through extensions (e.g., the java extension).
- Dependencies are declared in the dependencies block, covering both external components and between subprojects.