---
domain: android-kotlin
subdomain: gradle-build-scripts
concept: kotlin-vs-groovy-dsl
title: Understanding Gradle #24 – Kotlin DSL and Groovy DSL
sources:
  - title: "Understanding Gradle #24 – Kotlin DSL and Groovy DSL"
    url: "https://www.youtube.com/watch?v=pKsn2eZWQK0"
    author: "Jendrik Johannes"
    date: "2022-10-04T12:17:24+00:00"
---

# Understanding Gradle #24 – Kotlin DSL and Groovy DSL

The video explains that Gradle's build scripts are built on the Java API, with `org.gradle.api.Project` as the central interface. Both the Kotlin DSL and Groovy DSL are language-specific extensions of this API, allowing developers to configure projects and tasks in a syntax that fits the respective language (Jendrik Johannes, 2022). The Kotlin DSL provides type safety and static analysis, making it easier to catch errors at build-script compilation time, while the Groovy DSL leverages Groovy's dynamic features for a more concise and flexible syntax (Jendrik Johannes, 2022). The video demonstrates switching between `build.gradle.kts` and `build.gradle`, highlighting Groovy-specific conventions such as method calls without parentheses, special string notation, referencing types, configuring tasks via closures, and property assignment (Jendrik Johannes, 2022). Overall, both DSLs interoperate with the same Gradle API, and the choice between them often depends on the team's preference for type safety versus brevity.

- Gradle's DSLs are expressions over the Java API, with `org.gradle.api.Project` as the primary entry point.
- Kotlin DSL is type-safe and statically checked, while Groovy DSL is dynamic and allows more concise code.
- Groovy DSL allows method calls without parentheses, special string literals, and direct type references.
- Task configuration differs: Groovy uses closures, Kotlin uses typed lambdas.
- Build scripts can be written in either DSL, and switching between them is straightforward for simple projects.