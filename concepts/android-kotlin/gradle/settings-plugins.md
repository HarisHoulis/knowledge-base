---
domain: android-kotlin
subdomain: gradle
concept: settings-plugins
title: Understanding Gradle #14 – Settings Plugins
sources:
  - title: "Understanding Gradle #14 – Settings Plugins"
    url: "https://www.youtube.com/watch?v=tlx3tzuLSWk"
    author: "Jendrik Johannes"
    date: "2021-12-13T15:19:13+00:00"
---

# Understanding Gradle #14 – Settings Plugins

This video explains how to create and use settings plugins in Gradle to avoid repetition across multiple builds. Just as convention plugins are used for build files, settings plugins allow centralizing settings logic such as repository declarations, included builds, and project structure rules. The presenter demonstrates converting a repetitive settings file into a reusable plugin called 'myprojectstructure.settings', where code like dynamic detection of sibling builds and automatic inclusion of subprojects is placed.

- Settings plugins centralize settings file logic, similar to convention plugins for build files.
- Define a settings plugin by creating a file like 'myprojectstructure.settings.gradle.kts' in a build logic subproject.
- Settings plugins can dynamically include sibling builds and subprojects, reducing manual configuration.
- Using a settings plugin requires including the build logic project and applying the plugin in each build's settings file.
- This mechanism is valuable for enforcing structure in large multi-build projects.