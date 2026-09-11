"""Check the built theme coverage and preservation of published page routes."""
from pathlib import Path
from html.parser import HTMLParser
import re

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.html_count = 0
    def handle_starttag(self, tag, attrs):
        self.html_count += tag == 'html'
        attributes = dict(attrs)
        if 'id' in attributes:
            self.ids.append(attributes['id'])

count = redirects = 0
for directory in ('pages', 'news', 'iugs'):
    for source in Path(directory).rglob('*'):
        if source.suffix not in ('.md', '.html'):
            continue
        text = source.read_text()
        permalink = re.search(r'^permalink: (.+)$', text, re.M)
        url = permalink[1] if permalink else '/' + str(source.with_suffix('.html'))
        output = Path('_site') / (url.lstrip('/') or 'index.html')
        if output.is_dir():
            output /= 'index.html'
        if not output.exists():
            output = output.with_suffix('.html')
        assert output.exists(), f'Missing output: {source}'
        html = output.read_text()
        redirect = re.search(r'^redirect_to: (.+)$', text, re.M)
        if redirect:
            assert redirect[1] in html and 'http-equiv="refresh"' in html, source
            redirects += 1
            continue
        document = Document()
        document.feed(html)
        assert document.html_count == 1, source
        for element in ('ics-banner', 'navMenu', 'main-content'):
            assert document.ids.count(element) == 1, (source, element)
        assert 'setInterval' not in html, source
        assert 'International Commission on Stratigraphy' in html, source
        assert '/images/logo-ics-3D-dark.png' in html, source
        assert all(f'/images/banner-{i:02}.png' in html for i in range(1, 9)), source
        if source.suffix == '.html':
            original = Document()
            original.feed(text)
            assert set(original.ids) <= set(document.ids), source
        count += 1
print(f'PASS: {count} themed pages and {redirects} preserved redirects.')
