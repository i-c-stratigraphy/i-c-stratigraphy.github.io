import tempfile
import unittest
from pathlib import Path
from assemble_pages import assemble, preview_url, rebase_html


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.production = self.root / 'production'
        self.preview = self.root / 'preview'
        for path in (self.production, self.preview):
            path.mkdir()
            (path / 'index.html').write_text('<html>Home</html>')
        (self.production / 'CNAME').write_text('stratigraphy.org\n')
        (self.preview / 'executive.html').write_text('Executive')
        (self.preview / 'images').mkdir()
        (self.preview / 'images' / 'logo.png').write_bytes(b'logo')

    def test_known_pages_and_assets_are_rebased(self):
        for url, expected in [('/', '/new/'), ('/executive#chair', '/new/executive#chair'),
                              ('/images/logo.png?v=1', '/new/images/logo.png?v=1'),
                              ('/new/executive', '/new/executive'), ('/chart', '/chart'),
                              ('/new/chart', '/chart'), ('/new/guide/', '/guide/'),
                              ('https://stratigraphy.org/executive', 'https://stratigraphy.org/executive'),
                              ('news/152', 'news/152'), ('#toc', '#toc')]:
            self.assertEqual(preview_url(url, self.preview), expected)

    def test_only_html_url_attributes_change(self):
        source = '<a href="/executive">Link</a><script>const x = \'<a href="/executive">\';</script><!-- <a href="/executive"> -->'
        self.assertEqual(rebase_html(source, self.preview), source.replace('href="/executive"', 'href="/new/executive"', 1))

    def test_root_is_preserved(self):
        output = self.root / 'output'
        assemble(self.production, self.preview, output)
        for file in self.production.iterdir():
            self.assertEqual(file.read_bytes(), (output / file.name).read_bytes())
        self.assertTrue((output / 'new' / 'index.html').is_file())

    def test_identical_downloads_are_shared_but_changed_ones_are_retained(self):
        for root in (self.production, self.preview):
            (root / 'files').mkdir()
            (root / 'files' / 'same.pdf').write_bytes(b'same')
            (root / 'files' / 'changed.pdf').write_bytes(str(root).encode())
        (self.preview / 'index.html').write_text('<a href="/new/files/same.pdf">Same</a><a href="/files/changed.pdf">Changed</a>')
        output = self.root / 'output'
        assemble(self.production, self.preview, output)
        self.assertFalse((output / 'new/files/same.pdf').exists())
        self.assertTrue((output / 'new/files/changed.pdf').exists())
        self.assertIn('href="/files/same.pdf"', (output / 'new/index.html').read_text())
        self.assertIn('href="/new/files/changed.pdf"', (output / 'new/index.html').read_text())
        self.assertEqual(preview_url('../files/same.pdf', self.preview, {'files/same.pdf'}, '/new/news/123.html'), '/files/same.pdf')

    def test_existing_new_directory_is_never_overwritten(self):
        (self.production / 'new').mkdir()
        with self.assertRaises(AssertionError):
            assemble(self.production, self.preview, self.root / 'output')


if __name__ == '__main__':
    unittest.main()
