---
domain: android-kotlin
subdomain: state-management
concept: molecule-stable-release
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, developed by Cash App. The 1.0 release marks its first stable version, adding two major features: Kotlin multiplatform support (JVM, JS, and native) and an immediate recomposition mode that removes the need for a frame clock. These features enable state-producing composables to be decoupled from Compose UI, allowing them to be exposed to Views, notifications, widgets, or other platforms via StateFlow or Flow. The library simplifies testing by enabling unit tests with Turbine on the JVM, and it runs on all Kotlin targets supported by the JetBrains Compose runtime. This makes Molecule a versatile tool for managing state across Android, multiplatform, and web projects.

- Molecule 1.0 is a stable release with Kotlin multiplatform support including JVM, JS, and native targets.
- Immediate recomposition mode triggers recomposition on state changes, eliminating the need for a UI frame clock.
- State logic written as composables can be exposed to non-UI destinations like Views, notifications, and widgets through StateFlow.
- The library simplifies unit testing of composable state logic using Turbine, running on the JVM.
- Molecule works on all Kotlin targets supported by the JetBrains Compose runtime, enabling use in SwiftUI or DOM-based applications.