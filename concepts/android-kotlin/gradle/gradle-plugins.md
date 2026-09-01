---
domain: android-kotlin
subdomain: gradle
concept: gradle-plugins
title: Understanding Gradle #03 – Plugins
sources:
  - title: "Understanding Gradle #03 – Plugins"
    url: "https://www.youtube.com/watch?v=N95YI-szd78"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15"
---

# Understanding Gradle #03 – Plugins

This video explains Gradle plugins as the most important concept for keeping projects well-structured and maintainable. It introduces different kinds of plugins and demonstrates how to use them in a project, emphasizing the reuse of build configuration through convention plugins. A separate build logic build is created using the kotlin-dsl plugin, and a community plugin is declared as a dependency. The presenter writes a convention plugin in Kotlin DSL and applies it to all subprojects, showing how to centralize and share build logic effectively (onepiece.Software, 2021).

- Plugins are the core mechanism for structuring Gradle builds and reusing configuration.
- Convention plugins allow sharing build logic across projects and subprojects.
- A separate build logic build can be created using the kotlin-dsl plugin.
- Community plugins are declared as dependencies in the plugin management block.
- Writing convention plugins in Kotlin DSL provides type-safe, maintainable build code.