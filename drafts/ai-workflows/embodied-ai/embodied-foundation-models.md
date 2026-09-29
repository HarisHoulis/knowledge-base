---
domain: ai-workflows
subdomain: embodied-ai
concept: embodied-foundation-models
title: From VLM/VLA's to Embodied Agents
sources:
  - title: "From VLM/VLA's to Embodied Agents — Armen Aghajanyan, Perceptron AI"
    url: "https://www.youtube.com/watch?v=ZZcE0HeO-Hc"
    author: "AI Engineer"
    date: "2026-09-23T16:00:30+00:00"
---

# From VLM/VLA's to Embodied Agents

Armen Aghajanyan, co-founder and CEO of Perceptron, argues for moving away from distinctions between VLMs, VLAs, and world models toward what he calls “embodied fundamental models” (AI Engineer, 2026). He describes Perceptron’s North Star as creating physical foundations of AI that allow systems to perceive, understand, and interact with the physical world in real time, connecting the physical and digital worlds and providing intelligence to devices, tools, robots, cameras, and sensors (AI Engineer, 2026). He frames the ability to perceive, reason, and act as a unification of traditional multimodal modeling.

Aghajanyan surveys related model categories: VLMs take images, video, and text and output text; embodied thinking models may derive reference points for better spatial understanding or reasoning; VLAs expand output beyond text to actions; world models output video or future frames from inputs such as images, video, or actions; and “semantic models of the world” learn representations without inferring anything directly, hoping they will be useful later (AI Engineer, 2026). Perceptron views an embodied base model as a framing that lets standard perception, embodied thinking, and control happen within one model, reasoning over multiple input modalities and producing most of the mentioned output types.

The talk highlights two fundamental research challenges. Simulating something like one hour of video can involve around 1 million visual tokens, while common approaches such as extracting transcripts, synthetically tagging frames, or asking questions count loss on only a tiny fraction of tokens—about 0.2% in his example—so the training signal is too sparse, too synthetic, or indecipherable (AI Engineer, 2026). Predicting every pixel gives a dense signal but distributes attention poorly, treating background pixels with the same importance as gripper tips, contact points, faults, or physics.

Perceptron’s claimed core intellectual property is to think about what a natural perceptual target looks like: how to predict perceptions that will matter in the future, automatically (AI Engineer, 2026). As an example, he says one can hard-code that for a robotic arm, the tip of the grippers is a very useful perception that can be predicted in the future.

- Perceptron aims to replace separate VLM/VLA/world-model categories with a unified “embodied fundamental model” that perceives, reasons, and acts in the physical world in real time (AI Engineer, 2026).
- The talk categorizes multimodal models by input/output: VLMs (images/video/text to text), embodied thinking models (spatial reasoning), VLAs (actions), world models (video/future prediction), and semantic world models (learned representations) (AI Engineer, 2026).
- A core challenge is training signal design for video-scale data: synthetic labels can be too sparse or low-quality, while pixel prediction is dense but misallocates attention to unimportant regions (AI Engineer, 2026).
- Perceptron’s approach is to predict natural perceptual targets that matter for future interaction, such as the gripper tip of a robotic arm, rather than every pixel or only sparse synthetic annotations (AI Engineer, 2026).