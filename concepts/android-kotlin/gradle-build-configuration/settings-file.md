---
domain: android-kotlin
subdomain: gradle-build-configuration
concept: settings-file
title: Understanding Gradle #01 – The Settings File
sources:
  - title: "Understanding Gradle #01 – The Settings File"
    url: "https://www.youtube.com/watch?v=Ajs8pTbg8as"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:25:02+00:00"
---

# Understanding Gradle #01 – The Settings File

The settings file is the entry point of every Gradle project, defining the build's name and configuring how Gradle locates dependencies and plugins. It is where you declare repositories for libraries and plugin portals, either globally or per build, and it sets the overall structure of the build by including subprojects or other builds. The settings file also supports applying settings plugins and executing arbitrary script code to customize build behavior. This foundational file is distinct from build files, which focus on tasks and project configurations. The video demonstrates starting a Gradle project from scratch, emphasizing that the settings file is evaluated first and controls the entire build's scope.

- The settings file is the first file Gradle reads and defines the build's identity and structure.
- Repositories for dependencies and plugins can be declared centrally in the settings file.
- Subprojects and composite builds are included from the settings file.
- Settings plugins can be applied to extend build logic.
- The settings file can contain arbitrary Groovy or Kotlin script code for advanced setup.