# MCP & Agentic Security Directory (2026)

An open index mapping the security infrastructure landscape for the Model Context Protocol ecosystem — categorized by developer tooling, enterprise control planes, and governance frameworks.

**Live site:** [cve415.github.io/MCP-Security](https://cve415.github.io/MCP-Security/)

---

## About this directory

The Model Context Protocol went from an early experiment to foundational enterprise infrastructure in roughly 16 months. In December 2025, it moved under the **[Agentic AI Foundation](https://aaif.io)** alongside a security ecosystem that barely existed a year prior.

But "who are the leaders" is the wrong question—because a solo developer and a Fortune 500 security team are buying completely different things. This directory maps what actually exists and who needs it.

---

## How to use

The site has three tabs:

- **For Developers** — Free, open-source, and self-serve tools. Start here if you're hardening a local workstation or shipping MCP infrastructure at the edge.
- **Enterprise Platforms** — Vendor solutions bought and governed by security/platform teams. Spans network, identity, posture, runtime, and gateway layers.
- **Standards & Governance** — Not vendors; frameworks and organizations that set the rules (OWASP, NIST, CSA, MITRE ATLAS, etc.).

Search across all entries by name, description, developer, or category.

---

## Core workstation security best practices

Regardless of which tools you choose:

1. **Verify Supply Chain Integrity** — Pin all third-party MCP server package hashes and establish a cadence for reviewing them.
2. **Mandate Explicit Authorization** — Disable automatic approvals for tools; require active user consent for any sensitive operations.
3. **Secure Credential Management** — Replace plaintext credentials in configuration files with environment variables or secure secret managers; rotate all existing secrets.
4. **Network Perimeter Control** — Never expose MCP endpoints to public networks; utilize strict authentication (e.g., mTLS, API keys) for all connections.

---

## Contributing

This directory reflects mid-June 2026 sources and is actively maintained. 

To suggest additions, corrections, or removals, [open an issue](https://github.com/cve415/MCP-Governance/issues) or [submit a PR](https://github.com/cve415/MCP-Governance/pulls).

---

## Data structure

- `solo.json` — Developer tooling (open-source, free-tier, self-serve)
- `enterprise.json` — Enterprise platforms and control planes
- `governance.json` — Standards, frameworks, and governance bodies
- `index.html` — Static site with client-side filtering and search

---

**By Christopher Velasco, Agent Architect**
