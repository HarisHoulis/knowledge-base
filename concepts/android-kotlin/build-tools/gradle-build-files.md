---
domain: android-kotlin
subdomain: build-tools
concept: gradle-build-files
title: Understanding Gradle #02 – The Build Files
sources:
  - title: "Understanding Gradle #02 – The Build Files"
    url: "https://www.youtube.com/watch?v=OKjE_Lt_66U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:38:32+00:00"
---

# Understanding Gradle #02 – The Build Files

This video explains the role of Gradle build files as the central configuration scripts for a project. Each subproject should have its own build file, even if initially empty, to establish its identity within the build. Adding a build file gives Gradle a place to define what the subproject does and how it integrates with the overall build.

To give a subproject meaning, a plugin is applied via the build file. Plugins introduce tasks and conventions. After applying a plugin, its behavior can be customized through plugin-specific extensions, allowing fine-grained configuration. Dependencies between subprojects and external components are also declared in these build files, which is essential for managing multi-project builds.

The video emphasizes that build files are not arbitrary script files but structured configuration that should be kept minimal and declarative, focusing on 'what' the project needs rather than 'how' Gradle executes it.

- Every subproject should have its own Gradle build file, even if empty, to define its role.
- Applying a plugin gives a subproject its meaning and built-in functionality.
- Plugin extensions allow customizing the plugin's behavior in the build file.
- Build files are where dependencies between subprojects and external components are declared.