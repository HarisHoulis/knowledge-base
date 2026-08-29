---
domain: android-kotlin
subdomain: multiplatform-compose
concept: redwood
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's solution for multiplatform mobile client UI. Its core values emphasize using native UI toolkits on each platform for the best UI, reusing existing app components and styles, leveraging Kotlin for its tooling and ecosystem, and allowing incremental adoption. The approach combines Kotlin's ability to compile to multiple targets with Compose for UI node creation and state management, but uses a custom tree that interfaces with each platform's native UI toolkit.

A key aspect of Redwood is the use of a schema to define common UI widgets, from which Redwood generates composables and interfaces. Each platform then binds an implementation of these interfaces to its native UI components. The Redwood repository also includes Treehouse, which uses Zipline to dynamically update composable logic at runtime, enabling features between app upgrades. The release of Redwood 0.5, termed 'beta', permits breaking changes but maintains compatibility across the Treehouse bridge, allowing future versions to target older apps.

Redwood aims to provide a pragmatic path for adopting Kotlin Multiplatform in existing apps, as evidenced by Cash App's 'Summer of Kotlin Multiplatform' series. While current usage is limited, the beta release marks a step toward rolling out experiences to customers. (Source: Jake Wharton, article on Cash App code blog)

- Redwood prioritizes native UI per platform, reuse of existing components, Kotlin language, and incremental adoption.
- Uses Compose for UI state management but with a custom tree that talks to native UI toolkits.
- A schema defines UI widgets, generating composables and platform-bound interfaces.
- Treehouse and Zipline enable dynamic runtime updates of composable logic.
- Redwood 0.5 is released as 'beta' with forward compatibility across versions.