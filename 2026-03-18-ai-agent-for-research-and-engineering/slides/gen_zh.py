#!/usr/bin/env python3
"""
Clean zh.html: remove EN bilingual machinery, keep pure Chinese version.
"""
import re

with open('zh.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Remove EN script variants ─────────────────────────────────────────────
for name in ['CC_SCRIPT', 'SKILL0_SCRIPT', 'ARP_SCRIPT', 'BS1_SCRIPT', 'FS1_SCRIPT']:
    en_pattern = re.compile(
        r'const ' + re.escape(name) + r'_EN = \[.*?\n\];\n',
        re.DOTALL
    )
    content = en_pattern.sub('', content)

# ─── 2. Remove currentLang ternaries in run functions ─────────────────────────
for name in ['CC_SCRIPT', 'SKILL0_SCRIPT', 'ARP_SCRIPT', 'BS1_SCRIPT', 'FS1_SCRIPT']:
    content = re.sub(
        r'    const \w+Script = currentLang === .en. \? ' + re.escape(name) + r'_EN : ' + re.escape(name) + r';\n',
        '',
        content
    )
    # Restore loop variable back to canonical script name
    var_name = name.lower().replace('_script', '') + 'Script'
    content = content.replace(f'for (const msg of {var_name})', f'for (const msg of {name})')

# ─── 3. Replace pauseLabel / replayLabel with static Chinese ──────────────────
content = re.sub(
    r'function pauseLabel\(p\) \{[^\}]+\}\nfunction replayLabel\(\) \{[^\}]+\}',
    "function pauseLabel(p) { return p ? '▶ 继续' : '⏸ 暂停'; }\nfunction replayLabel() { return '↺ 重播'; }",
    content
)

# ─── 4. Remove setLang machinery and lang-toggle ──────────────────────────────
# Remove the lang-toggle div
content = re.sub(r'\n<div id="lang-toggle">.*?</div>\n', '\n', content, flags=re.DOTALL)

# Remove LANGUAGE TOGGLE section (currentLang + setLang + localStorage init)
content = re.sub(
    r'/\* =+\n   LANGUAGE TOGGLE\n   =+ \*/\nlet currentLang = .zh.;\n.*?\}\)\(\);\n',
    '',
    content,
    flags=re.DOTALL
)

# ─── 5. Remove lang-toggle CSS and data-lang image rules ──────────────────────
content = re.sub(r'#lang-toggle \{[^}]+\}\n', '', content)
content = re.sub(r'#lang-toggle button \{[^}]+\}\n', '', content)
content = re.sub(r'#lang-toggle button\.active \{[^}]+\}\n', '', content)
content = re.sub(r'html\[data-lang="en"\] \.zh-img \{[^}]+\}\n', '', content)
content = re.sub(r'html\[data-lang="en"\] \.en-img \{[^}]+\}\n', '', content)

# ─── 6. en-img already hidden via .en-img { display:none } in CSS ─────────────
# No changes needed — en-img is hidden by default CSS

with open('zh.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("zh.html cleaned successfully")
