---
domain: engineering-culture
subdomain: build-tools
concept: gradle-dsl
title: Kotlin DSL and Groovy DSL in Gradle
sources:
  - title: "Understanding Gradle #24 – Kotlin DSL and Groovy DSL"
    url: "https://www.youtube.com/watch?v=pKsn2eZWQK0"
    author: "Jendrik Johannes"
    date: "2022-10-04"
---

# Kotlin DSL and Groovy DSL in Gradle

The video explains how Gradle's Kotlin DSL and Groovy DSL are both implemented as extensions over the Gradle Java API, specifically the org.gradle.api.Project interface. A Gradle build file is essentially a script that configures an instance of Project, and the DSLs provide a more convenient syntax for interacting with this API.

The Kotlin DSL uses typed lambda receivers, giving strong type safety and better IDE assistance. In contrast, the Groovy DSL is dynamic and leverages Groovy's flexible syntax, such as omitting parentheses for method calls, using single or double quotes for strings, and allowing direct assignment to Gradle properties. The author demonstrates switching a project from Kotlin DSL to Groovy DSL, showing practical differences in convention plugins, task configuration, and property assignment.

- Both Kotlin and Groovy DSLs are thin wrappers over Gradle's Java API, with Project as the central type.
- Kotlin DSL is statically typed and offers type safety and IDE autocompletion.
- Groovy DSL is dynamically typed and more concise due to Groovy's syntax flexibility.
- Groovy-specific syntax includes method calls without parentheses, flexible string notation, and direct property assignment.
- Task configuration and Gradle property handling differ between the two DSLs, with Groovy allowing more implicit syntax.