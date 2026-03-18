# Talk Design: AI Agent for Research and Engineering

**Date:** 2026-03-18
**Venue:** Lab/group seminar
**Duration:** 50 min talk + 10 min Q&A
**Tool:** frontend-slides (HTML presentation)

---

## Audience

- Primary: PhD students and professors (AI background, familiar with LLMs)
- Secondary: A handful of engineers
- Assumption: Audience knows what LLMs are; technical depth is welcome but should come at the end

---

## Core Thesis

> "AI Agent 已经强到可以干真实的事了。我用它做了一篇 NeurIPS 投稿和一个生产级 app——同时进行。"

Narrative mode: Personal story (A) + Evidence-based argument (C)

---

## Structure

### Part 0 — 开场（5 min）

- Hook: "大家可能听过 Codex、Cursor、Claude Code、OpenClaw——它们本质都一样"
- One slide: AI Agent = LLM + tool use + memory，用一张图建立共识
- Thesis statement: 今天用两个真实项目来说明 agent 已经可以干真实的事

### Part 1 — Research: CalibrationAGT（18 min）

Project: NeurIPS 2026 submission on confidence calibration under ambiguous ground truth

Story arc:
- 问题背景（1-2 min）：标注歧义下的 calibration；ECE_voted vs ECE_true
- Agent 怎么帮的（重点）：文献调研 → 实验设计 → 代码实现 → 结果分析 → 写论文
- 展示真实交互截图或 demo
- 展示 toy example figure + 结果表格
- Takeaway: Agent 不是"帮你打字"，是真正的协作者

### Part 2 — Engineering: 猫咪寄养系统（15 min）

Project: 阿里嘎多猫咪寄养 — 女朋友做宠物寄养，原来完全没有系统、非常乱；做 research 的同时做的 side project

Opening line (俏皮):
> "大家都知道我女朋友是做宠物寄养的——不知道的等下可以来了解一下。她们原来完全没有系统，记录全靠脑子和纸。我做 research 的空档，用 Claude Code 花了几天给她做了个。"

Story arc:
- 展示系统截图（桌面版 + 手机版 PWA）
- 功能：寄养管理、上门喂养、预约链接、电子签名、收入统计
- Agent 怎么建的：需求 → 数据库设计 → 前端 → Supabase 后端 → 部署，全程 Claude Code
- Takeaway: AI Agent 大幅降低了跨领域执行的门槛；一个做 ML research 的人可以同时交付生产级全栈 app

### Part 3 — 技术解剖（10 min）

> "为什么 agent 能做这些事？"

Technical content (audience has LLM background):
1. LLM 只会文字接龙，但 agent 框架把它包成了能动手的系统
2. Tool use 机制：LLM → `[tool_use]` → 执行 → 结果回到 context window
3. Memory 架构：system prompt 里的 markdown 文件 = 长期记忆（CLAUDE.md、memory files）
4. Sub-agent：并行 spawn 解决 context window 限制 → Context Engineering
5. 一句话总结：Agent 强大 = LLM 理解力 × 无限工具调用 × 记忆系统

Reference: 李宏毅《解剖小龍蝦》(OpenClaw) 的概念框架，但更精简

### Bonus — gnvitop（5 min）

Easter egg / 广告，俏皮风格:
- "顺带一提，做这两个项目的时候我经常需要知道哪个 GPU 是空的..."
- 展示 gnvitop dashboard
- `pip install gnvitop && gnvitop`，一行命令监控所有 GPU 服务器
- 广告语借势当下 All Claw 大乱斗生态："各种 agent 打得热闹，GPU 还是要自己抢"

---

## Visual Style

- HTML slides (frontend-slides skill)
- Dark theme (academic/tech feel)
- Heavy use of screenshots: CalibrationAGT figures, cat boarding system UI, gnvitop dashboard
- Diagrams for technical section (tool use loop, memory architecture)
- Light humor throughout; not overly formal

---

## Key Screenshots / Assets Available

- `/home/linwei/CalibrationAGT/paper/figs/toy_example.png`
- `/home/linwei/CalibrationAGT/paper/figs/fig_intro_ambiguity.png`
- `/tmp/screenshots2/desktop_tab_boarding.png` (and others)
- `/home/linwei/gnvitop/` (README has dashboard screenshot URL)

---

## Success Criteria

- Audience walks away convinced that AI agents are ready for real research + engineering work
- At least a few people ask "how do I get started with Claude Code?"
- The gnvitop easter egg gets a laugh
