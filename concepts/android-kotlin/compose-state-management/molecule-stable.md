---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-stable
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule, a Compose-based library for managing application state, has reached its first stable version 1.0. Originally announced two years ago, it now supports Kotlin multiplatform targets (JVM, JS, and native) in addition to Android. The library also introduces an immediate recomposition mode that eliminates the need for a frame clock, allowing state to be produced as soon as changes occur. These features enable state-producing composables to be reused across different UI frameworks and platforms.

- Molecule 1.0 is the first stable release, adding Kotlin multiplatform support for JVM, JS, and native.
- Immediate recomposition mode triggers state production on changes without waiting for a frame clock.
- State logic written in Compose can be exposed as StateFlow or Flow, making it testable and usable outside Compose UI.
- Molecule runs on every Kotlin target supported by the JetBrains Compose runtime, enabling use on iOS, web, and more.
- Unit testing is simplified with Turbine, and tests can run on the JVM.