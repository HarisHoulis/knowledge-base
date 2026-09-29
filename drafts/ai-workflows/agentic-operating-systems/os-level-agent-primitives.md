---
domain: ai-workflows
subdomain: agentic-operating-systems
concept: os-level-agent-primitives
title: How will AI change operating systems? Part 2: Windows
sources:
  - title: "How will AI change operating systems? Part 2: Windows"
    url: "https://newsletter.pragmaticengineer.com/p/windows-and-ai"
    author: "Gergely Orosz"
    date: "2026-09-22"
---

# How will AI change operating systems? Part 2: Windows

Microsoft is rebuilding Windows around agentic primitives, aiming to win back developers who have drifted to macOS and Linux. Windows still holds ~63% of mainstream desktop market share, but among developers its position is weaker: Stack Overflow's 2025 survey, a JetBrains survey, and two Pragmatic Engineer social polls (~10,000 combined responses) all put Windows behind macOS and/or Linux, with the social polls placing it third behind Linux. Microsoft attributes part of this to past product decisions that cluttered the Start menu and search, and is now addressing those criticisms (Pragmatic Engineer).

Agents are treated as first-class users of the OS. Agent identification is handled through Entra ID agent users, so an agent appears in Task Manager as a separate user alongside the human, with the same observability. Because a rogue agent could impersonate a user, Defender is becoming "agent aware" and scans for known local agent activity much like it scans for viruses. Agent discovery runs through the Windows On Device Agent Registry (ODR), a centralized place where agents register and find local MCP servers, including connectors for core OS components like File Explorer and System Settings. Reverse engineering by Origin Technology indicates ODR inserts itself as a proxy between MCP client and server, giving Windows a choke point to inspect payloads — behavior Microsoft has not confirmed (Pragmatic Engineer).

For isolation, Microsoft is building Microsoft Execution Containers (MXC), an OS-agnostic mechanism that spawns agentic tools in sandboxes configured by JSON containment policies covering network, filesystem, UI, and execution restrictions. MXC offers escalating containment levels — process, session, WSL containers, lightweight Hyper-V containers, and full VMs — trading startup speed against blast radius, and abstracts isolation away from the agent itself. It already runs on Windows, Linux, and macOS, and enterprises will manage policies through Intune.

On local models, Windows ML is Microsoft's second hardware-agnostic layer after DirectML. Where DirectML was a low-level, GPU-only library built on DirectX 12, Windows ML is a higher-level abstraction based on the ONNX format, offering broader hardware coverage across GPU, NPU, and CPU. Windows also ships WSL, whose continued popularity suggests embracing Linux is part of the strategy to attract developers, and Windows on ARM is finally becoming a credible alternative alongside an upcoming NVIDIA collaboration (Pragmatic Engineer).

- Windows leads mainstream desktop at ~63% share but is losing developer mindshare to macOS and Linux, per Stack Overflow, JetBrains, and Pragmatic Engineer polls.
- Agents get OS-level identity via Entra ID agent users and are discoverable as separate users in Task Manager; Defender is being made agent-aware to catch impersonation.
- The Windows On Device Agent Registry centralizes MCP server discovery and provides OS connectors like File Explorer; research suggests ODR proxies MCP traffic, though Microsoft hasn't confirmed this.
- Microsoft Execution Containers (MXC) sandbox agent tools using JSON policies with selectable containment levels from processes up to full VMs, and run cross-platform on Windows, Linux, and macOS.
- Windows ML, built on ONNX, replaces the GPU-only, low-level DirectML as a hardware-agnostic layer spanning GPU, NPU, and CPU.