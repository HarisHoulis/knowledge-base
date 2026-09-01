---
domain: android-kotlin
subdomain: state-management
concept: molecule-state-management
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule 1.0 is released as a stable version of Cash App's Compose-based library for managing application state. The announcement highlights two major features added since the original post: Kotlin multiplatform support (JVM, JS, native) in addition to Android, and an immediate recomposition mode that eliminates the need for a frame clock. These features extend the utility of Compose state management beyond UI rendering, allowing state-producing composables to be reused across platforms and contexts.

- Molecule 1.0 is stable and supports Kotlin multiplatform targets: JVM, JS, native, and Android.
- Immediate recomposition mode triggers recomposition as soon as state changes occur, without needing a UI frame clock.
- State-producing composables can be exposed as StateFlow or Flow, enabling use in View-based Android apps, notifications, widgets, and web targets.
- The library simplifies unit testing by integrating with Turbine, allowing tests to run on the JVM.
- Molecule works on every Kotlin multiplatform target supported by the JetBrains Compose runtime.