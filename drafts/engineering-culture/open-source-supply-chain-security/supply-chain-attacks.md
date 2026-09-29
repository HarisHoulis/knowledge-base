---
domain: engineering-culture
subdomain: open-source-supply-chain-security
concept: supply-chain-attacks
title: Targeted attacks on prominent Rustaceans
sources:
  - title: "Be alert: targeted attacks on prominent Rustaceans"
    url: "https://blog.rust-lang.org/2026/09/17/targeted-attacks/"
    date: "2026-09-17"
  - title: "Be alert: targeted attacks on prominent Rustaceans (Simon Willison's Weblog)"
    url: "https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/"
    date: "2026-09-17"
  - title: "Supply chain attack on arrayref"
    url: "https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/"
    date: "2026-08-20"
  - title: "We should all be using dependency cooldowns"
    url: "https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns"
    date: "2025-11-21"
---

# Targeted attacks on prominent Rustaceans

The Rust project warns of an ongoing campaign targeting rust-lang members and owners of popular crates, aimed at compromising devices and accounts so they can be used to publish malware (blog.rust-lang.org, 2026-09-17). The attack vector is a pretextual video call — framed as a job, project, or contract opportunity — after which the target is induced to install something (such as a purportedly missing audio codec) or to execute a command, for example one placed on the clipboard.

This social-engineering approach was used successfully in a supply chain attack against the `arrayref` crate the previous month, among others. The broader lesson drawn is that any software depending on open source — which is almost all software — inherits a network of humans who hold publishing rights in its dependency graph and are therefore potential attack vectors.

Simon Willison argues the best current defense is dependency cooldowns: delaying upgrades to new package releases by a few days on the hope that someone else spots a supply chain attack first.

- Ongoing campaign targets rust-lang members and popular crate owners to compromise devices/accounts for publishing malware.
- Initial vector is a fake video call for a job, project, or contract, leading to installing malware (e.g. fake audio codec) or executing clipboard-delivered commands.
- The same trick was used in a successful supply chain attack on the `arrayref` crate in August 2026.
- Everyone with publish rights in a dependency network is a potential attack vector for any software that depends on open source.
- Dependency cooldowns — waiting a few days before upgrading to new releases — are proposed as the best available defense.