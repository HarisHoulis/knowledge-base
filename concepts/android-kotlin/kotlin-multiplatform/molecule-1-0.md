---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: molecule-1-0
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule, a Compose-based library for managing application state, has reached its first stable version 1.0. The release introduces two major features: support for Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, and an immediate recomposition mode that does not require a frame clock. The library allows state-producing composables to be separated from UI-rendering composables, as demonstrated with a counter composable that can be tested or reused independently.

By running Compose outside of the UI context, Molecule enables state logic to be exposed as a StateFlow or Flow, making it easy to integrate with non-Compose destinations like notifications, widgets, or legacy View-based Android apps. The immediate recomposition mode triggers whenever state changes, avoiding the need to tie recomposition to the UI framework's frame clock. This makes the state flow behave like a regular reactive stream.

The library simplifies testing by allowing state to be collected as a Flow and tested with Turbine on the JVM, even when the logic is intended for multiplatform use. Because Molecule runs on every Kotlin multiplatform target supported by the JetBrains Compose runtime, the same state-producing composables can be used on iOS (e.g., SwiftUI) or web (e.g., DOM), broadening the reach of Compose-based state management.

- Molecule 1.0 adds Kotlin multiplatform support (JVM, JS, native) and an immediate recomposition mode.
- State-producing composables can be run outside Compose UI and exposed as StateFlow or Flow for reuse in non-UI contexts.
- Immediate mode recomposes only on actual state changes, decoupling from the UI frame clock.
- Unit testing is simplified via Flow and Turbine, running on the JVM across platforms.
- Works on all Kotlin multiplatform targets supported by the Compose runtime, enabling iOS and web usage.