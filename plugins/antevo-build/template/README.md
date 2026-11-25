# Startup Launch Intelligence — the template

One page that renders one file. `workspace.json` holds the launch workspace your agent builds from
six Antevo engines; `index.html` shows it. The file here is a real run of 25 November 2026 for an
example AI fintech (the name, Lumora, is an example, not a suggestion).

```bash
python3 -m http.server 8000   # in this folder, then open http://localhost:8000
```

## The file

| field | what goes in it |
|---|---|
| `idea`, `markets`, `name`, `built` | the founder's idea, home market then next market, the name tried, the date |
| `brand`, `market`, `competition`, `risk` | each a `verdict`, a `level` (`red`, `green`, `amber`, `ink`), the `evidence` lines and the `source` with its date |
| `links` | how the findings connect: two engines (`a`, `b`) and one sentence |
| `roadmap` | three blocks of `days` and what to `do`: options to consider |
| `watch` | the dates and indicators the engines named |
| `note`, `disclaimer` | keep them: every figure is an engine's answer on the date shown; not advice; a screen is not clearance |

Fill it with the `startup-launch` skill in this plugin, or from your own agent calling the six
connectors. Change the page, restyle it, turn it into your own product.
