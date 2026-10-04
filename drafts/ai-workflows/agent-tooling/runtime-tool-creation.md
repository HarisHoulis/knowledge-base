---
domain: ai-workflows
subdomain: agent-tooling
concept: runtime-tool-creation
title: Agents That Write Their Own Tools at Runtime
sources:
  - title: "Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS"
    url: "https://www.youtube.com/watch?v=33Oct2hqGnk"
    author: "Sandhya Subramani (AI Engineer)"
    date: "2026-10-04"
---

# Agents That Write Their Own Tools at Runtime

Sandhya Subramani (AWS) argues that most agents today cannot fix themselves at runtime: when something breaks in production, you typically have to stop the agent, fix it yourself, and restart it (Subramani, AI Engineer talk). Her talk demonstrates the alternative — an agent that recognizes a missing capability, writes a new tool on the fly, and immediately uses it without restarting anything.

The demo starts with a minimal `agents.py` whose toolbox contains no tool files at all — only a system prompt and three callable tools (Subramani). Asked to solve a math equation, the agent creates a `math_calculator.tool` with functions like min and max, then calls it to return a square root. Asked something unexpected — counting characters in a word — the agent determines none of its existing tools fit, writes a character counter, and invokes it. It also applies the new tool unprompted when the speaker just types in letters.

Subramani frames the pattern as a "meta-toolbox" built on Strands Agents, the open-source agent platform from AWS, and says the whole mechanism reduces to three tool types — an editor, a shell, and a boot tool — plus a system prompt that enables the behavior. In her framing, this is a highly specialized capability meant for embedding into daily engineering work rather than a general-purpose feature.

- Agents that write their own tools at runtime can create and immediately invoke a new capability without stopping or restarting the process.
- The demonstration agent ships with no tool files in its toolbox — only a system prompt and three tools — yet generates a `math_calculator.tool` on demand and later a character counter.
- The implementation is described as a "meta-toolbox" requiring only three tool types: an editor, a shell, and a boot tool, plus an enabling system prompt.
- It is built on Strands Agents, AWS's open-source agent platform, and is positioned as a specialized pattern for everyday development work.