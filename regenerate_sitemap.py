import os, re
from urllib.parse import quote

base = '/Users/vickhung/Desktop/easyappwebsite'
articles = os.path.join(base, 'articles')
today = '2026-11-02'

# Collect all article HTML files
files = sorted([f for f in os.listdir(articles) if f.endswith('.html')])
print(f'Total articles: {len(files)}')

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

# Homepage
lines.append('  <url>')
lines.append('    <loc>https://www.easyappwebsite.com/</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>1.0</priority>')
lines.append('  </url>')

# Articles index
lines.append('  <url>')
lines.append('    <loc>https://www.easyappwebsite.com/articles/index.html</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>0.9</priority>')
lines.append('  </url>')

# All articles
def natural_key(f):
    m = re.match(r'^(\d+)-', f)
    return (0, int(m.group(1))) if m else (1, f)

for fn in sorted(files, key=natural_key):
    url = f'https://www.easyappwebsite.com/articles/{quote(fn)}'
    lines.append('  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append('    <changefreq>monthly</changefreq>')
    lines.append('    <priority>0.8</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

out = os.path.join(base, 'sitemap.xml')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')

print(f'Wrote sitemap.xml with {len(files) + 2} URLs')
