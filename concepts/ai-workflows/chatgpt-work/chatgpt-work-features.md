---
domain: ai-workflows
subdomain: chatgpt-work
concept: chatgpt-work-features
title: Understanding ChatGPT Work
sources:
  - title: "Understanding ChatGPT Work"
    url: "https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/"
    author: "Simon Willison"
    date: "2026-08-30"
---

# Understanding ChatGPT Work

According to Simon Willison's article 'Understanding ChatGPT Work' (2026), the product has two main variants: Work Cloud, which runs in the browser and mobile apps, and Work Local, the desktop app formerly called Codex. The article focuses on Work Cloud, which is available only to $20/month+ subscribers. It is presented as an alternative to Chat, offering different model selections (e.g., GPT-5.6 Sol/Luna/Terra with reasoning levels up to Ultra) and is billed against the Codex allowance rather than Chat's separate allowance (Willison, 2026).

The key distinction from Chat is Work's execution environment: it can access the internet, install packages, clone GitHub repositories, and run a full Chrome browser via the 'control-browser' skill. The browser tool can load pages, fill forms, capture screenshots, and execute JavaScript against the DOM. Work also features persistent /workspace scratch folders shared across sessions, the ability to build and deploy websites to Cloudflare Workers, sub-agents for parallel tasks, and scheduled prompts. Willison demonstrates these capabilities by building a site about London pelican imagery and extracting headings from his own website using JavaScript (Willison, 2026).

Willison raises safety concerns, noting that ChatGPT Work combines private data, exposure to untrusted content, and a means to exfiltrate information—what he calls the 'lethal trifecta.' He also criticizes the lack of clear documentation, which led him to have Work itself generate a reference site listing its 223 tools and 44 skills, including detailed browser documentation (Willison, 2026).

- ChatGPT Work has two forms: Work Cloud (web/mobile) and Work Local (desktop app, formerly Codex); Work Cloud is the article's focus.
- Unlike Chat, Work's code execution environment has open internet access, allowing package installation, repo cloning, and full browser automation with JavaScript execution.
- Work provides persistent workspace folders, the ability to deploy websites to Cloudflare Workers, sub-agents, and scheduled tasks.
- The article highlights potential prompt injection risks due to the combination of private data, untrusted content, and communication channels.
- OpenAI's documentation was insufficient, leading Willison to build a self-generated tool and skill reference site.