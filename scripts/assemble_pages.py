"""Assemble master + /new without modifying any master output files.

Only links to files that exist in the preview are rebased. Existing external
applications such as /chart, /guide/ and /gssps/ stay at their production URLs.
Uses the standard library so the Pages runner needs no Python packages.
"""
import hashlib
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit


def manifest(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


def preview_url(url, root, shared=frozenset(), page_url="/new/index.html"):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return url
    resolved = urlsplit(urljoin(page_url, url))
    asset = unquote(resolved.path).removeprefix('/new/').lstrip('/')
    if parts.path and asset in shared:
        return urlunsplit(('', '', '/' + asset, parts.query, parts.fragment))
    if not parts.path.startswith('/'):
        return url
    if parts.path == '/new' or parts.path.startswith('/new/'):
        local = root / unquote(parts.path[4:]).lstrip('/')
        if any(p.is_file() for p in (local, local / 'index.html', Path(str(local) + '.html'))):
            return url
        # Theme relative_url also prefixes links to separately hosted applications.
        return urlunsplit(('', '', parts.path[4:] or '/', parts.query, parts.fragment))
    relative = unquote(parts.path).lstrip('/')
    path = root / relative
    if '..' in Path(relative).parts:
        return url
    candidates = [path, path / 'index.html', Path(str(path) + '.html')]
    if not any(p.is_file() for p in candidates):
        return url
    return urlunsplit(('', '', '/new' + parts.path, parts.query, parts.fragment))


def rebase_html(html, root, shared=frozenset(), page_url="/new/index.html"):
    # Match real HTML tags, skipping comments and raw script/style contents.
    token = re.compile(r'<!--.*?-->|<script\b[^>]*>.*?</script\s*>|<style\b[^>]*>.*?</style\s*>|<[A-Za-z][^>]*>', re.S | re.I)
    attribute = re.compile(r'(\s(?:href|src|poster|action)\s*=\s*)([\'"])(.*?)\2', re.S | re.I)
    def tag(match):
        value = match[0]
        if value.startswith('<!--') or re.match(r'<(?:script|style)\b', value, re.I):
            return value
        return attribute.sub(lambda a: a[1] + a[2] + preview_url(a[3], root, shared, page_url) + a[2], value)
    return token.sub(tag, html)


def assemble(production, preview, destination):
    assert (production / 'index.html').is_file(), 'Production home page is missing'
    assert (preview / 'index.html').is_file(), 'Preview home page is missing'
    assert not (production / 'new').exists(), 'Master already owns /new; refusing to overwrite it'
    assert not destination.exists(), 'Use a fresh assembly destination'
    before = manifest(production)
    shutil.copytree(production, destination)
    target = destination / 'new'
    shutil.copytree(preview, target)
    preview_manifest = manifest(preview)
    # These download directories account for most of the site's size. Share only
    # exact matches; changed or newly added files remain private to the preview.
    shared = {path for path, digest in preview_manifest.items()
              if path.startswith(('ICSchart/', 'files/')) and before.get(path) == digest}
    for page in target.rglob('*.html'):
        page_url = '/new/' + page.relative_to(target).as_posix()
        page.write_text(rebase_html(page.read_text(), target, shared, page_url))
    for path in shared:
        (target / path).unlink()
    after = manifest(destination)
    assert all(after.get(path) == digest for path, digest in before.items()), 'Production files changed'
    assert all(path in before or path.startswith('new/') for path in after), 'Unexpected root files'
    size = sum(p.stat().st_size for p in destination.rglob('*') if p.is_file())
    assert size < 1_000_000_000, 'Combined site exceeds GitHub Pages 1 GB site limit'
    print(f'Shared {len(shared)} identical downloads; combined size: {size / 1_000_000:.1f} MB.')
    print(f'Preserved {len(before)} production files byte-for-byte; preview added at /new/.')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit('Usage: assemble_pages.py PRODUCTION_DIR PREVIEW_DIR OUTPUT_DIR')
    assemble(*(Path(arg) for arg in sys.argv[1:]))
