import os, re
from urllib.parse import quote
from datetime import date

base = '/Users/vickhung/Desktop/easyappwebsite/articles'
today = date.today().isoformat()

files = [f for f in os.listdir(base) if f.endswith('.html')]
files.sort(key=lambda f: int(re.match(r'^(\d+)-', f).group(1)) if re.match(r'^(\d+)-', f) else 99999)

lines = []
lines.append('<?xml version="1.0" encoding="UTF-8"?>')
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
lines.append('  <url>')
lines.append('    <loc>https://www.easyappwebsite.com/</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>1.0</priority>')
lines.append('  </url>')
lines.append('  <url>')
lines.append('    <loc>https://www.easyappwebsite.com/articles/index.html</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>0.9</priority>')
lines.append('  </url>')

for f in files:
    encoded = quote(f)
    url = f'https://www.easyappwebsite.com/articles/{encoded}'
    lines.append('  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append('    <changefreq>monthly</changefreq>')
    lines.append('    <priority>0.8</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

with open('/Users/vickhung/Desktop/easyappwebsite/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Sitemap regenerated with {len(files)} articles, date: {today}')
