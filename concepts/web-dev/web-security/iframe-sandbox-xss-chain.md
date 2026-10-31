---
domain: web-dev
subdomain: web-security
concept: iframe-sandbox-xss-chain
title: How We Took Over ChatGPT Accounts
sources:
  - title: "How We Took Over ChatGPT Accounts"
    url: "https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/"
    author: "Simon Willison"
    date: "2026-10-31"
---

# How We Took Over ChatGPT Accounts

Parameter discovered a complex attack chain that let a crafted ChatGPT share URL exfiltrate private data or take actions on behalf of any signed-in user who visited it. The root issue was that HTML in sandboxed iframes must be tightly isolated to prevent untrusted code from interacting with OpenAI APIs and private data.

The chain began with MathLive, a JavaScript library used for graph support that includes its own virtual keyboard. That keyboard can be triggered in the parent page via postMessage() from a sandboxed iframe, and the message-receiving code used innerHTML. Because nothing prevented other sandboxed frames, including HTML preview frames, from calling that method, untrusted iframe code could inject HTML, and while innerHTML doesn't execute script elements directly, it could inject a new iframe without sandbox restrictions.

OpenAI's CSP blocked inline scripts and allowed script loading only from a handful of domains, but YouTube was among them, and the YouTube oEmbed endpoint could reflect JavaScript back in an executable form. With JavaScript execution on ChatGPT, fetching private user data from APIs and exfiltrating it via an image reference was trivial. OpenAI closed the hole and paid a $5,000 bug bounty, which Simon Willison considers cheap for a vulnerability this serious.

- Sandboxed iframes must be tightly isolated so untrusted HTML can't reach OpenAI APIs or private data
- postMessage handlers using innerHTML let untrusted frames inject a new iframe without sandbox restrictions
- CSP allowlisting of YouTube was bypassed via the YouTube oEmbed endpoint reflecting executable JavaScript
- Once JS executed on the page, private data could be fetched and exfiltrated via an image reference
- OpenAI fixed the issue and paid a $5,000 bounty, which the author considers low for the severity