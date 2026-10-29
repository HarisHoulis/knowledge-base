---
domain: ai-workflows
subdomain: agentic-engineering
concept: supervisory-engineering
title: Fragments: October 28 — The Widening LLM Gap and Supervisory Engineering
sources:
  - title: "Fragments: October 28"
    url: "https://martinfowler.com/fragments/2026-10-28.html"
    author: "Martin Fowler"
---

# Fragments: October 28 — The Widening LLM Gap and Supervisory Engineering

Martin Fowler reflects on Andrej Karpathy's observation of a widening gap in how people perceive LLM capabilities: the general public sees a "derpy chatbot," most professionals see modest uplift, while a small sliver experiences "the vertigo of the curve going vertical" (Karpathy). Fowler notes that even free-tier tools remain unreliable enough to undermine their usefulness, and that this perception gap matters for understanding the broader landscape.

At O'Reilly's Foocamp unconference, Fowler encountered the bleeding-edge crowd. Coaches running agentic engineering immersion courses reported that the biggest impact was emotional rather than technical, since these tools challenge developers' identity. Enterprises, meanwhile, have "acquired a Swiss-army knife, but are only using the toothpick" — held back by risk aversion, security concerns like the lethal trifecta, and poor data readiness.

Annie Vella's framing of direct versus supervisory control (drawing on Endsley and Kiris's five-level automation model) resonates: coding agents increasingly close the loop themselves, moving developers from direct control to supervision. Vella cautions that unlike traditional automation, an AI agent's account of what it did may not match reality, requiring arguably more supervision. Her conclusion — redesign the job and the system in tandem, treating the SDLC as a control system to build and supervise — aligns with Fowler's view.

Other threads: Laurie Voss argues today resembles 1997 for AI investment (bubble valuations, but real payoff still ahead); Adam Tornhill asks whether years of coding were wasted, with Fowler betting on problem-solving and systems thinking over code-writing; Tim Bray highlights ethical and economic discomforts; Eric Evans's DDD Europe keynote video is now available; and Thoughtworks' Andy Nolan describes a token sourcing strategy that rents frontier models while owning open-weight capacity for IP-sensitive or high-volume workloads.

- Karpathy's perception gap: public, most professionals, and a bleeding-edge sliver experience LLM capabilities very differently at the same time
- Agentic engineering immersion courses show the biggest barrier is emotional/identity, not technical
- Enterprises underuse AI due to risk, security (lethal trifecta), and poor data readiness
- Vella's supervisory control framing: agents close the loop, but their self-reports can't be trusted, so supervision may need to increase
- Thoughtworks' token strategy classifies workloads by domain differentiation and security/sovereignty to rent frontier models and own open-weight capacity