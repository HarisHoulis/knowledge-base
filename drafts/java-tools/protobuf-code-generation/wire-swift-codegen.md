---
domain: java-tools
subdomain: protobuf-code-generation
concept: wire-swift-codegen
title: Wire Support For Swift, Part 1
sources:
  - title: "Wire Support For Swift, Part 1"
    url: "https://code.cash.app/wire-support-for-swift-part-1"
---

# Wire Support For Swift, Part 1

Square's Wire compiler, which already generates Java and Kotlin from protocol buffer files, adds support for Swift (https://code.cash.app/wire-support-for-swift-part-1). While Google maintains the official `protoc` compiler and Apple maintains the official Swift plugin, Wire exists for technical and ergonomic reasons: the original Java implementation addressed Android's method-count limits and the bloat of `protoc` output, and it also serves as a tool to help protos scale with a large organization by simplifying the feature set while staying compatible with the wire format.

- Wire adds Swift code generation to its existing Java and Kotlin support, producing a simpler, more idiomatic API than `protoc` while remaining wire-format compatible.
- Wire omits groups, dynamically loaded extensions (extensions must compile together, enabling compile-time conflict checking), and default values—making optional fields simply nullable.
- Roots and prunes let you intelligently trim the proto message tree, shrinking the generated API and shipping binary while guaranteeing a complete dependency tree.
- A manifest-driven module system handles Swift's compilation-unit-based namespacing, letting types be assigned to modules at the type level rather than the file level.