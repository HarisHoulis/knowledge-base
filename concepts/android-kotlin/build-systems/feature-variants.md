---
domain: android-kotlin
subdomain: build-systems
concept: feature-variants
title: Understanding Gradle #17 – Feature Variants
sources:
  - title: "Understanding Gradle #17 – Feature Variants"
    url: "https://www.youtube.com/watch?v=XCzyUESaBHQ"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-06-27T15:33:06+00:00"
---

# Understanding Gradle #17 – Feature Variants

Feature variants in Gradle allow a single component to be split into multiple optional features, which consumers can select based on their needs. The video demonstrates this by extending a data model project with JSON and XML serialization capabilities. These serializers are placed in separate source sets, keeping the main code decoupled from optional serialization logic. Consumers can then depend on the main variant by default or choose a specific feature variant by requiring the associated capability (e.g., 'json' or 'xml').

The key insight is that feature variants do not introduce new core Gradle functionality; instead, they combine existing concepts like source sets, configurations, capabilities, and variant-aware dependency management. Registering a feature variant on the java extension creates a new variant tied to a source set, with a unique capability derived from the source set name. During dependency resolution, Gradle selects the matching variant based on the requested capability, enabling multiple variants of the same component to coexist without conflict.

- Feature variants let a component expose optional features that consumers can opt into.
- They are implemented using existing Gradle concepts: source sets, configurations, capabilities, and variant-aware resolution.
- Registering a feature variant on the java extension ties it to a source set and gives it a distinct capability.
- Consumers select a feature variant by declaring a dependency with the required capability (e.g., 'json' or 'xml').
- The main variant is the default; additional variants are named after their source sets.