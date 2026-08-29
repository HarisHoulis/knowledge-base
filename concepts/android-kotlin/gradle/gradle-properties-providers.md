---
domain: android-kotlin
subdomain: gradle
concept: gradle-properties-providers
title: Understanding Gradle #34 – Properties and Providers
sources:
  - title: "Understanding Gradle #34 – Properties and Providers"
    url: "https://www.youtube.com/watch?v=n8Tgr4aLB18"
    author: "Jendrik Johannes"
    date: "2023-08-31T04:56:30+00:00"
---

# Understanding Gradle #34 – Properties and Providers

This video explains Gradle's Property and Provider abstractions, which enable lazy configuration and avoid eagerly reading values at configuration time. Properties are mutable holders for typed values (e.g., DirectoryProperty) used in tasks and extensions, while Providers are read-only sources that can be derived from properties or other providers. Using these abstractions decouples task configuration from execution, improving performance and flexibility.

The video demonstrates practical usage: defining a DirectoryProperty as a task input, accessing extension properties via Property instead of raw fields, and composing providers with map() and flatMap() to transform or chain values. It also highlights provider-friendly Gradle APIs, optional providers (without values), and how to access provider values during configuration when needed. FileCollections and the list of supported property types are covered, emphasizing Gradle's built-in support for common types.

In summary, Properties and Providers are central to Gradle's lazy configuration model. They allow tasks to configure outputs based on inputs that may not be finalized yet, and they make build logic more robust and maintainable.

- Properties are mutable typed containers (e.g., DirectoryProperty) for lazy configuration in tasks and extensions.
- Providers are read-only, derivable sources of values, supporting transformations like map() and flatMap().
- Using Properties instead of fields avoids eager resolution and enables Gradle to track task inputs/outputs correctly.
- Provider-friendly APIs in Gradle accept Provider directly, simplifying wiring of values.
- Supported property types include common types like Directory, RegularFile, and List/Map properties.