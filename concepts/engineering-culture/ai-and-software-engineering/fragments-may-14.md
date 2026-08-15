---
domain: engineering-culture
subdomain: ai-and-software-engineering
concept: fragments-may-14
title: Fragments: May 14
sources:
  - title: "Fragments: May 14"
    url: "https://martinfowler.com/fragments/2026-05-14.html"
    author: "Martin Fowler"
---

# Fragments: May 14

Martin Fowler's May 14 'Fragments' reflects on the future of software engineering in the age of agentic programming, drawing from a retreat at Mechanical Orchard and his own reading. A notable story involves a team building a behavioral clone of the GNU Cobol compiler in Rust, producing 70K lines in just 3 days, which Fowler cites as evidence of LLMs' ability to port code effectively (Fowler, 2026). He also discusses how LLMs can interrogate human experts to verify specification correctness, an 'Interrogatory LLM' approach, and highlights the value of reading an organization's change-control board guidelines as a window into its historical 'scar tissue'.

Fowler revisits the 'lift and shift' pattern, noting that while it was previously dismissed as a missed opportunity due to feature bloat, LLMs have lowered the cost of porting so dramatically that it should now be the first step in legacy migration. He also raises the idea of using agentic programming to build separate, simpler systems for each jurisdiction in financial products, with LLMs ensuring consistency. On the topic of AI reliability, he cites James Pritchard's argument that LLMs are better used as functions than as autonomous agents, since agents are unpredictable and harder to debug, and warns against over-using skills configuration, recommending a clean codebase and clear patterns instead.

The piece also touches on teaching judgment to junior developers via pair programming, the potential for a 'Chaos Monkey for AI' to test hallucination detection, and the darker side of AI raised by Kyle Kingsbury's long article, which questions the societal impact and ethical responsibilities of AI engineers. Fowler, identifying as both a 'hoper and a doomer', acknowledges the risks but chooses to stay on the 'big bus' of technological change, hoping to influence its direction.

- LLMs excel at porting code to new platforms, making lift-and-shift a viable first step in legacy modernization, but not the final destination.
- Specifications can be validated by having an LLM interview human experts, a pattern called 'Interrogatory LLM'.
- Agents should be limited to unpredictable steps; known workflows are better implemented as deterministic LLM function calls or program code.
- Skills folders are often overused; improving codebase clarity and patterns yields better LLM test generation than explicit skills.
- Pair programming remains a key tool for transferring judgment to junior developers in an agentic programming world.