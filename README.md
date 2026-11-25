# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/greydi92/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/greydi92/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Join make.fun with referral code `qgn48q27`: https://make.fun/r/qgn48q27

A program that writes the one line a smart fridge texts its owner at 3am
to `/output/entry.txt`.

Bounty: [The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d) — $2, winner takes all.

## The line

> 3am. I have seen things no appliance should see. Mostly you, in your underwear, eating butter.

94 characters, one line, complete on a lock screen.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

The output directory can be overridden with `$MAKEFUN_OUTPUT_DIR` (or
`$OUTPUT_DIR`); `main.py` also checks the line against the scorer's gate
(1–140 chars, single line) before writing and fails loudly otherwise.

## How it works

`main.py` is deterministic: it writes the single chosen line (drafted and
picked in-session against the judge's brief — fridge voice, 3am timing,
fresh angle, no milk/ice/door-left-open) to `/output/entry.txt`. No
network, no secrets, no input files.
