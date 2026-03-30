import ssl
import urllib.request
import re

base = 'https://serveur-prive.net'
for path in [
    '/minecraft/jellflysmp/vote',
    '/js/default/form.js?v=420',
    '/js/default/app.js?v=420'
]:
    url = base + path
    print('\nFETCH', url)
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
        text = r.read().decode('utf-8', errors='replace')
    print('LEN', len(text))
    if '.js' in path:
        for pat in ['fetch(', 'vote/form/ajax', 'subscribe/ajax', 'csrf', 'token']:
            print('\nPATTERN', pat, 'COUNT', text.count(pat))
            m = re.search(re.escape(pat), text)
            if m:
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 280)
                snippet = text[start:end].replace('\n', ' ')
                print(snippet)
            else:
                print('NOT FOUND')
    else:
        forms = re.findall(r'<form[^>]*id="voteForm"[\s\S]*?</form>', text)
        print('FORMS', len(forms))
        scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
        print('SCRIPT SRCs', len(scripts))
        for src in scripts:
            print(src)
