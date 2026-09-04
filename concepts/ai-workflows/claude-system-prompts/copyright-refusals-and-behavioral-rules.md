---
domain: ai-workflows
subdomain: claude-system-prompts
concept: copyright-refusals-and-behavioral-rules
title: Anthropic's New Claude System Prompts Strengthen Copyright Bars and Add New Conduct Rules
sources:
  - title: "Claude's new system prompt really doesn't want to reproduce song lyrics"
    url: "https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/"
    author: "Simon Willison"
    date: "2026-09-02"
---

# Anthropic's New Claude System Prompts Strengthen Copyright Bars and Add New Conduct Rules

According to Simon Willison's post, Anthropic has updated the system prompts for Claude consumer apps, and the Fable 5.1 release adds a substantial new section prohibiting reproduction of song lyrics, poems, and book passages—including partial lines, choruses, and user-provided lyrics. It also extends the same logic to visual works, logos, characters, and code-generated images such as SVGs or ASCII art. Willison notes that this change landed shortly after major publishers sued Anthropic over song-lyric training data, implying that the new rules likely reflect that legal pressure.

The updated prompt also alters Claude's conversational and safety behavior. It tells Claude to keep responses concise, avoid over-apologizing or becoming submissive when users are rude, and stop using modifiers like "genuinely," "honestly," or "straightforward." Interestingly, the previous instruction allowing Claude to end abusive conversations has been removed from the published prompt, though Fable 5.1 told Willison that related tool-specific instructions still exist in unpublished context layers. The prompt adds new harm-reduction guidance for illegal-substance questions, including external URLs such as dancesafe.org and tripsit.me.

Willison has built a GitHub repository, claude-system-prompts, that archives and diffs Anthropic's published system-prompt history. He used GPT-5.6 Luna to automatically generate changelog summaries because he did not want to rely on Claude to summarize its own system prompts. The entire automation pipeline was written by Claude Fable 5.1, and the commit history makes it easy to compare changes across model versions.

- Fable 5.1's system prompt explicitly bars reproducing lyrics, poems, and book passages—even partial ones—and refuses reworded attempts for the rest of the conversation.
- Copyright refusal is extended to visual designs, including code-generated images, and to recognizable characters like Sonic the Hedgehog.
- Claude is instructed to be more concise, avoid disingenuous modifiers, and handle rudeness with self-respect rather than submissiveness.
- The published prompt no longer mentions the end_conversation tool, but Claude reports that tool-specific instructions still exist in unpublished system-prompt layers.
- Willison's GitHub repo provides a diffable history of Anthropic's published Claude system prompts with an LLM-generated changelog.