"""Publish the current site at root and the previous site at /old."""

import hashlib
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit


def manifest(root):
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob("*")
        if p.is_file()
    }


def archive_url(url, root, shared=frozenset(), page_url="/old/index.html"):
    parts = urlsplit(url)
    if parts.netloc in (
        "stratigraphy.org",
        "www.stratigraphy.org",
    ) and parts.scheme in ("", "http", "https"):
        url = urlunsplit(("", "", parts.path or "/", parts.query, parts.fragment))
        parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return url
    resolved = urlsplit(urljoin(page_url, url))
    asset = unquote(resolved.path).removeprefix("/old/").lstrip("/")
    if parts.path and asset in shared:
        return urlunsplit(("", "", "/" + asset, parts.query, parts.fragment))
    if not parts.path.startswith("/"):
        return url
    if parts.path == "/old" or parts.path.startswith("/old/"):
        local = root / unquote(parts.path[4:]).lstrip("/")
        if any(
            p.is_file()
            for p in (local, local / "index.html", Path(str(local) + ".html"))
        ):
            return url
        # Theme relative_url also prefixes links to separately hosted applications.
        return urlunsplit(("", "", parts.path[4:] or "/", parts.query, parts.fragment))
    relative = unquote(parts.path).lstrip("/")
    path = root / relative
    if ".." in Path(relative).parts:
        return url
    candidates = [path, path / "index.html", Path(str(path) + ".html")]
    if not any(p.is_file() for p in candidates):
        return url
    return urlunsplit(("", "", "/old" + parts.path, parts.query, parts.fragment))


def rebase_html(html, root, shared=frozenset(), page_url="/old/index.html"):
    # Match real HTML tags, skipping comments and raw script/style contents.
    token = re.compile(
        r"<!--.*?-->|<script\b[^>]*>.*?</script\s*>|<style\b[^>]*>.*?</style\s*>|<[A-Za-z][^>]*>",
        re.DOTALL | re.IGNORECASE,
    )
    attribute = re.compile(
        r'(\s(?:href|src|poster|action)\s*=\s*)([\'"])(.*?)\2',
        re.DOTALL | re.IGNORECASE,
    )

    def tag(match):
        value = match[0]
        if value.startswith("<!--") or re.match(
            r"<(?:script|style)\b", value, re.IGNORECASE
        ):
            return value
        return attribute.sub(
            lambda a: a[1] + a[2] + archive_url(a[3], root, shared, page_url) + a[2],
            value,
        )

    result = token.sub(tag, html)
    # Legacy inline JavaScript contains root-relative banner image paths.
    return re.sub(
        r"""(["'])(/images/[^"'\s]+)\1""",
        lambda m: m[1] + archive_url(m[2], root, shared, page_url) + m[1],
        result,
    )


def assemble(production, preview, destination):
    assert (production / "index.html").is_file(), "Production home page is missing"
    assert (preview / "index.html").is_file(), "Preview home page is missing"
    assert not (production / "old").exists(), (
        "Master already owns /old; refusing to overwrite it"
    )
    assert not destination.exists(), "Use a fresh assembly destination"
    before = manifest(production)
    shutil.copytree(production, destination)
    target = destination / "old"
    shutil.copytree(preview, target)
    preview_manifest = manifest(preview)
    # These download directories account for most of the site's size. Share only
    # exact matches; changed or newly added files remain private to the preview.
    shared = {
        path
        for path, digest in preview_manifest.items()
        if path.startswith(("ICSchart/", "files/")) and before.get(path) == digest
    }
    for page in target.rglob("*.html"):
        page_url = "/old/" + page.relative_to(target).as_posix()
        page.write_text(rebase_html(page.read_text(), target, shared, page_url))
    for css in target.rglob("*.css"):
        css.write_text(
            re.sub(
                r"""url\(\s*(["']?)(/[^)'"\s]+)\1\s*\)""",
                lambda m: 'url("' + archive_url(m[2], target, shared) + '")',
                css.read_text(),
            )
        )
    # Preserve bookmarks to the former preview, including nested news routes.
    for page in production.rglob("*.html"):
        relative = page.relative_to(production)
        redirect = destination / "new" / relative
        redirect.parent.mkdir(parents=True, exist_ok=True)
        url = "/" + relative.as_posix()
        if url.endswith("/index.html"):
            url = url[:-10]
        import html

        escaped = html.escape(url, quote=True)
        redirect.write_text(
            '<!doctype html><meta charset="utf-8">'
            f'<link rel="canonical" href="{escaped}">'
            f'<meta http-equiv="refresh" content="0; url={escaped}">'
            f'<a href="{escaped}">Continue to the website</a>'
        )
    for path in shared:
        (target / path).unlink()
    after = manifest(destination)
    assert all(after.get(path) == digest for path, digest in before.items()), (
        "Production files changed"
    )
    assert all(path in before or path.startswith(("old/", "new/")) for path in after), (
        "Unexpected root files"
    )
    size = sum(p.stat().st_size for p in destination.rglob("*") if p.is_file())
    assert size < 1_000_000_000, "Combined site exceeds GitHub Pages 1 GB site limit"
    print(
        f"Shared {len(shared)} identical downloads; combined size: {size / 1_000_000:.1f} MB."
    )
    print(
        f"Preserved {len(before)} production files byte-for-byte; preview added at /old/."
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: assemble_pages.py PRODUCTION_DIR PREVIEW_DIR OUTPUT_DIR")
    assemble(*(Path(arg) for arg in sys.argv[1:]))
