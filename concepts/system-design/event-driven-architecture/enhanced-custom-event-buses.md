---
domain: system-design
subdomain: event-driven-architecture
concept: enhanced-custom-event-buses
title: AWS Introduces Enhanced Custom Event Buses for EventBridge
sources:
  - title: "AWS Introduces Enhanced Custom Event Buses for EventBridge"
    url: "https://www.infoq.com/news/2026/10/aws-enhanced-eventbridge-buses/"
    author: "Renato Losio"
    date: "2026-10-11"
---

# AWS Introduces Enhanced Custom Event Buses for EventBridge

AWS announced enhanced custom event buses for Amazon EventBridge, enabling organizations to share a centralized bus across accounts. The update targets multi-account event routing by allowing a single bus to serve as a shared backbone rather than requiring per-account bus duplication.

The enhanced buses add ordered delivery, simplified subscriber management, event replay, and content-based deduplication. These capabilities address common event-driven architecture concerns: preserving event order, managing who receives which events, recovering from downstream failures by replaying events, and suppressing duplicate events based on their content.

AWS also introduced a new publisher/subscriber-based pricing model alongside the feature set, shifting cost alignment toward the publish and subscribe patterns central to event-driven designs.

- Enhanced custom event buses can be shared centrally across AWS accounts.
- New capabilities include ordered delivery, simplified subscriber management, event replay, and content-based deduplication.
- A new publisher/subscriber-based pricing model accompanies the feature.