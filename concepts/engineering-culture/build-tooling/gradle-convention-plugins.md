---
domain: engineering-culture
subdomain: build-tooling
concept: gradle-convention-plugins
title: Understanding Gradle #03 – Plugins
sources:
  - title: "Understanding Gradle #03 – Plugins"
    url: "https://www.youtube.com/watch?v=N95YI-szd78"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:48:29+00:00"
---

# Understanding Gradle #03 – Plugins

This video explains the importance of Gradle plugins for structuring and maintaining projects. It distinguishes different kinds of plugins, such as script plugins, binary plugins, and convention plugins, with the latter being key to reusing build configuration across subprojects. The presenter demonstrates how to create a separate 'build logic' build using the 'kotlin-dsl' plugin to write convention plugins in Kotlin DSL, and then apply them to all subprojects via the plugins block. Community plugins can also be declared as dependencies and applied in the same way. The approach helps avoid duplication and keeps build files clean and maintainable.

- Plugins are central to structuring Gradle builds and reusing configuration.
- Convention plugins allow encapsulating and sharing build logic across subprojects.
- A separate build logic build, using the 'kotlin-dsl' plugin, enables writing convention plugins in Kotlin DSL.
- Community plugins are declared as dependencies and applied via the plugins DSL.
- Applying convention plugins to all subprojects simplifies build scripts and improves maintainability.