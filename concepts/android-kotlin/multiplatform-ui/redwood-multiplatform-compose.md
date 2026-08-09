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

Redwood is Cash App's approach to multiplatform mobile UI, prioritizing native UI toolkits on each platform. The system is designed to let engineers reuse existing styles and custom controls, use Kotlin for its multi-platform compilation capabilities, and support incremental adoption within existing apps. It leverages Compose for state management and custom tree structures, while a schema defines common UI widgets like TextInput (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

From the widget schema, Redwood generates both a composable function and an interface for each widget. Platform-specific bindings implement the interface to connect with native components. This architecture enables developers to write standard Compose code with generated composables, while Redwood handles the underlying plumbing. Additionally, the Treehouse module uses Zipline to dynamically update composable logic at runtime, allowing app logic to be updated between app store releases (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

The article announces Redwood 0.5 as a beta release. While breaking changes are still possible, all changes will remain compatible with previous versions via the updatable Treehouse bridge, meaning future Redwood versions can target older apps running 0.5. The team notes that usage to date has been limited, but they are excited to roll out experiences to all customers soon (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

- Redwood renders using native UI toolkits and reuses existing app styles/controls.
- Kotlin and Compose are used to create a multiplatform composable layer with a schema-defined widget system.
- Treehouse leverages Zipline for runtime updates of UI logic, enabling out-of-band app changes.
- Redwood 0.5 beta allows backward compatibility across the Treehouse bridge for future versions.
- Incremental adoption is a core goal, allowing use in only needed parts of an existing app.