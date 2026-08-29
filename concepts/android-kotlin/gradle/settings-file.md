---
domain: android-kotlin
subdomain: gradle
concept: settings-file
title: Understanding Gradle #01 – The Settings File
sources:
  - title: "Understanding Gradle #01 – The Settings File"
    url: "https://www.youtube.com/watch?v=Ajs8pTbg8as"
    author: "Jendrik Johannes"
    date: "2021-08-15T18:25:02+00:00"
---

# Understanding Gradle #01 – The Settings File

The settings file is the entry point of every Gradle project. It is the first file Gradle reads when starting a build, and it defines the name of the build, configures repositories for dependencies and plugins, and specifies the project structure including subprojects and included builds. According to the video, the settings file can also apply settings plugins, which can influence the build configuration process itself. The file is written as an executable script, allowing arbitrary code to control the build setup.

- The settings file is mandatory for every Gradle build and serves as the entry point.
- It declares repositories for libraries and plugin repositories, as well as locations for other builds (composite builds).
- It defines the structure of the build, including subprojects and included builds.
- Settings plugins can be applied in the settings file to customize the build configuration.
- The settings file contains script code, making it highly flexible.