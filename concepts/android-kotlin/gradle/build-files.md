---
domain: android-kotlin
subdomain: gradle
concept: build-files
title: Understanding Gradle #02 – The Build Files
sources:
  - title: "Understanding Gradle #02 – The Build Files"
    url: "https://www.youtube.com/watch?v=OKjE_Lt_66U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-15T18:38:32+00:00"
---

# Understanding Gradle #02 – The Build Files

In this video, Jendrik Johannes explains the purpose of Gradle build files (e.g., build.gradle). He recommends adding an empty build file to each subproject, then giving it meaning by applying a plugin to introduce tasks and conventions. Plugins are configured via extensions, such as the 'java' extension, allowing fine-grained control without writing custom logic. Dependencies are declared directly in the build file, including dependencies on other subprojects and external components, making the build script a concise declarative specification.

The key insight is that build files should be simple and declarative, not procedural. By applying plugins and configuring extensions, you avoid scripting logic and keep the build maintainable. The video also points to related resources on plugins and dependency declaration for deeper understanding.

- Each subproject should have a build file to be part of the Gradle build.
- Plugins are applied to give a subproject meaning, adding tasks and conventions.
- Extensions allow configuring plugin behavior without writing custom code.
- Dependencies between subprojects and on external components are declared in the build file.
- Build files should be declarative and free of custom logic.