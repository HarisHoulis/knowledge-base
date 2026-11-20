---
domain: ai-workflows
subdomain: coding-agents
concept: idiomatic-rust-rewrite-with-ai
title: RIIIR: Rewrite It In Idiomatic Rust (with AI)
sources:
  - title: "Presentation: RIIIR: Rewrite It In *Idiomatic* Rust (with AI)"
    url: "https://www.infoq.com/presentations/rust-ai-symposium-agent-client-protocol/"
    author: "Niko Matsakis"
    date: "2026-11-19"
---

# RIIIR: Rewrite It In Idiomatic Rust (with AI)

Niko Matsakis argues that AI makes Rust an ideal choice for modern production systems because the compiler's guardrails let developers skip the steep adoption hurdles normally associated with the language. Rather than relying solely on human expertise to learn idiomatic patterns, AI-assisted rewriting can move code toward idiomatic Rust while the compiler enforces correctness.

He introduces Symposium, an open-source, agent-oriented toolchain from the Rust Foundation, as the vehicle for this workflow. The talk also covers the Agent Client Protocol (ACP), which standardizes agent-to-tool extensibility so agents can plug into diverse enterprise developer workflows.

Together, the compiler-as-guardrail idea and ACP-based tooling point to a model where AI agents perform large-scale idiomatic rewrites and integrate with existing toolchains through a common protocol.

- AI lowers Rust adoption friction by leveraging compiler guardrails during rewriting
- Symposium is an open-source, agent-oriented toolchain from the Rust Foundation
- The Agent Client Protocol (ACP) standardizes agent-to-tool extensibility
- ACP aims to support diverse enterprise developer workflows