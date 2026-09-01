---
domain: android-kotlin
subdomain: gradle
concept: gradle-build-files
title: Understanding Gradle #02 – The Build Files
sources:
  - title: "Understanding Gradle #02 – The Build Files"
    url: "https://www.youtube.com/watch?v=OKjE_Lt_66U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:38:32+00:00"
---

# Understanding Gradle #02 – The Build Files

In the video, Jendrik Johannes explains the purpose of Gradle build files: they are the central configuration scripts for a project. A build file can be added to each subproject, and its role is to define what that subproject does and how it is built. Without a build file, a subproject has no meaning to Gradle; adding an empty build file is the first step to include it in the build.

To give a subproject meaning, a plugin is applied. For example, applying the 'java' plugin makes the subproject a Java project, enabling standard Java build tasks. Plugins come with extensions that allow fine-grained configuration; for instance, the 'java' extension lets you set source compatibility or other project-specific details. The video emphasizes that extensions are the primary way to customize plugin behavior.

Finally, build files are where dependencies are declared. Gradle supports declaring dependencies between subprojects and on external components (libraries). This is essential for multi-project builds, as it defines the relationships and external resources needed to compile and run the code. The video summarizes that build files serve three main purposes: applying plugins, configuring them, and declaring dependencies.

- Build files are the central configuration scripts for Gradle projects.
- Applying a plugin (e.g., 'java') gives a subproject its build meaning.
- Plugins are configured through dedicated extensions.
- Dependencies (between subprojects or external components) are declared in build files.