---
domain: ai-workflows
subdomain: ai-coding-agents
concept: verification-bottleneck
title: Agents Now Write Most First-Draft Code; Verification Becomes the Bottleneck
sources:
  - title: "The Roundup by ByteByteGo"
    url: "https://blog.bytebytego.com/p/the-roundup-by-bytebytego"
    author: "ByteByteGo"
    date: "2026-11-11"
---

# Agents Now Write Most First-Draft Code; Verification Becomes the Bottleneck

GitHub's Octoverse 2026 reports that over 40% of pull requests in September began as agent-generated first drafts, up from 17% in March—roughly 110 million PRs in a single month. Anthropic went further, replacing Git in its monorepo with an in-house system called Scion, where daily merges grew from ~2,500 in May to over 30,000 in September; a team of seven moved the monorepo off Git in five months, using 200X less CPU and memory than the Git mirror fleet it replaced. The author notes open questions: who reviews 110M PRs, how agent authorship is even detected, and what defect or revert rate accompanies Scion's throughput.

The author's thesis is that code generation has become the cheap part of software engineering. The scarce resources are now human review time, CI capacity, and merge rate, so the next wave of developer tooling will focus on verifying code rather than writing it. Building custom version control used to require Google- or Meta-scale resources; Anthropic did it with a fraction of the people because agents did the coding.

GitHub Universe brought Copilot Fusion, a generally available model router that picks which model handles each task—scoring within two points of Claude Opus 5.5 Max on the Artificial Analysis Coding Agent Index at about half the cost and 40% less time per task—plus multi-repo parallel agent projects and usage-based Enterprise billing via AI credits. The author compares this to the cloud adoption shift and warns that model choice now happens invisibly, raising governance and reliability concerns.

Anthropic's S-1 filing gives the first audited look at AI coding economics: $16.3B H1 2026 revenue (up from $1.2B), 14K+ enterprise customers, ~250 spending $10M+ annually, and 900% net revenue retention. It also disclosed that four models reached external systems during third-party security testing due to a misconfigured internet access setting. Separately, PHP shipped emergency fixes for two critical "PHP2Shell" bugs (CVSS 9.2, unauthenticated RCE), with ~73.5% of internet-facing PHP services running unpatched 8.1 or older—a reminder that language runtimes are dependencies too.

- Over 40% of GitHub PRs in September 2026 started as agent-generated drafts, up from 17% in March (~110M PRs/month).
- Anthropic replaced Git with Scion for its monorepo, scaling from ~2,500 to 30,000+ daily merges with 7 developers and 200X lower CPU/memory than its Git mirror fleet.
- The bottleneck is shifting from writing code to verifying it: human review time, CI capacity, and merge rate are now the scarce resources.
- GitHub's Copilot Fusion router makes model selection automatic and moves Enterprise to usage-based AI credit billing, echoing the cloud adoption shift.
- Anthropic's S-1 shows $16.3B H1 2026 revenue and 900% net revenue retention, while PHP2Shell shows runtimes must be tracked as dependencies—73.5% of exposed PHP services run unpatched versions.