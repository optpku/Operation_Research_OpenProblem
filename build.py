#!/usr/bin/env python3
"""Render the selected Markdown problems as standalone static pages."""
from pathlib import Path
import json
import re
import shutil
from html import escape
from urllib.parse import urlsplit
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
REPO_URL = 'https://github.com/optpku/Operation_Research_OpenProblem'


def problem_path(root, record):
    return root / 'problems' / record['area_slug'] / f"{record['slug']}.md"


def load_library(root=ROOT):
    areas = json.loads((root / 'problems/areas.json').read_text(encoding='utf-8'))
    catalog = json.loads((root / 'problems/catalog.json').read_text(encoding='utf-8'))
    by_slug = {}
    for area in areas:
        slug = area['slug']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in by_slug:
            raise ValueError(f'Invalid or duplicate research area: {slug}')
        by_slug[slug] = area
    ids, slugs = set(), set()
    for record in catalog:
        for field in ('id', 'slug', 'title', 'area', 'area_slug', 'type',
                      'summary', 'review_status', 'research_status', 'updated'):
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"Missing or invalid {field} for {record.get('id', 'problem')}")
        if record['id'] in ids or record['slug'] in slugs:
            raise ValueError(f"Duplicate problem ID or slug: {record['id']}")
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', record['slug']):
            raise ValueError(f"Invalid problem slug: {record['slug']}")
        area = by_slug.get(record['area_slug'])
        if area is None or record['area'] != area['name']:
            raise ValueError(f"Unknown or mismatched research area for {record['id']}")
        source = problem_path(root, record)
        if not source.is_file():
            raise ValueError(f'Missing problem source: {source.relative_to(root)}')
        ids.add(record['id'])
        slugs.add(record['slug'])
    return areas, catalog


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
<meta name="theme-color" content="#f5f5ef"><meta name="description" content="Open problems in operations research and optimization.">
<title>{escape(title)} · Open Problems</title>
<link rel="icon" href="{prefix}assets/favicon.svg"><link rel="stylesheet" href="{prefix}vendor/katex/katex.min.css"><link rel="stylesheet" href="{prefix}assets/styles.css">
<script defer src="{prefix}vendor/katex/katex.min.js"></script><script defer src="{prefix}vendor/katex/auto-render.min.js"></script><script defer src="{prefix}assets/app.js"></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="header"><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">∴</span><span>Open Problems</span></a><nav aria-label="Main navigation"><a href="{prefix}index.html#library">Problems</a><a href="{REPO_URL}/issues">Discuss</a><a href="{REPO_URL}">GitHub ↗</a></nav></header>
<main id="main">{body}</main><footer class="footer"><a href="{REPO_URL}/blob/main/LICENSE">Apache-2.0</a></footer></body></html>'''


def build(root=ROOT, docs=DOCS):
    research_areas, catalog = load_library(root)
    by_area = {area['slug']: area for area in research_areas}
    source_slugs = {problem_path(root, r).resolve(): r['slug'] for r in catalog}
    (docs / 'assets').mkdir(parents=True, exist_ok=True)
    for name in ['styles.css', 'app.js', 'favicon.svg']:
        shutil.copyfile(root / 'site' / name, docs / 'assets' / name)
    # KaTeX is vendored in the checked-in docs tree; preserve it in preview builds.
    if docs.resolve() != (root / 'docs').resolve():
        shutil.copytree(root / 'docs/vendor', docs / 'vendor', dirs_exist_ok=True)
    (docs / '.nojekyll').touch()
    cards = {area['slug']: [] for area in research_areas}
    for record in catalog:
        slug = record['slug']
        source = problem_path(root, record)
        text = source.read_text(encoding='utf-8')
        tokens = markdown.parse(text.partition('\n')[2])
        sections = []
        for i, token in enumerate(tokens):
            if token.type == 'heading_open' and token.tag == 'h2':
                anchor = f'section-{len(sections)+1}'
                token.attrSet('id', anchor)
                sections.append((anchor, tokens[i+1].content))
            for child in token.children or []:
                if child.type == 'link_open':
                    link = urlsplit(child.attrGet('href'))
                    target = (source.parent / link.path).resolve()
                    if not link.scheme and not link.netloc and target in source_slugs:
                        href = f'../{source_slugs[target]}/index.html'
                        if link.query:
                            href += f'?{link.query}'
                        if link.fragment:
                            href += f'#{link.fragment}'
                        child.attrSet('href', href)
        html = markdown.renderer.render(tokens, markdown.options, {})
        folder = docs / 'problems' / slug
        folder.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, folder / 'problem.md')
        toc = ''.join(f'<a href="#{anchor}">{escape(title)}</a>' for anchor, title in sections)
        area = by_area[record['area_slug']]
        maintainers = ', '.join(area['maintainers'])
        maintainer_info = f'<dt>Area maintainers</dt><dd>{escape(maintainers)}</dd>' if maintainers else ''
        body = f'''<div class="breadcrumbs"><a href="../../index.html#library">Problems</a> / <a href="../../index.html#area-{area['slug']}">{escape(record['area'])}</a></div>
<section class="detail-head"><span class="eyebrow">{record['id']}</span><h1>{escape(record['title'])}</h1></section>
<div class="detail-layout"><aside class="sidebar"><dl>{maintainer_info}<dt>Type</dt><dd>{escape(record['type'])}</dd><dt>Review</dt><dd>{escape(record['review_status'])}</dd><dt>Status</dt><dd>{escape(record['research_status'])}</dd><dt>Updated</dt><dd>{escape(record['updated'])}</dd></dl><div class="buttons"><a class="button" href="problem.md" download>Markdown ↓</a></div><nav class="toc" aria-label="On this page">{toc}</nav></aside><article class="article">{html}</article></div>'''
        (folder / 'index.html').write_text(page(record['title'], body, '../../'), encoding='utf-8')
        search = ' '.join(str(value) for value in record.values()) + ' ' + text
        cards[record['area_slug']].append(f'''<a class="card" href="problems/{slug}/index.html" data-area="{escape(record['area'], quote=True)}" data-status="{escape(record['research_status'], quote=True)}" data-search="{escape(search.lower(), quote=True)}"><div class="card-meta"><span>{record['id']}</span><span class="pill">{escape(record['type'])}</span></div><h3>{escape(record['title'])}</h3><p>{markdown.renderInline(record['summary'])}</p><div class="research">{escape(record['research_status'])}</div></a>''')
    areas = ''.join(f'<option>{escape(area["name"])}</option>' for area in research_areas if cards[area['slug']])
    statuses = ''.join(f'<option>{escape(status)}</option>' for status in dict.fromkeys(r['research_status'] for r in catalog))
    active_areas = [area for area in research_areas if cards[area['slug']]]
    groups = []
    for area in active_areas:
        maintainers = ', '.join(area['maintainers'])
        maintainer_note = f'<p>Maintainers: {escape(maintainers)}</p>' if maintainers else ''
        count = len(cards[area['slug']])
        count_text = f'{count} problem' + ('' if count == 1 else 's')
        groups.append(f'''<section class="area-group" id="area-{area['slug']}"><div class="section-head"><div><h2>{escape(area['name'])}</h2>{maintainer_note}</div><span class="muted area-count">{count_text}</span></div><div class="grid">{''.join(cards[area['slug']])}</div></section>''')
    body = f'''<section class="hero"><h1>Open Problems</h1><p>Research questions in operations research and optimization.</p></section>
<section id="library" aria-label="Problem index"><div class="filters"><input id="search" type="search" aria-label="Search problem text" placeholder="Search problems…"><select id="area" aria-label="Filter by research area"><option value="">All areas</option>{areas}</select><select id="research-status" aria-label="Filter by status"><option value="">All statuses</option>{statuses}</select></div><div class="section-head"><span class="muted" id="count" aria-live="polite">{len(catalog)} problems</span></div>{''.join(groups)}<p id="empty" class="empty" hidden>No matching problems.</p></section>
<div class="community"><a href="{REPO_URL}/issues">Discuss or report progress ↗</a><a href="{REPO_URL}/blob/main/templates/problem.md">Submit a problem ↗</a></div>'''
    (docs / 'index.html').write_text(page('Problem library', body), encoding='utf-8')
    print(f'Built {len(catalog)} problem pages in {docs}')


if __name__ == '__main__':
    build()
