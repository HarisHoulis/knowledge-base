---
domain: engineering-culture
subdomain: cognitive-debt
concept: cognitive-debt
title: AI is removing the middle class of software engineering
sources:
  - title: "Quoting Florian Herrengt"
    url: "https://simonwillison.net/2026/Aug/12/florian-herrengt/"
    author: "Simon Willison"
    date: "2026-08-12T15:08:47+00:00"
---

# AI is removing the middle class of software engineering

The quote highlights a common failure mode in AI-assisted development: users report a persistent bug, but the team cannot fix it because the project has become an unmanageable tangle of layers and services. Even AI tools, like 'Fable' or 'Claude', fail to provide reliable solutions, leaving the team staring at confident but unverifiable text (Willison, 2026). The developer responsible for the feature admits they don't know where the data comes from and resorts to asking Claude for an explanation, demonstrating the loss of human understanding over systems that AI helped create (Willison, 2026). This scenario illustrates 'cognitive debt'—the accumulation of code and architecture that no one fully comprehends, often exacerbated by AI-generated contributions. The author argues that this trend is removing the middle class of software engineering, as projects become so convoluted that even experienced engineers cannot reason about them, leading to a reliance on AI that perpetuates the problem (Willison, 2026).

- AI-generated code can create opaque layers and services that no one on the team understands.
- Developers often depend on AI to explain code, but the AI's outputs are not guaranteed to be true or accurate.
- Debugging becomes nearly impossible when the system architecture is beyond human comprehension.
- This 'cognitive debt' may eliminate mid-level engineering roles that traditionally maintain and understand the codebase.
- The solution is not to rely on AI more, but to enforce clarity and human oversight in software development.