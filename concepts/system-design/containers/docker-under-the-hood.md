---
domain: system-design
subdomain: containers
concept: docker-under-the-hood
title: How Docker Works Under the Hood
sources:
  - title: "EP221: How Docker Works Under the Hood"
    url: "https://blog.bytebytego.com/p/ep221-how-docker-works-under-the"
    author: "ByteByteGo"
    date: "Sat, 11 Jul 2026 15:30:14 GMT"
---

# How Docker Works Under the Hood

Docker containers are not lightweight VMs but ordinary Linux processes isolated by kernel features. The Docker CLI sends an API call to the dockerd daemon, which checks for the image locally or pulls it from a registry, then prepares the container config. Rather than starting the container directly, dockerd hands the request to containerd, which manages the container lifecycle and assembles an OCI bundle with config and root filesystem. containerd then invokes runc, which creates the necessary Linux namespaces and mounts, starts the process, and exits. The result is a regular process with its own PID, network, and mount namespaces, using a stack of read-only image layers plus a writable layer. No hypervisor or guest OS is involved; isolation comes from namespaces and resource limits from cgroups (ByteByteGo, 2026).

- Docker CLI → dockerd → containerd → runc: each layer has a specific role in pulling images, managing lifecycle, and creating the isolated environment.
- A running container is just a Linux process with dedicated namespaces and cgroups, not a virtual machine.
- The filesystem consists of read-only image layers with a writable top layer, ensuring container changes don't alter the image.
- The article also briefly covers git merge/rebase, vector databases, pagination, and LLM deep research workflows.