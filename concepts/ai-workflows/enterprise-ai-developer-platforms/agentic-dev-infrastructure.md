---
domain: ai-workflows
subdomain: enterprise-ai-developer-platforms
concept: agentic-dev-infrastructure
title: Uber's AI Infrastructure for Developers, From the Inside
sources:
  - title: "Uber's AI infra, from the inside"
    url: "https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside"
    author: "Gergely Orosz"
    date: "2026-10-14"
---

# Uber's AI Infrastructure for Developers, From the Inside

Uber's Distinguished Engineer Uday Kiran Medisetty describes how the company's decade of in-house developer tooling investment made it possible to build agentic AI tooling quickly. Uber built many systems itself because off-the-shelf software could not handle its scale or did not exist, including uOwn for ownership, M3DB for metrics, Cadence for durable workflows, and Morpheus for feature flags and experimentation. Cities are a first-class primitive that reaches down to physical infrastructure, with each city pinned to a cloud region and able to fail over to another.

A key architectural decision was a single AI Model Gateway built in 2023 to keep everything model- and harness-agnostic, supporting Anthropic, OpenAI, other vendors, and open models. It enabled AI Guard for security checks and latency measurement, per-user spend tracking, and audit logs and session traces. AIFX wraps supported harnesses like Claude Code, Codex, and OpenCode so engineers keep settings, skills, and plugins when switching. Uber uses a hybrid spend approach with allocated tiers, manager sign-off to exceed limits, and a CostCheck plugin that has helped reduce token costs by about 50% in recent months.

Code review remains human but is supported by AI review, screenshots and videos, and risk scores before a developer reviews a change. Uber declared an internal code red for CI after jobs more than doubled in a year, moving simple jobs like linting and build checks into the inner loop via the afx validate command before PRs are opened. PRs are now tagged by type—feature, bugfix, maintenance, testing, docs—because raw PR velocity is less meaningful when agents can generate many PRs; feature PRs are rising while maintenance PRs are falling.

Medisetty argues the engineer's job is increasingly about building context for agents, context engineering, multitasking, and verifying agent output to avoid regressions. Uber's seemingly fast AI tooling build rests on years of prior work: Minion built in 2025 runs on DevPods from 2017, the MCP Gateway leveraged existing Thrift and Protobuf registries, and Jaeger tracing aided Slate routing and the context graph. As he puts it, all the things built to make life easier for engineers also make it easier for agents.

- Uber's AI tooling was built quickly because it sits on a decade of in-house developer infrastructure like DevPods, Thrift/Protobuf registries, and Jaeger tracing.
- A single model- and harness-agnostic Model Gateway, built in 2023, enabled AI Guard security checks, per-user spend tracking, and audit visibility across vendors and open models.
- Uber uses hybrid AI spend controls with allocated tiers, manager approval to exceed limits, and CostCheck; token costs dropped about 50% in recent months.
- All PRs are still human-reviewed, but AI review, screenshots/videos, and risk scores precede review, and PRs are tagged by type because raw PR velocity is less meaningful with agents.
- The engineer's role is shifting toward context engineering, multitasking, and verifying agent output to prevent regressions.