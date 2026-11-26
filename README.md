# news-image-20261126 — The World Today

![Competition](https://img.shields.io/badge/competition-news--image--20261126-blue)
![Prize](https://img.shields.io/badge/prize-%24100%20top%2050-green)
![Date](https://img.shields.io/badge/date-Thursday%2026%20November%202026-red)

A program that writes one 1024×1024 newspaper front page summing up the
world's news of **Thursday, 26 November 2026** — six stories, one image.

Entry for the make.fun competition:
[news-image-20261126](https://make.fun/c/news-image-20261126)

## The six stories

1. **Space / China (lead)** — Pakistan's first astronaut reaches Tiangong
   (Muhammad Zeeshan Ali aboard China's space station, Shenzhou-24)
2. **Trade / Washington** — New U.S. tariffs hit 14 partners
3. **Israel / Jerusalem** — Judges urge dropping Netanyahu bribery charges
4. **Korea / Pyongyang** — North Korea orders the Swiss envoy out in 48 hours
5. **Bangladesh / Dhaka** — Garment workers win a 36% pay rise
6. **U.S. / Thanksgiving Day** — Thanksgiving dinner costs 11% more

## How it works

`main.py` is standard-library only: it copies the poster `entry.png`
(1024×1024, under 1 MiB) that ships in this repository to
`/output/entry.png`, then verifies the copy is a real PNG of the
expected size. The poster itself was drawn fresh for this day's news
with Pillow and DejaVu fonts — masthead, lead story with a space
illustration, and five story cards with small pictograms.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network is used. Two runs write identical bytes.

## License

MIT — see [LICENSE](LICENSE).
