---
domain: ai-workflows
subdomain: tokenization-tools
concept: token-counting-cli
title: ttok 0.4: Token Counting CLI Update
sources:
  - title: "ttok 0.4"
    url: "https://simonwillison.net/2026/Oct/8/ttok/"
    author: "Simon Willison"
    date: "2026-10-08"
---

# ttok 0.4: Token Counting CLI Update

Simon Willison released ttok 0.4, a CLI tool for counting tokens that uses OpenAI's open source tiktoken library. The tool had not been updated in a couple of years, but this release fixes a Click warning, updates CI, and adds a --list-models command for listing available models. It works with uvx, allowing users to count tokens in files via a simple pipe command such as `cat file.txt | uvx ttok`.

- ttok is a CLI tool for counting tokens built on OpenAI's tiktoken library
- Version 0.4 fixes a Click warning, updates CI, and adds a --list-models command
- It can be run without installation via uvx, e.g. `cat file.txt | uvx ttok`