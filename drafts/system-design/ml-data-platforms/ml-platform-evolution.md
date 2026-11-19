---
domain: system-design
subdomain: ml-data-platforms
concept: ml-platform-evolution
title: Behind Booking.com's AI Evolution: The Unpolished Story
sources:
  - title: "Presentation: Behind Booking.com's AI Evolution: The Unpolished Story"
    url: "https://www.infoq.com/presentations/bookingcom-ml-data-platform-evolution/"
    author: "Jabez Eliezer Manuel"
    date: "2026-11-18"
---

# Behind Booking.com's AI Evolution: The Unpolished Story

Jabez Eliezer Manuel recounts the 20-year evolution of Booking.com's data management and machine learning platforms, tracing the path from scaled MySQL topologies to a modern cloud-based ML stack. The talk emphasizes the pragmatic, incremental nature of this journey rather than a clean top-down redesign.

A central theme is the migration away from Hadoop toward cloud architecture, alongside the construction of high-throughput model serving and feature stores. These systems now operate at roughly 400 billion predictions per day, underscoring the scale at which Booking.com's personalization runs.

Manuel also covers personalization and interleaved experimentation as core practices, and introduces the company's new agentic AI foundation as the next step in its platform evolution.

- Booking.com's ML and data platforms evolved incrementally over roughly 20 years rather than through a single redesign
- The company scaled MySQL topologies before sunsetting Hadoop in favor of cloud architecture
- Its model serving and feature stores handle about 400 billion predictions per day
- Personalization and interleaved experimentation are central practices, with a new agentic AI foundation now being built