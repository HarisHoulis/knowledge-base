---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-multiplatform-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile client UI, built on the principle that native UI is the best UI. Unlike many existing solutions, Redwood emphasizes rendering with the native UI toolkit on each platform while retaining the ability to reuse existing components and styles. It leverages Kotlin as a mobile language with great tooling, allowing compilation to Android, iOS, and web, and is designed for incremental adoption within existing apps rather than requiring an all-or-nothing framework migration.

- Redwood prioritizes native UI on each platform, enabling engineers to use existing skills and maintain a single source of truth for components.
- It uses Kotlin Multiplatform and Compose's state management with a custom tree that interfaces with native UI toolkits on Android, iOS, and web.
- A schema defines UI widgets like TextInput, from which Redwood generates composables and interfaces that each platform binds to native components.
- Treehouse, built on Zipline, allows dynamic runtime updates of composable logic, improving the development experience and enabling updates between app releases.
- Redwood 0.5 is now in beta, with backward compatibility across versions when using the Treehouse bridge, facilitating gradual rollout to all customers.