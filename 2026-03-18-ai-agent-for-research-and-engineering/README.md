# AI Agent for Research and Engineering

**Date:** 2026-03-18
**Venue:** Lab Seminar
**Duration:** 50 min + Q&A

用两个真实项目说明 AI Agent 已经可以干真实的事：一篇 NeurIPS 2026 投稿（CalibrationAGT）和一个生产级全栈 app（阿里嘎多猫咪寄养系统），同时完成。

## 启动幻灯片

```bash
cd slides
python3 -m http.server 8080
```

然后在浏览器打开 `http://localhost:8080`。

**局域网访问（投影用）：**

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

打开 `http://<your-ip>:8080`（用 `hostname -I` 查本机 IP）。

**操作：**
- `→` / `Space` 下一张，`←` 上一张
- 直接滚动或触控滑动也可以
- 按 `E` 进入编辑模式，点击文字直接修改，`Ctrl+S` 保存到 localStorage

## 内容结构

| Part | 主题 | 时长 |
|------|------|------|
| 开场 | AI Agent 是什么，context 的本质 | 5 min |
| Part 1 | CalibrationAGT — NeurIPS 投稿全流程 | 15 min |
| Part 2 | 猫咪寄养管理系统 — 生产级 app 全程 Claude Code | 12 min |
| Part 3 | 技术解剖：Tool use、Memory、Sub-agent | 10 min |
| Part 4 | 反思：科研和工程在 Agent 时代会怎么变？ | 8 min |
| Bonus | gnvitop — GPU 监控小工具 | 2 min |

## 文件结构

```
slides/
├── index.html          # 完整幻灯片（单文件，零依赖）
└── assets/
    ├── paper.pdf                    # CalibrationAGT 论文
    ├── toy_example.png              # ECE_voted vs ECE_true 示意图
    ├── fig_intro_ambiguity.png      # 标注歧义图
    ├── desktop_tab_boarding.png     # 猫咪系统桌面截图
    └── ...
```
