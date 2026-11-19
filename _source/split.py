"""Split the pandoc Markdown of the Calydon GDD into MkDocs pages."""
import re, sys, os, pathlib
src, out = sys.argv[1], pathlib.Path(sys.argv[2])
text = open(src, encoding='utf-8').read()
text = text[text.index('# ** **Calydon Quick Sheet'):].replace('# ** **Calydon Quick Sheet', '# Calydon Quick Sheet')

SLUGS = ['quick-sheet','product-overview','purpose-and-organization','opening-gameplay',
         'races-characters-factions','story-structure','interface','obstacles',
         'level-walkthrough','gameplay','art','audio-requirements']
FIG = {}  # filled per figure
figno = 0

def fix_common(t):
    t = t.replace('\\<REDACTED\\>', '<span class="redacted">Redacted</span>')
    t = re.sub(r'\\<Rest of the write-up is redacted\\>\s*', '<span class="redacted">Rest of the write-up is redacted</span>', t)
    t = t.replace('<br><br>• ', '<br>• ')
    t = re.sub(r'\*\*(Category|Description|Enemy|No\.|Name|Interface Element|Control Category|Key|Mouse|[A-Z][\w /]*?)\*\*(\s*\|)', r'\1\2', t)  # bold header cells
    # Notes -> admonitions
    t = re.sub(r'^\*\*Note\(s\):\*\* (.+)$', lambda m: '!!! note\n\n    ' + m.group(1), t, flags=re.M)
    t = re.sub(r'^\*\*Note:\*\* (.+)$', lambda m: '!!! note\n\n    ' + m.group(1), t, flags=re.M)
    t = re.sub(r'^Note: (.+)$', lambda m: '!!! note\n\n    ' + m.group(1), t, flags=re.M)
    t = re.sub(r'[ \t]+$', '', t, flags=re.M)
    return t

chunks = re.split(r'^# ', text, flags=re.M)[1:]
assert len(chunks) == 12, len(chunks)
nav = []
for n, chunk in enumerate(chunks, 1):
    title, body = chunk.split('\n', 1)
    title = title.strip().replace('“', '"').replace('”', '"')
    h2 = h3 = 0
    lines = []
    for line in body.split('\n'):
        m = re.match(r'^(#{2,4}) +(.*)$', line)
        if m:
            lvl, h = len(m.group(1)), m.group(2).strip()
            h = re.sub(r'<img[^>]*/>', '', h).strip()
            if lvl == 2:
                h2 += 1; h3 = 0
                if n > 1: h = f'{n}.{h2} {h}'
            elif lvl == 3:
                h3 += 1; h = f'{n}.{h2}.{h3} {h}'
            line = '#' * lvl + ' ' + h
        lines.append(line)
    body = fix_common('\n'.join(lines))
    page = f'# {n} {title}\n' + body
    fname = f'{n:02d}-{SLUGS[n-1]}.md'
    (out / fname).write_text(page.rstrip() + '\n', encoding='utf-8')
    nav.append((f'{n}. {title}', fname))
for t, f in nav: print(f'  - "{t}": {f}')
