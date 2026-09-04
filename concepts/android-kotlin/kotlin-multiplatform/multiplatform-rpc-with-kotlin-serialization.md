---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: multiplatform-rpc-with-kotlin-serialization
title: Simple Multiplatform RPC with Kotlin Serialization
sources:
  - title: "Simple Multiplatform RPC with Kotlin Serialization"
    url: "https://jakewharton.com/simple-multiplatform-rpc-with-kotlin-serialization/"
---

# Simple Multiplatform RPC with Kotlin Serialization

Jake Wharton describes using kotlinx.serialization to implement a simple unidirectional RPC between an Android app and a Cast display. The Android app and Cast display share Kotlin model objects in a multiplatform library. Initially, Moshi serialized models to JSON on Android, and the Cast side received already-deserialized JS objects via unsafeCast, which restricted models to JS-native collections like Array and prevented custom serialization. To overcome these limitations, they switched to kotlinx.serialization, which is reflection-free and multiplatform. Android uses Json.stringify to produce JSON, while the Cast display uses DynamicObjectParser to parse the incoming JS object directly through the same Kotlin serializer. This enables the use of List, custom serializers, and other library features while maximizing code reuse.

- kotlinx.serialization allows Kotlin models to be shared between Android and JS without losing Kotlin type features like List and custom serializers.
- DynamicObjectParser on the JS side can parse JS objects as if they were JSON, eliminating the need for unsafeCast or manual mapping.
- Sealed classes with polymorphic serialization provide a type discriminator in the JSON, enabling robust handling of event types.
- The Kotlin compiler's exhaustive when checks ensure all event types are handled on the Cast display, making the RPC system type-safe.
- This approach is suitable for simple RPC needs; more complex requirements like bidirectional streaming would warrant a system like gRPC.