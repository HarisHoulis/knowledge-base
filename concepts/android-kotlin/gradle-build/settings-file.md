---
domain: android-kotlin
subdomain: gradle-build
concept: settings-file
title: Understanding Gradle #01 – The Settings File
sources:
  - title: "Understanding Gradle #01 – The Settings File"
    url: "https://www.youtube.com/watch?v=Ajs8pTbg8as"
    author: "Jendrik Johannes"
    date: "2021-08-15T18:25:02+00:00"
---

# Understanding Gradle #01 – The Settings File

The settings file is the entry point of every Gradle project, as explained in this first instalment of the Understanding Gradle series by Jendrik Johannes. It is where you name your Gradle build, configure repositories for libraries and plugins, and define the overall structure of the build, including subprojects and included builds (composite builds). The video demonstrates starting a Gradle project from scratch, showing how to declare repositories centrally and set up custom plugin repositories.

The settings file also supports script code and settings plugins, allowing for more advanced build logic. The presenter emphasizes that the settings file is the first thing Gradle looks at, making it a crucial concept for anyone working with Gradle builds. The video provides a summary and links to further reading, including official Gradle documentation on repository declaration, plugin repositories, composite builds, and multi-project builds.

- The settings file is the entry point for every Gradle project and is used to name the build and configure repositories.
- It defines the build structure, including subprojects and included builds via composite builds.
- Settings plugins and script code can be used in the settings file for advanced customization.
- Centralized repository declaration and custom plugin repositories can be managed from the settings file.