---
domain: android-kotlin
subdomain: kotlin-library-design
concept: public-api-compatibility
title: Public API challenges in Kotlin
sources:
  - title: "Public API challenges in Kotlin"
    url: "https://jakewharton.com/public-api-challenges-in-kotlin/"
    author: "Jake Wharton"
---

# Public API challenges in Kotlin

The article compares Java and Kotlin representations of a value type like Person and shows how adding a new property to a Kotlin data class can silently break binary compatibility. While a Java class can evolve by preserving old constructors and adding fields/getters, a Kotlin data class's generated componentN() and copy() methods change signature as soon as a property is added, causing NoSuchMethodError for existing callers (Jake Wharton, Public API challenges in Kotlin, https://jakewharton.com/public-api-challenges-in-kotlin/). Even appending properties only protects componentN(); copy() and copy$default() always change (Jake Wharton, Public API challenges in Kotlin, https://jakewharton.com/public-api-challenges-in-kotlin/).

The recommended solution is to avoid the data modifier on public API types and write equals(), hashCode(), toString(), and any required copy() functions manually. Old copy() overloads can be preserved in bytecode by marking them @Deprecated(level = HIDDEN), so existing callers keep working while new callers only see the latest version (Jake Wharton, Public API challenges in Kotlin, https://jakewharton.com/public-api-challenges-in-kotlin/).

The article also discusses Java interop. A Builder is useful for Java callers, but fluent setters must be manually written; using plain public vars in Kotlin generates void setters incompatible with method chaining. The @set:JvmSynthetic annotation can hide the void setter from Java while still allowing Kotlin property access. Since private constructors cannot be hidden from Java, Kotlin callers can be served with top-level factory functions marked @JvmSynthetic, though these face the same signature-compatibility problems as copy and require hidden deprecated overloads. An alternative is a DSL-style factory function taking a builder initializer, which remains source- and binary-compatible as properties evolve (Jake Wharton, Public API challenges in Kotlin, https://jakewharton.com/public-api-challenges-in-kotlin/).

- Kotlin data classes generate componentN() and copy() methods whose signatures change when properties are added, breaking binary compatibility for library consumers.
- Appending new properties at the end preserves componentN(), but copy() and copy$default() signatures still change.
- For public value types that may evolve, avoid 'data' and manually implement equals/hashCode/toString and copy/factory overloads, hiding obsolete signatures with @Deprecated(level = HIDDEN).
- Java-friendly builders require fluent setter functions; use @set:JvmSynthetic on public vars to keep Kotlin property syntax while hiding the void setter from Java.
- Kotlin factory functions or builder-DSLs hidden with @JvmSynthetic can provide idiomatic construction while preserving compatibility as properties are added.