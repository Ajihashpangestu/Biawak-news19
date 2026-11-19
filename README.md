[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A single-image world front page for Thursday 19 November 2026: thirteen illustrated news cards, thirty sourced briefs, eight key numbers, story locators and a date-check footer. All artwork and typography live in one self-contained SVG in cand.html. News copy follows the supplied editorial brief.

Run `python3 scripts/verify.py` for structural and browser text-bound checks, then `bash render.sh` to create the 1024 × 1024 entry.png. Rendering requires Pillow and the specified headless Chromium installation. Browser QA uses Chromium directly. `node main.ts` prints the image byte count and SHA-256 on Node 22 with TypeScript support.

The embedded world outline is reused from the supplied Natural Earth-derived world.svg. The renderer crops against the paper background with tolerance 8 and margin 8, then resizes using LANCZOS.
