---
domain: ai-workflows
subdomain: coding-agents
concept: agent-generated-service-emulator
title: AWS Releases a Free Local Emulator of AWS Built Entirely by Agents
sources:
  - title: "AWS Releases a Free Local Emulator of AWS Built Entirely by Agents"
    url: "https://www.infoq.com/news/2026/11/aws-emulator-local-testing/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-20"
---

# AWS Releases a Free Local Emulator of AWS Built Entirely by Agents

AWS has released AWS Emulator, a free, CC0-licensed local stand-in for more than 200 AWS services, generated from the company's public API models and aimed at the test loops of coding agents (InfoQ, 2026). Rather than a hand-built mock, the emulator is derived from API specifications, which lets it cover a broad surface of services without per-service manual implementation.

AWS states that agents wrote and maintain all of the code, and it publishes per-release fidelity scores so users can gauge how closely the emulator matches real behavior. This transparency is notable given that the tool is agent-authored end to end.

There are caveats: the documentation says the emulator does not evaluate IAM, so authorization behavior is not reproduced. Practitioners are reportedly split on trusting an emulator that nobody has reviewed, raising questions about reliability for test loops that depend on faithful service behavior.

- AWS Emulator is a free, CC0-licensed local emulator covering 200+ AWS services, generated from public API models.
- All code is written and maintained by agents, with per-release fidelity scores published.
- The emulator does not evaluate IAM, so authorization semantics are absent.
- Practitioners are divided on trusting an agent-built emulator that no human has reviewed.