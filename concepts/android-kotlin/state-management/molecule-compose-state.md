---
domain: android-kotlin
subdomain: state-management
concept: molecule-compose-state
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library from Cash App for managing application state. Version 1.0 marks its first stable release, adding Kotlin multiplatform support for JVM, JS, and native targets, as well as an immediate recomposition mode that removes the need for a frame clock [1]. The library enables separating state-producing composables from UI-rendering composables, allowing state logic to be reused outside Compose UI—for example, exposed as a StateFlow to Views, notifications, or widgets [1]. The immediate mode triggers recomposition whenever state changes, making it suitable for presenter-like scenarios. This also simplifies testing via Turbine, with unit tests running on the JVM [1]. Multiplatform support extends the same state logic to iOS (SwiftUI) and the web (DOM), as demonstrated by a snippet that collects a Flow and updates a DOM element [1].

- Molecule 1.0 is the first stable version, supporting Kotlin multiplatform targets (JVM, JS, native).
- Immediate recomposition mode allows state-producing composables to run without a frame clock.
- State logic can be exposed as StateFlow and reused in Views, notifications, widgets, and more.
- Unit testing is simplified with Turbine, running on the JVM.
- Multiplatform usage enables targeting iOS and web with the same Compose-based state management.