#!/usr/bin/env python3
"""Render the selected Markdown problems as standalone static pages."""
from pathlib import Path
import json
import shutil
from html import escape
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
REPO_URL = 'https://github.com/optpku/Operation_Research_OpenProblem'


def render_math(content, display=False):
    delimiter = '$$' if display else '$'
    tag = 'div' if display else 'span'
    mode = 'block' if display else 'inline'
    return f'<{tag} class="math {mode}">{escape(delimiter + content + delimiter)}</{tag}>'


def math_inline(state, silent):
    if not state.src.startswith('$`', state.pos):
        return False
    end = state.src.find('`$', state.pos + 2)
    if end == -1:
        return False
    if not silent:
        token = state.push('math_inline', 'math', 0)
        token.content = state.src[state.pos + 2:end]
    state.pos = end + 2
    return True


markdown = MarkdownIt('commonmark', {'html': False})
markdown.inline.ruler.before('escape', 'math_inline', math_inline)
markdown.renderer.rules['math_inline'] = lambda tokens, idx, options, env: render_math(tokens[idx].content)
default_fence = markdown.renderer.rules['fence']


def render_fence(tokens, idx, options, env):
    if tokens[idx].info.strip() == 'math':
        return render_math(tokens[idx].content.strip(), display=True) + '\n'
    return default_fence(tokens, idx, options, env)


markdown.renderer.rules['fence'] = render_fence


def page(title, body, prefix='./'):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f5f5ef"><meta name="description" content="Mathematical problems in geometry, combinatorial optimization, and decision processes, with precise statements, related results, and references.">
<title>{escape(title)} · Open Problems</title>
<link rel="icon" href="{prefix}assets/favicon.svg"><link rel="stylesheet" href="{prefix}vendor/katex/katex.min.css"><link rel="stylesheet" href="{prefix}assets/styles.css">
<script defer src="{prefix}vendor/katex/katex.min.js"></script><script defer src="{prefix}vendor/katex/auto-render.min.js"></script><script defer src="{prefix}assets/app.js"></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="header"><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">∴</span><span>Open Problems<small>Geometry · Optimization · Decision processes</small></span></a><nav aria-label="Main navigation"><a href="{prefix}index.html#library">Problems</a><a href="{REPO_URL}">GitHub ↗</a></nav></header>
<main id="main">{body}</main><footer class="footer"><strong>Open Problems</strong><a href="{REPO_URL}">GitHub repository ↗</a></footer></body></html>'''


def build():
    catalog = json.loads((ROOT / 'problems/catalog.json').read_text())
    slugs = {record['slug'] for record in catalog}
    (DOCS / 'assets').mkdir(parents=True, exist_ok=True)
    for name in ['styles.css', 'app.js', 'favicon.svg']:
        shutil.copyfile(ROOT / 'site' / name, DOCS / 'assets' / name)
    (DOCS / '.nojekyll').touch()
    cards = []
    for record in catalog:
        slug = record['slug']
        text = (ROOT / 'problems' / f'{slug}.md').read_text()
        tokens = markdown.parse(text.partition('\n')[2])
        sections = []
        for i, token in enumerate(tokens):
            if token.type == 'heading_open' and token.tag == 'h2':
                anchor = f'section-{len(sections)+1}'
                token.attrSet('id', anchor)
                sections.append((anchor, tokens[i+1].content))
            for child in token.children or []:
                if child.type == 'link_open':
                    target = Path(child.attrGet('href'))
                    if target.suffix == '.md' and target.stem in slugs:
                        child.attrSet('href', f'../{target.stem}/index.html')
        html = markdown.renderer.render(tokens, markdown.options, {})
        folder = DOCS / 'problems' / slug
        folder.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / 'problems' / f'{slug}.md', folder / 'problem.md')
        toc = ''.join(f'<a href="#{anchor}">{escape(title)}</a>' for anchor, title in sections)
        body = f'''<div class="breadcrumbs"><a href="../../index.html#library">Problems</a> / {escape(record['area'])} / {record['id']}</div>
<section class="detail-head"><span class="eyebrow">{record['id']}</span><h1>{escape(record['title'])}</h1></section>
<div class="detail-layout"><aside class="sidebar"><dl><dt>Area</dt><dd>{escape(record['area'])}</dd><dt>Type</dt><dd>{escape(record['type'])}</dd><dt>Status</dt><dd>{escape(record['research_status'])}</dd><dt>Updated</dt><dd>{record['updated']}</dd></dl><div class="buttons"><a class="button" href="problem.md" download>Download Markdown ↓</a></div><nav class="toc" aria-label="On this page">{toc}</nav></aside><article class="article">{html}</article></div>'''
        (folder / 'index.html').write_text(page(record['title'], body, '../../'), encoding='utf-8')
        search = ' '.join(str(value) for value in record.values()) + ' ' + text
        cards.append(f'''<a class="card" href="problems/{slug}/index.html" data-area="{escape(record['area'], quote=True)}" data-status="{escape(record['research_status'], quote=True)}" data-search="{escape(search.lower(), quote=True)}"><div class="card-meta"><span>{record['id']} · {escape(record['area'])}</span><span class="pill">{escape(record['type'])}</span></div><h3>{escape(record['title'])}</h3><p>{markdown.renderInline(record['summary'])}</p><div class="research">Status: {escape(record['research_status'])}</div><div class="card-foot"><span>Read problem</span><span>↗</span></div></a>''')
    areas = ''.join(f'<option>{escape(area)}</option>' for area in dict.fromkeys(r['area'] for r in catalog))
    statuses = ''.join(f'<option>{escape(status)}</option>' for status in dict.fromkeys(r['research_status'] for r in catalog))
    area_counts = dict.fromkeys((r['area'] for r in catalog), 0)
    for record in catalog:
        area_counts[record['area']] += 1
    area_list = ''.join(f'<p>{escape(area)}: {count}</p>' for area, count in area_counts.items())
    body = f'''<section class="hero"><div><div class="eyebrow">GEOMETRY · OPTIMIZATION · DECISION PROCESSES</div><h1>Open Problems</h1><p>A collection of mathematical problems with precise statements, related results, and references.</p><div class="buttons"><a class="button primary" href="#library">Browse problems →</a></div></div><aside class="hero-panel"><span class="big">{len(catalog):02}</span><h2>Problems in {len(area_counts)} research areas</h2>{area_list}</aside></section>
<section id="library"><div class="section-head"><h2>Problem library</h2><span class="muted" id="count" aria-live="polite">{len(catalog)} problems</span></div><div class="filters"><input id="search" type="search" aria-label="Search problem text" placeholder="Search titles, keywords, references, or full text…"><select id="area" aria-label="Filter by research area"><option value="">All areas</option>{areas}</select><select id="research-status" aria-label="Filter by status"><option value="">All statuses</option>{statuses}</select></div><div class="grid">{''.join(cards)}</div><p id="empty" class="empty" hidden>No matching problems. Try another keyword, area, or status.</p></section>'''
    (DOCS / 'index.html').write_text(page('Problem library', body), encoding='utf-8')
    print(f'Built {len(catalog)} problem pages in {DOCS}')


if __name__ == '__main__':
    build()
