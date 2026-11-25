# Build with Antevo

Tools you build on six Antevo engines. One prompt, the engines answer, your assistant joins the
findings into something new. Page: https://antevo.ch/mcp/build/

## Startup Launch Intelligence (skill `startup-launch`)

Give it your idea, your home market and the next one, and up to five candidate names. It:

1. screens the names across the trademark registers, the companies registered under them and their domains (**Trademark**);
2. finds the competition in the Swiss commercial register (**Companies**);
3. reads today's business board of risks and openings for companies (**Strategy Radar**);
4. reads the market regime and the risk radar (**Executive**);
5. reads how strained markets are this week (**Tremor Watch**);
6. asks the economy desk about rates, inflation, currency, growth and funding (**Research**);

then writes how the findings connect and builds the workspace: brand, market entry, competition,
risk, a 90-day roadmap and what to watch. `template/` renders it.

## Connections

| engine | address | access |
|---|---|---|
| Trademark | `https://trademark.antevo.ch/mcp` | free, no account |
| Strategy Radar | `https://api.antevo.ch/mcp/strategy/mcp` | free, no account |
| Executive | `https://api.antevo.ch/mcp/executive/mcp` | free, no account |
| Tremor Watch | `https://api.antevo.ch/mcp/tremor/mcp` | free, no account |
| Companies | `https://api.antevo.ch/mcp/companies/mcp` | any Antevo account; finding is free, opening a file uses credits |
| Research | `https://api.antevo.ch/mcp/research/mcp` | any Antevo account; answers use credits |

Every figure keeps its date. A trademark screen is not legal clearance. The roadmap is options to
consider, never investment, legal or tax advice.
