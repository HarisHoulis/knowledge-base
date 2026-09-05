---
domain: android-kotlin
subdomain: bytecode-optimization
concept: source-level-bytecode-optimization
title: Optimizing Bytecode by Manipulating Source Code
sources:
  - title: "Optimizing Bytecode by Manipulating Source Code"
    url: "https://jakewharton.com/optimizing-bytecode-by-manipulating-source-code/"
    author: "Jake Wharton"
---

# Optimizing Bytecode by Manipulating Source Code

Jake Wharton explores how to optimize DEX bytecode by restructuring the generated Java source code rather than patching bytecode directly. He starts from a generated view-binding method that throws NullPointerException when a required view is missing. After switching from dx to D8, the exceptional branches are moved to the end of the method by D8, but the common path now loads the exception message prefix even when no exception occurs, which is undesirable. Wharton identifies an ideal bytecode layout with no jumps on the normal path, a single shared exception block, and the missing-view name supplied by a branch that jumps into that block (Jake Wharton, "Optimizing Bytecode by Manipulating Source Code").

- D8 inverts null checks to move exceptional paths to the end, but hoisting the shared exception-prefix string into the normal path is wasteful.
- The ideal bytecode has the success path flowing through without jumps and one de-duplicated exception block at the end.
- Removing the throw from the if body makes D8 treat the null cases as ordinary control flow, reintroducing jumps on the happy path.
- Nesting conditionals (or using an infinite loop or labeled block with break) produces the exact desired bytecode while flattening source code.
- A labeled block is a cleaner source-level construct than a non-looping while, even though both compile to the same bytecode.