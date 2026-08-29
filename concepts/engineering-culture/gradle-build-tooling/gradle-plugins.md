---
domain: engineering-culture
subdomain: gradle-build-tooling
concept: gradle-plugins
title: Understanding Gradle #03 – Plugins
sources:
  - title: "Understanding Gradle #03 – Plugins"
    url: "https://www.youtube.com/watch?v=N95YI-szd78"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:48:29+00:00"
---

# Understanding Gradle #03 – Plugins

Plugins are a central concept in Gradle for keeping projects well structured and maintainable. According to [Understanding Gradle #03 – Plugins](https://www.youtube.com/watch?v=N95YI-szd78), there are different kinds of plugins, including script plugins, binary plugins, and convention plugins. The video demonstrates how to use plugins in an example project and emphasizes reusing build configuration through convention plugins to avoid duplication across subprojects.

A recommended approach is to create a separate build logic build to hold convention plugins. Using the `kotlin-dsl` plugin allows writing these convention plugins in a type-safe Kotlin DSL. Community plugins can be declared as dependencies via the plugin portal and then applied. The example shows how to write a convention plugin in Kotlin DSL and apply it to all subprojects, making the overall build configuration more consistent and maintainable.

- Plugins are the most important concept for structuring and maintaining Gradle projects.
- Different plugin types exist: script, binary, and convention plugins.
- Convention plugins enable reuse of build configuration across subprojects, reducing duplication.
- A separate build logic build with the kotlin-dsl plugin provides type-safe convention plugins.
- Community plugins are declared as dependencies and applied via the plugins DSL.