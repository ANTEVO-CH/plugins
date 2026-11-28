# The template: one page, one file

`index.html` renders `workspace.json`. The file here is the Startup Launch Intelligence run of
25 November 2026 for an example AI fintech (Morvane and Quorvia taken, Tirano Pay clear; the names
are examples, not suggestions).

```bash
python3 -m http.server 8000   # in this folder, then open http://localhost:8000
```

`index.html?w=other.json` renders another file in the same folder: `index.html?w=due-diligence.json`
is the Company Due Diligence run of 25 November 2026 (an example supplier; nothing is alleged), and
`index.html?w=supply-chain.json` the Supply Chain Watch run of the same day (Taiwan to Basel), and `index.html?w=m-and-a.json` the
M&A Intelligence run (Swiss robotics; nothing says any company is for sale). `index.html?w=real-estate.json` is the
Real Estate Acquisition run (a new apartment near Zurich; nothing says the company is party to any sale),
`index.html?w=family-office.json` the Family Office run (an example Swiss family, in words with no amounts), and
`index.html?w=market-entry.json` the Market Entry run (an example Swiss instrument maker opening in Singapore), and
`index.html?w=fintech-launch.json` the Fintech Launch run (an example Swiss payments company, planned to Germany).
`index.html?w=strategic-planner.json` the Strategic Planner run (an example Swiss machine maker's 2027 plan).
`index.html?w=invoice-check.json` the Invoice Check run (an example invoice with new bank details).
`index.html?w=banks-on-one-page.json` the All Your Banks run (an example family with three made-up banks).
`index.html?w=inside-your-funds.json` the Inside Your Funds run (an example family with five funds, four opened).
`index.html?w=risks-in-francs.json` the Risks In Francs run (five risks for an example family).
`index.html?w=a-banks-monday.json` the A Bank's Monday run (a made-up bank, one example family and its loan).

## The file

Every block is optional; the page shows the ones that are there.

| field | what goes in it |
|---|---|
| `kind`, `title`, `subtitle`, `built`, `note` | the build's name, the headline (the clear name), one line on the idea and markets, the date, and the note that every figure is an engine's answer on the date shown |
| `tries` | `label`, `item` (what each card is called: `Try`, `Check`, `Leg`, `Company`, `Holding`, `Piece`), `source` and `items`: each option checked in turn, with `name`, `verdict`, `level` (`red`, `green`, `amber`, `ink`, `grey` for not checked) and `evidence` lines |
| `steps` | `label` and `items`: each next action with `do`, `why` and `links` (`label`, `url`; https only) |
| `sections` | each finding: `title`, `verdict`, `level`, `so_what` (what it means for this plan), `evidence`, `source` with its date |
| `links` | how the findings connect: two engines (`a`, `b`) and one sentence |
| `roadmap` | blocks of `days` and what to `do`: options to consider |
| `thesis` | the strategy in one paragraph: `label`, `text` |
| `plan` | stages: `when`, `title`, `do` (a list) and the `gate` that must hold before the next stage |
| `risks` | each `risk`, the `trigger` that would set it off, the `response`, and a `level` |
| `kpis` | what to measure: `k` and `why` |
| `next` | the parts of a series: `n`, `title`, a `url` or `here` |
| `watch` | the dates and indicators the engines named |
| `disclaimer` | keep it: not advice; a screen is not clearance |

Fill it with the `startup-launch`, `due-diligence`, `supply-chain`, `m-and-a`, `real-estate`, `family-office`, `market-entry`, `fintech-launch`, `strategic-planner`, `invoice-check`, `banks-on-one-page`, `inside-your-funds`, `risks-in-francs` or `a-banks-monday` skill in this plugin, or from your own
agent calling the connectors. Change the page, restyle it, turn it into your own product.
