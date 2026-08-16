---
domain: ai-workflows
subdomain: taxonomy-mapping
concept: hallucinate-then-embed
title: Don't Classify. Hallucinate!
sources:
  - title: "Don't classify. Hallucinate!"
    url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
    author: "Simon Willison"
    date: "2026-08-14T21:54:35+00:00"
---

# Don't Classify. Hallucinate!

In this technique, instead of forcing an LLM to classify a query into a predefined taxonomy, you instruct it to generate novel, open-ended tags that might fit. Then, using vector embeddings, you compare these hallucinated tags against the existing vocabulary and select the concrete tags that are semantically closest. This approach avoids the rigidity of closed classification and leverages the model's generative flexibility (Willison, 2026).

The method is illustrated with a prompt that includes examples of the expected tag structure, such as 'Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables'. The model is asked to create 'novel, never seen before' classifications for a query like 'brown coffee table'. This guides the model to produce realistic, hierarchical candidate labels, which are then matched to actual tags via embeddings (Willison, 2026).

By decoupling generation from classification, this workflow taps into semantic similarity rather than exact matches, making it robust for noisy or varied search queries. It is a practical example of using embeddings for flexible information retrieval and label normalization in production systems (Willison, 2026).

- Generate novel tags with the LLM first, then match them to existing taxonomy via embeddings.
- Include example tag shapes in the prompt to guide the model's output format.
- This approach avoids the constraints of direct classification and improves semantic matching for search queries.
- Useful for handling varied or unseen query phrasings against a fixed set of labels.