---
domain: ai-workflows
subdomain: voice-driven-coding
concept: voice-driven-development
title: Building a Blog Feature with Voice-Driven Coding Agents
sources:
  - title: "A new feature for my blog, built using my voice"
    url: "https://simonwillison.net/2026/Oct/9/built-using-my-voice/"
    author: "Simon Willison"
    date: "2026-10-09"
---

# Building a Blog Feature with Voice-Driven Coding Agents

Simon Willison shipped a new Newsletters index page for his blog, building it almost entirely by talking to his laptop while cooking dinner. He used the ChatGPT desktop app's Codex tab in voice conversation mode against a local development environment, starting by typing 'Start dev server and open in browser' to get a visual preview, then clicking 'Start new voice chat' and setting up his laptop in the kitchen. He had a clear idea of the feature—a new Django model, migration, view code, templates, and import functions—and was confident the model (GPT-6 Astra High) could handle it.

The voice transcript, disfluencies and all, was clear enough for the model to understand the requirements, including nuanced decisions about where newsletter content should appear (not on tag pages or the blog index, but on date-based pages, and searchable once public). They worked this way for about half an hour, with the model occasionally asking clarifying questions and modifying code. The feature got surprisingly far entirely by voice, but the imports required sitting at the keyboard: one import needed to pull from a private GitHub repository, requiring a new API key.

After cooking, Willison had Codex create a branch and open a pull request, then reviewed the code in GitHub's PR interface. He found it had used Git in a subprocess for an import script and switched to typing to have Codex replace it with an API-based import, plus made display tweaks. An additional half hour of typing-based prompting got it ready to deploy. He notes that while voice-driven demos work well for OpenAI events like DevDay, this won't be a daily driver for him—he still switches to typing for details like pasting examples, error messages, or highlighting code. The killer feature is multi-tasking: he usually cooks with a podcast or TikTok running, and now he can build stuff instead.

- Voice-driven coding with a visual preview enabled building a complete Django feature (model, migration, views, templates, imports) in about 30 minutes of cooking time
- The model understood nuanced requirements from disfluent speech, including where content should and shouldn't appear and searchability rules
- Typing remained necessary for details: API key setup, pasting examples and error messages, and highlighting code for changes
- The main benefit cited is multi-tasking during otherwise idle time like cooking, not replacing typed workflows