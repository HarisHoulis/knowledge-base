---
domain: ai-workflows
subdomain: rag-in-production
concept: rag-for-financial-rulebooks
title: Your Fridge Is a Valid Payment Device: RAG in Production
sources:
  - title: "Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket"
    url: "https://www.youtube.com/watch?v=gonAewBZxfU"
    author: "AI Engineer"
    date: "2026-10-14"
---

# Your Fridge Is a Valid Payment Device: RAG in Production

Eleonora Drykina and Nina Žižakić of In The Pocket describe a production RAG system built for a large Belgian fintech client that operates the country's largest payment system. The client's rules are spread across roughly 270 PDF rulebooks totaling about 6,000 pages, with most information contained in approximately 3,000 tables, and the rulebooks frequently cross-reference each other. The talk's title comes from a page in these documents listing unusual payment devices, including cufflinks, handbags, clothes, and even a refrigerator.

The financial context imposes two hard requirements: every answer must be correct and must include a link to the specific section and page of the rules, and the generic LLM must not inject outside knowledge. General concepts like what a bank is are acceptable, but details such as how another payment system works or what it charges must not appear unless present in the rules.

The system is a chatbot that answers questions from the rules, displays the relevant table when the answer comes from one, and lists sources with section and page so users can open the document. Architecturally it splits into an offline indexing part and an online serving part. On each new rule release, PDFs are converted into fragments and stored in a vector database; at query time an agent searches that database and streams the response to the user.

Indexing takes PDFs, splits them into fragments, adds metadata, performs special table processing, and generates both dense and BM25 embeddings. Fragmentation extracts text per page, divides it into paragraphs, and groups paragraphs into snippets of about 2,000 characters without breaking tables across snippets. Section headings such as "section three" or "4.2.1" are detected with regular expressions, giving each fragment a path used both for citation links and for retrieving an entire section when the agent needs more context; because fragments do not overlap, a chapter is simply an ordered collection of fragments. Metadata such as guide title and page number enables source cards and direct links to the PDF.

- The client's knowledge lives in ~270 PDF rulebooks (~6,000 pages, ~3,000 tables) with heavy cross-referencing, making table handling and citation essential.
- Financial RAG requires every answer to cite a specific section and page, and must prevent the generic LLM from adding outside knowledge not present in the rules.
- Indexing splits PDFs into ~2,000-character snippets without breaking tables, detects section headings via regex to build a citation path, and adds metadata like guide title and page number.
- The system generates both dense and BM25 embeddings and separates offline indexing from online agent-based retrieval and streaming responses.