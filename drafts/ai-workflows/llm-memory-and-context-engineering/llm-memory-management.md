---
domain: ai-workflows
subdomain: llm-memory-and-context-engineering
concept: llm-memory-management
title: Do LLMs Have the Memory of a Goldfish?
sources:
  - title: "Do LLMs Have the Memory of a Goldfish?"
    url: "https://blog.bytebytego.com/p/do-llms-have-the-memory-of-a-goldfish"
    author: "ByteByteGo"
    date: "2026-09-15"
---

# Do LLMs Have the Memory of a Goldfish?

LLMs appear to remember a conversation, but the model itself has no personal or persistent memory of previous interactions. As ByteByteGo puts it, an LLM "doesn't remember a conversation like human beings do"; instead it receives information about the conversation so far with each new message. All of this is handled by the application built around the model — storing messages, maintaining summaries, retrieving relevant memories, and maintaining a user profile — and inserting that information into the prompt. "From the user's perspective, the model appears to remember. But technically, the surrounding application is doing most of the remembering."

The article separates three distinct senses of "memory." Trained memory lives in the model's parameters and encodes general knowledge, but is not personal: if a user says their preferred language is TypeScript, a normal API response does not rewrite the weights. Working memory is the context window, which contains system instructions, prior messages, retrieved documents, tool definitions and results, saved preferences, summaries, and space for the output — closer to a desk than to human memory, since once the desk is cleared the model cannot recover what was there. Persistent application memory lives outside the model in a database, file, vector store, or profile service, and is retrieved and inserted into context when needed.

Because most providers expose a stateless Messages API, the application must resend prior turns for multi-turn conversation — the article's example shows that "What is my name?" fails alone but succeeds when the earlier exchange is included. Server-managed conversation state that reconstructs history from a conversation identifier makes the API easier to use but does not give the model personal memory; the article calls the resulting continuity "reconstructed memory or context-based memory" rather than fake memory. Growth has real costs: each round reprocesses more text, so ten requests of ~1,000 tokens each cost roughly 55K input tokens even though the visible conversation is only ~10K, and longer contexts also add latency. Large windows don't guarantee recall either — degradation known as "context rot" makes it harder to separate important facts from irrelevant or contradictory material. Prompt caching reduces cost and latency for repeated prefixes but "doesn't give the model unlimited memory"; it is "an optimization, not a memory architecture."

When the window fills, behavior varies: requests may be rejected, oldest messages removed, a rolling window applied, old material replaced with a compact summary, or server-side compaction used. Compaction preserves central state in smaller form but is lossy, and summarization can omit nuance or convert assumptions into facts — "much like repeatedly copying a photocopy" — so the article recommends storing important facts separately. Practical techniques include sliding-window memory (simple and predictable, but old facts vanish), conversation summarization (preserves direction efficiently but is interpretative and can distort over repeated passes), and structured entity extraction into fields such as preferred language, database, framework, current project, and confirmed decisions, which is more reliable than searching a long summary for exact project state.

- LLMs have no persistent memory; chat applications create the illusion of memory by resending or injecting conversation history, summaries, and retrieved facts into the context window.
- Three distinct memory types: trained memory in weights (not personal), working memory in the context window (a "desk," not human memory), and persistent application memory stored outside the model in databases or vector stores.
- Stateless Messages APIs require resending history each turn; server-managed conversation state with a conversation ID reconstructs context but still isn't model memory.
- Growing conversations repeatedly reprocess earlier tokens, raising cost and latency, and large context windows still suffer "context rot"; prompt caching is an optimization, not a memory architecture.
- When context fills, systems reject, truncate, roll, summarize, or compact — and all lossy approaches risk dropping or distorting details, so important facts should be stored separately in structured form.