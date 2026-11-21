# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/kuni29/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/kuni29/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world news of Saturday 21 November 2026, drawn as a newspaper front page: the date as the headline, a world-map strip marking where the day happened, three hero stories — Russia's biggest barrage of the year on Ukraine with missiles landing in Poland, Wall Street's AI rout dragging the S&P and Dow into correction, and two tankers hit in the Strait of Hormuz — plus three more features (COP31 in overtime, a pancreatic-cancer pill breakthrough, the UK–EU post-Brexit deals) and 24 one-line briefs from every region, 30 stories in all. Every story was first reported on 21 November 2026. The picture is designed in `design.html` with hand-drawn SVG illustrations and rendered to `entry.png` by `render.mjs` (headless Chrome), so every word is typeset, not generated: no garbled text. `main.py` delivers the image bytes to the output directory, unchanged on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under the 1 MiB cap).

---
<sub>Entered on [make.fun](https://make.fun/?ref=sjptyjw4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
