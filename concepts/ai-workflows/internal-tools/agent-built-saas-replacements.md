---
domain: ai-workflows
subdomain: internal-tools
concept: agent-built-saas-replacements
title: Building Polished Internal Tools with Agents Instead of SaaS
sources:
  - title: "Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway"
    url: "https://www.youtube.com/watch?v=oixzVKMAXG0"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Building Polished Internal Tools with Agents Instead of SaaS

Mahmoud Abdelwahab of Railway describes replacing multiple marketing SaaS products with a single agent-built internal tool that manages website content, changelog, blog, email, social posting, media, a mini-CRM, task tracking, launch planning, and a calendar with real-time comments and editing. He frames the real gap not as whether agents can generate working software, but the vast gulf between software created on the fly and software that is actually enjoyable, polished, and pleasant to use [source].

His first principle is that the technology stack still matters. When an agent works in a properly structured codebase with solid abstractions, new features come out more consistent because the agent follows existing patterns instead of reinventing the wheel each time. He recommends single-stack libraries for web work and Payload specifically for content-related projects, noting he studied CMS options rather than building one from scratch [source].

He observes that users of everyday SaaS products don't notice how much care went into their processes until they try to recreate that experience. Simple actions like sending an email or posting something are easy with server-side rendering and forms, but a tool used daily needs to feel better than that. He lists polish patterns agents typically omit unless asked directly, starting with autosave that saves progress in the background without blocking work, plus a second layer of protection that prevents closing a browser tab when there are unsaved changes, and optionally real-time collaboration for simultaneous editing [source].

He notes the landscape is changing quickly and that everything he says could change within months, with the recording dated autumn 2026. He describes a breakthrough when GPT-6 arrived, with everything automatically deployed on Railway [source].

- The real gap in agent-built software is not working code but polished, enjoyable software that people actually want to use daily.
- A properly structured codebase with solid abstractions makes agents more consistent, since they follow existing patterns instead of reinventing them.
- Stack choice matters less than structure, but single-stack libraries and Payload for content projects are his current picks.
- Agents omit everyday polish patterns like autosave, unsaved-changes tab protection, and real-time collaboration unless explicitly asked.