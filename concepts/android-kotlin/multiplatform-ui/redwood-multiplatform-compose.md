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

Redwood is Cash App's take on multiplatform mobile client UI, prioritizing native UI toolkit rendering on each platform, component reuse, Kotlin programming language for tooling, and incremental adoption in existing apps. The library leverages Kotlin's multi-platform compilation targets (Java bytecode, LLVM, JavaScript) to support Android, iOS, and web, and builds on Compose to manage state and create UI nodes via a custom tree that interfaces with each platform's native UI toolkit. A schema-based definition of UI widgets (e.g., TextInput) generates composables and platform-specific interfaces, which each platform binds to native components. (Source: Jake Wharton, "Native UI and multiplatform Compose with Redwood", https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood)

The Redwood repository also includes Treehouse, a module using Zipline to dynamically update composable logic at runtime, improving development experience and enabling app logic updates without full app releases. The article announces Redwood 0.5 beta, which allows breaking changes but maintains compatibility across the Treehouse bridge, meaning future versions can still target older apps. Redwood, Zipline, and Treehouse are significant efforts, and the article references several conference talks for deeper details. (Source: Jake Wharton, same URL)

- Redwood's core values: native UI rendering, component reuse, Kotlin language, and incremental adoption.
- Uses a schema of UI widgets to generate composables and platform-specific interface implementations.
- Kotlin multiplatform enables targeting Android, iOS, and web with intrinsic execution.
- Treehouse (powered by Zipline) allows runtime-updatable composable logic.
- Redwood 0.5 beta released with compatibility guarantees for future versions.