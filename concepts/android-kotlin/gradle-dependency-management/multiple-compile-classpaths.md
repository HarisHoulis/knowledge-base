---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: multiple-compile-classpaths
title: Understanding Gradle #27 – Multiple Compile Classpaths
sources:
  - title: "Understanding Gradle #27 – Multiple Compile Classpaths"
    url: "https://www.youtube.com/watch?v=Z5n9VK3sOnI"
    author: "Jendrik Johannes"
    date: "2022-12-05"
---

# Understanding Gradle #27 – Multiple Compile Classpaths

This video explains how Gradle handles multiple compile classpaths in Java projects with multiple components. It demonstrates that each component has its own compile classpath, which includes only the artifacts necessary for compilation, rather than all transitive dependencies. This is achieved through dependency scopes that control what is exposed to consumers at compile time and runtime.

The video introduces the 'api' scope, which makes dependencies available to consumers on their compile classpath, in contrast to 'implementation' dependencies that remain internal. It highlights that using 'api' can have side effects, such as forcing all consumers to recompile when the API dependency changes. The key takeaway is that Gradle reduces compile classpaths to improve build times and avoid unnecessary coupling, while still ensuring runtime behavior is correct.

- Gradle separates compile classpaths from runtime classpaths, allowing each component to compile against only the dependencies it directly needs.
- Transitive dependencies are not automatically visible at compile time; they must be declared as 'api' to be exposed to consumers.
- Using 'api' has a side effect: any change to the API dependency triggers recompilation of all consuming components.
- The 'implementation' scope hides dependencies, reducing the compile classpath and improving encapsulation.
- Understanding dependency scopes is essential for managing multi-module Gradle builds efficiently.