---
domain: android-kotlin
subdomain: desugaring
concept: java-8-desugaring
title: Android's Java 8 Support
sources:
  - title: "Android's Java 8 Support"
    url: "https://jakewharton.com/androids-java-8-support/"
---

# Android's Java 8 Support

Jake Wharton's article explains how Android's Java 8 language feature support works, focusing on lambdas. When Java source is compiled with javac, lambdas are encoded using invokedynamic bytecode, which Android did not support before API 26. To avoid restricting apps to modern devices, the Android toolchain runs a process called desugaring, converting lambdas into synthetic classes and methods that run on older API levels. The article traces this evolution from third-party Retrolambda through an experimental Eclipse-based compiler to the D8 dexer, which now performs desugaring during dexing.

Using a simple logger lambda, the article decodes the generated Dalvik bytecode: D8 creates a synthetic class (e.g., Java8$1) that implements the target interface, and the lambda body is moved to a synthetic static method on the original class so it can access private members. Method references are handled differently—D8 emits a direct call to the referenced method inside the generated class and captures the receiving instance as a field.

The article also reveals why D8 always desugars lambdas even when --min-api 26 is set. Although Android's runtime supports the invokedynamic bytecode, it lacks java.lang.invoke.LambdaMetafactory, the JDK class that bootstraps lambda creation at runtime. Hence Android must rely on compile-time desugaring, rather than runtime lambda instantiation.

- Java 8 lambdas compile to invokedynamic bytecode, which Android only supports natively on API 26+; desugaring is required for older devices.
- Desugaring converts lambdas into synthetic classes that implement the target interface and synthetic methods that contain the lambda body.
- The Android toolchain evolved from Retrolambda and an experimental ECJ-based compiler to D8, which integrates desugaring during dexing.
- D8 desugars lambdas even when min-api 26 is requested because Android lacks java.lang.invoke.LambdaMetafactory, the runtime bootstrap mechanism for invokedynamic lambdas.
- Method references are desugared by directly calling the target method and capturing the receiver, rather than generating an extra lambda-body method.