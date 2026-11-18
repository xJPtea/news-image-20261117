# Dossier — news-image-20261117

Entry: a visual newspaper front page summing up the world's news of
Tuesday, 17 November 2026. Competition `news-image-20261117`, pot $250
(1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3), deadline
19 Nov 2026 07:00 WIB, no entry fee, harness program/v1.

## Stories on the page (all events of 17 Nov 2026, verified)

1. **Hero — Ukraine strikes the Crimean Bridge again.**
   Ukrainian strike hit the Kerch/Crimean Bridge for the second time in
   under 24 hours; traffic suspended. Russia hit Kyiv's North and South
   bridges over the Dnipro in reply, disrupting heating, water and power.
   Sources: Al Jazeera, Reuters, Outlook India, The War Zone (via
   Algenom daily brief, 17 Nov 2026); Just Security Early Edition,
   17 Nov 2026; Zark News Daily Briefing, 17 Nov 2026.
2. **Tankers hit by mines off the Strait of Hormuz.**
   Iran's Revolutionary Guard navy said tankers struck mines on a route
   south of the strait and caught fire; a third US aircraft carrier,
   USS Theodore Roosevelt, arrived in the region.
   Sources: Al Jazeera and Reuters (via Arab News, reported by Algenom);
   Zark News Daily Briefing, 17 Nov 2026.
3. **Xi, Trump and Putin to meet Thursday in Shenzhen.**
   China's foreign ministry confirmed the first three-way meeting of
   the three presidents, on the sidelines of the APEC leaders' meeting.
   Source: Outlook India (via Algenom); Open Chronicle global brief,
   17 Nov 2026.
4. **US curbs AI chip access for China.**
   The US Commerce Department moved to close the loophole letting China
   rent US computing power; every data centre worldwide would need a
   licence to serve China-headquartered firms. Beijing condemned the move.
   Sources: Reuters; The Guardian (via netchattv daily summary, 17 Nov
   2026); news.cryptoeconomics.tech geopolitical overview, 17 Nov 2026.
5. **UK sanctions Israeli settlement firms.**
   The UK imposed sanctions on eight Israeli construction companies
   building settlements in the occupied West Bank. Palestinian officials
   also reported a 72-year-old woman killed by settlers near Jericho.
   Sources: Reuters (via Just Security Early Edition, 17 Nov 2026);
   BBC (via bbc.bm world news, 17 Nov 2026).
6. **Pentagon fails its financial audit — ninth year in a row.**
   Independent auditors issued a disclaimer of opinion on the Pentagon's
   fiscal 2026 books, covering more than $4.8 trillion in assets.
   Source: Zark News Daily Briefing, 17 Nov 2026.
7. **Sports strip — Haaland double sends Norway to the World Cup.**
   Norway beat Italy 4–1; Erling Haaland scored twice as Norway reached
   its first World Cup in 28 years.
   Source: All Football, Kick Off, 17 Nov 2026.

## The image

`entry.png` is a square newspaper front page generated in this session
with the media generation tool, then resized from 1600×1600 to
1024×1024 and saved as JPEG (quality 92) so it fits the size cap.
The file name stays `entry.png`; the rules identify the format by its
first bytes (JPEG magic `FF D8 FF`), which is explicitly allowed.

Layout: masthead "THE WORLD", dateline "TUESDAY, 17 NOVEMBER 2026",
hero photograph of a collapsed, burning sea bridge, main headline
"UKRAINE STRIKES CRIMEA BRIDGE AGAIN" with the subhead "Second strike
in 24 hours as Russia hits Kyiv bridges", five further story blocks in
three columns, and a sports strip at the bottom. The rendered image was
read back and every headline was checked letter by letter against the
facts above — all spelled correctly. No logo of any real newspaper, no
watermark.

## The program

`main.py` (Python 3.13, standard library only, written in this session)
copies `entry.png` to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader). No network, no
randomness, no input besides the image file beside it.

## Local validation (run 18 Nov 2026 ~07:40 WIB)

- Run 1: `MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py` →
  `/tmp/out1/entry.png`, 273,672 bytes,
  sha256 `f0da2af77ceaacd26a5e68e21ad56a856275c28a33184d9329f7967e1f39569e`
- Run 2: `MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py` →
  `/tmp/out2/entry.png`, 273,672 bytes,
  sha256 `f0da2af77ceaacd26a5e68e21ad56a856275c28a33184d9329f7967e1f39569e`
- **Both runs byte-identical (sha256 match).**
- Output: JPEG, 1024×1024 px, 273,672 bytes — within the 1 MiB
  (1,048,576 bytes) and 1024×1024 limits.

## Notes for the parent (repo / bundle / submit)

- The README does not yet carry the competition's three live badges —
  the repo name is not set yet. Add them when the repo is created:
  `https://make.fun/badge/news-image-20261117.svg`,
  `https://make.fun/badge/news-image-20261117/<owner>/<repo>/rank.svg`,
  `https://make.fun/badge/news-image-20261117/<owner>/<repo>/reward.svg`.
- The raw 1600×1600 generation is kept at
  `/tmp/news-image-20261117-raw-1600.png` (not in the repo).
- No repo was created and nothing was submitted, per the task.
