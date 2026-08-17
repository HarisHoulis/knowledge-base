---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile client UI, prioritizing native UI toolkits on each platform. The library allows engineers to reuse existing app components and styles, leveraging the Kotlin language for its ability to compile to multiple targets. Redwood uses Compose for managing state and creating UI nodes, but with a custom tree that interfaces with each platform's native UI toolkit.

A schema defines common UI widgets, from which Redwood generates composables and interfaces. Each platform binds these interfaces to native UI components. The article also introduces Treehouse, a module using Zipline for dynamic updates of composable logic at runtime, enabling app updates between releases. Redwood 0.5 is released as a beta, marking a step toward broader adoption.

- Redwood renders using native UI toolkits on each platform, not a cross-platform widget set.
- It uses Kotlin and Compose for a unified codebase while allowing incremental adoption in existing apps.
- A schema defines widgets and generates composables and interfaces for platform-specific bindings.
- Treehouse uses Zipline to dynamically update composable logic at runtime, improving development and enabling over-the-air updates.
- Redwood 0.5 is the first beta release, with compatibility maintained across versions for the Treehouse bridge.