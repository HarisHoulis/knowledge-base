---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-state-management
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state, originally announced by Cash App in 2021. Version 1.0 marks its first stable release, adding Kotlin multiplatform support (JVM, JS, native) and an immediate recomposition mode that triggers recomposition whenever there are new changes, eliminating the need for a frame clock. These features allow state-producing composables to be separated from UI rendering composables, increasing reuse across platforms and destinations, as described in the source article.

The article demonstrates how a pure Compose UI can separate state-producing composables from UI-rendering composables, with state logic migrated early to Compose and exposed to Views as a StateFlow using launchMolecule. Alternatively, moleculeFlow with Immediate mode produces a Flow that emits new values whenever internal state changes, enabling simpler testing with Turbine. Since Molecule runs on every Kotlin multiplatform target supported by the JetBrains Compose runtime, the same state logic can be tested on the JVM and used on platforms like iOS or web, making it a versatile tool for state management in Kotlin projects. The article concludes that Molecule is useful for both full Compose UI apps and Kotlin multiplatform projects, citing the source content for these claims.

- Molecule 1.0 is a stable release of a Compose-based state management library with multiplatform support (JVM, JS, native).
- An immediate recomposition mode allows state changes to trigger recomposition without waiting for a frame clock.
- State-producing composables can be exposed as StateFlow or Flow via launchMolecule and moleculeFlow, decoupling from UI rendering.
- This design enables unit testing with Turbine on the JVM and reuse across platforms such as Android Views, iOS, and web.
- Molecule simplifies migrating large View-based apps by allowing state logic to be migrated to Compose early.