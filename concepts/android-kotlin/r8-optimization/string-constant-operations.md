---
domain: android-kotlin
subdomain: r8-optimization
concept: string-constant-operations
title: R8 Optimization: String Constant Operations
sources:
  - title: "R8 Optimization: String Constant Operations"
    url: "https://jakewharton.com/r8-optimization-string-constant-operations/"
    author: "Jake Wharton"
---

# R8 Optimization: String Constant Operations

R8 can optimize operations on string literals at compile time because string constants live in a dedicated bytecode section. For example, computing the length of a constant string is replaced with its hardcoded integer value, as shown with the WILDCARD constant in OkHttp; D8 can also perform this simple folding (Jake Wharton, 'R8 Optimization: String Constant Operations', https://jakewharton.com/r8-optimization-string-constant-operations/). The article explains that Java and Dalvik bytecode treat strings specially, storing both source literals and structural names in constant pools or string data sections.

The bigger win comes when inlining is combined with R8's SSA intermediate representation. By tracing variables back to string literals, R8 can transform and then dead-code-eliminate calls such as startsWith and the conditional around it. The example in the article starts with a patternHost method and, after inlining, results in a dex containing only pattern.substring(2), removing the WILDCARD string entirely.

Not every string operation is folded at compile time. Methods that return primitives (length, startsWith, isEmpty, equals, etc.) are safe because they do not add new string data. But operations that produce a new string, like substring and concatenation, are intentionally not evaluated because the resulting string would enlarge the string data section even though bytecode shrinks. The article notes this trade-off and links to issue trackers for future additions.

- R8 can compute primitive-valued string operations like length() and startsWith() at compile time when both receiver and arguments are constant strings.
- These optimizations combine with inlining, where R8's SSA form traces local variables back to literals, enabling dead-code elimination of always-true conditionals.
- Operations that return booleans/ints are folded because they don't add generated string entries, keeping the dex size neutral or smaller.
- Substring and string concatenation are not yet computed at compile time because the resulting new strings would increase the string data section, a trade-off that R8 currently avoids.