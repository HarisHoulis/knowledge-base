---
domain: python-backend
subdomain: python-releases
concept: release-candidate-testing
title: Python 3.15.0 candidate 2 is here!
sources:
  - title: "Python 3.15.0 candidate 2 is here!"
    url: "https://simonwillison.net/2026/Sep/1/python-315-rc-2/"
    date: "2026-09-01T14:59:18+00:00"
---

# Python 3.15.0 candidate 2 is here!

Python 3.15.0 has entered the release candidate phase with candidate 2. During this phase, only reviewed code changes that are clear bug fixes are allowed. The Python core team strongly encourages maintainers of third-party projects to test their code against the RC, publish Python 3.15 wheels on PyPI, and help other projects test. Any binary wheels built against Python 3.15.0 release candidates will work with future versions of Python 3.15.

The author emphasizes the importance of testing RC releases, recalling a bug they found in Python 3.10 after it shipped because they hadn't tested during the RC period. For CI, the RC isn't yet available on GitHub Actions, but you can configure setup-python with allow-prereleases and check-latest to automatically test against the latest RC and eventually the stable release.

- Python 3.15.0 RC2 marks feature freeze; only bug fixes allowed until final release.
- Third-party projects should test and publish Python 3.15 wheels during the RC phase.
- Wheels built against RC versions are compatible with future 3.15 releases.
- Testing release candidates can catch bugs before they ship, as the author discovered with Python 3.10.
- GitHub Actions doesn't have RC2 yet, but allow-prereleases and check-latest can track the latest RC.