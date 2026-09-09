---
domain: java-tools
subdomain: open-source-libraries
concept: purpose-built-libraries
title: MimeCraft, JavaWriter, and ProtoParser
sources:
  - title: "MimeCraft, JavaWriter, and ProtoParser"
    url: "https://developer.squareup.com/blog/mimecraft-javawriter-and-protoparser"
    author: "Jake Wharton"
---

# MimeCraft, JavaWriter, and ProtoParser

The post describes three small, focused libraries Square uses to solve specific problems, following the rule 'perform one task and perform it well'. MimeCraft provides a fluent API for building form-encoded and multipart request bodies, which can write directly to an OutputStream and supply header information like MIME type and content length, for use with HTTP clients like OkHttp.

- MimeCraft offers terse APIs for form-encoding and multipart bodies without heavyweight HTTP abstractions.
- ProtoParser parses .proto files into an object representation without requiring protoc, enabling alternate documentation, validation, and code generation.
- JavaWriter is a simple declarative helper for generating Java source code, developed alongside Dagger and intentionally delegates code structure to its caller.
- These libraries are intentionally tiny in scope and purpose-built for specific tasks across Square's infrastructure.