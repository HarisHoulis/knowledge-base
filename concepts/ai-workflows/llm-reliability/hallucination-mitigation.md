---
domain: ai-workflows
subdomain: llm-reliability
concept: hallucination-mitigation
title: Why Do LLMs Lie? Understanding and Reducing Hallucinations
sources:
  - title: "Why Do LLMs Lie?"
    url: "https://blog.bytebytego.com/p/why-do-llms-lie"
    author: "ByteByteGo"
    date: "2026-09-29"
---

# Why Do LLMs Lie? Understanding and Reducing Hallucinations

The article defines hallucination as generated information that is factually incorrect, invented, or inconsistent with the material the model is supposed to use. It distinguishes factual hallucinations, which contradict reality; faithfulness hallucinations, which contradict supplied evidence; and fabrication, which invents content such as fake policies, confirmation numbers, or research papers. A hallucination is not literally a lie because it does not establish intent to deceive, but it can present an invented detail as established fact (ByteByteGo).

The mechanism comes from next-token prediction: LLMs calculate probable continuations, and a likely continuation is not a verified statement. Pretraining captures patterns, concepts, relationships, and facts, but familiarity with a subject cannot guarantee every specific fact about a particular case. Training incentives can also encourage guessing when wrong answers and admissions of uncertainty receive the same score, while abstention receives zero. Confidence percentages require calibration evidence to be meaningful (ByteByteGo).

RAG is a major defense: it retrieves relevant approved material and adds it to the model’s input before generation. However, retrieval can fail by returning retired policies, the wrong product’s policy, or incomplete passages, and the model can still misread correct evidence or add unsupported promises. Tools complement RAG by fetching customer-specific facts through APIs, such as purchase date or account usage, but the lookup must actually happen and tool failures must remain visible to the application (ByteByteGo).

Other defenses include making insufficient evidence a valid outcome, such as a “needs review” state, rather than forcing every response into eligible or ineligible. Chain-of-thought explanations are not proof because they may contain false premises or fail to faithfully describe what influenced the result; instead, applications should request concise justifications tied to checkable evidence. Verification as a separate workflow step—drafting an answer, generating verification questions, and answering them independently—reduced hallucinations on evaluated tasks, though the checker itself can make mistakes (ByteByteGo).

- Hallucinations are not intentional lies but confident falsehoods from normal generation; they can be split into factual hallucinations, faithfulness hallucinations, and fabrication.
- LLMs generate probable text rather than verified facts, and training incentives can reward guessing over admitting uncertainty.
- RAG supplies evidence but depends on well-prepared, non-conflicting documents and checking what the model actually retrieves.
- Tools and APIs provide missing individual facts, but actual successful execution must be verified rather than assumed.
- Allowing uncertainty as a valid outcome and using separate verification steps can make LLM answers more dependable.