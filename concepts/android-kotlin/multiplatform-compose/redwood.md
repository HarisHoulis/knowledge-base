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

Redwood is Cash App's approach to multiplatform mobile client UI, with a focus on using native UI toolkits on each platform. It prioritizes four core values: rendering with native UI for the best look and feel, reusing existing app components and styles, leveraging Kotlin for its great tooling and cross-platform capabilities, and allowing incremental adoption within an existing app. The article explains that Kotlin compiles to Java bytecode, native (via LLVM), and JavaScript, supporting Android, iOS, and the web with intrinsic execution (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

On top of Kotlin, Redwood uses Compose for creating UI nodes and managing state. Instead of using Compose UI directly, it runs Compose on a custom tree structure that interfaces with each platform's native UI toolkit via a schema. Developers define UI widgets like TextInput as data classes, and Redwood generates both a composable function and a platform interface. Each platform then binds that interface to its associated native UI component, enabling a shared Kotlin codebase to drive native UI (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

Redwood also includes Treehouse, a module that uses Zipline to dynamically update the composable logic at runtime, improving development and allowing app logic updates between app store releases. The article announces the release of Redwood 0.5, which it calls "beta," allowing breaking changes while maintaining compatibility across the updatable Treehouse bridge. Usage of Redwood so far has been limited, but the beta is intended to roll out experiences to customers soon (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

- Uses native UI toolkits on each platform for rendering, preserving existing styles and custom controls.
- Defines a common schema of UI widgets, from which Redwood generates composables and platform interfaces.
- Built on Kotlin and Compose, enabling use on Android, iOS, and the web with incremental adoption.
- Treehouse uses Zipline for dynamic logic updates; Redwood 0.5 is now beta.