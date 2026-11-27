---
domain: ai-workflows
subdomain: coding-agents
concept: software-factories-vs-exploration
title: Stop Building Software Factories — Justin McCarthy, Diffusion
sources:
  - title: "Stop Building Software Factories — Justin McCarthy, Diffusion"
    url: "https://www.youtube.com/watch?v=1S4hx3wgvBE"
    author: "AI Engineer"
    date: "2026-11-26"
---

# Stop Building Software Factories — Justin McCarthy, Diffusion

Justin McCarthy, founder and CEO of Diffusion, argues that teams should stop trying to industrialize every software effort into a "software factory." He notes that factory-style agent loops already showed promise even on the Claude 4 series models, though they were expensive in tokens and required complex hand-assembled designs; now that the pattern is widely understood, the real question is when it is appropriate (AI Engineer talk).

His core distinction is between exploration and production. When searching for product-market fit or entering new territory, we often don't yet know what we want, so industrializing an undefined process yields the wrong result or wastes time and money. In contrast, proven production work is already validated by customer money and usage, and its stability is built into the process, making it a better fit for automation.

McCarthy frames product qualities as "promises" — functionality, value and price, safety — that teams rarely want to break. For existing ("brownfield") products, these expectations can be encoded into loops, which he describes as taking input, output, and feedback. Borrowing the amplifier block-diagram analogy, he warns that breaking the feedback loop just amplifies noise, so the goal is to return precision to the system input, especially in brownfield environments.

- Stop forcing ideas and ambitions through an assembly-line "software factory" process when you don't yet know what you want
- Distinguish exploration/product-market-fit mode from proven production mode, where customer usage already validates the work
- Treat product qualities (functionality, price, safety) as "promises" that can be encoded into agent loops
- Loops need input, output, and feedback; without feedback you only amplify noise
- Brownfield systems benefit most from carefully closing the feedback loop