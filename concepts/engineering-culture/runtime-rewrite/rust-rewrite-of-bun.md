---
domain: engineering-culture
subdomain: runtime-rewrite
concept: rust-rewrite-of-bun
title: Claude Code uses Bun written in Rust
sources:
  - title: "Claude Code uses Bun written in Rust now"
    url: "https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything"
    author: "Simon Willison"
    date: "2026-07-19"
  - title: "Rewriting Bun in Rust"
    url: "https://bun.com/blog/bun-in-rust"
    author: "Jarred Sumner"
    date: "2026"
---

# Claude Code uses Bun written in Rust

Claude Code v2.1.181, released June 17th, 2026, and later versions use a Rust rewrite of Bun instead of the original Zig-based version. According to Jarred Sumner's blog post 'Rewriting Bun in Rust', startup time on Linux became 10% faster, but otherwise the change went largely unnoticed (Simon Willison, 2026). This underscores the principle that 'boring is good' in production deployments—a successful rewrite that improves performance without disrupting users. Willison verified the claim by running strings commands on his local Claude Code binary, finding that it reports Bun v1.4.0 (a pre-release version) and contains over 500 Rust source file paths, confirming that the Rust port is shipping to millions of devices (Simon Willison, 2026).

- Claude Code v2.1.181+ bundles a Rust port of Bun, replacing the original Zig-based runtime.
- Startup performance improved by 10% on Linux, but the change was seamless for users.
- The Rust version is based on Bun v1.4.0, a not-yet-released canary build.
- Verification via strings commands reveals Rust source files embedded in the Claude binary.
- This exemplifies a 'boring is good' approach to a critical runtime rewrite in production.