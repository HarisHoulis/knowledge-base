---
domain: engineering-culture
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

Feature variants are a Gradle concept that allows a component to be split into multiple optional features, which consumers can selectively choose. The video explains this through a practical example: a data model project that contains core data classes and two alternative serializers (JSON and XML). By placing each serializer in its own source set, the code remains decoupled from the core model, and dependencies for each serializer can be managed separately.

- Feature variants allow splitting a component into optional features, selected by consumers via capabilities.
- They are built on existing Gradle concepts: source sets, configurations, capabilities, and variant-aware dependency management.
- Registering a feature variant for a source set makes it consumable externally, with a unique capability.
- Consumers select a feature variant by declaring the required capability on their dependency.
- The main variant of a project always exists and can be depended on normally; feature variants are additional alternatives.