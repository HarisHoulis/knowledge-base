---
domain: ai-workflows
subdomain: chatgpt-work
concept: chatgpt-work-capabilities
title: Understanding ChatGPT Work
sources:
  - title: "Understanding ChatGPT Work"
    url: "https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/"
    author: "Simon Willison"
    date: "2026-08-30"
---

# Understanding ChatGPT Work

Simon Willison's article explores OpenAI's ChatGPT Work, a powerful but confusing product available in two flavors: Work Cloud (via web/mobile) and Work Local (desktop app formerly Codex). The author focuses on Work Cloud, which offers exclusive features not found in regular ChatGPT Chat, including selectable GPT-5.6 models (Sol, Luna, Terra) with varying reasoning levels, and billing tied to the Codex allowance rather than Chat sessions. The article notes that ChatGPT Work's code execution environment can access the internet broadly, enabling cloning of GitHub repositories, installing dependencies, and interacting with web services, whereas Chat is restricted.

- ChatGPT Work comes in two forms: Work Cloud (web/mobile) and Work Local (desktop app), with different feature sets and access levels.
- Work Cloud provides an unrestricted internet-connected code execution environment, allowing tasks like cloning repos and installing packages.
- The browser tool can launch a full Chrome instance, fill forms, handle 2FA, and run JavaScript against page DOM, controlled via a Playwright-like API.
- Unlike Chat's ephemeral filesystem, Work Cloud persists a shared /workspace volume across sessions, and can build/deploy sites to Cloudflare Workers.
- Work supports sub-agents and scheduled tasks, but raises security concerns about prompt injection (the 'lethal trifecta').