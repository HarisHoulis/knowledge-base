---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-stable-release
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, originally announced two years ago. With the release of version 1.0, it now offers full Kotlin multiplatform support (JVM, JS, and native) in addition to Android, and an immediate recomposition mode that removes the need for a frame clock. These features make it possible to use Compose state logic outside the UI, such as exposing state to Views as a StateFlow or collecting it as a Flow (source).

The article demonstrates separating state-producing composables from UI composables, allowing state logic to be migrated to Compose early and exposed to existing View-based Android apps. Molecule's immediate mode triggers recomposition whenever state changes, enabling state to be represented as a Flow. This also simplifies testing with Turbine on the JVM, and opens up usage on other Kotlin multiplatform targets like iOS and web (source).

- Molecule 1.0 is the first stable release of the Compose-based state management library.
- Adds support for Kotlin multiplatform targets: JVM, JS, and native.
- Immediate recomposition mode allows state to be produced without an external frame clock.
- State can be exposed as a StateFlow or Flow, enabling reuse across UI frameworks and platforms.
- Unit testing is simplified with Turbine and runs on the JVM.