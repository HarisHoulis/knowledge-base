---
domain: system-design
subdomain: gradle
concept: aggregating-custom-artifacts
title: Aggregating Custom Artifacts with Gradle
sources:
  - title: "Understanding Gradle #13 – Aggregating Custom Artifacts"
    url: "https://www.youtube.com/watch?v=2gPJD0mAres"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-06T09:38:42+00:00"
---

# Aggregating Custom Artifacts with Gradle

The key to aggregation is creating custom configurations that extend existing ones (like implementation) and setting attributes (e.g., usage = 'java-sources') to distinguish the variant being resolved. However, simply adding a resolvable configuration in the aggregator is insufficient unless each subproject exposes the desired artifacts as a consumable configuration (a variant). The video shows how to add such a consumable configuration to all projects via a shared Java plugin, enabling the aggregated output to collect source sets from all dependencies. This pattern generalizes to any custom artifact type, making it a powerful technique for build customization.

- Custom artifact aggregation in Gradle requires using resolvable configurations and understanding variants.
- The runtime classpath is a pre-configured resolvable configuration that can be used in custom tasks to collect all runtime dependencies.
- To aggregate source code (e.g., for javadoc), create a custom resolvable configuration with a unique usage attribute extending implementation.
- Each project must expose its artifacts via a consumable configuration (variant) for the aggregator to resolve them.
- This approach can be applied to other custom artifacts like code coverage reports, not just javadoc.