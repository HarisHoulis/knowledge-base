---
domain: android-kotlin
subdomain: gradle
concept: settings-plugins
title: Understanding Gradle #14 – Settings Plugins
sources:
  - title: "Understanding Gradle #14 – Settings Plugins"
    url: "https://www.youtube.com/watch?v=tlx3tzuLSWk"
    author: "Jendrik Johannes"
    date: "2021-12-13"
---

# Understanding Gradle #14 – Settings Plugins

Settings plugins allow you to avoid repetition in Gradle settings files across multiple builds or repositories. In large software projects, settings files often need to define repositories, included builds, and project structure repeatedly; a settings plugin centralizes this logic in a single place, similar to how convention plugins work for build files (Johannes, 2021).

A settings plugin is created just like a project plugin, but lives in a subproject with a `settings.gradle.kts` file instead of `build.gradle.kts`. Inside this file, you can write arbitrary settings logic, such as dynamically discovering and including all Gradle builds in a parent folder or including all subprojects that contain a build script. This makes the plugin generic and reusable across different components (Johannes, 2021).

To use the settings plugin, you include the build logic in your settings file (or publish the plugin) and then apply the plugin. This reduces the settings file to just those two steps. Settings plugins are particularly useful in multi-repo or monorepo setups to enforce a uniform architecture, control which repositories are used for dependency resolution, and determine where Gradle locates other builds (Johannes, 2021).

- Settings plugins centralize settings logic, avoiding duplication across multiple Gradle builds.
- They are implemented as a subproject with a settings.gradle.kts file instead of a build.gradle.kts.
- The plugin can dynamically include builds or subprojects by scanning directories for build scripts.
- Applying a settings plugin requires including the build logic and adding the plugin to the settings file.
- Settings plugins help enforce consistent structure and repository configuration across large multi-build projects.