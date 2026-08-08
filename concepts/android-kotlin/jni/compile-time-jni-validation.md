---
domain: android-kotlin
subdomain: jni
concept: compile-time-jni-validation
title: Compile-time validation of JNI signatures
sources:
  - title: "Compile-time validation of JNI signatures"
    url: "https://jakewharton.com/compile-time-validation-of-jni-signatures/"
    author: "Jake Wharton"
---

# Compile-time validation of JNI signatures

JNI requires Java native methods to be paired with C functions whose names encode the full Java signature, including package, class, and parameter types. If any part of the encoding is wrong, the failure appears only at runtime as an UnsatisfiedLinkError. To eliminate this entire class of errors, Jake Wharton shows how javac's -h flag can automatically generate a C header from Java native method declarations, enabling the C compiler to validate the signatures at build time (Jake Wharton, "Compile-time validation of JNI signatures", https://jakewharton.com/compile-time-validation-of-jni-signatures/).

Gradle automatically configures javac with -h for JVM projects, making the generated headers available as an include directory. However, Kotlin cannot use javac -h because it does not produce Java sources. The article explores workarounds: writing native stubs in Java (which the Kotlin compiler can reference), using the removed javah tool on old JDKs, or building a custom tool. Each approach has tradeoffs, but all aim to keep JNI signatures validated before runtime.

A longer-term solution is the Java 22+ Foreign Function & Memory (FFM) API, which inverts ownership. Using jextract, you generate Java bindings from C headers, so changes to native code now break Java compilation rather than the other way around. This eliminates the need for manually maintained JNI signatures and shifts validation to the language boundaries where the native API is the source of truth (Jake Wharton, "Compile-time validation of JNI signatures", https://jakewharton.com/compile-time-validation-of-jni-signatures/).

- javac -h generates C headers from Java native methods, turning JNI signature mismatches into compile-time errors.
- Gradle automatically applies javac -h for JVM projects, making header generation part of the standard build.
- Kotlin has no built-in equivalent; Java stubs, javah, or custom tools are necessary workarounds.
- The Java 22+ FFM API and jextract reverse the approach: native header changes cause Java compilation failures, ensuring correctness from the native side.