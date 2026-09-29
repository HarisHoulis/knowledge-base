---
domain: ai-workflows
subdomain: retrieval-augmented generation
concept: rag-vector-retrieval
title: How LLMs Find a Needle in a Haystack: RAG and Vector Search
sources:
  - title: "How LLMs Can Find a Needle in a Haystack"
    url: "https://blog.bytebytego.com/p/how-llms-can-find-a-needle-in-a-haystack"
    author: "ByteByteGo"
    date: "2026-09-16"
---

# How LLMs Find a Needle in a Haystack: RAG and Vector Search

LLMs do not automatically know what is inside a company’s private documents, so applications must provide evidence either by putting documents directly into the input or by retrieving relevant passages when a question arrives (ByteByteGo). Retrieval-augmented generation, or RAG, uses an embedding model to convert the question into a numerical representation, a search system to find promising passages, and then supplies the original text to the LLM. This division matters because if the application retrieves an outdated policy or misses an exception, even a capable model will produce an outdated or incomplete answer (ByteByteGo).

Documents are divided into chunks so search can identify a specific passage instead of a whole handbook. Chunking balances precision and context: small chunks may miss exceptions, while large chunks may include unrelated policies, so useful chunks preserve a complete idea, use headings, and sometimes overlap (ByteByteGo). Embeddings map text to vectors so related meanings sit nearby, but query and document embeddings must come from compatible encoders. Each record also needs a connection to the original text, plus metadata such as document ID, section, effective date, and version (ByteByteGo). Similarity metrics such as cosine similarity, Euclidean distance, and dot product define “nearby,” and normalization affects ranking. A similarity score is not a probability that a passage answers the question correctly; it only provides evidence of relevance (ByteByteGo).

Searching every vector is exact but grows with collection size, roughly O(n). Inverted-File indexes cluster vectors into groups and search selected groups via nprobe, trading recall for less work; HNSW builds a layered graph that navigates from sparse upper layers to a detailed bottom layer, also performing approximate nearest-neighbor search (ByteByteGo). HNSW parameters like M, ef_construction, and ef_search tune graph connectivity, construction breadth, and query exploration, with recall/latency tradeoffs that should be measured using representative questions. Metadata filtering—pre-filtering or post-filtering—is needed to restrict results to eligible policies, such as the employee’s region and current effective date, and filtering-aware graph search or exact scans may be required (ByteByteGo).

Finally, the collection must remain correct as documents change. If a hotel reimbursement limit rises from ₹5,000 to ₹7,000 and both versions remain eligible, the assistant may retrieve either figure or receive contradictory evidence. Changes to embedded text require new embeddings, so retrieval quality depends on chunking, indexing, filtering, and freshness before generation (ByteByteGo).

- RAG separates retrieval from generation: the LLM needs retrieved passages to answer and cite private-document questions.
- Chunking should preserve complete ideas and conditions; headings and overlap help retain context.
- Embeddings enable semantic search, but similarity scores indicate relevance, not correctness or probability of a right answer.
- Flat search is exact but O(n); IVF and HNSW reduce work through approximate search, with recall/latency tradeoffs tuned by parameters such as nprobe, M, ef_construction, and ef_search.
- Metadata filtering and fresh indexing are required so the closest match is not the wrong regional policy or an outdated version.