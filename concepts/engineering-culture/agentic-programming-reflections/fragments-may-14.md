---
domain: engineering-culture
subdomain: agentic-programming-reflections
concept: fragments-may-14
title: Fragments: May 14
sources:
  - title: "Fragments: May 14"
    url: "https://martinfowler.com/fragments/2026-05-14.html"
    author: "Martin Fowler"
    date: "2026-05-14"
---

# Fragments: May 14

In this fragment, Martin Fowler shares observations from a retreat on the future of software development with agentic programming. Key highlights include a behavioral clone of GNU Cobol in Rust built in just 3 days, demonstrating LLMs' ability to port code effectively. Attendees also proposed using interrogatory LLMs to verify large specifications by interviewing human experts, and noted that reading an organization's change-control guidelines reveals the 'scar tissue' of past failures (Fowler, 2026).

Legacy modernization is also reconsidered: while 'lift and shift' was often dismissed, the reduced cost of LLM-based porting makes it a sensible first step. For complex financial systems spanning multiple jurisdictions, building simpler individual systems per jurisdiction and using LLMs to maintain consistency is emerging as a viable approach. The conversation touched on bounded contexts and the question of duplication in software design.

Concerns about junior developers were prevalent, with pair programming highlighted as a key mechanism for transferring judgment about agentic programming. Martin also reflects on structured-prompt-driven development, emphasizing that human review in AI-assisted workflows is essential for learning and skill growth. He cites James Pritchard's argument that LLMs are often better used as functions than as autonomous agents, and that skills are frequently overused in favor of clean architecture (Fowler, 2026).

Finally, Martin notes Kyle Kingsbury's pessimistic article on AI's future, acknowledging both hope and doomerism. He personally sees powerful technology as a bus one must board to influence its direction, and shares a brief personal aside about an elbow injury and the challenges of voice input for his writing style (Fowler, 2026).

- LLMs are highly effective at porting code, making lift-and-shift a logical first step in legacy modernization.
- Human review in AI-assisted development is crucial for long-term skill growth and judgment.
- Agents are often overused; LLMs are better suited as predictable function calls in known workflows.
- Skills should be used sparingly; a clean codebase and minimal configuration yield better results.
- Pair programming remains a vital tool for transferring agentic programming skills to juniors.