---
domain: android-kotlin
subdomain: kotlin-inline-classes
concept: inline-class-database-ids
title: Inline Classes Make Great Database IDs
sources:
  - title: "Inline Classes Make Great Database IDs"
    url: "https://jakewharton.com/inline-classes-make-great-database-ids/"
---

# Inline Classes Make Great Database IDs

The article advocates using Kotlin's experimental inline classes to create type-safe database IDs. Since inline classes are erased at runtime, they add compile-time safety without runtime overhead. This is particularly useful for database models where many entities have the same underlying ID type, such as a Long.

By defining inline classes like CustomerId, InstrumentId, and PaymentId, and integrating them with SQLDelight, the generated query APIs become strongly typed. This prevents accidentally passing a PaymentId where a CustomerId is expected, a bug that would otherwise compile silently and fail at runtime. SQLDelight also automatically uses these types for model properties and query parameters, and may enforce foreign key type consistency in the future.

The article demonstrates a concrete example where a payment's own ID was mistakenly used to query payments by sender. The inline class caught the error at compile time, showing how this feature adds a layer of safety to database interactions with minimal effort.

- Inline classes wrap underlying values like Long with compile-time type safety while being erased at runtime.
- Using inline classes for database IDs prevents mixing up IDs of different entities in query arguments.
- SQLDelight can generate model objects and query functions that automatically use these inline classes.
- The approach catches erroneous ID usage at compile time rather than at runtime.