---
domain: android-kotlin
subdomain: d8-r8
concept: vendor-version-vm-bugs
title: Avoiding Vendor- and Version-Specific VM Bugs
sources:
  - title: "Avoiding Vendor- and Version-Specific VM Bugs"
    url: "https://jakewharton.com/avoiding-vendor-and-version-specific-vm-bugs/"
---

# Avoiding Vendor- and Version-Specific VM Bugs

D8 is primarily responsible for dexing Java bytecode into Dalvik bytecode for Android's VM, but this process is not a solved problem. When D8 was built, it uncovered vendor-specific and version-specific bugs in different VMs. For example, the Java bitwise-not operation is compiled to an xor with -1 in Java bytecode. While Dalvik has a dedicated not-int instruction, the old dx tool never emitted it, so some vendor JITs do not support it. To avoid crashes, D8 avoids not-int unless the minimum API level is 21 or higher, which guarantees ART support [1]. Similarly, a vendor-specific JIT bug crashes when a non-zero check immediately follows a less-than-zero check after cmp-long; D8 avoids this by emitting a second cmp-long when targeting older APIs, but uses the efficient single cmp-long when targeting API 21+ [1].

- D8 may avoid valid Dalvik instructions like not-int because the predecessor dx never used them and some vendor JITs do not support them.
- Passing --min-api 21 to D8 enables more efficient bytecodes such as not-int and deduplicated cmp-long sequences.
- A vendor-specific JIT bug on old Android versions caused crashes when a cmp-long result was checked for non-zero immediately after a less-than-zero check, requiring D8 to duplicate the cmp-long operation.
- Android 6.0's dex2oat AOT compiler could crash on highly recursive methods due to inlining analysis; D8 inserts a catch-and-rethrow block to disable the analysis when targeting API levels below 24.