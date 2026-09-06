---
domain: android-kotlin
subdomain: code-generation
concept: economics-of-generated-code
title: The Economics of Generated Code
sources:
  - title: "The Economics of Generated Code"
    url: "https://jakewharton.com/the-economics-of-generated-code/"
---

# The Economics of Generated Code

Jake Wharton explores how performance and size optimizations that are unidiomatic for handwritten code become worthwhile in code generation because a generator is written once, but its output is produced many times. He presents two Android/Dalvik examples where small generator changes yield broad benefits across hundreds of generated classes. The first concerns method reference counts: generated classes extending a shared base class still generate per-class virtual method references unless explicitly invoking methods via super. By changing generated code from getUnknownPairs() to super.getUnknownPairs(), method references collapse to a single shared reference point. The second example concerns string literals in error messages. Unique, full-sentence exception strings consume dozens of bytes each in the dex string table; using String.concat with a shared prefix reduces 22KB of string data to 33 bytes while reusing already-present field-name strings.

- Investing in more efficient generated code pays off because changes apply to hundreds or thousands of output locations.
- Generating non-super method calls on a superclass-typed field can inflate method reference counts; explicitly using super avoids this.
- R8 can optimize method references automatically, but not all users run R8, so generator-level fixes help everyone.
- String de-duplication in dex means splitting error messages into a shared prefix and variable ID significantly reduces binary size.
- Handwritten code should not adopt these optimizations, but code generators should consider them.