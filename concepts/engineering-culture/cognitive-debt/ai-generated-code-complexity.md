---
domain: engineering-culture
subdomain: cognitive-debt
concept: ai-generated-code-complexity
title: AI is removing the middle class of software engineering
sources:
  - title: "AI is removing the middle class of software engineering"
    url: "https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html"
    author: "Florian Herrengt"
    date: "2026-08-12"
  - title: "Quoting Florian Herrengt"
    url: "https://simonwillison.net/2026/Aug/12/florian-herrengt/"
    author: "Simon Willison"
    date: "2026-08-12"
---

# AI is removing the middle class of software engineering

Florian Herrengt describes a scenario where a team repeatedly fails to fix a recurring bug in a feature built by an engineer who no longer understands how the code works. The developer admits they do not know where the data comes from and suggests asking Claude, an AI assistant, to explain. Herrengt highlights the irony that even AI tools like Fable cannot resolve the issue, while the team watches an endless wall of confident but unverifiable text from the AI. The project has become so layered and convoluted that no one on the team can reasonably understand it, leading to a form of cognitive debt where maintainability and debugging are compromised. This illustrates the risk of AI-generated code accumulating without human oversight, potentially making junior and mid-level engineers dependent on AI while eroding their ability to reason about the system as a whole (Herrengt, 2026, as quoted by Willison, 2026).

- AI-generated code can create systems that no single team member fully understands.
- Even advanced AI tools struggle to debug complex, AI-generated codebases, as shown by the recurring bug in the example.
- Relying on AI for code generation without proper review fosters cognitive debt and reduces system transparency.
- This trend may eliminate the 'middle class' of software engineers who traditionally bridge the gap between business logic and implementation.
- Teams risk losing the ability to reason about their own projects as AI output becomes an opaque dependency.