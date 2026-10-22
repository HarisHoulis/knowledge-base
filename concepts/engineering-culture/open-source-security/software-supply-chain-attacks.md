---
domain: engineering-culture
subdomain: open-source-security
concept: software-supply-chain-attacks
title: Open Source Under Attack: Supply Chain Risk and AI's Amplifying Effect
sources:
  - title: "Open Source Is Under Attack & AI Made It Worse • Steve Poole & Olimpiu Pop • GOTO 2026"
    url: "https://www.youtube.com/watch?v=aUIbUnWj8N0"
    author: "GOTO Conferences"
    date: "2026-10-22"
---

# Open Source Under Attack: Supply Chain Risk and AI's Amplifying Effect

In this GOTO Unscripted conversation, Steve Poole (Hero Devs, formerly Sonatype, Red Hat, IBM) and Olimpiu Pop discuss how the software supply chain has become a primary attack surface. Poole argues the ecosystem has hit a turning point: everyone depends on open source, consumed on the assumption that its maintainers are trustworthy, but that trust has been steadily eroded by attackers motivated by the money involved. Attackers target the dependencies, tools, and configuration developers install rather than only stealing credentials.

Poole outlines several concrete attack vectors: running unchecked bash scripts, and typo-squatting ("typo confusion"), where a misspelled dependency name resolves to a real, malicious package that gets installed. Dependencies can also be compromised at the source when the upstream project itself is attacked, turning downstream products into Trojan horses.

Poole singles out AI as the factor that changed everything. While it could be framed positively, in his view AI has mainly accelerated the discovery of vulnerabilities, worsening an already deteriorating situation. Hero Devs exists as a commercial response, providing support for open source packages that no longer have maintainers, helping close some of these gaps.

- Software supply chain attacks exploit the dependencies, tools, and install steps developers rely on, not just stolen credentials.
- Typo-squatting is a simple but effective vector: a misspelled package name can resolve to a real malicious package.
- Upstream open source projects themselves can be compromised, making downstream products unwitting Trojan horses.
- AI has accelerated vulnerability discovery, worsening the erosion of trust in open source.
- Maintainer abandonment is a structural gap that commercial support models like Hero Devs aim to fill.