---
domain: android-kotlin
subdomain: gradle
concept: feature-variants
title: Understanding Gradle #17 – Feature Variants
sources:
  - title: "Understanding Gradle #17 – Feature Variants"
    url: "https://www.youtube.com/watch?v=XCzyUESaBHQ"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-06-27T15:33:06+00:00"
---

# Understanding Gradle #17 – Feature Variants

The approach relies on existing Gradle concepts like source sets, configurations, capabilities, and variant-aware dependency management. Registering a feature variant gives it a unique capability, so consumers can select it by declaring a dependency with that capability. Because capabilities enforce exclusivity, only one variant per capability can be selected, but multiple variants with different capabilities can coexist (Understanding Gradle #17, 2022).

- Feature variants let a component offer optional features that consumers can choose from.
- They are implemented on top of source sets, not as a new core functionality.
- Consumers select a feature variant by requiring its corresponding capability in the dependency declaration.
- Multiple variants of the same component can be used simultaneously when they expose different capabilities.
- This pattern decouples optional logic (e.g., different serializers) from the core data classes.