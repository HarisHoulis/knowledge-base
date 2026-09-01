---
domain: android-kotlin
subdomain: gradle-build-settings
concept: settings-plugins
title: Understanding Gradle #14 – Settings Plugins
sources:
  - title: "Understanding Gradle #14 – Settings Plugins"
    url: "https://www.youtube.com/watch?v=tlx3tzuLSWk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-13T15:19:13+00:00"
---

# Understanding Gradle #14 – Settings Plugins

In this video, Jendrik Johannes explains how to create and use settings convention plugins to avoid repetition across multiple Gradle builds. The settings file is the entry point for every build and defines repositories, included builds, and project structure. In large multi-project or multi-repository setups, settings files often repeat the same logic. By extracting that logic into a settings plugin, you centralize the conventions.

A settings plugin is defined similarly to a project plugin, but uses the `settings.gradle.kts` extension instead of `build.gradle.kts`. It can contain script code equivalent to a normal settings file. For example, you can dynamically detect and include sub-projects or other builds from the parent folder. The plugin can then be applied in any build's settings file, along with an include of the build logic project where the plugin resides.

The video demonstrates a practical example where two projects share settings logic. Using a settings plugin reduces duplication and enforces a consistent structure. This mechanism is especially useful for larger software projects split into multiple builds within a monorepo or distributed across repositories. It also allows centralized control over repositories and included builds.

- Settings plugins are convention plugins applied to the settings file, not the build file.
- They are created with a file named `settings.gradle.kts` and applied with `apply(plugin = ...)` in the settings script.
- Settings plugins can define repositories, included builds, and project structure programmatically.
- Allows centralizing build conventions and reducing duplication across multiple projects.
- Useful for enforcing architecture in monorepos or multi-repository setups.