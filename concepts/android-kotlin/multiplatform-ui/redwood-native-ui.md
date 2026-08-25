---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-native-ui
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

In this article, Jake Wharton introduces Redwood, Cash App's take on multiplatform mobile UI. Unlike other solutions, Redwood prioritizes using the native UI toolkit on each platform—Android, iOS, and web—while retaining the ability to reuse existing app components and styles. It leverages Kotlin for its ability to compile to Java bytecode, LLVM, and JavaScript, and builds on Compose to manage state and create UI nodes with a custom tree that talks to each platform's native UI toolkit. (source: [Native UI and multiplatform Compose with Redwood](https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood))

The core mechanism is a schema: UI widgets are defined as Kotlin data classes, from which Redwood generates a composable and a widget interface. Each platform then binds its native UI component to that interface, allowing developers to write regular Compose code with generated composables while Redwood handles the plumbing. This design enables incremental adoption in existing apps, as it's a library rather than an all-or-nothing framework. (source: [Native UI and multiplatform Compose with Redwood](https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood))

The Redwood repo also includes Treehouse, a module using Zipline to dynamically update composable logic at runtime—improving development experience and allowing app logic updates without waiting for app upgrades. The article announces Redwood 0.5 as a "beta" release: breaking changes are still allowed, but future versions will remain compatible with older running versions across the Treehouse bridge. Cash App's usage is limited so far, but they plan to roll out experiences to customers soon. (source: [Native UI and multiplatform Compose with Redwood](https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood))

- Redwood renders via native UI toolkits on each platform, not a custom-drawn cross-platform UI.
- A schema of Kotlin data classes generates composables and widget interfaces that bind to platform-specific native components.
- Treehouse + Zipline enable runtime dynamic updates of UI logic, supporting over-the-air changes.
- Redwood 0.5 ("beta") allows incremental adoption and promises cross-version compatibility via the Treehouse bridge.