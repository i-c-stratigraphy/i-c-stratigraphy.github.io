import tempfile
import unittest
from pathlib import Path

from assemble_pages import archive_url, assemble, rebase_html


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.production = self.root / "production"
        self.preview = self.root / "preview"
        for path in (self.production, self.preview):
            path.mkdir()
            (path / "index.html").write_text("<html>Home</html>")
        (self.production / "CNAME").write_text("stratigraphy.org\n")
        (self.preview / "executive.html").write_text("Executive")
        (self.preview / "images").mkdir()
        (self.preview / "images" / "logo.png").write_bytes(b"logo")

    def test_known_pages_and_assets_are_rebased(self):
        for url, expected in [
            ("/", "/old/"),
            ("/executive#chair", "/old/executive#chair"),
            ("/images/logo.png?v=1", "/old/images/logo.png?v=1"),
            ("/old/executive", "/old/executive"),
            ("/chart", "/chart"),
            ("/old/chart", "/chart"),
            ("/old/guide/", "/guide/"),
            ("https://stratigraphy.org/executive", "/old/executive"),
            ("https://stratigraphy.org", "/old/"),
            ("news/152", "news/152"),
            ("#toc", "#toc"),
        ]:
            self.assertEqual(archive_url(url, self.preview), expected)

    def test_only_html_url_attributes_change(self):
        source = '<a href="/executive">Link</a><script>const x = \'<a href="/executive">\';</script><!-- <a href="/executive"> -->'
        self.assertEqual(
            rebase_html(source, self.preview),
            source.replace('href="/executive"', 'href="/old/executive"', 1),
        )

    def test_root_is_preserved(self):
        output = self.root / "output"
        assemble(self.production, self.preview, output)
        for file in self.production.iterdir():
            self.assertEqual(file.read_bytes(), (output / file.name).read_bytes())
        self.assertTrue((output / "old" / "index.html").is_file())

    def test_identical_downloads_are_shared_but_changed_ones_are_retained(self):
        for root in (self.production, self.preview):
            (root / "files").mkdir()
            (root / "files" / "same.pdf").write_bytes(b"same")
            (root / "files" / "changed.pdf").write_bytes(str(root).encode())
        (self.preview / "index.html").write_text(
            '<a href="/old/files/same.pdf">Same</a><a href="/files/changed.pdf">Changed</a>'
        )
        output = self.root / "output"
        assemble(self.production, self.preview, output)
        self.assertFalse((output / "old/files/same.pdf").exists())
        self.assertTrue((output / "old/files/changed.pdf").exists())
        self.assertIn('href="/files/same.pdf"', (output / "old/index.html").read_text())
        self.assertIn(
            'href="/old/files/changed.pdf"', (output / "old/index.html").read_text()
        )
        self.assertEqual(
            archive_url(
                "../files/same.pdf",
                self.preview,
                {"files/same.pdf"},
                "/old/news/123.html",
            ),
            "/files/same.pdf",
        )

    def test_existing_old_directory_is_never_overwritten(self):
        (self.production / "old").mkdir()
        with self.assertRaises(AssertionError):
            assemble(self.production, self.preview, self.root / "output")

    def test_legacy_banner_fonts_and_preview_redirects(self):
        (self.preview / "style").mkdir()
        (self.preview / "style/font.woff").write_bytes(b"font")
        (self.preview / "style/ics.css").write_text("src: url('/style/font.woff')")
        (self.preview / "index.html").write_text(
            '<script>const banner = "/images/logo.png";</script>'
            '<a href="https://stratigraphy.org/">Home</a>'
            '<a href="/chart">Chart application</a>'
        )
        (self.production / "news").mkdir()
        (self.production / "news/123.html").write_text("News")
        output = self.root / "output"
        assemble(self.production, self.preview, output)
        archived = (output / "old/index.html").read_text()
        self.assertIn('banner = "/old/images/logo.png"', archived)
        self.assertIn('href="/old/"', archived)
        self.assertIn('href="/chart"', archived)
        self.assertIn(
            "/old/style/font.woff", (output / "old/style/ics.css").read_text()
        )
        self.assertIn('url=/"', (output / "new/index.html").read_text())
        self.assertIn("url=/news/123.html", (output / "new/news/123.html").read_text())


if __name__ == "__main__":
    unittest.main()
