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

Redwood is Cash App's take on multiplatform mobile client UI, designed to render using the native UI toolkit on each platform while retaining the ability to reuse existing app components and styles. It leverages Kotlin for cross-platform execution and Compose for managing UI state and tree structures, with a custom tree that interfaces with native UI toolkits. Developers define UI widgets in a schema, from which Redwood generates composables and platform-specific interfaces that bind to native components, ensuring a single source of truth for the design system. Treehouse, a module within Redwood, uses Zipline to dynamically update composable logic at runtime, enabling app logic updates between app upgrades. Redwood 0.5 is now in beta, allowing backward-compatible updates across versions, and the team plans to roll out experiences to customers soon (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

- Redwood uses native UI toolkits on each platform while leveraging Kotlin and Compose for state management and UI tree creation.
- A schema defines common UI widgets, generating composables and interfaces that can be implemented per platform.
- Incremental adoption is supported; Redwood can be used only where needed in an existing app.
- Treehouse and Zipline enable runtime updates of composable logic, allowing dynamic code changes without app store releases.
- Redwood 0.5 is a beta release with a compatibility guarantee for future versions.