---
domain: web-dev
subdomain: frontend-testing
concept: testing-trophy
title: The Testing Trophy and Testing Classifications
sources:
  - title: "The Testing Trophy and Testing Classifications"
    url: "https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications"
    author: "Kent C. Dodds"
    date: "2021-06-03"
---

# The Testing Trophy and Testing Classifications

Kent C. Dodds explains the origin and intent of the Testing Trophy, a model for prioritizing front-end test efforts. He describes how it grew out of his earlier post "Write tests. Not too many. Mostly integration." and his agreement with Guillermo Rauch's tweet emphasizing integration testing. Dodds defines a "unit" as a single function, class, or object that contains logic, and classifies unit tests as those with mocked collaborators, while integration tests verify multiple units working together (Kent C. Dodds, 2021, kentcdodds.com). He stresses that testing terminology is not universally agreed upon, quoting a 1990s "test expert" who covered 24 different definitions of "unit test," and argues that classification debates are a distraction from the real goal: confidence. The Testing Trophy places static analysis at the base, then unit tests, with integration tests as the largest focus, and end-to-end tests at the top. Dodds emphasizes that the model applies primarily to monolith codebases and that every testing decision should balance the investment of time against the return of confidence in shipping code.

- The Testing Trophy is a mental model for front-end testing: static analysis forms the base, then unit tests, then a large layer of integration tests, with end-to-end tests at the top.
- Unit tests check a single unit (function/class/object) with dependencies mocked; integration tests verify multiple units working together.
- Testing terminology is ambiguous—there are many definitions of "unit test"—so focus on achieving confidence rather than debating labels.
- The trophy was designed for monolith codebases, not microservices or serverless functions.
- Testing is an investment where the return is confidence; prioritize efforts where you get the best confidence-to-time ratio.