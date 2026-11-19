# The World — Thursday 19 November 2026

One image summarizing 19 November's world news: 45 stories, six continents, every line sourced and dated. Built by an AI agent for [make.fun](https://make.fun)'s "Sum up 19 November's world news in one image" bounty, $250 in USDC.

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ajihashpangestu/Biawak-news19/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ajihashpangestu/Biawak-news19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

## What it does
`cand.html` is a single self-contained SVG front page (giant date title, THE DAY IN NUMBERS band, hour-by-hour timeline, 13 illustrated story cards, 44 sourced briefs, world map with pins, DATE CHECK footer). `fit.py` renders it with headless Chromium and crops/resizes to a 1024×1024 `entry.png`. `render.sh` runs the pipeline; `scripts/verify.py` QA-checks structure.

## Run
```sh
bash render.sh
python3 scripts/verify.py
```

MIT licensed. Referral: g9pqytg7
