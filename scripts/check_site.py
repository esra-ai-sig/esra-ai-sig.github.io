"""Check generated pages and their internal destinations without extra packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links = path, set(), []
        self.h1 = 0
        self.json = None
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'{self.path}: duplicate id {a["id"]}'
            self.ids.add(a['id'])
        self.h1 += tag == 'h1'
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag in ('script', 'img', 'link'):
            value = a.get('src') if tag != 'link' else a.get('href')
            if value and not value.startswith(('http', 'data:')):
                assert (root / value.lstrip('/')).is_file(), f'{self.path}: missing asset {value}'
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.json = ''
    def handle_data(self, data):
        if self.json is not None:
            self.json += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.json is not None:
            json.loads(self.json)
            self.json = None

paths = [root / 'index.html'] + [root / name / 'index.html' for name in
    ('about', 'activities', 'papers', 'resources', 'workflows', 'join')]
pages = {p: Page(p) for p in paths}
for path, page in pages.items():
    assert page.h1 == 1, f'{path}: expected one h1, found {page.h1}'
    for href in page.links:
        url = urlsplit(href)
        if url.scheme or url.netloc:
            continue
        target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path:
            target = path
        elif target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'{path}: broken internal link {href}'
        if url.fragment:
            target_page = pages.get(target) or Page(target)
            assert unquote(url.fragment) in target_page.ids, f'{path}: missing fragment {href}'
print(f'PASS: {len(pages)} pages; headings, unique IDs, local links/assets and JSON-LD')
