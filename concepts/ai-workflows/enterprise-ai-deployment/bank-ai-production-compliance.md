---
domain: ai-workflows
subdomain: enterprise-ai-deployment
concept: bank-ai-production-compliance
title: Shipping AI Into Major Banks Without a 12-Month Compliance Wait
sources:
  - title: "Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco"
    url: "https://www.youtube.com/watch?v=Bz1HFxQA1o8"
    author: "AI Engineer"
    date: "2026-10-20"
---

# Shipping AI Into Major Banks Without a 12-Month Compliance Wait

Al Chen (Cisco) describes why deploying AI agents in the production systems of the world's largest banks is slow, and how his team shortens the path from a year to a few weeks. He frames compliance and risk teams as strict graders: like his 10th-grade math teacher Mr. Gaff, they care less about the answer than the proof of how you arrived at it. The real difficulty is "production" — not prototypes, testing, or internal RAG agents for employee productivity, but the customer-facing applications millions of people use when they log into a bank's website or mobile app.

Standard SaaS AI deployment fails in a bank because outgoing internet traffic can leak confidential information; running AI on the bank's own servers without internet access adds complexity. Chen examines three aspects: the assembly line itself (how banks load software images into their cluster), the data recovery plan if a region fails during a query, and — most importantly — ensuring confidential data does not reach internal employees or leave the bank's VPC. Compliance speed is inextricably linked to CVE handling, and no platform is complete without a plan for that first hurdle.

CVE remediation is complicated because the platform carries many images, each with many CVEs, and fixes must serve many banks at once. Banks use different image versions with unique CVEs, run various scanning tools, and apply their own policies on which CVEs are critical, their severity levels, and SLA remediation timelines. Images depend on open-source projects with transitive dependencies whose CVEs the development team cannot remove, so the team constantly reviews release notes to explain to bank security teams why certain vulnerabilities cannot be fixed. Banks also disagree on versions — one wants 3.8 of a package, another considers it too high in CVEs and wants to stay on an older version — so the software must still work across all of them.

Chen's solution is a scaling system: a tool that does the heavy lifting, prepares reports, and conducts internal research, producing a table telling the team which CVEs need fixing and explaining to bank security services what cannot change due to transitive dependencies. Because scanners like Sysdig, Wiz, or Prisma only check whether a package was updated to a specific version — not whether the exploit remains in the application's code — the team creates a Harbor task (a sandbox for testing the agent) containing instructions, the actual Docker images, and tests. The agent is told a CVE and that version 2.6.2 supposedly fixes it, then asked to write an exploit against the older version, check whether the new version contains it, and write a test verifying whether the exploit worked; Harbor, Modal, or Daytona sandboxes can run many containers in parallel.

- Production deployment in banks is the hard part — customer-facing apps, not prototypes or internal RAG agents, are what matter.
- Standard SaaS AI fails in banks due to internet egress leaking confidential data; self-hosted, no-internet deployments add complexity around image loading, region-failure recovery, and keeping data inside the VPC.
- CVE remediation is complicated by many images, per-bank version preferences, differing scanning tools and severity/SLA policies, and transitive open-source dependencies the team cannot remove.
- A scaling tool produces a table of CVEs to fix plus explanations for bank security teams about what cannot change.
- Harbor sandbox tasks let agents write exploits against old versions and tests to verify whether a patched version still contains the exploit, run in parallel across Harbor, Modal, or Daytona.