---
domain: ai-workflows
subdomain: physical-ai-data
concept: video-data-for-robot-training
title: Physical AI's Next Bottleneck Is Finding the Right Video
sources:
  - title: "Physical AI's Next Bottleneck Is Finding the Right Video — Rafael Levi, Bright Data"
    url: "https://www.youtube.com/watch?v=I_VEh7XSwyc"
    author: "AI Engineer"
    date: "2026-09-24T14:00:34+00:00"
---

# Physical AI's Next Bottleneck Is Finding the Right Video

Rafael Levi of Bright Data argues that AI models are no longer the hard part; the bottleneck for physical AI and robotics is data. While chat LLMs have trillions of words and image generation has billions of tagged images, robotics has only about a million videos of how robots do things—a small, limited dataset. Companies often pay people to record specific actions like opening a door or sitting on a chair, but Levi calls this "instructed" data: people behave unnaturally when told to perform for a camera, making the movements different from real life and biased for robot training.

Levi dismisses common alternatives: virtual simulations are cheap but their physics is not enough to teach a robot; manual robot control can record only limited hours per day and does not scale; ready-made datasets remain small. The alternative is the internet and web video. YouTube alone may hold billions of videos, with millions of hours of first-person actions such as opening doors, plus natural cause-and-effect and object interactions. He cites a Meta-trained model that used about a million hours of real-world video and then needed only 62 hours of real robotics data to control a real robot.

The core problem is noise: web video is abundant but messy, so finding the right video for training agent world models is the next bottleneck.

- Robotics has far less training data (~1 million videos) than text (trillions of words) or images (billions of tagged images).
- Paid or scripted recordings produce unnatural "instructed" behavior and biased data that may not transfer to real robots.
- Simulations, manual control, and existing datasets are insufficient for scale.
- Internet video, especially YouTube, offers billions of videos and millions of hours of natural first-person actions for robot training.
- Meta used ~1 million hours of real-world video and only 62 hours of robotics data to control a real robot, but noise makes finding the right video the key challenge.