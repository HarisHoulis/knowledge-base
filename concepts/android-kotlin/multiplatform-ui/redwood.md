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

Redwood is Cash App's approach to multiplatform mobile UI, prioritizing native UI toolkits on each platform. Unlike cross-platform frameworks that render via custom engines, Redwood renders using the native UI components of Android, iOS, and the web, allowing engineers to reuse existing styles and custom controls as a single source of truth. It leverages Kotlin for its ability to compile to Java bytecode, native code, and JavaScript, and uses Compose (the underlying technology) to manage state and drive a custom UI tree that interfaces with each platform's native widgets.

- Native UI is considered the best UI, and Redwood ensures each platform uses its own toolkit while sharing logic via Kotlin Multiplatform and Compose.
- A schema defines common UI widgets (e.g., TextInput), from which Redwood generates composables and interfaces; each platform binds these to native components.
- Treehouse, built on Zipline, enables dynamic runtime updates of composable logic, improving development and allowing app updates between releases.
- Redwood supports incremental adoption—it's a library that can be used only where needed, not an all-or-nothing framework.
- Redwood 0.5 is released as a beta, with backward compatibility across the Treehouse bridge for future versions.