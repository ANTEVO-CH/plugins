# The template: one page, one file

`index.html` renders `workspace.json`. The file here is the Startup Launch Intelligence run of
25 November 2026 for an example AI fintech (Novara and Lumora taken, Tirano Pay clear; the names
are examples, not suggestions).

```bash
python3 -m http.server 8000   # in this folder, then open http://localhost:8000
```

`index.html?w=other.json` renders another file in the same folder: `index.html?w=due-diligence.json`
is the Company Due Diligence run of 25 November 2026 (an example supplier; nothing is alleged).

## The file

Every block is optional; the page shows the ones that are there.

| field | what goes in it |
|---|---|
| `kind`, `title`, `subtitle`, `built`, `note` | the build's name, the headline (the clear name), one line on the idea and markets, the date, and the note that every figure is an engine's answer on the date shown |
| `tries` | `label`, `item` (what each card is called: `Try`, `Check`), `source` and `items`: each option checked in turn, with `name`, `verdict`, `level` (`red`, `green`, `amber`, `ink`) and `evidence` lines |
| `steps` | `label` and `items`: each next action with `do`, `why` and `links` (`label`, `url`; https only) |
| `sections` | each finding: `title`, `verdict`, `level`, `so_what` (what it means for this plan), `evidence`, `source` with its date |
| `links` | how the findings connect: two engines (`a`, `b`) and one sentence |
| `roadmap` | blocks of `days` and what to `do`: options to consider |
| `watch` | the dates and indicators the engines named |
| `disclaimer` | keep it: not advice; a screen is not clearance |

Fill it with the `startup-launch` or `due-diligence` skill in this plugin, or from your own agent calling the six
connectors. Change the page, restyle it, turn it into your own product.
