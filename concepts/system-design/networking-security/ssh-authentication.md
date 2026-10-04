---
domain: system-design
subdomain: networking-security
concept: ssh-authentication
title: How SSH Works
sources:
  - title: "EP228: How SSH Works"
    url: "https://blog.bytebytego.com/p/ep228-how-ssh-works"
    author: "ByteByteGo"
    date: "Sat, 03 Oct 2026 15:30:39 GMT"
---

# How SSH Works

Secure Shell (SSH) is a method for accessing a remote machine securely over an unsecured network. It starts with a TCP connection from the SSH client to the remote SSH server, after which both machines exchange SSH versions and negotiate crypto algorithms (ByteByteGo, EP228).

Each side then runs a key exchange protocol. The SSH server sends its public key and a signature; the client verifies the signature and checks the host key against its known_hosts file. Both machines then derive session keys independently, and those keys are never shared over the network (ByteByteGo, EP228).

SSH authentication begins when the client sends the public key for login. The server matches that public key in authorized_keys, and the client signs the auth request with its private key and sends the digital signature. The private key never leaves the client machine; the server verifies the signature with the client public key. This completes authentication and opens the session for communication (ByteByteGo, EP228).

- SSH begins with a TCP connection and version/crypto algorithm negotiation.
- The server sends a public key and signature; the client verifies it and checks known_hosts.
- Session keys are derived separately on each side and never transmitted over the network.
- Authentication uses the client's public key in authorized_keys and a private-key signature that the server verifies.
- The private key never leaves the client machine.