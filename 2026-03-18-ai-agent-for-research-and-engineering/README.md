# AI Agent for Research and Engineering

**Date:** 2026-03-18
**Venue:** Lab Seminar, School of Computer Science, USYD
**Duration:** 50 min + Q&A
**Languages:** Chinese (primary) · English

## Abstract

AI agents can now handle substantial parts of real research and engineering work. This talk walks through two concrete projects built entirely with Claude Code: a NeurIPS 2026 submission on confidence calibration (CalibrationAGT) and a production-ready full-stack web app (Arigato Cat Boarding System) — developed in parallel. The second half covers the technical internals of how agents work (tools, memory, sub-agents, hooks) and discusses how research and engineering workflows are changing.

## Slides

Open `slides/index.html` in a browser to choose your language, or go directly to:

- `slides/zh.html` — Chinese
- `slides/en.html` — English

**Serve locally** (recommended, some assets require HTTP):

```bash
cd slides
python3 -m http.server 8080
# open http://localhost:8080
```

**Navigation:** `→` / `Space` next · `←` previous · scroll / swipe also works
**Edit mode:** press `E` to edit any text inline, `Ctrl+S` to save to localStorage

## Content

| Part | Topic | Duration |
|------|-------|----------|
| Intro | What is an AI Agent? Context window as a workspace | 5 min |
| Part 1 | CalibrationAGT — full NeurIPS submission pipeline with Claude | 15 min |
| Part 2 | Arigato Cat Boarding — production full-stack app, Claude Code only | 12 min |
| Part 3 | Technical deep dive: tool use, memory, sub-agents, hooks, cron | 10 min |
| Part 4 | Discussion: how research and engineering change in the agent era | 8 min |

## Files

```
slides/
├── index.html       # language picker
├── zh.html          # Chinese slides (source of truth)
├── en.html          # English slides (generated — do not edit directly)
├── gen_en.py        # generates en.html from zh.html
└── assets/
    ├── paper.pdf                  # CalibrationAGT paper
    ├── fig_intro_ambiguity.png    # annotation ambiguity figure
    ├── agent4science.png          # Agents4Science conference stats
    ├── claude_report_cn.jpg       # Claude Workforce Report (CN)
    ├── claude_report_en.webp      # Claude Workforce Report (EN)
    └── ...
```

To regenerate `en.html` after editing `zh.html`:

```bash
cd slides
python3 gen_en.py
```
