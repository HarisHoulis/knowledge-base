---
domain: web-dev
subdomain: javascript-code-readability
concept: avoid-nesting-closures
title: Why I avoid nesting closures
sources:
  - title: "Why I avoid nesting closures"
    url: "https://kentcdodds.com/blog/why-i-avoid-nesting-closures"
    author: "Kent C. Dodds"
    date: "2019-12-13"
---

# Why I avoid nesting closures

Kent C. Dodds explains that he prefers to move nested functions out to module scope so they sit as close to the left side of the screen as reasonably possible. The main reason is cognitive load: a nested closure can access variables from the enclosing function, so readers must think about those outer variables while working inside the inner function. Once the function is extracted, those variables are impossible to access, reducing what has to be kept in mind (Kent C. Dodds, 2019).

Dodds notes that performance and testing arguments exist but are usually weak. Recreating a closure on every call is not a meaningful concern in typical code, and exporting a helper for isolated testing is only occasionally useful. He also acknowledges that nesting is sometimes unavoidable, such as when an inner function truly depends on an outer parameter; in those cases he may leave the code as-is rather than force an extraction.

He frames the preference as a tendency, not a rule, and says he is not religious about it. The broader goal is to reduce trivial mental overhead so brain space can be reserved for more important problems. He also warns against turning the idea into an ESLint rule, while suggesting it as something to consider when simplifying complicated code (Kent C. Dodds, 2019).

- Prefer extracting nested functions to module scope to reduce the number of variables an inner function can capture.
- Nested closures increase cognitive load because readers must consider outer variables and possible variable shadowing.
- Performance gains from avoiding closure recreation are usually negligible, and isolated testing is only sometimes worth extracting.
- Nesting can be necessary when the inner function depends on outer variables; Dodds treats the preference as a nuanced tendency, not a strict rule.
- Do not turn this style preference into an ESLint rule; use it as a heuristic for simplifying complex code.