---
domain: engineering-culture
subdomain: open-source-security
concept: coordinated-disclosure-leak
title: PHP Security Release and the Leak That Accelerated Exploitation
sources:
  - title: "Today's PHP Security Release, and How We're Strengthening PHP Security"
    url: "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/"
    author: "PHP Foundation"
    date: "2026-10-21"
  - title: "PHP2Shell: PHP RCE"
    url: "https://www.wiz.io/blog/php2shell-php-rce"
    author: "Wiz Research"
    date: "2026-10-21"
  - title: "Today's PHP Security Release, and How We're Strengthening PHP Security (Simon Willison)"
    url: "https://simonwillison.net/2026/Oct/21/php-security-release/"
    author: "Simon Willison"
    date: "2026-10-21"
---

# PHP Security Release and the Leak That Accelerated Exploitation

The PHP Foundation published a post explaining how its coordinated security release went wrong: two CVE IDs began circulating on forums and social media on October 20th with an incorrect release time and an inflated CVSS score of 10.0 (the actual score was 9.2), though no technical details leaked. In response, the project moved its pre-announcement forward to 19:30 UTC and shifted the release from October 22nd to October 21st at 14:00 UTC. Around 20:00 UTC, one of the security firms that had reported the issues mistakenly published a video showing its proof of concept against several targets, revealing limited additional details; copies of the deleted video circulated on social media and accelerated development of further PoCs.

Wiz Research, which discovered the original vulnerability, documented the intended responsible-disclosure timeline: discovery on August 19, 2026 using Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol; confirmation of unauthenticated RCE against Drupal on August 20 and WordPress on August 21; reporting to the PHP security team on August 24; PHP's acknowledgment and coordinated fix work beginning September 21; and patched releases with public disclosure on October 21.

The episode illustrates how early leakage of CVE identifiers and premature third-party disclosure can compress a carefully coordinated timeline and spur exploitation before patches are broadly deployed.

- CVE IDs leaked on October 20th with a wrong release time and an incorrect CVSS score of 10.0 (actual 9.2), prompting PHP to move its pre-announcement and release earlier.
- A reporting security firm mistakenly published a PoC video, and copies circulated on social media, accelerating PoC development.
- Wiz Research found the vulnerability on August 19, 2026 and reported it to PHP on August 24; PHP began coordinated fix work on September 21.
- Unauthenticated RCE was confirmed against both Drupal and WordPress before the report was filed.