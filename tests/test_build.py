"""Regression checks for categorized builds, local links, and Markdown math."""
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.parse import urlsplit

from build import ROOT, build, load_library, markdown, problem_path


class MathText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.expressions = []
        self.in_math = False

    def handle_starttag(self, tag, attrs):
        self.in_math = 'math' in dict(attrs).get('class', '').split()

    def handle_endtag(self, tag):
        self.in_math = False

    def handle_data(self, data):
        if self.in_math:
            self.expressions.append(data)


class GitHubMathTests(unittest.TestCase):
    def test_inline_tex_survives_markdown_punctuation(self):
        text = r'Compare $`\nu^{=}(G)`$ with $`\{x_i:0<x_i<1\}`$ and $`\|x\|_C`$.'
        html = markdown.render(text)
        parser = MathText()
        parser.feed(html)
        self.assertEqual(parser.expressions, [r'$\nu^{=}(G)$', r'$\{x_i:0<x_i<1\}$', r'$\|x\|_C$'])
        self.assertNotIn('<em>', html)
        self.assertNotIn('<code>', html)

    def test_display_formula_is_math_while_python_stays_code(self):
        formula = r'P_n=\mathrm{conv}\{(x,y):y_{ij}=x_ix_j\}.'
        html = markdown.render('```math\n' + formula + '\n```\n\n```python\nprint(1)\n```')
        parser = MathText()
        parser.feed(html)
        self.assertEqual(parser.expressions, ['$$' + formula + '$$'])
        self.assertIn('<code class="language-python">print(1)', html)


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.groups = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'area-group' in attrs.get('class', '').split():
            self.groups.append(attrs['id'])
        for attribute in ('href', 'src'):
            if attribute in attrs:
                self.links.append(attrs[attribute])


class LibraryBuildTests(unittest.TestCase):
    def test_categorized_build_preserves_sources_and_local_links(self):
        areas, catalog = load_library()
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / 'docs'
            build(docs=docs)
            pages = {}
            for path in docs.rglob('*.html'):
                parser = PageLinks()
                parser.feed(path.read_text(encoding='utf-8'))
                pages[path.resolve()] = parser
            self.assertEqual(len(pages), len(catalog) + 1)
            self.assertEqual(pages[(docs / 'index.html').resolve()].groups,
                             ['area-' + area['slug'] for area in areas])
            for record in catalog:
                folder = docs / 'problems' / record['slug']
                self.assertEqual((folder / 'problem.md').read_bytes(),
                                 problem_path(ROOT, record).read_bytes())
                detail = (folder / 'index.html').read_text(encoding='utf-8')
                self.assertIn(record['review_status'], detail)
                self.assertIn(record['research_status'], detail)
            for path, parser in pages.items():
                for href in parser.links:
                    link = urlsplit(href)
                    if link.scheme or link.netloc:
                        continue
                    target = (path.parent / link.path).resolve() if link.path else path
                    with self.subTest(page=str(path), link=href):
                        self.assertTrue(target.is_file(), f'Missing target: {target}')
                        if link.fragment and target in pages:
                            self.assertIn(link.fragment, pages[target].ids)
            detail = (docs / 'problems/variable-discount-mdp/index.html').read_text()
            self.assertIn('href="../strongly-polynomial-mdp/index.html"', detail)

    def test_invalid_classification_and_duplicate_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'problems', root / 'problems')
            path = root / 'problems/catalog.json'
            original = json.loads(path.read_text())
            for field, value, message in (
                ('area_slug', 'missing-area', 'research area'),
                ('area', 'Wrong name', 'research area'),
                ('slug', '../outside', 'Invalid problem slug'),
                ('slug', 'missing-source', 'Missing problem source'),
                ('review_status', '', 'review_status'),
                ('id', original[1]['id'], 'Duplicate problem'),
            ):
                with self.subTest(field=field):
                    catalog = [dict(record) for record in original]
                    catalog[0][field] = value
                    path.write_text(json.dumps(catalog))
                    with self.assertRaisesRegex(ValueError, message):
                        load_library(root)


if __name__ == '__main__':
    unittest.main()
