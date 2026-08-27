---
domain: android-kotlin
subdomain: gradle-dsl
concept: kotlin-vs-groovy-dsl
title: Understanding Gradle #24 – Kotlin DSL and Groovy DSL
sources:
  - title: "Understanding Gradle #24 – Kotlin DSL and Groovy DSL"
    url: "https://www.youtube.com/watch?v=pKsn2eZWQK0"
    author: "Jendrik Johannes"
    date: "2022-10-04T12:17:24+00:00"
---

# Understanding Gradle #24 – Kotlin DSL and Groovy DSL

In the video 'Understanding Gradle #24 – Kotlin DSL and Groovy DSL', Jendrik Johannes explains that both Gradle DSLs are layers on top of Gradle's Java API, centered around the `org.gradle.api.Project` interface. The Kotlin DSL is a type-safe and expressive language built with Kotlin lambdas, providing better IDE support and compile-time validation. The Groovy DSL leverages Groovy's dynamic method dispatch and closures, allowing more concise and flexible syntax but with less safety.

Key differences highlighted include method call syntax, string handling, and property assignment. In Groovy, method parentheses are optional and strings can be single-quoted or GStrings, making scripts shorter. Kotlin requires explicit parentheses and uses `=` or `set()` for property assignment. Task configuration also differs: Groovy uses closures with delegate, while Kotlin uses typed lambdas with receiver. The video suggests that while Groovy offers flexibility, Kotlin DSL is the modern default for new Gradle builds.

The choice between Kotlin DSL and Groovy DSL depends on project needs and team preferences, but the video emphasizes that understanding the underlying Java API is crucial for effectively using either DSL.

- Both Kotlin and Groovy DSLs wrap the same Java API, with `Project` as the main entry point.
- Kotlin DSL is type-safe, giving compile-time checks and great IDE support.
- Groovy DSL is more flexible but less safe, with features like parentheses-free method calls and dynamic strings.
- Kotlin DSL is recommended for new Gradle builds, but Groovy DSL remains a valid choice for legacy or scripting-style projects.