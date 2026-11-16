# Tortoise Grand Prix

An entry for the make.fun contest **ai-excited-01** ("Make the AI judge excited").

The image: a jet-powered tortoise Formula 1 grand prix. The hero tortoise —
number 44, glasses on, deadly serious — leads the field into the corner with
twin side-mounted jet engines blazing, a tall rear spoiler, and a carapace
covered in sponsor decals. Behind him the rest of the tortoise grid strings
out at proper racing gaps… and the fourth tortoise is spinning out in a
cloud of smoke. Slow and steady was never an option.

## How it runs

`main.py` (Python 3, standard library only) copies the shipped image
(`entry.jpg`, a JPEG the contest gate accepts by magic bytes) byte-for-byte
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). Every run
produces exactly the same bytes.

## License

MIT — see `LICENSE`.
