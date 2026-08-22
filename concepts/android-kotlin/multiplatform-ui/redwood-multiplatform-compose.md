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

Redwood is Cash App's approach to multiplatform mobile client UI, built around the principle that native UI is the best UI. It renders using each platform's native toolkit while allowing code reuse and incremental adoption. The framework leverages Kotlin for its ability to compile to Java bytecode, LLVM, and JavaScript, enabling intrinsic execution on Android, iOS, and the web. Compose is used for managing state and creating UI nodes, but Redwood replaces Compose UI's tree with a custom tree that interfaces with native components per platform.

- Redwood prioritizes native UI rendering on each platform, allowing reuse of existing styles and custom controls.
- Kotlin is chosen for its multiplatform capabilities, supporting Android, iOS, and web via different compilation targets.
- A schema defines common UI widgets, from which Redwood generates composables and interface bindings for each platform.
- Treehouse, built on Zipline, enables dynamic runtime updates of composable logic for improved development and over-the-air updates.
- Redwood 0.5 is released as a beta, with breaking changes allowed but maintaining compatibility across the Treehouse bridge.