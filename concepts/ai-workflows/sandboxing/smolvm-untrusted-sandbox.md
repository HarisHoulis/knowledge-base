---
domain: ai-workflows
subdomain: sandboxing
concept: smolvm-untrusted-sandbox
title: smolmachines/smolvm as a sandbox for untrusted Python & JavaScript
sources:
  - title: "smolmachines / smolvm as a sandbox for untrusted Python & JavaScript"
    url: "https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/"
    author: "Simon Willison"
    date: "2026-08-19"
  - title: "Research: smolmachines-untrusted-sandbox"
    url: "https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox#readme"
    author: "Simon Willison"
    date: "2026-08-19"
  - title: "Notes: smolmachines-untrusted-sandbox"
    url: "https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/notes.md"
    author: "Claude Fable 5"
    date: "2026-08-19"
  - title: "GitHub Actions workflow: smolvm-sandbox-test"
    url: "https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/.github/workflows/smolvm-sandbox-test.yml"
    author: "Simon Willison"
    date: "2026-08-19"
  - title: "Test script: run-tests.sh"
    url: "https://github.com/simonw/research/blob/5e6861e54441472d194de96b49b901fd99ebc153/smolmachines-untrusted-sandbox/run-tests.sh"
    author: "Simon Willison"
    date: "2026-08-19"
---

# smolmachines/smolvm as a sandbox for untrusted Python & JavaScript

Simon Willison explores using smolmachines.com and its smolvm tool as a fast, secure sandbox for running untrusted Python and JavaScript code. The goal is to execute user-provided tasks like data transformations while limiting RAM, CPU time (to protect against infinite loops), and restricting network and filesystem access to designated files only. The research is delegated to Claude Fable 5 running in Claude Code for web, which attempts to test the sandbox environment.

- smolvm can create lightweight microVMs for sandboxing untrusted code, but requires KVM support (/dev/kvm).
- The Claude Code for web environment lacks /dev/kvm and CPU virtualization flags, preventing nested virtualization and direct smolvm execution.
- As a workaround, the AI agent used a GitHub Actions runner (which exposes /dev/kvm) to run the real sandbox tests via a temporary workflow.
- The research evaluates protections against CPU-hogging loops, memory limits, network isolation, and filesystem access control.
- This demonstrates a creative approach to overcoming environmental constraints when testing infrastructure tools with an AI coding agent.