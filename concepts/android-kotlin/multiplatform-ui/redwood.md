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

Redwood is Cash App's approach to multiplatform mobile client UI, prioritizing native UI toolkits on each platform, reusability of existing components, Kotlin for tooling, and incremental adoption. It uses a common widget schema to define UI elements like TextInput, from which Redwood generates composables and interfaces. Each platform provides an implementation binding these interfaces to native components, while regular Compose code drives the UI. Redwood integrates with Treehouse and Zipline to allow dynamic updates of composable logic at runtime, and recently released version 0.5 as a beta, with compatibility guarantees for forward cross-version usage.

- Redwood renders using native UI toolkits on each platform, retaining native quality and styles.
- A schema of widget definitions generates composables and platform-specific widget interfaces.
- Treehouse uses Zipline to dynamically update UI logic in production between app releases.
- Redwood 0.5 is a beta release that allows incremental adoption and future cross-version compatibility.