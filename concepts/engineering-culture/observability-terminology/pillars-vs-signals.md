---
domain: engineering-culture
subdomain: observability-terminology
concept: pillars-vs-signals
title: How many pillars of observability can you fit on the head of a pin?
sources:
  - title: "How many pillars of observability can you fit on the head of a pin?"
    url: "https://charity.wtf/p/the-pillar-is-a-lie"
    author: "Charity Majors"
    date: "Thu, 30 Oct 2025 05:27:38 GMT"
---

# How many pillars of observability can you fit on the head of a pin?

Charity Majors argues that "pillar" is a marketing term, not a technical one, and that the language of pillars traps engineers in an outdated mental model. She contrasts this with "signal," which is a technical term defined by OpenTelemetry: traces, metrics, logs, and baggage are supported signal types, with events and profiles in development. OTel does not mention pillars at all, so profiling is technically a signal, but whether it's a "pillar" is a vendor claim ([source](https://charity.wtf/p/the-pillar-is-a-lie)).

Majors explains that vendors use the pillars concept to sell siloed storage for each signal type, leading to massive data duplication and cost multipliers. She contrasts the "multiple pillars model" (observability 1.0) with the "unified storage model" (o11y 2.0), where all signals are stored together in one database, preserving context and enabling users to zoom in and out without hopping between tools. She cites her own writing and Honeycomb's architecture to illustrate this ([source](https://charity.wtf/p/the-pillar-is-a-lie)).

She also addresses profiling specifically: in a unified world, profiling means finer resolution, like zooming from rooftops to license plates. However, she notes that most teams that think they need profiling actually need better tracing, and that the "pillar" framing is a sales tactic rather than a technical necessity ([source](https://charity.wtf/p/the-pillar-is-a-lie)).

- Pillar is a marketing term; signal is a technical term; OTel defines signals but never mentions pillars.
- Profiling is a telemetry signal type, but whether it's a 'pillar' is a vendor-driven claim.
- The multiple pillars model duplicates data and raises costs; the unified storage model (o11y 2.0) stores data once and lets you zoom across signals.
- Unified storage eliminates 'bunny hopping' between siloed tools by deriving metrics, logs, and traces from the same underlying data.
- Most users who think they need profiling data actually need good distributed tracing first.