# Talks

My public talks and presentations. Each is a self-contained HTML presentation — no build tools, no dependencies, just open in a browser.

## Talks

| Date | Title | Venue |
|------|-------|-------|
| 2026-03-18 | [AI Agent for Research and Engineering](./2026-03-18-ai-agent-for-research-and-engineering/) | Lab Seminar |

## 快速启动

```bash
cd <talk-directory>/slides
python3 -m http.server 8080
# open http://localhost:8080
```

投影时用局域网地址：

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# open http://<your-ip>:8080
```

## 结构

```
talks/
└── YYYY-MM-DD-talk-title/
    ├── README.md        # 摘要、启动说明、内容结构
    ├── slides/
    │   ├── index.html   # 幻灯片主文件（单 HTML，零依赖）
    │   └── assets/      # 图片、PDF 等本地资源
    └── docs/            # 设计文档、草稿
```
