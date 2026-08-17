---
domain: engineering-culture
subdomain: ai-agentic-programming
concept: fragments-may-14
title: Fragments: May 14
sources:
  - title: "Fragments: May 14"
    url: "https://martinfowler.com/fragments/2026-05-14.html"
    author: "Martin Fowler"
    date: "2026-05-14"
---

# Fragments: May 14

The article summarizes insights from a retreat on agentic programming. Notable examples include a team porting GNU Cobol to Rust in 70K lines within 3 days, demonstrating LLMs' capability for rapid code porting. Also discussed was an "interrogatory LLM" approach where an LLM interviews human experts to verify specification correctness, echoing the author's earlier concept. Change-control board guidelines are highlighted as "scar tissue" revealing past failures, valuable for understanding organizational history ([Fragments: May 14](https://martinfowler.com/fragments/2026-05-14.html)).

On legacy modernization, the article notes a shift: given LLMs' porting abilities, "lift and shift" should now be the first step in migration, as the cost has dropped and a new platform enables cheaper evolution. In the financial sector, where multi-jurisdiction products create complex rule-consistency problems, LLMs could enable building simpler per-jurisdiction systems while maintaining cross-system consistency. A key design question emerges: how LLMs can help manage the tension between duplication and consistency across bounded contexts.

The article also addresses junior developer training, suggesting pair programming to transfer judgment in an agentic world. Chaos engineering concepts are extended to AI, proposing deliberate hallucination injection to test detection systems. References to SPDD's FAQ emphasize that human review allows learning from AI's choices, which should be preserved. Pritchard's perspective is cited, arguing that LLMs are better used as functions than agents, and that skills files are overused—clean codebases and architecture trump configuration. Finally, Kingsbury's critical article "The Future of Everything is Lies, I Guess" is discussed, contrasting pessimism with the author's stance of being both "hoper and doomer" who chooses to ride the bus of powerful technology.

- LLMs can dramatically accelerate code porting; a GNU Cobol compiler was cloned in Rust in 3 days (70K lines).
- Lift-and-shift is recommended as the first step in legacy migration now that LLMs reduce cost; it enables cheaper evolution.
- An 'interrogatory LLM' can interview human experts to validate large spec documents.
- Pair programming remains vital for transferring judgment to junior developers in AI-augmented work.
- LLMs are often better used as predictable functions rather than autonomous agents, and skills files should be minimized in favor of clean architecture.