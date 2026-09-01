---
domain: android-kotlin
subdomain: gradle
concept: convention-plugins
title: Understanding Gradle #03 – Plugins
sources:
  - title: "Understanding Gradle #03 – Plugins"
    url: "https://www.youtube.com/watch?v=N95YI-szd78"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15"
---

# Understanding Gradle #03 – Plugins

This video explains the central role of plugins in Gradle for keeping projects well structured and maintainable. It introduces different kinds of plugins and demonstrates how to use them in a build, emphasizing the importance of reusing build configuration through convention plugins. The presenter shows how to create a separate build logic build (like buildSrc), apply the 'kotlin-dsl' plugin, and declare dependencies on community plugins from the Gradle Plugin Portal. Convention plugins written in Kotlin DSL can then be applied to all subprojects, promoting consistency and reducing duplication. The example is available on GitHub, and the video references official Gradle documentation for further reading on the Plugins DSL, Plugin Portal, and defining convention plugins.

- Gradle plugins are essential for extending and sharing build logic across projects.
- Convention plugins allow reuse of build configuration, making multi-project builds cleaner.
- Create a separate build logic build (e.g., buildSrc) and use the kotlin-dsl plugin to write convention plugins in Kotlin DSL.
- Use the Plugins DSL to declare community plugin dependencies from the Gradle Plugin Portal.
- Apply convention plugins to all subprojects to maintain consistency and reduce duplication.