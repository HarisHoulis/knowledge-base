---
domain: ai-workflows
subdomain: agentic-code-maintenance
concept: prose-as-code-maintenance
title: Agents Made Code Free. Maintaining It Didn't Get Cheaper.
sources:
  - title: "Agents Made Code Free. Maintaining It Didn't Get Cheaper. - Dmitry Buykin, Maersk"
    url: "https://www.youtube.com/watch?v=oeknLUsN_GE"
    author: "AI Engineer"
    date: "2026-11-11"
---

# Agents Made Code Free. Maintaining It Didn't Get Cheaper.

Dmitry Buykin (Maersk) describes how code-writing agents made code cheap but also made entropy cheaper: in one project his agents generated so much unused boilerplate and tests that he deleted it all and rewrote the project, losing useful parts, and the chaos returned once agents kept writing. Rewriting didn't help, so he drew a line: stay below the threshold where more changes arrive than anyone can verify, using small weekly cleanups and feedback built into the system rather than drowning in chaos or breaking what people use.

A large share of the system—roughly three-quarters by his estimate—is prose (instructions for agents), and prose needs an engineering approach too. Borrowing mutation testing, he found that breaking a sentence rarely turned a test red, because prose has no compiler; so they built one, linking modified files to a registry and tracking agent 'walks' through the text. When agents repeatedly walk the same path, that path becomes a workflow tool and the text they followed is deleted.

Correctness ultimately depends on people, not tests: business experts see the rules while developers see what's under the water, where most mistakes hide. One document serves two readers—agents read accurate blocks, experts read and sign the surrounding text—and experts correct assignments one at a time while agents work the same text all day, with every accepted or rejected result tracked to show where human judgment is still needed. Agents alone cannot build a complex system; they fix what is easy to see and destroy consistency along the way.

- Code-writing agents made code cheap but made entropy even cheaper; unbounded agent output forced a full rewrite that still didn't stop the chaos.
- Set a verification threshold: stay below the volume of changes anyone can verify, using small weekly cleanups and built-in feedback.
- Prose instructions (about 3/4 of the system) need engineering rigor—mutation testing rarely caught issues, so they built a compiler-like registry and tracked agent 'walks'.
- Correctness depends on human experts, not tests: business experts know the rules, developers see the hidden connections, and both must be involved from the start.
- Repeated agent paths should be converted into workflow tools, deleting the prose they followed.