---
domain: java-tools
subdomain: kotlin-bitmasks
concept: corner-character-mapping
title: Sixteen Corners
sources:
  - title: "Sixteen corners"
    url: "https://jakewharton.com/sixteen-corners/"
    author: "Jake Wharton"
---

# Sixteen Corners

The article describes a challenge encountered while building Picnic, a Kotlin library for rendering terminal tables: how to select the correct box-drawing character for each corner. A corner requires drawing up/down/left/right segments based on adjacent cell borders, yielding 16 possible characters. Rather than using nested conditionals, the author maps the four booleans to bits and uses the resulting integer as an index into a string of all 16 corner characters, producing cleaner and more efficient code. The same bit representation is then exploited to write a single test table that visually exercises all 16 corners at once.

- Four booleans representing a corner's drawn segments can be treated as bits to produce an index into a hard-coded string of 16 box-drawing characters.
- Nested conditionals can be replaced by bitwise OR of shifted boolean values for simpler corner lookup.
- A single test table designed to include all 16 corners offers a more compact and readable test than writing 16 separate cases.
- Counting valid permutations of corner characters was optimized by recursive backtracking with early pruning and a bitmask for used corners, reducing runtime from over an hour to 57 ms.
- Only 652 out of 20,922,789,888,000 possible permutations pass segment-level validation, and some still produce orphan corners that are not expressible by actual cell borders.