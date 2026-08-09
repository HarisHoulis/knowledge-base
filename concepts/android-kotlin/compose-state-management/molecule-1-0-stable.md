---
domain: android-kotlin
subdomain: compose-state-management
concept: molecule-1-0-stable
title: A stable, multiplatform Molecule 1.0
sources:
  - title: "A stable, multiplatform Molecule 1.0"
    url: "https://code.cash.app/molecule-1-0"
    author: "Jake Wharton"
---

# A stable, multiplatform Molecule 1.0

Molecule is a Compose-based library for managing application state. The 1.0 release adds Kotlin multiplatform support (JVM, JS, and native) and an immediate recomposition mode that triggers on state changes rather than waiting for a frame clock. This allows state-producing composables to be reused outside Compose UI, such as being exposed as StateFlow to existing View-based apps or used in notifications, widgets, web, and SwiftUI targets.

- Molecule 1.0 is the first stable release, now supporting Kotlin multiplatform targets (JVM, JS, and native).
- Immediate recomposition mode eliminates the need for a frame clock, producing values as soon as state changes.
- State-producing composables can be launched with launchMolecule and exposed as StateFlow to Android Views or other non-Compose destinations.
- Molecule output can be unit tested with Turbine and runs on JVM, JS, and native platforms.
- Molecule enables state management with Compose even when UI is not rendered by Compose, improving reusability and portability.