---
domain: android-kotlin
subdomain: gradle-build
concept: lazy-configuration
title: Understanding Gradle #34 – Properties and Providers
sources:
  - title: "Understanding Gradle #34 – Properties and Providers"
    url: "https://www.youtube.com/watch?v=n8Tgr4aLB18"
    author: "Jendrik Johannes (onepiece.Software)"
    date: "2023-08-31T04:56:30+00:00"
---

# Understanding Gradle #34 – Properties and Providers

This video explains Gradle's Property and Provider abstractions, which support lazy configuration. Properties replace plain fields in custom Gradle types, such as using DirectoryProperty for a task input instead of a File. This ensures the value is only resolved when the task executes, avoiding premature configuration-time evaluation. Extensions should expose properties rather than fields so values can be assigned lazily and tracked by Gradle.

- Property types like DirectoryProperty and RegularFileProperty delay value resolution until task execution.
- Providers are lazily computed values; map and flatMap allow transformations without eager evaluation.
- Gradle APIs accept providers directly for task inputs/outputs, avoiding configuration-time provider access.
- Supported property types include RegularFileProperty, DirectoryProperty, ListProperty, MapProperty, and more.