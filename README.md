# Funniest Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![make.fun rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/danzzkeceh4-bit/makefun-u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![make.fun reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/danzzkeceh4-bit/makefun-u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for the [Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) bounty on [make.fun](https://make.fun/): a single warning label for a time machine, 120 characters at most, aiming for the biggest laugh.

## The label

```
CAUTION: Do not operate if you have already crashed. The manufacturer is not liable for your grandfather.
```

105 characters. A straight-faced safety notice: the paradox of having already
crashed before operating, with the surprise saved for the last words — the
grandfather paradox, and a manufacturer that disclaims liability for him.

## How it works

`main.py` writes the label to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`),
with no trailing newline, and validates the 1–120 character gate.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
