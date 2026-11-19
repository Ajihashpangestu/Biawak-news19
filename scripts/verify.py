"""Validate editorial structure and actual rendered SVG text bounds."""
import json
import html as html_module
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import subprocess

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'cand.html').read_text()
svg = ET.fromstring(re.search(r'(<svg\b.*</svg>)', html, re.S).group(1))
ns = {'s': 'http://www.w3.org/2000/svg'}
groups = svg.findall('.//s:g', ns)
cards = [g for g in groups if g.get('class') == 'card']
briefs = [g for g in groups if g.get('class') == 'brief']
stats = [g for g in groups if g.get('class') == 'stat']
assert len(cards) == 13, f'{len(cards)} cards'
assert [int(g.get('data-number')) for g in cards] == list(range(1, 14))
assert len(briefs) >= 40, f'{len(briefs)} briefs'
assert [int(g.get('data-number')) for g in briefs] == list(range(14, 14 + len(briefs)))
for brief in briefs:
    content = ''.join(brief.itertext()).strip()
    assert re.search(r'\([^()]+, 19 Nov\)$', content), content
assert len(stats) == 8, f'{len(stats)} stats'
assert svg.get('width') == svg.get('height') == '1024'
assert all(not scene.findall('.//s:text', ns) for scene in groups if scene.get('class') == 'scene')
print(json.dumps({'cards': len(cards), 'briefs': len(briefs), 'brief_range': [14, 13 + len(briefs)],
                  'band_stats': len(stats), 'structural_checks': 'passed'}), flush=True)
rendered = subprocess.run([
    '/root/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome',
    '--headless=new', '--no-sandbox', '--disable-gpu', '--dump-dom',
    '--window-size=1024,1400', '--virtual-time-budget=1000',
    (ROOT / 'cand.html').as_uri(),
], capture_output=True, text=True)
if rendered.returncode:
    print(json.dumps({'browser_checks': 'blocked', 'text_overflow': 'unverified',
                      'error': rendered.stderr.strip()}))
    raise SystemExit(1)
rendered = rendered.stdout
match = re.search(r'data-qa-overflow="([^"]*)"', rendered)
assert match, 'Browser did not report text bounds'
overflow = json.loads(html_module.unescape(match.group(1)))
assert not overflow, json.dumps(overflow)
print(json.dumps({'cards': len(cards), 'briefs': len(briefs), 'brief_range': [14, 13 + len(briefs)], 'band_stats': len(stats), 'text_overflow': overflow, 'passed': True}))
