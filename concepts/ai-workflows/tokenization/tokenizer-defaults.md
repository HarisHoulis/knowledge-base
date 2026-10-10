---
domain: ai-workflows
subdomain: tokenization
concept: tokenizer-defaults
title: ttok 1.0: Defaulting to the GPT-5/GPT-6 Tokenizer
sources:
  - title: "ttok 1.0"
    url: "https://simonwillison.net/2026/Oct/9/ttok/"
    author: "Simon Willison"
    date: "2026-10-09"
---

# ttok 1.0: Defaulting to the GPT-5/GPT-6 Tokenizer

Simon Willison released ttok 1.0, prompted by noticing that version 0.4 defaulted to the GPT-4 tokenizer when it should default to the GPT-5/GPT-6 tokenizer instead. He describes switching the default as a reasonable excuse to finally ship a 1.0 release.

OpenAI has not officially confirmed that GPT-6 uses the same tokenizer as the GPT-5 family, and there is an angry issue about it in the tiktoken repository. However, Willison cites a commit by William Liu reporting an experiment that suggests the tokenizers are likely the same: all seven GPT models (5.5, 5.6 Sol/Terra/Luna, 6 Astra/Sol/Luna) reported 44,794 tokens and matched each other on every one of the 31 fixtures, with GPT-6 introducing no input-count change on that corpus.

- ttok 1.0 changes the default tokenizer from GPT-4 to GPT-5/GPT-6
- OpenAI has not officially confirmed GPT-6 shares the GPT-5 family tokenizer
- William Liu's experiment found all seven GPT models matched on 31 fixtures at 44,794 tokens