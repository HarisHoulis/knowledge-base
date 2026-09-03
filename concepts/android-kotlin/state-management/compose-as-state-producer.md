---
domain: android-kotlin
subdomain: state-management
concept: compose-as-state-producer
title: The state of managing state (with Compose)
sources:
  - title: "The state of managing state (with Compose)"
    url: "https://code.cash.app/the-state-of-managing-state-with-compose"
    author: "Jake Wharton"
    date: "2021-11-04"
---

# The state of managing state (with Compose)

Jake Wharton recounts the evolution of state management at Cash App, beginning with a UI/rendering split using RxJava that became increasingly opaque as business logic was lost in operator nesting. After migrating to kotlinx.coroutines and Flow, he realized the underlying problem was not the stream type but how state-producing logic was expressed. He introduces Molecule, a Cash App library that uses Compose's runtime and compiler plugin to define state-producing logic as ordinary composable functions, which are then exposed as StateFlow via `launchMolecule` ([Wharton](https://code.cash.app/the-state-of-managing-state-with-compose)).

Molecule allows developers to write plain `if`/`else`, `when`, and `for` loops instead of chaining Flow operators, while still leveraging Compose's `remember`, derived state, and effects. The article shows a Counter presenter and a class-based presenter matching Cash App's dependency-injection style. Molecule is not yet 1.0 but has been integrated into Cash App for real-world testing, and the author invites experimentation ([Wharton](https://code.cash.app/the-state-of-managing-state-with-compose)).

- Molecule uses Compose's compiler and runtime to turn composable functions into StateFlow producers without rendering UI.
- Plain imperative Kotlin replaces complex RxJava/Flow operator chains for state management.
- The library integrates cleanly with class-based presenters and dependency injection in production.
- Molecule is experimental and now open-source for broader testing.