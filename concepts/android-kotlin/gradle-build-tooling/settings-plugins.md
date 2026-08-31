---
domain: android-kotlin
subdomain: gradle-build-tooling
concept: settings-plugins
title: Understanding Gradle #14 – Settings Plugins
sources:
  - title: "Understanding Gradle #14 – Settings Plugins"
    url: "https://www.youtube.com/watch?v=tlx3tzuLSWk"
    author: "Jendrik Johannes"
    date: "2021-12-13"
---

# Understanding Gradle #14 – Settings Plugins

Gradle settings files are the entry point for every build, defining repositories, included builds, and project structure. In multi-build or multi-repository setups, these settings can become repetitive across projects. To solve this, Jendrik Johannes introduces settings plugins: convention plugins applied to settings files, defined with a `.settings.gradle.kts` extension (Johannes, 2021, "Understanding Gradle #14 – Settings Plugins").

A settings convention plugin contains script code just like a regular settings file. In the example, the plugin defines a loop that dynamically includes all Gradle builds in the parent folder and all subprojects with `build.gradle.kts` files, making the convention generic. Then each project's settings file only needs to include the build-logic build and apply the settings plugin.

Settings plugins are powerful for large software projects: they can enforce a standard structure or architecture, control which repositories are used for dependency publishing, and specify where Gradle finds other builds—all from a central place.

- Settings plugins are convention plugins for settings files, defined with a `.settings.gradle.kts` extension.
- They reduce repetition in Gradle settings across multiple builds or repositories.
- Settings plugins can dynamically detect and include component builds or subprojects.
- To use a local settings plugin, include the build-logic build and apply the plugin in each settings file.
- They provide a central mechanism to enforce architecture, repository usage, and build structure in large projects.