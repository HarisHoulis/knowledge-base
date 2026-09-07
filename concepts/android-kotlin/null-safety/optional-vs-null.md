---
domain: android-kotlin
subdomain: null-safety
concept: optional-vs-null
title: An Optional's Place in Kotlin
sources:
  - title: "An Optional's place in Kotlin"
    url: "https://developer.squareup.com/blog/an-optionals-place-in-kotlin"
---

# An Optional's Place in Kotlin

The article examines whether Kotlin needs an Optional type given its null-safe type system. It argues that nullability being first-class does not mean null is always permitted in all contexts. For instance, RxJava 2 disallows null values in its streams, so representing an absent response body requires an abstraction like Optional when using Retrofit with RxJava 2. [source: Square, "An Optional's place in Kotlin", https://developer.squareup.com/blog/an-optionals-place-in-kotlin]

Retrofit 2.3.0 introduced delegating converters for Guava and Java 8 Optional types. These converters do not perform byte-to-object conversion themselves; instead, they delegate to other converters (e.g., Moshi, Gson, Wire) and wrap the potentially-null result into an Optional. They are added alongside serialization converters in the Retrofit builder, allowing service methods to return Optional types. [source: Square, "An Optional's place in Kotlin", https://developer.squareup.com/blog/an-optionals-place-in-kotlin]

Although Retrofit 2.3.0 also includes JSR 305 annotations for explicit nullability in Java and Kotlin, the article concludes that annotations or a type system capable of modeling nullability are sometimes insufficient. Therefore, Optional retains its place in both Java and Kotlin for cases where null is not allowed. [source: Square, "An Optional's place in Kotlin", https://developer.squareup.com/blog/an-optionals-place-in-kotlin]

- Kotlin's nullable type system does not eliminate the need for Optional in contexts where null is prohibited, such as RxJava 2 streams.
- Retrofit 2.3.0 adds delegating converters for Guava and Java 8 Optional, which wrap nullable deserialized results.
- These Optional converters must be placed before the serialization converter in the Retrofit builder.
- JSR 305 annotations express nullability but cannot cover all absence-of-value scenarios, keeping Optional relevant.