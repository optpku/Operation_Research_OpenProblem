"""Regression checks for literal TeX surviving GitHub Markdown syntax."""
from html.parser import HTMLParser
import unittest

from build import markdown


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


if __name__ == '__main__':
    unittest.main()
