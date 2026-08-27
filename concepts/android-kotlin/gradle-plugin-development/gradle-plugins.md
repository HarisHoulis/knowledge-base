---
domain: android-kotlin
subdomain: gradle-plugin-development
concept: gradle-plugins
title: Understanding Gradle #03 – Plugins
sources:
  - title: "Understanding Gradle #03 – Plugins"
    url: "https://www.youtube.com/watch?v=N95YI-szd78"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:48:29+00:00"
---

# Understanding Gradle #03 – Plugins

In this video, Jendrik Johannes explains Gradle plugins, emphasizing them as the most important concept for keeping projects well-structured and maintainable. He distinguishes different kinds of plugins and demonstrates how to apply them in a build, including community plugins and convention plugins for reusing build configuration across projects (Johannes, 2021).

The tutorial walks through creating a separate build logic build using the `kotlin-dsl` plugin, declaring dependencies on community plugins, and writing custom convention plugins in Kotlin DSL. The convention plugins can then be applied to all subprojects, centralizing and standardizing build logic (Johannes, 2021).

- Plugins are key to structuring Gradle builds and reusing configuration.
- There are different plugin types: community plugins, core plugins, and convention plugins.
- Convention plugins allow sharing build logic across projects via a separate build logic build.
- The `kotlin-dsl` plugin enables writing convention plugins in Kotlin DSL.
- Applying convention plugins to all subprojects keeps builds consistent and maintainable.