---
domain: ai-workflows
subdomain: rag-support-assistants
concept: rag-knowledge-assistant
title: How Uber Built Genie to Answer Engineering Support Questions
sources:
  - title: "How Uber Built a Genie to Answer Questions Correctly"
    url: "https://blog.bytebytego.com/p/how-uber-built-a-genie-to-answer-051"
    author: "ByteByteGo"
    date: "2026-10-19"
---

# How Uber Built Genie to Answer Engineering Support Questions

Uber's Genie is an internal AI assistant that answers engineering support questions in Slack by retrieving relevant passages from internal documentation and using an LLM to explain them. The problem it addresses is scale: Uber's internal support channels receive roughly 45K questions per month, and much of the needed information is scattered across Engwiki, internal Stack Overflow, and other documents, making it easier to ask a colleague than to search. Genie surfaces that existing knowledge where developers already ask for help.

Uber chose retrieval-augmented generation (RAG) over fine-tuning because it could launch sooner using existing documentation and could improve by updating the knowledge collection without retraining the model. An ETL pipeline built on Apache Spark extracts content from internal sources, chunks it with LangChain, and generates embeddings with an OpenAI embedding model via custom Python functions in Spark, preserving source URLs for later attribution.

Serving is separated from preparation: a bootstrap job ingests data into Uber's vector database Sia, Spark jobs build and merge an index stored in Terrablob, and serving machines download and synchronize the index to handle live searches. When a question arrives, the Knowledge Service embeds it, retrieves related chunks, and passes them to the LLM along with the question and answering instructions. Each retrieved result is presented as a separate sub-context with its source URL, and the model is instructed to cite sources, reducing hallucination risk.

Genie also handles the cases where it can't help: responses include buttons to ask a follow-up, mark resolved, or contact human support, and escalation mutes Genie while an on-call engineer takes over. Feedback is collected in Slack across four categories (Resolved, Helpful, Not Helpful, Not Relevant) to distinguish partial help from wrong answers and out-of-scope requests.

- Uber chose RAG over fine-tuning so Genie could launch on existing documentation and improve by updating the knowledge base without retraining.
- An Apache Spark ETL pipeline extracts, chunks (via LangChain), and embeds documents, preserving source URLs for citation.
- Index building (Sia vector DB, Terrablob storage) is decoupled from serving, where leaf machines handle live searches.
- Retrieved passages are passed as separate sub-contexts with source URLs, and the model is instructed to cite them to reduce hallucination.
- Genie escalates to human on-call support when it can't answer, and collects four-category feedback to distinguish partial help from incorrect or out-of-scope answers.