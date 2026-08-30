---
domain: android-kotlin
subdomain: gradle
concept: settings-file
title: Understanding Gradle #01 – The Settings File
sources:
  - title: "Understanding Gradle #01 – The Settings File"
    url: "https://www.youtube.com/watch?v=Ajs8pTbg8as"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:25:02+00:00"
---

# Understanding Gradle #01 – The Settings File

The settings file is the entry point of every Gradle project. It defines the build's name, configures repositories for both dependencies and plugins, and establishes the overall project structure, including subprojects and composite builds. Without it, Gradle cannot determine what to build or where to fetch dependencies from (Jendrik, 2021).

The video demonstrates starting a Gradle project from scratch, emphasizing that the settings file contains script code that runs during configuration. It also highlights the role of settings plugins, which can be applied early to influence the build setup. By centralizing repository declarations and project layout, the settings file provides a foundation for scalable multi-project builds (Jendrik, 2021).

- The settings file names the Gradle build and is required for every project.
- It declares repositories for external libraries and for Gradle plugins separately.
- It defines the structure of the build, including subprojects and included builds (composite builds).
- The settings file can contain arbitrary script code and apply settings plugins to customize the build environment.