---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: redwood
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's solution for multiplatform mobile UI, prioritizing native UI toolkits on each platform. Unlike cross-platform renderers, Redwood relies on the native UI toolkit for each platform, allowing engineers to reuse existing styles, controls, and skills. The framework is built on Kotlin, which compiles to Java bytecode, native code, and JavaScript, and leverages Compose for state management and UI tree construction. Redwood uses a custom tree that interfaces with each platform's native UI components.

The core of Redwood is a schema that defines UI widgets (e.g., TextInput) as data classes. From this schema, Redwood generates Compose composables and interfaces. Each platform binds an implementation of the generated interface to its native UI component. This enables developers to write regular Compose code using these generated composables while Redwood handles the plumbing to native UIs.

Redwood also integrates with Treehouse, which uses Zipline to dynamically update composable logic at runtime. This improves development workflows and allows app logic updates between app upgrades. Redwood 0.5 is now in beta, allowing breaking changes while maintaining compatibility across the Treehouse bridge for older versions.

- Redwood uses each platform's native UI toolkit rather than a rendering engine, preserving native look and feel and enabling reuse of existing custom components.
- Kotlin and Compose are used as the foundation, with a schema defining UI widgets that generate composables and interfaces for platform-specific bindings.
- Redwood is designed for incremental adoption in existing apps, not as an all-or-nothing framework.
- Treehouse (built on Zipline) supports runtime updates of composable logic, and Redwood 0.5 is the first beta release.