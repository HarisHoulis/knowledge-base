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

Redwood is Cash App's approach to multiplatform mobile client UI, emphasizing native UI toolkits on each platform, reusability of existing app components, the Kotlin language, and incremental adoption (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood). It leverages Kotlin's ability to compile to Java bytecode, native, and JavaScript, enabling use on Android, iOS, and the web. Compose is used for creating UI nodes and managing state, but with a custom tree that talks to the native UI toolkit on each platform, rather than Compose UI itself (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

To support multiplatform composables, Redwood defines a schema of UI widgets (e.g., TextInput), from which it generates a composable and an interface. Each platform binds an implementation of that interface to its native UI component. This allows developers to write regular Compose code with generated composables while Redwood handles the plumbing (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood). The Redwood repo also includes Treehouse, a module using Zipline for dynamically updating composable logic at runtime, enabling app logic updates between app upgrades. Redwood 0.5 is now released as a 'beta', allowing breaking changes while maintaining compatibility across the Treehouse bridge (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

- Redwood prioritizes native UI toolkits, component reuse, Kotlin, and incremental adoption.
- Uses Compose for state and tree management, but interfaces with native UI via a custom tree.
- Schema definitions generate composables and platform-specific widget interfaces.
- Treehouse enables dynamic updates of composable logic via Zipline.
- Redwood 0.5 'beta' is released with cross-version compatibility through the Treehouse bridge.