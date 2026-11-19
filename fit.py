"""Render the front page, crop paper margins, and produce a square PNG."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
CHROME = '/root/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'


def main():
    destination = Path(sys.argv[1] if len(sys.argv) > 1 else 'entry.png')
    command = [CHROME, '--headless=new', '--no-sandbox', '--disable-gpu',
               '--hide-scrollbars', '--screenshot=full.png',
               '--window-size=1024,1400', (ROOT / 'cand.html').as_uri()]
    run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if run.returncode:
        print(json.dumps({'output': str(destination), 'rendered': False,
                          'exit_code': run.returncode, 'error': run.stderr.strip(),
                          'overflow': 'unverified'}))
        raise SystemExit(1)
    with Image.open(ROOT / 'full.png') as original:
        rgb = original.convert('RGB')
        background = Image.new('RGB', rgb.size, '#f7f5ef')
        difference = ImageChops.difference(rgb, background)
        channels = difference.split()
        maximum = ImageChops.lighter(ImageChops.lighter(channels[0], channels[1]), channels[2])
        box = maximum.point(lambda value: 255 if value > 8 else 0).getbbox()
        if box is None:
            raise ValueError('The page contains no visible content')
        left, top, right, bottom = box
        crop = (max(0, left - 8), max(0, top - 8),
                min(rgb.width, right + 8), min(rgb.height, bottom + 8))
        result = rgb.crop(crop).resize((1024, 1024), Image.Resampling.LANCZOS)
        result.save(destination)
    # Reopen the saved artifact so the reported dimensions verify the actual PNG.
    with Image.open(destination) as saved:
        assert saved.size == (1024, 1024), 'Output dimensions must be exactly square'
    payload = destination.read_bytes()
    print(json.dumps({'output': str(destination), 'screenshot': [1024, 1400],
                      'content_bbox': box, 'crop_bbox': crop, 'size': [1024, 1024],
                      'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest()}))


if __name__ == '__main__':
    main()
