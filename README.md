# Talks

Public talks and presentations. Each is a self-contained HTML slide deck — no build tools, no dependencies, just open in a browser.

## Talks

| Date | Title | Venue |
|------|-------|-------|
| 2026-04-20 | [Agents in My Workflow: Five Cases](./2026-04-20-agent-use-cases-apple/) | Internal Talk, Apple Research |
| 2026-03-25 | [Claude Code for Physics](./2026-03-25-claude-code-physics/) | Guest Talk — Céline Bœhm group |
| 2026-03-24 | [AI Agents for Research and Engineering: From Automation to Reliable Autonomy](./2026-03-24-ai-agents-sjtu/) | Invited Talk — Young Scientist Seminar, SJTU |
| 2026-03-18 | [AI Agent for Research and Engineering](./2026-03-18-ai-agent-for-research-and-engineering/) | Lab Seminar, USYD |


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
