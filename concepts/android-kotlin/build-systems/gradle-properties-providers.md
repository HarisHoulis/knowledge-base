---
domain: android-kotlin
subdomain: build-systems
concept: gradle-properties-providers
title: Understanding Gradle #34 – Properties and Providers
sources:
  - title: "Understanding Gradle #34 – Properties and Providers"
    url: "https://www.youtube.com/watch?v=n8Tgr4aLB18"
    author: "Jendrik Johannes (onepiece.Software)"
    date: "2023-08-31"
---

# Understanding Gradle #34 – Properties and Providers

In the video "Understanding Gradle #34 – Properties and Providers" by Jendrik Johannes (2023), the concepts of Property and Provider in Gradle are introduced as a way to achieve lazy configuration. Properties are typed containers that hold values but defer real-time resolution until they are actually needed, making build scripts more efficient and avoiding unnecessary work during configuration time. The video uses a concrete example with a DirectoryProperty as a task input, showing why using a Property instead of a plain field is beneficial when wiring extensions to tasks.

The video also explains Providers, which are read-only views over values that can be transformed using map{} and flatMap{}. These transformations allow values to be derived from other providers in a lazy manner, ensuring that computations only happen when the final value is queried. Additionally, the video covers provider-friendly Gradle APIs, optional providers without values, and the importance of avoiding direct access during configuration. It also touches on dealing with FileCollections and lists the supported property types, culminating in a summary of best practices for using lazy configuration in Gradle builds.

- Properties and Providers enable lazy configuration, deferring value resolution until task execution time.
- Use DirectoryProperty (or other Property types) for task inputs instead of plain fields to support configuration avoidance and flexibility.
- Providers support map{} and flatMap{} for lazy transformation of values, allowing derived configuration to stay lazy.
- Avoid accessing provider values during configuration time; use provider-friendly APIs like FileCollections to maintain laziness.
- Gradle supports various Property types (e.g., DirectoryProperty, RegularFileProperty, ListProperty, MapProperty) to model build configuration.