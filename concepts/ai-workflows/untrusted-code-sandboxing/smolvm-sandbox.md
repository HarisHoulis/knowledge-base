---
domain: ai-workflows
subdomain: untrusted-code-sandboxing
concept: smolvm-sandbox
title: smolmachines / smolvm as a sandbox for untrusted Python & JavaScript
sources:
  - title: "smolmachines / smolvm as a sandbox for untrusted Python & JavaScript"
    url: "https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/"
    author: "Simon Willison"
    date: "2026-08-19"
---

# smolmachines / smolvm as a sandbox for untrusted Python & JavaScript

Simon Willison documented an experiment using smolmachines.com's smolvm as a fast, secure sandbox for executing untrusted Python and JavaScript code. The research goal was to assess whether smolvm could safely run user-provided tasks like data transformations with strict limits on RAM, CPU time, network access, and filesystem access. The investigation was carried out by Claude Fable 5 in Claude Code for web, which was instructed to test the sandbox's capabilities and limitations.

A key obstacle emerged: the Claude Code for web environment runs inside a Firecracker guest without /dev/kvm or VMX/SVM CPU flags, making nested virtualization impossible. As a result, smolvm's `machine run` command failed with "kvm not available." To work around this environmental limitation, the agent pivoted to using GitHub Actions runners, which do expose /dev/kvm, and ran the full test battery via a temporary workflow. This proactive workaround highlights both the constraints of nested virtualization in cloud sandboxes and the resourcefulness of AI agents in adapting to them.

The experiment underscores that smolvm can serve as a viable sandbox for untrusted code, but only on hosts with KVM support. The ability to enforce CPU, memory, network, and filesystem restrictions is central to its use case, making it suitable for safely executing user-supplied transformations. The process also demonstrates a practical pattern for evaluating sandboxing tools: combine an AI research agent with CI infrastructure that provides the necessary hardware virtualization capabilities.

- smolvm is positioned as a fast, secure sandbox for running untrusted Python and JavaScript with resource limits.
- smolvm requires KVM support; it fails with 'kvm not available' on environments without /dev/kvm or virtualization CPU flags.
- Claude Code for web lacked nested virtualization, so the agent used GitHub Actions runners (which expose /dev/kvm) to run the real tests.
- The desired sandbox profile includes restricting RAM, CPU time (anti-while-true), network access, and filesystem access to designated files.
- AI coding agents can proactively overcome environmental constraints by finding alternative execution paths.