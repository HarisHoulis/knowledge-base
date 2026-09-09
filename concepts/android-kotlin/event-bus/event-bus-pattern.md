---
domain: android-kotlin
subdomain: event-bus
concept: event-bus-pattern
title: Decoupling Android App Communication with Otto
sources:
  - title: "Decoupling Android App Communication with Otto"
    url: "https://developer.squareup.com/blog/decoupling-android-app-communication-with-otto"
    author: "Jake Wharton"
---

# Decoupling Android App Communication with Otto

According to Jake Wharton's article on Square's developer blog, as Android apps grow, components need to update based on events from many places like location, authentication, settings, and sync. The common listener-interface pattern forces each interested component to register with every manager, producing an unmanageable dependency graph and making testing difficult because managers must be mocked to simulate updates.

The article introduces the event bus (publisher/subscriber) pattern, borrowed from Swing, as a solution. With an event bus, a component registers once via bus.register(this), and methods annotated with @Subscribe receive relevant events. Event producers call bus.post(event) without knowing subscribers, decoupling communication. Square's Otto library, forked from Guava, implements this pattern for Android, enabling more loosely coupled and testable apps. The article notes the pattern is similar to Android's intent system at a lower level.

- Listener-interface registration creates tight coupling and cumbersome dependency graphs as components grow.
- The event bus pattern centralizes communication: components register once and receive events through @Subscribe-annotated methods.
- Producers post events on the bus without needing to track listeners, reducing coupling.
- Testing simplifies because arbitrary events can be posted to simulate any application state without mocking multiple managers.
- Otto is Square's Guava-derived library that brings the event bus pattern to Android.