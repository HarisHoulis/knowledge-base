---
domain: ai-workflows
subdomain: llm-security
concept: llm-threat-model
title: LLM Security Basics: The Full Threat Model
sources:
  - title: "LLM Security Basics: The Full Threat Model"
    url: "https://blog.bytebytego.com/p/llm-security-basics-the-full-threat"
    author: "ByteByteGo"
    date: "Mon, 03 Aug 2026 15:31:14 GMT"
---

# LLM Security Basics: The Full Threat Model

Almost every LLM vulnerability traces to the fact that a language model receives instructions and data as a single sequence of tokens, with no marker separating commands from information (ByteByteGo, 2026). This enables prompt injection, both direct and indirect, as demonstrated by the EchoLeak incident where Microsoft 365 Copilot was manipulated via a hidden instruction in an email to transmit internal files without user interaction. Unlike SQL parameterization, no equivalent separation exists for natural language, making filtering porous and defense-in-depth essential.

- LLMs cannot distinguish between instructions and data in their input, making prompt injection (direct and indirect) a fundamental vulnerability.
- The OWASP Top 10 for LLM applications can be mapped onto a pipeline of input, retrieval, model, tools, output, and supply chain stages.
- The 'lethal trifecta'—access to private data, exposure to untrusted content, and an outbound channel—creates the highest material risk when combined in a single agent.
- Model theft and training-data extraction are real but often bounded; the more common risks lie in excessive agency and improper output handling.
- Supply chain compromise and serialization-based attacks (e.g., nullifAI) highlight the need for model provenance and safer serialization formats.