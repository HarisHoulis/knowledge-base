---
domain: engineering-culture
subdomain: developer-tooling
concept: dockerfile-shebang
title: Treating Dockerfiles as Shell Scripts
sources:
  - title: "Treating Dockerfiles as shell scripts"
    url: "https://jakewharton.com/treating-dockerfiles-as-shell-scripts/"
    author: "Jake Wharton"
---

# Treating Dockerfiles as Shell Scripts

The article describes a technique for turning Dockerfiles into directly executable scripts, improving the editing and running workflow. By using a shebang line pointing to a helper script, a Dockerfile can be run like `./tool.dockerfile` instead of manually typing `docker build` and `docker run`. The helper builds the image if needed and then runs a container, forwarding any arguments. The author provides a simple bash implementation and links to a more complete tool that supports flags such as volume mounts and environment variables.

- A Dockerfile can be made executable by using a shebang that invokes a helper script.
- The helper runs `docker build` (which only rebuilds when necessary) and then `docker run` with passed arguments.
- This workflow combines the isolation of Docker with the convenience of shell scripts.
- A production-ready version is available on GitHub, supporting flags like `-v` and `-e` before the command.