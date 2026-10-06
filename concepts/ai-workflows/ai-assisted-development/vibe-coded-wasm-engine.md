---
domain: ai-workflows
subdomain: ai-assisted-development
concept: vibe-coded-wasm-engine
title: pwasm 0.2a0: AI-Improved Pure Python WebAssembly Engine
sources:
  - title: "pwasm 0.2a0"
    url: "https://simonwillison.net/2026/Oct/1/pwasm/"
    author: "Simon Willison"
    date: "2026-10-01"
---

# pwasm 0.2a0: AI-Improved Pure Python WebAssembly Engine

pwasm is a pure Python WebAssembly engine that Simon Willison vibe-coded in January during his first bout of "AI mania" (simonwillison.net, 2026). After leaving it untouched since January, he turned Claude Opus 5.5 loose on it with a prompt to evaluate the current state, figure out what it would take to get the MicroPython and micro JavaScript experiments from his research repo working under it, and speed it up.

After 42 commits (with minimal follow-up prompting), pwasm now handles almost all of the WASM specification, and the wheel published to PyPI bundles working WASM builds of MicroPython, QuickJS, and Micro QuickJS.

Willison explicitly warns that he would not trust the project, hence the alpha version tag, but frames the result as an interesting demonstration: today's models can measurably improve on the work produced by models from 10 months earlier.

- pwasm is an entirely vibe-coded, pure Python WebAssembly engine originally built in January.
- Claude Opus 5.5 drove 42 commits with minimal follow-up prompting, expanding coverage to almost the full WASM spec.
- The PyPI wheel now bundles working WASM builds of MicroPython, QuickJS, and Micro QuickJS.
- The release is tagged alpha because the author would not trust it.
- The experiment illustrates newer models improving on the output of older models.