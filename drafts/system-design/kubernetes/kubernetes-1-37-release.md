---
domain: system-design
subdomain: kubernetes
concept: kubernetes-1-37-release
title: Kubernetes 1.37 Released: Stable Metrics API and Rootless Kubelet in Beta
sources:
  - title: "Kubernetes 1.37 Released: Stable Metrics API and Rootless Kubelet in Beta"
    url: "https://www.infoq.com/news/2026/09/kubernetes-1-37/"
    author: "Mostafa Radwan"
    date: "2026-09-21"
---

# Kubernetes 1.37 Released: Stable Metrics API and Rootless Kubelet in Beta

The CNCF announced Kubernetes 1.37, codenamed "Garhwal", with a focus on stability, security, and AI/ML workload optimization (InfoQ). The release includes 67 enhancements: 27 alpha features, 23 graduating to beta, 16 becoming generally available or stable, and 1 deprecation or removal (InfoQ).

Key stable features include the general availability of the Metrics API, `metrics.k8s.io`, which supports the Horizontal Pod Autoscaler, Vertical Pod Autoscaler, and `kubectl top` (InfoQ). Resilient watchcache initialization also became generally available, preventing the kube-apiserver from flooding etcd after restarts or cache connection loss by delegating bounded requests and rejecting others with HTTP 429 responses (InfoQ). Pod certificates graduated to stable, providing native support for secure pod-to-pod communication and mTLS bootstrapping without external tools (InfoQ).

Alpha and beta features target scheduling, recovery, and security. The `InPlacePodVerticalScalingSchedulerPreemption` feature gate enables workload-aware scheduling by preempting low-priority workloads to free node resources for pending in-place resizing of high-priority applications (InfoQ). Pod-level checkpoint and restore lets the kubelet snapshot and restore a running pod's memory and process trees for debugging or security analysis (InfoQ). StatefulSet Recreate rollout strategy enters alpha, deleting all existing pods for clean recovery of stuck or pending pods during updates (InfoQ). HorizontalPodAutoscaler scale-to-zero support is beta and enabled by default, helping reduce costs for GPU-intensive AI/ML workloads (InfoQ). Kubelet rootless mode, via the `KubeletInUserNamespace` feature gate, is also beta and enabled by default, allowing kubelet to run as non-root using Linux user namespaces to reduce container escape impact (InfoQ). A CNCF webinar on Kubernetes 1.37 is scheduled for September 23, 2026, and Kubernetes 1.38 is expected in December 2026 (InfoQ).

- Metrics API (`metrics.k8s.io`) is generally available and powers HPA, VPA, and `kubectl top`.
- Resilient watchcache initialization is stable, preventing etcd request floods from kube-apiserver restarts with bounded requests and HTTP 429 responses.
- Rootless Kubelet (`KubeletInUserNamespace`) is beta and enabled by default, running core node components as non-root via Linux user namespaces.
- HPA scale-to-zero is beta and enabled by default, reducing costs for AI/ML workloads requiring GPUs.
- Pod certificates are stable, enabling native pod-to-pod mTLS without external bootstrapping tools.