# Talks

Public talks and presentations. Each is a self-contained HTML slide deck — no build tools, no dependencies, just open in a browser.

**Live site:** https://linwei94.github.io/talks/

## Talks

| Date | Title | Venue |
|------|-------|-------|
| 2026-04-20 | [Agents in My Workflow: Five Cases](https://linwei94.github.io/talks/2026-04-20-agent-use-cases-apple/slides/) | Internal Talk, Apple Research |
| 2026-03-25 | [Claude Code for Physics](https://linwei94.github.io/talks/2026-03-25-claude-code-physics/slides/) | Guest Talk — Céline Bœhm group |
| 2026-03-24 | [AI Agents for Research and Engineering: From Automation to Reliable Autonomy](https://linwei94.github.io/talks/2026-03-24-ai-agents-sjtu/slides/) | Invited Talk — Young Scientist Seminar, SJTU |
| 2026-03-18 | [AI Agent for Research and Engineering](https://linwei94.github.io/talks/2026-03-18-ai-agent-for-research-and-engineering/slides/) | Lab Seminar, USYD |


## Quick Start

```bash
cd <talk-directory>/slides
python3 -m http.server 8080
# open http://localhost:8080
```

For projection over LAN:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# open http://<your-ip>:8080
```

## Structure

```
talks/
└── YYYY-MM-DD-talk-title/
    ├── README.md
    └── slides/
        ├── index.html    # language picker
        ├── zh.html       # Chinese slides
        ├── en.html       # English slides (generated)
        ├── gen_en.py     # generates en.html from zh.html
        └── assets/       # images, PDFs, audio
```
