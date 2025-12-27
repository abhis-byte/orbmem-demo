# Security Policy

## Overview

Orbmem is an open-source Python package designed as a memory and reasoning backend for AI systems.  
We take security seriously and aim to responsibly address vulnerabilities that could impact users, developers, or downstream systems.

This policy outlines how to report security issues and what to expect from the response process.

---

## Supported Versions

Security updates are provided for the latest released version of Orbmem on PyPI.

| Version | Supported |
|--------|-----------|
| Latest | ✅ Yes |
| Older versions | ❌ No |

Users are strongly encouraged to upgrade to the latest version to receive security fixes.

---

## Reporting a Vulnerability

If you discover a security vulnerability, **please do not open a public GitHub issue**.

Instead, report it privately follow our email:

- **Email:** `orbynt@gmail.com` *(recommended)*  

When reporting, please include:
- A clear description of the issue
- Steps to reproduce (if applicable)
- Potential impact
- Affected versions
- Any relevant logs, stack traces, or proof-of-concept code

---

## What to Expect

- We will acknowledge receipt of your report within **48 hours**
- We will investigate and assess the issue as quickly as possible
- If confirmed, we will work on a fix and release a patched version
- Responsible disclosure will be coordinated before public release

---

## Security Scope

This security policy covers:
- The Orbmem Python package distributed via PyPI
- Core memory, indexing, and reasoning components
- Configuration, serialization, and data-handling logic

This policy does **not** cover:
- User-deployed infrastructure
- Third-party integrations
- Misconfigurations outside Orbmem’s documented usage

---

## Dependencies

Orbmem relies on third-party open-source libraries.  
While we aim to keep dependencies up to date, vulnerabilities originating from external dependencies should be reported if they affect Orbmem’s security posture.

---

## Responsible Disclosure

We appreciate and encourage responsible disclosure.  
Security researchers will be credited (with permission) in release notes or advisories.

Thank you for helping keep Orbmem and its users safe.

— The Orbmem Maintainers
