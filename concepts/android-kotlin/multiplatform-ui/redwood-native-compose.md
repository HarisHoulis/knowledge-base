---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-native-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile client UI. Unlike many existing solutions, it emphasizes rendering with each platform's native UI toolkit, retaining component reusability, using a mobile language with strong tooling (Kotlin), and allowing incremental adoption. Redwood leverages Compose to manage state and build UI trees, but instead of Compose UI's rendering, it uses a custom tree that bridges to native UI components on each platform (Jake Wharton, "Native UI and multiplatform Compose with Redwood").

To enable cross-platform UI, Redwood defines a schema—programmatic representations of UI widgets like TextInput. From this schema, Redwood generates both a composable and an interface for each widget. Platform-specific implementations bind these interfaces to native UI components, allowing developers to write regular Compose code using the generated composables while Redwood handles the plumbing to native widgets (Jake Wharton, "Native UI and multiplatform Compose with Redwood").

The Redwood repository also includes Treehouse, a module using Zipline to dynamically update composable logic at runtime, improving development experience and enabling app logic updates between app upgrades. Redwood 0.5 is now in beta, allowing future versions to remain compatible with older apps through the updatable Treehouse bridge (Jake Wharton, "Native UI and multiplatform Compose with Redwood").

- Redwood prioritizes native UI toolkits, reusing existing components, Kotlin, and incremental adoption.
- A schema of UI widgets generates composables and interfaces that bridge to native components on each platform.
- Compose manages UI state and tree creation, while Redwood's custom tree talks to native UI toolkits.
- Treehouse (with Zipline) enables runtime updates to composable logic across app versions.
- Redwood 0.5 is now beta, with backward compatibility via the Treehouse bridge.