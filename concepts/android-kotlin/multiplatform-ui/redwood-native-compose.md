---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-native-compose
title: Native UI and Multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and Multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile client UI, built with distinct values: using native UI toolkits on each platform, reusing existing app components, leveraging Kotlin for its multi-platform compilation, and enabling incremental adoption within existing apps. The project renders through each platform's native UI, allowing engineers to maintain their existing skills while sharing code across Android, iOS, and web via Kotlin's ability to compile to JVM, LLVM, and JavaScript.

Redwood uses Compose not as a UI toolkit but as a state-management and tree-construction layer. A common schema defines UI widgets like TextInput, from which Redwood generates composables and interfaces. Each platform binds an implementation of these interfaces to its native UI components, letting developers write standard Compose code with generated composables while Redwood handles the plumbing between the Compose tree and native widgets.

The Redwood repository also includes Treehouse, a module built on Zipline that enables dynamic runtime updates of composable logic. The article announces Redwood 0.5 as a 'beta' release, allowing future versions to maintain compatibility with older apps through the Treehouse bridge. The post also mentions conference talks for further learning, such as KotlinConf and Droidcon presentations, and states that Redwood usage has been limited but will roll out to customers soon.

- Redwood prioritizes native UI rendering on each platform while using Kotlin Multiplatform for shared logic.
- UI widgets are defined as a schema, from which Redwood generates composables and platform-specific interfaces.
- Compose is used for state and tree management, not as the final rendering layer, enabling native bindings.
- Treehouse with Zipline allows dynamic updates of composable logic at runtime.
- Redwood 0.5 is a beta release designed for backward compatibility across versions via the Treehouse bridge.