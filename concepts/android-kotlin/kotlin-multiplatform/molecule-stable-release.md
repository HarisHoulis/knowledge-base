---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: molecule-stable-release
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule, a Compose-based library for managing application state, has reached version 1.0, its first stable release. Originally announced two years ago, the library now supports Kotlin multiplatform targets (JVM, JS, and native) in addition to Android, and introduces an immediate recomposition mode that eliminates the need for a frame clock. These features enable state-producing composables to be reused across platforms and tested more easily (Jake Wharton, A stable, multiplatform Molecule 1.0).

The library allows separating state-producing composables from UI-rendering composables, as shown with a simple counter example. State logic can be exposed to existing View-based Android apps as a StateFlow via launchMolecule, allowing gradual migration to Compose UI. The immediate mode triggers recomposition whenever state changes, producing a Flow that emits values each time the internal timer updates. This makes state logic testable with Turbine on the JVM, and because Molecule runs on all Kotlin multiplatform targets supported by the JetBrains Compose runtime, the same logic can be used on iOS or the web (Jake Wharton, A stable, multiplatform Molecule 1.0).

Overall, Molecule 1.0 provides a stable, multiplatform solution for managing state with Compose, whether in a 100% Compose UI app, a Kotlin multiplatform project, or a hybrid scenario. It is part of Cash App's Summer of Kotlin Multiplatform series (Jake Wharton, A stable, multiplatform Molecule 1.0).

- Molecule 1.0 is the first stable release, supporting JVM, JS, and native targets via Kotlin multiplatform.
- Immediate recomposition mode allows state-producing composables to work without a frame clock.
- State logic exposed as StateFlow or Flow can be reused in Views, notifications, widgets, and other destinations.
- Unit testing is simplified using Turbine, and tests can run on the JVM across platforms.