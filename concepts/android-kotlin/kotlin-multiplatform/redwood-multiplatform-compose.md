---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: redwood-multiplatform-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile UI, emphasizing native UI toolkits on each platform while leveraging Kotlin and Compose for state management and UI composition. The project is built on four core values: using native UI for best quality, reusing existing app components, employing a mobile language with strong tooling, and allowing incremental adoption in existing apps. By choosing Kotlin, Redwood can target Android, iOS, and the web through intrinsic execution on each platform.

Redwood uses Compose to manage state alongside a custom tree that interfaces with each platform's native UI toolkit. A shared schema defines common UI widgets, from which Redwood generates composables and interfaces. Each platform binds these interfaces to native UI components, enabling developers to write regular Compose code while Redwood handles the plumbing. The repository also includes Treehouse, a module that uses Zipline for dynamic runtime updates of composable logic, improving development and allowing app logic updates between releases.

The article announces Redwood 0.5 as a beta release, allowing breaking changes while maintaining compatibility across the Treehouse bridge. This enables future versions to target older apps. Redwood's usage has been limited so far, but the beta marks a step toward broader adoption. The post is part of Cash App's Summer of Kotlin Multiplatform series.

- Redwood renders with native UI toolkits on each platform while using Kotlin and Compose for state management.
- A schema defines common UI widgets, generating composables and interfaces that are bound to native components per platform.
- Treehouse, built on Zipline, enables dynamic runtime updates of composable logic.
- Redwood 0.5 is a beta release that supports incremental adoption and future compatibility via the Treehouse bridge.