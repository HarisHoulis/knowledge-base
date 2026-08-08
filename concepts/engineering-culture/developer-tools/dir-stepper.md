---
domain: engineering-culture
subdomain: developer-tools
concept: dir-stepper
title: Live coding with dir stepper
sources:
  - title: "Live coding with dir stepper"
    url: "https://jakewharton.com/live-coding-with-dir-stepper/"
    author: "Jake Wharton"
---

# Live coding with dir stepper

Jake Wharton describes the pain of using git commits to manage steps in a live coding presentation, as interactive rebases become messy and going forward through history is awkward. He created dir-stepper, a small command-line tool that stores each step as a numbered directory and copies the files into the working directory. The current step is persisted via an empty file (e.g., .step.2) placed in the project root, making it easy to track and reset during rehearsal. (Jake Wharton, "Live coding with dir stepper")

The tool is a 50-line Kotlin/Native program acting as a glorified cp, supporting next, prev, and reset commands. He integrated it with IntelliJ IDEA using External Tools and assigned keybindings so he could change steps invisibly during the talk. The IDE is set to auto-sync external changes, making the transition seamless. The tool is open source and worked well, despite him forgetting to use it halfway through the talk. (Jake Wharton, "Live coding with dir stepper")

- Git commits are a poor fit for live coding step management due to rebasing overhead and awkward forward navigation.
- Dir-stepper stores each step as numbered directories and copies files into the working directory on demand.
- The current step is tracked with a special marker file, which aids rehearsal and real-time presentation.
- Integration with IntelliJ external tools and keyboard shortcuts allows invisible step changes during a presentation.
- The tool is open source and implemented as a simple Kotlin/Native CLI.