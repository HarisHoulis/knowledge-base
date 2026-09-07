---
domain: java-tools
subdomain: code-generation
concept: kotlin-poet
title: Generating Kotlin code with KotlinPoet
sources:
  - title: "Generating Kotlin code with KotlinPoet"
    url: "https://developer.squareup.com/blog/generating-kotlin-code-with-kotlinpoet/"
---

# Generating Kotlin code with KotlinPoet

The article introduces KotlinPoet, Square's library for generating Kotlin source code. It explains the motivation: existing code generation tools like Dagger, Butter Knife, and Wire generate Java code, which can feel foreign to Kotlin consumers and lack Kotlin-specific features. KotlinPoet builds on the success of JavaPoet, providing an immutable builder-based model for creating Kotlin files, classes, properties, and functions.

A concrete example demonstrates generating a simple Greeter class and a main function, illustrating KotlinPoet's API and the resulting Kotlin code. The article highlights that generating Kotlin rather than Java has a key advantage: Kotlin supports JavaScript and native compilation targets, so the same generated code can be used across multiple platforms. KotlinPoet is released as an early-access version, and the article invites the community to use it and provide feedback (Source: https://developer.squareup.com/blog/generating-kotlin-code-with-kotlinpoet/).

- KotlinPoet is a Kotlin code generation library inspired by JavaPoet, providing builders and an immutable model for generating Kotlin source.
- Generated Java code from existing tools can lack Kotlin-friendly features, motivating a Kotlin-native code generation solution.
- KotlinPoet can generate Kotlin code that runs on JVM, JavaScript, and native platforms, offering more flexibility than Java generation.
- The library is currently in early access but already supports core constructs like classes, constructors, properties, functions, and string interpolation templates.