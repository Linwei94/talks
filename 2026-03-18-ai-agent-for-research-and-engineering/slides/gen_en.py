#!/usr/bin/env python3
"""
Generate en.html from index.html (zh.html):
1. Swap data-en content into element innerHTML
2. Switch zh-img hidden / en-img visible
3. Use EN terminal scripts directly (remove ZH variants)
4. Remove lang-toggle and setLang machinery
5. Fix pause/replay button labels to English
"""
import re

with open('zh.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Replace data-en element content ───────────────────────────────────────
# Strategy: find opening tags with data-en="...", then replace content up to
# the matching closing tag.  Works for leaf + shallow elements used in slides.

def replace_data_en(html):
    # Handle both data-en="..." (double quotes) and data-en='...' (single quotes)
    for q in ('"', "'"):
        pattern = re.compile(
            r'(<(\w+)(?:[^>]*?)\s+data-en=' + q + r'((?:[^' + q + r'\\]|\\.)*)' + q + r'\s*(?:[^>]*)?>)'
            r'(.*?)'
            r'(</\2>)',
            re.DOTALL
        )

        def replacer(m, _q=q):
            full_open = m.group(1)
            tag_name  = m.group(2)
            en_val    = m.group(3)
            close     = m.group(5)
            # Remove data-en and data-zh (both quote styles) from opening tag
            clean_open = re.sub(r'\s+data-en="(?:[^"\\]|\\.)*"', '', full_open)
            clean_open = re.sub(r"\s+data-en='(?:[^'\\]|\\.)*'", '', clean_open)
            clean_open = re.sub(r'\s+data-zh="(?:[^"\\]|\\.)*"', '', clean_open)
            clean_open = re.sub(r"\s+data-zh='(?:[^'\\]|\\.)*'", '', clean_open)
            return f'{clean_open}{en_val}{close}'

        prev = None
        while prev != html:
            prev = html
            html = pattern.sub(replacer, html)
    return html

content = replace_data_en(content)

# ─── 2. Image visibility: hide zh-img, show en-img ───────────────────────────
# zh-img: change display style to none
content = re.sub(
    r'(<img\s[^>]*class="zh-img"[^>]*style=")[^"]*(")',
    r'\1display:none\2',
    content
)
# en-img: change display style to block (or inline-block)
content = re.sub(
    r'(<img\s[^>]*class="en-img"[^>]*style=")[^"]*(")',
    lambda m: m.group(0).replace('display:none', 'display:block'),
    content
)

# ─── 3. Terminal scripts: replace ZH scripts with EN variants ─────────────────
# Remove ZH scripts (they are defined first, then _EN variants follow)
for name in ['CC_SCRIPT', 'SKILL0_SCRIPT', 'ARP_SCRIPT', 'BS1_SCRIPT', 'FS1_SCRIPT']:
    # Remove the ZH script block (from "const NAME = [" to "];" at start of line)
    zh_pattern = re.compile(
        r'const ' + re.escape(name) + r' = \[.*?\n\];\n',
        re.DOTALL
    )
    content = zh_pattern.sub('', content)
    # Rename _EN variant to canonical name
    content = content.replace(f'const {name}_EN = [', f'const {name} = [')

# Remove the ternary script selectors (e.g. "currentLang === 'en' ? CC_SCRIPT_EN : CC_SCRIPT")
for name in ['CC_SCRIPT', 'SKILL0_SCRIPT', 'ARP_SCRIPT', 'BS1_SCRIPT', 'FS1_SCRIPT']:
    content = re.sub(
        r'const \w+Script = currentLang === .en. \? ' + re.escape(name) + r'_EN : ' + re.escape(name) + r';\n',
        '',
        content
    )
    # Also rename the local script variable usage back to canonical name
    # e.g. "for (const msg of ccScript)" → "for (const msg of CC_SCRIPT)"
    var_name = name.lower().replace('_script', '') + 'Script'
    content = content.replace(f'for (const msg of {var_name})', f'for (const msg of {name})')

# ─── 4. Fix button labels to English static text ─────────────────────────────
content = content.replace('>⏸ 暂停<', '>⏸ Pause<')
content = content.replace('>↺ 重播<', '>↺ Replay<')

# Replace pauseLabel / replayLabel functions with static English
content = re.sub(
    r'function pauseLabel\(p\) \{[^\}]+\}\nfunction replayLabel\(\) \{[^\}]+\}',
    "function pauseLabel(p) { return p ? '▶ Resume' : '⏸ Pause'; }\nfunction replayLabel() { return '↺ Replay'; }",
    content
)

# ─── 5. Remove lang-toggle button and setLang machinery ───────────────────────
# Remove the lang-toggle div
content = re.sub(r'\n<div id="lang-toggle">.*?</div>\n', '\n', content, flags=re.DOTALL)

# Remove setLang function and its call
content = re.sub(
    r'/\* =+\n   LANGUAGE TOGGLE\n   =+ \*/\nlet currentLang = .zh.;\n.*?\}\)\(\);\n',
    '',
    content,
    flags=re.DOTALL
)

# ─── 6. CSS: remove lang-toggle styles and data-lang image switching ──────────
content = re.sub(r'#lang-toggle \{[^}]+\}\n', '', content)
content = re.sub(r'#lang-toggle button \{[^}]+\}\n', '', content)
content = re.sub(r'#lang-toggle button\.active \{[^}]+\}\n', '', content)
content = re.sub(r'html\[data-lang="en"\] \.zh-img \{[^}]+\}\n', '', content)
content = re.sub(r'html\[data-lang="en"\] \.en-img \{[^}]+\}\n', '', content)

# ─── 7. Set html lang attribute ───────────────────────────────────────────────
content = content.replace('<html lang="zh-CN">', '<html lang="en">', 1)

# ─── 8. Update page title ─────────────────────────────────────────────────────
content = content.replace(
    '<title>AI Agent for Research and Engineering</title>',
    '<title>AI Agent for Research and Engineering (EN)</title>',
    1
)

# ─── 9. Fix remaining Chinese text ───────────────────────────────────────────
# CSS comments (not visible but clean anyway)
content = content.replace('THEME: Swiss Modern × 投影优化 × 中文', 'THEME: Swiss Modern × Projection Optimized × English')
content = content.replace('/* 投影优化字号：偏大 */', '/* Projection-optimized sizes: slightly large */')
# HTML comments (slide markers)
content = re.sub(r'<!-- =+ SLIDE \d+: [^=]+=+ -->', lambda m: m.group(0), content)
# iframe title attribute
content = content.replace('title="猫咪寄养系统"', 'title="Cat Boarding System"')
# Alt attributes on zh-img/en-img
content = content.replace('alt="Claude职业报告（中文）"', 'alt="Claude Workforce Report (Chinese)"')
content = content.replace('alt="Claude Workforce Report (EN)"', 'alt="Claude Workforce Report (English)"')

# ─── 10. en-img visibility: make sure en-img is shown by default ──────────────
# Since we removed the CSS data-lang rules, en-img might still be display:none in static CSS
# Remove the .zh-img { display:none } / .en-img { display:none } rules and replace with proper defaults
content = re.sub(r'\.zh-img\s*\{[^}]*display\s*:\s*none[^}]*\}', '.zh-img { display: none }', content)
content = re.sub(r'\.en-img\s*\{[^}]*display\s*:\s*none[^}]*\}', '.en-img { display: block }', content)

with open('en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("en.html generated successfully")
