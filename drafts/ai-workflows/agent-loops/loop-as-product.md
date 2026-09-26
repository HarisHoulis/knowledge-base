---
domain: ai-workflows
subdomain: agent-loops
concept: loop-as-product
title: The Loop Is the Product
sources:
  - title: "The Loop Is the Product — Roland Gavrilescu, Introspection"
    url: "https://www.youtube.com/watch?v=7taOQBfjDyE"
    author: "AI Engineer"
    date: "2026-09-26"
---

# The Loop Is the Product

Roland Gavrilescu (co-founder of Introspection, previously at xAI on agent infrastructure) argues that the frontier of AI engineering has moved through stages — from RLHF-for-models, to the model as a commodity where bindings matter, to now the loop itself, and that the cycle is a product (Gavrilescu, 'The Loop Is the Product'). He frames this around the idea of OODA loops (rendered in the transcript as 'UDA cycles'), coined in the 1970s by the US Air Force for jet fighters responding in dynamic environments; models that call tools and make observations follow the same observe-orient-decide-act pattern. In a loop, the quality of the signal determines the level of success of the cycle, and the quality of the verifier calibrates whether that success is actually correct.

He illustrates with the story of Clawbot (the original name for what is now Openbay), where AJ built the first loop around the product: go to Reddit, find prices and availability, talk to dealers, pit them against each other on price, have a proven way to know when the price is right, and seal the deal. The deeper point is cyclical transformation: taking the artifacts produced at the end of the first cycle and putting them back into the signal so a second cycle can launch and the system improves continuously.

His second idea is that 'distillation of the system is a mode' — the ability to understand what went well and what went wrong in the first cycle and process it into the second. Each cycle generates useful information about bindings, profiles, estimates, models, resources, tools and the environment, and that information needs to remain portable, versioned, and able to evolve over time. He draws an analogy to data recipes in RL research, which were constantly changed to combat hallucinations and reward hacking, and notes no equivalent exists for agents — hence the proposal of the 'agent recipe' as an artifact that incorporates ratings, settings, and human judgment determined as you learn more about your agent operating in its environment.

The agent recipe is what allows reproducible advanced AI systems and a moat that gets better over time, lives within your company, and is agnostic to the models and vendors you use. Cycles should be the way you turn systems into recipes: failure patterns must become judges and assessors, repeated behaviors should become skills and cues, and signals like user frustration, extensions and recalls should be folded back in.

- The unit of competition has shifted from models (RLHF) to bindings to loops — the cycle itself is the product.
- Loop success depends on signal quality, and verifier quality calibrates whether success is actually correct.
- Cyclical transformation means feeding the artifacts of one cycle back into the signal so the next cycle compounds improvement.
- Codify learnings as portable, versioned 'agent recipes' that stay owned by the company and agnostic to models and vendors.
- Turn failure patterns into judges and assessors, and repeated behaviors into skills and cues.