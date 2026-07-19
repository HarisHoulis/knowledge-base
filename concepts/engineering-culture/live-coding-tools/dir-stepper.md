---
domain: engineering-culture
subdomain: live-coding-tools
concept: dir-stepper
title: Live coding with dir stepper
sources:
  - title: "Live coding with dir stepper"
    url: "https://jakewharton.com/live-coding-with-dir-stepper/"
    author: "Jake Wharton"
---

# Live coding with dir stepper

Jake Wharton introduces dir-stepper, a command-line tool he created to manage step-by-step code progression during live coding presentations. Frustrated by the complexity of using git commits—which required frequent interactive rebasing and caused conflicts when modifying earlier steps—he built a simpler solution. The tool stores each presentation step as a numbered subdirectory containing the full file structure for that step. On invocation, it copies the files from the target step directory into the working project folder, overwriting the previous state. A marker file (e.g., `.step.2`) in the project root tracks the current step, making it easy to reference during the talk. Wharton integrated dir-stepper into IntelliJ IDEA as an external tool, assigning keyboard shortcuts for 'next', 'prev', and 'reset' commands. This setup allowed him to change steps invisibly during the presentation without leaving the IDE. The tool is open-source and demonstrated in a video linked in the README.

- Git commits are impractical for live coding because rebasing earlier steps causes conflicts and disrupts flow.
- dir-stepper uses a directory of numbered step folders; each contains the full file state for that step.
- The tool copies files from the chosen step to the working directory, with a .step.N marker file tracking the current step.
- IntelliJ IDEA's external tools feature allows binding keyboard shortcuts to invoke dir-stepper invisibly during a presentation.
- The tool supports 'next', 'prev', and 'reset' commands for forward, backward, and reset navigation.