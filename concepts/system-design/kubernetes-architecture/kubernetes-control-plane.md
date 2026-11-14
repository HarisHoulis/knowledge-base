---
domain: system-design
subdomain: kubernetes-architecture
concept: kubernetes-control-plane
title: Kubernetes Explained for Busy Engineers
sources:
  - title: "EP233: Kubernetes Explained for Busy Engineers"
    url: "https://blog.bytebytego.com/p/ep233-kubernetes-explained-for-busy"
    author: "ByteByteGo"
    date: "2026-11-14"
---

# Kubernetes Explained for Busy Engineers

Kubernetes is an orchestration platform that manages the deployment and maintenance of containerized applications across multiple machines. The flow starts when you describe the desired state of your application in a deployment.yaml file, which the API server validates and stores in etcd, a persistent database holding Kubernetes resources like replica counts, pods, nodes, and their assignments [ByteByteGo].

The controller manager runs controllers that reconcile desired state with actual state—for example, ensuring four Pods exist when a Deployment requests four replicas. The scheduler then assigns each pod to worker nodes based on available CPU and memory, placement rules, or other constraints. Worker nodes run the assigned pods via a container runtime that downloads the image and runs the container, while the kubelet tracks node-to-pod assignments and ensures pods run properly [ByteByteGo].

Once pods are running, a Kubernetes Service provides a stable endpoint, and Ingress or Gateway exposes that Service to external users. A key architectural detail is that components never call each other directly: controllers and the scheduler only watch and update objects through the API server, and scheduling is just binding a Pod to a node by setting spec.nodeName. Each kubelet watches for pods bound to its node, so if the scheduler dies, running pods are unaffected—only new ones sit Pending [ByteByteGo].

- Desired state is declared in deployment.yaml, validated by the API server, and persisted in etcd.
- Controllers reconcile actual state to desired state (e.g., maintaining the requested replica count).
- The scheduler binds pods to nodes based on resources and constraints; kubelets run and monitor pods on their nodes.
- Services provide stable endpoints, with Ingress/Gateway exposing them externally.
- Components communicate only through the API server, so a failed scheduler doesn't affect already-running pods.