---
domain: ai-workflows
subdomain: robot foundation models
concept: deployment-data-flywheel
title: Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics
sources:
  - title: "Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics"
    url: "https://www.youtube.com/watch?v=Sjfz1TqxzEs"
    author: "AI Engineer"
    date: "2026-09-24"
---

# Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics

Jason Ma, co-founder of Dyna Robotics, describes his company's approach to building a general-purpose robot manipulation foundation model. Dyna was founded in September 2024, has raised about $120 million as a Series A company, and focuses on general-purpose manipulation, with the mission of creating a robust foundation for model autonomy in the real world — a single platform (models plus hardware) that can perform many economically useful physical tasks.

The core thesis is that robots become truly usable at a commercial level only when cutting-edge research is combined with commercial deployments, forming a research-and-deployment flywheel: in-house research determines which real-world workflows can be commercialized, and active deployment both collects high-quality data and reveals where models and hardware underperform, so research effort is directed at problems that actually matter rather than the many possible problems in robotics. Dyna currently has over five deployment locations performing a range of tasks.

On modeling, Ma describes a pre-training data pyramid with three sources: data collected outside the robot (people with cameras, public datasets, and increasingly modeling data), robot data spanning industrial, household, laundry, and hotel tasks, and high-quality deployment data that closes the train/test distribution gap — since robots are usually developed in a lab but deployed in a completely different environment. Dyna reports over 200,000 hours of data in its training pipeline.

The model architecture pairs a high-level reasoning model with a low-level action model that infers agile actions at fine-grained, high-frequency levels. Input is a representation of the world (e.g., camera video of a table) and output is robot joint positions or torque to control the robot. Ma argues physical tasks require both semantic understanding of the world and granular understanding of physical interaction in order to recover from mistakes and perform precise actions.

- Dyna Robotics (founded Sept 2024, ~$120M raised) bets on a research-and-deployment flywheel: real deployments direct which robotics problems are worth solving and supply high-quality data.
- The pre-training data pyramid combines non-robot data (human camera footage, public datasets, modeling data), robot data across task domains, and deployment data that closes the lab-to-real-world distribution gap.
- Over 200,000 hours of data are in the training pipeline.
- The model architecture uses a high-level reasoning model plus a low-level action model for fine-grained, high-frequency control, mapping world representations (camera video) to joint positions or torque.
- The stated goal is to move robotics beyond demos and videos into reliable commercial tasks impacting millions of people.