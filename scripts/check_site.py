"""Validate static Pages URLs, metadata, data uniqueness and research cross-links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, parse_qs
import json

ROOT = Path(__file__).resolve().parents[1] / 'docs'
BASE = 'https://cve415.github.io/MCP-Security-2026/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.ids=set(); self.links=[]; self.meta={}; self.canonical=None; self.h1=0; self.title=False
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate HTML id: {a["id"]}'
            self.ids.add(a['id'])
        if tag=='h1': self.h1+=1
        if tag=='title': self.title=True
        if tag=='meta': self.meta[a.get('name',a.get('property'))]=a.get('content')
        if tag=='link' and a.get('rel')=='canonical': self.canonical=a['href']
        for key in ('href','src'):
            if key in a: self.links.append(a[key])

pages={p:Page(p) for p in ROOT.rglob('*.html')}
data={name:json.loads((ROOT/f'{name}.json').read_text()) for name in ('solo','enterprise','governance')}
for name,items in data.items():
    for field in ('name','id'):
        values=[x[field].casefold() for x in items if field in x]
        assert len(values)==len(set(values)), f'Duplicate {field} in {name}'
    for company in ('semgrep','snyk','checkmarx','veracode','gitguardian'):
        matches=[x for x in items if company in x.get('developer',x['name']).casefold()]
        assert len(matches)<=1, f'Duplicate company {company} in {name}'
    for item in items:
        assert all(item.get(k) for k in ('name','description','url'))
        if 'research' in item:
            article=ROOT/'research'/item['research']/'index.html'
            assert article in pages
            assert ('snyk' if item['id']=='mcp-scan' else item['id']) in pages[article].ids
for path,page in pages.items():
    rel=path.relative_to(ROOT).as_posix()
    url=BASE+(rel[:-10] if rel.endswith('index.html') else rel)
    assert page.title and page.h1==1, path
    assert page.canonical==url, (path,page.canonical,url)
    for field in ('description','og:title','og:description','og:type','og:url','og:image','twitter:card'):
        assert page.meta.get(field), (path,field)
    for link in page.links:
        target=urlsplit(urljoin(url,link))
        if target.netloc!=urlsplit(BASE).netloc: continue
        assert target.path.startswith('/MCP-Security-2026/'), link
        dest=ROOT/target.path[len('/MCP-Security-2026/'):]
        if dest.is_dir():dest=dest/'index.html'
        assert dest.exists(), (path,link)
        if target.fragment:
            if dest==ROOT/'index.html' and 'audience' in parse_qs(target.query):
                audience=parse_qs(target.query)['audience'][0]
                assert target.fragment in {x.get('id') for x in data[audience]}, link
            else: assert target.fragment in pages[dest].ids, (path,link)
print(f'PASS: {len(pages)} pages; {sum(map(len,data.values()))} records; metadata, local links, fragments, research links and company uniqueness.')
