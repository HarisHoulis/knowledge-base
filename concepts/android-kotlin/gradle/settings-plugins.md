---
domain: android-kotlin
subdomain: gradle
concept: settings-plugins
title: Understanding Gradle #14 – Settings Plugins
sources:
  - title: "Understanding Gradle #14 – Settings Plugins"
    url: "https://www.youtube.com/watch?v=tlx3tzuLSWk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-13T15:19:13+00:00"
---

# Understanding Gradle #14 – Settings Plugins

This video explains how to create and use settings plugins in Gradle to avoid repetition in settings files across multiple builds. Settings plugins are analogous to convention plugins for build files, but instead they encapsulate logic for the settings file, which is the entry point of every Gradle build. The settings file typically defines repositories, included builds, and the structure of the project. By moving this logic into a settings plugin, teams can centralize and enforce consistent build setup across multiple projects, whether in a monorepo or a multi-repository setup. (Source: Understanding Gradle #14 – Settings Plugins, 2021)

The example demonstrates creating a settings plugin in a separate build logic subproject. The plugin file uses a .settings.gradle.kts extension and contains script code that can be made generic—for instance, dynamically discovering and including all Gradle builds in a parent folder or all subprojects with a build.gradle.kts file. To apply the plugin, the settings file first includes the build logic build and then applies the plugin. This approach reduces duplication and makes it easy to impose architectural conventions across many builds. (Source: Understanding Gradle #14 – Settings Plugins, 2021)

Settings plugins are a powerful mechanism for scaling build configuration. They allow you to control which repositories are used, where to find other builds, and what project structure to expect, all from a central place. The video concludes the first season of the 'Understanding Gradle' series, encouraging viewers to suggest topics for future videos. (Source: Understanding Gradle #14 – Settings Plugins, 2021)

- Settings plugins reuse settings-file configuration across multiple Gradle builds.
- A settings plugin is defined with a .settings.gradle.kts extension in a build logic project.
- Plugins can dynamically include other builds or subprojects, reducing repetitive manual configuration.
- Settings plugins provide a central place to enforce repository, build inclusion, and project structure conventions.
- To use a settings plugin, the settings file must first include its build logic build and then apply the plugin.