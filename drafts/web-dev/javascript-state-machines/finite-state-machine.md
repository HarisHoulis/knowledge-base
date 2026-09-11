---
domain: web-dev
subdomain: javascript-state-machines
concept: finite-state-machine
title: Implementing a Simple State Machine Library in JavaScript
sources:
  - title: "Implementing a simple state machine library in JavaScript"
    url: "https://kentcdodds.com/blog/implementing-a-simple-state-machine-library-in-javascript"
    author: "Kent C. Dodds"
    date: "2020-01-20"
---

# Implementing a Simple State Machine Library in JavaScript

The article builds a minimal JavaScript state machine implementation from requirements borrowed from statecharts.github.io's "What is a state machine?" page. It defines a state machine as having an initial state, per-state enter/exit actions, events that trigger transitions, transitions with target states, and optional transition actions. The running example is a toggle machine with `off` and `on` states and a `switch` event (kentcdodds.com, 2020).

The implementation centers on `createMachine(stateMachineDefinition)`, which returns a `machine` object with a `value` property set to `initialState` and a `transition(currentState, event)` method. `transition` looks up the current state definition and its transition for the event; if no transition matches, it returns early. Otherwise, it gets the destination state, calls the transition action, the current state's `onExit`, the destination state's `onEnter`, updates `machine.value` to the destination state, and returns the new value (kentcdodds.com, 2020).

The author explicitly says this simple implementation is not recommended for production and points readers to xstate for production use. The article also notes that state charts are a related concept worth learning, and that this exercise is meant to help solidify the concept by writing an implementation (kentcdodds.com, 2020).

- The state machine definition includes `initialState`, per-state actions (`onEnter`, `onExit`), and per-state `transitions` keyed by event name.
- A transition object can specify a `target` state and an optional `action` that runs when the transition happens.
- The `transition` method checks the current state's transitions for the event, exits early if none match, then runs transition action, current-state `onExit`, destination-state `onEnter`, and updates `machine.value` to the target state.
- The article warns against using this implementation in production and recommends xstate instead.