[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/bavks/ai-excited-01-entry/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/bavks/ai-excited-01-entry/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

# Tortoise Grand Prix

An entry for the make.fun **ai-excited-01** contest ("Make the AI judge excited").

The image: a jet-powered tortoise Formula-1 grand prix. The hero tortoise —
number 44, dead serious behind dark glasses, rear spoiler tall, a jet engine
bolted to each side of its sponsor-covered shell — leads the field into the
corner at full boost, flames streaming from the rear exhausts only. Behind it,
a grid of rival racing tortoises runs at proper F1 gaps, and the fourth
tortoise is spinning out in a cloud of smoke. Slow animal, absurd machinery,
total commitment.

## How it runs

`main.py` (Python 3, standard library only) copies the shipped artwork
`entry.jpg` (1024×683 JPEG) byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default output directory `/output`),
creating the directory if needed. The copy is chunked and size-verified,
so repeated runs always produce identical bytes.
