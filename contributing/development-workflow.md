---
title: Development Workflow
parent: Contributing
nav_order: 3
review_date: 2026-08-01
guide_category:
  - Contributing
guide_category_order: 3
guide_description: Git practices, working with AI assistants, and development best practices
guide_difficulty: intermediate
guide_time: 10 min
guide_emoji: 🔄
guide_labels:
  - Git
  - Best Practices
  - AI Assistants
---

# Development Workflow

This guide covers git practices, working with AI coding assistants, and best practices for contributing to TrustGraph.

## Git Branching

### Branch Naming

- **Release branches**: `release/vX.Y` (e.g. `release/v1.8`)
- **Feature branches**: `feature/FEATURE-NAME` (e.g. `feature/authentication`)
- **Bugfix branches**: `fix/FIX-NAME` (e.g. `fix/gateway-proto-failure`)
- **Maintenance branches**: `maint/MAINT-NAME` (e.g. `maint/update-pulsar-deps`)

### Release Tags

- Format: `vX.Y.Z` (e.g. `v1.8.3`)

### Branch from Release

Always branch from the latest `release/vX.Y` branch, not `main`. Release branches contain the latest code used to build containers and are the stable base for new work.

```bash
git checkout release/v1.8
git checkout -b feature/my-feature
```

## Working with AI Assistants

AI coding assistants (Claude, Qwen, etc.) can accelerate development, but work best with some guidance.

### Tips for Effective Use

- **AI assistants aren't perfect** — Learn their limitations and verify their output
- **Write things down** — Submit a tech spec with your PR so others can use AI assistants to review and enhance your work
- **Keep it modular** — Well-defined classes and modules reduce the need for the assistant to "know everything" at once
- **Catch them early** — Assistants can go off-track when confused; redirect before they waste time
- **Know the codebase** — Understand existing patterns to prevent assistants from reinventing solved problems

### Suggested Process

1. **Read TEST_STRATEGY.md** — Have the assistant understand the testing approach
2. **Write a tech spec** — Create `docs/tech-specs/FEATURE.md` before implementing
3. **Iterate on the spec** — Review and refine before coding
4. **Commit the spec** — Save it before implementation begins
5. **Implement incrementally** — Commit regularly to bank progress
6. **Test frequently** — Run tests yourself and paste errors to the assistant (saves tokens)

### Package Reinstalls

AI assistants may forget that packages need reinstalling after code changes. Since `pip install -e` doesn't work well with TrustGraph's namespace packages, manually run:

```bash
pip install ./trustgraph-base
pip install ./trustgraph-flow
# etc.
```

## Best Practices

### Code Quality

- **Modular code** — Well-architected code helps both AI assistants and human reviewers
- **Solve common problems commonly** — Reuse existing patterns; saves time and tokens
- **Incremental changes** — Small, focused commits are easier to review and roll back

### Testing

- **Test frequently** — Catch issues early
- **Run the full suite** before submitting PRs:
  ```bash
  pytest tests/unit
  pytest tests/integration -m 'not slow'
  pytest tests/contract
  ```
- **Write tests for new features** — Comprehensive coverage is expected

### Pull Requests

- **Keep PRs focused** — One feature or fix per PR
- **Include context** — Explain what and why in the PR description
- **Link to tech specs** — Reference any design documents
- **Ensure tests pass** — CI will verify, but check locally first

## Share Your Experiences

We love hearing how contributors use AI assistants and other tools. Join us on [Discord](https://discord.gg/sQMwkRz5GX) and share what works for you.

## Next Steps

- [Getting Started with Development](development-setup) — Set up your environment
- [Contributing Guidelines](contributing) — PR process and CLA
- [Documentation Guidelines](documentation-guidelines) — Standards for docs contributions
