---
domain: android-kotlin
subdomain: state-management
concept: molecule-1-0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Cash App has released Molecule 1.0, the first stable version of its Compose-based library for managing application state. The release adds Kotlin multiplatform support for JVM, JS, and native targets, and introduces an immediate recomposition mode that triggers recomposition whenever new state changes are available, without requiring a frame clock. These features extend Molecule's utility beyond Android and enable state-producing composables to be reused across platforms and test environments.

- Molecule 1.0 supports Kotlin multiplatform targets (JVM, JS, native) in addition to Android.
- Immediate recomposition mode allows state to be produced as a Flow without needing a UI frame clock.
- State logic written in Compose can be exposed as StateFlow for use with Views, notifications, widgets, and other non-UI targets.
- The library simplifies testing by allowing state flows to be unit tested with Turbine on the JVM.
- The article demonstrates using Molecule for a counter example that works in pure Compose UI, with View-based Android, and on web via Kotlin/JS.