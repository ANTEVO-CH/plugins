#!/usr/bin/env python3
"""Antevo intelligence terminal: one morning page from four free Antevo engines.

Calls Executive Brief, Tremor Watch, Strategy Radar and (optionally) Trademark over MCP
(JSON-RPC over HTTP), needs no account and no API key, and writes workspace.json in the
format the Antevo build template renders (https://antevo.ch/mcp/build/).

    python3 antevo-terminal.py                 # writes ./workspace.json
    python3 antevo-terminal.py --out today.json --watch-name "Your Brand"

Python 3.9+, standard library only. Every line in the output is an engine's answer, with
its date; the script adds no opinion of its own. Not investment advice.
"""
import argparse, json, sys, urllib.request
from datetime import date

ENGINES = {
    "executive": "https://api.antevo.ch/mcp/executive/mcp",
    "tremor": "https://api.antevo.ch/mcp/tremor/mcp",
    "strategy": "https://api.antevo.ch/mcp/strategy/mcp",
    "trademark": "https://trademark.antevo.ch/mcp",
}
HEADERS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
           "User-Agent": "antevo-terminal/1.0"}


class Engine:
    """A minimal MCP client: initialize once, then call tools."""

    def __init__(self, url):
        self.url, self.sid, self.n = url, None, 0
        self._rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                 "clientInfo": {"name": "antevo-terminal", "version": "1.0"}})
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _post(self, payload):
        h = dict(HEADERS)
        if self.sid:
            h["Mcp-Session-Id"] = self.sid
        req = urllib.request.Request(self.url, json.dumps(payload).encode(), h)
        with urllib.request.urlopen(req, timeout=90) as r:
            self.sid = r.headers.get("Mcp-Session-Id") or self.sid
            return r.read().decode()

    def _rpc(self, method, params):
        self.n += 1
        raw = self._post({"jsonrpc": "2.0", "id": self.n, "method": method, "params": params})
        if "data:" in raw[:300]:  # streamable HTTP answers as server-sent events
            raw = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")][-1]
        msg = json.loads(raw)
        if "error" in msg:
            raise RuntimeError(f"{method}: {msg['error']}")
        return msg["result"]

    def call(self, tool, **args):
        res = self._rpc("tools/call", {"name": tool, "arguments": args})
        return json.loads(res["content"][0]["text"])


LEVEL = {"Calm": "green", "Elevated": "amber", "High": "red", "Severe": "red"}
IMPACT = {"severe": 0, "high": 1, "medium": 2, "low": 3}


def clip(text, limit):
    """Keep whole clauses (split on '; ') up to limit; never cut a word in half."""
    out = ""
    for part in text.rstrip(";. ").split("; "):
        nxt = part if not out else out + "; " + part
        if len(nxt) > limit:
            break
        out = nxt
    if not out:  # first clause alone is too long: cut at a word
        out = text[:limit].rsplit(" ", 1)[0].rstrip(",;") + "…"
    return out


def build(watch_name=None):
    ex, tr, sr = (Engine(ENGINES[k]) for k in ("executive", "tremor", "strategy"))
    brief = ex.call("get_executive_brief", sections="title,regime,plain_language,watch")["brief"]
    cats = ex.call("get_catalysts", days_ahead=14)["items"]
    tidx = tr.call("get_tremor_index")
    pairs = tr.call("get_tremor_pairs", limit=3)["pairs"]
    board = sr.call("get_business_board")
    entries = sorted(board["entries"], key=lambda e: IMPACT.get(e["impact"], 9))
    day, week = brief.get("as_of") or str(date.today()), tidx["week"]
    rd, fam = tidx["reading"], sorted(tidx["families"], key=lambda f: -f["times_normal"])
    risks = [e for e in entries if e["kind"] == "risk"]
    openings = [e for e in entries if e["kind"] != "risk"]
    rising = [e for e in entries if e["trend"] in ("rising", "new")]

    tries = [
        {"name": "Markets today", "verdict": brief["regime"]["label"], "level": "ink",
         "evidence": [f"{t['theme']}: {t['read']}" for t in brief["plain_language"]["theme_reads"][:3]]},
        {"name": "Market strain", "verdict": f"{rd['status']}, {rd['times_normal']} times a normal week",
         "level": LEVEL.get(rd["status"], "ink"),
         "evidence": [f"Week to {week}; the week before: {tidx['last_week']['status']}, {tidx['last_week']['times_normal']} times",
                      "Most unusual families: " + ", ".join(f"{f['family']} {f['times_normal']}x" for f in fam[:3]),
                      f"Most unusual pair: {pairs[0]['anchor']} and {pairs[0]['asset']}, z {pairs[0]['z']}" if pairs else "No pair breaking"]},
        {"name": "Business board", "verdict": f"{len(risks)} risk{'s' * (len(risks) != 1)}, {len(openings)} opening{'s' * (len(openings) != 1)}", "level": "amber" if risks else "green",
         "evidence": [f"{e['title']} ({e['impact']} impact, {e['trend']})" for e in entries[:3]]},
        {"name": "The next two weeks", "verdict": f"{len(cats)} dated events", "level": "ink",
         "evidence": [f"{c['date']}: {clip(c['event'], 110)}" for c in cats[:3]]},
    ]
    if watch_name:  # optional: a free screen of one name, today only
        tm = Engine(ENGINES["trademark"]).call("check_names", names=[watch_name], classes=[9, 42])
        r = tm["ranked"][0]
        tries.append({"name": f"The name {watch_name}", "verdict": r["label"],
                      "level": "green" if r["verdict"] == "none_found" else "amber",
                      "evidence": [f"{r['near_marks']} near marks in classes 9 and 42", "A screen is not legal clearance"]})

    return {
        "template": "Built on Antevo · https://antevo.ch/mcp/build/intelligence-terminal/",
        "kind": "Intelligence Terminal", "title": brief["title"],
        "subtitle": brief["plain_language"]["headline"].rstrip("."), "built": day,
        "note": "Written by antevo-terminal.py from four free Antevo engines, no account, no AI model in between. Every line is an engine's answer on the date shown.",
        "tries": {"label": "The panels", "item": "Panel",
                  "source": f"Antevo Executive Brief {day}; Antevo Tremor Index, week of {week}; Antevo Executive Brief business board {board['as_of']}.",
                  "items": tries},
        "steps": {"label": "The dates, with the signal to read", "items": [
            {"do": f"{c['date']} · {clip(c['event'], 400)}", "why": c["signal"], "links": []} for c in cats[:6]]},
        "sections": [
            {"title": e["title"], "verdict": f"{e['kind'].capitalize()} · {e['impact']} impact · {e['likelihood']} likelihood · {e['trend']}",
             "level": "red" if e["impact"] == "severe" else "amber" if e["kind"] == "risk" else "green",
             "so_what": "Touches: " + e.get("who_it_touches", ""),
             "evidence": [e["why"], "Watch: " + e["watch"], e["act_when"]],
             "source": f"Antevo Executive Brief, business board of {e.get('why_date', board['as_of'])}"} for e in entries[:6]],
        "links": [
            {"a": "Tremor Watch", "b": "Strategy Radar",
             "text": f"Markets read {rd['status']} ({rd['times_normal']} times a normal week); {len(rising)} of the board's {len(entries)} entries are rising or new."},
            {"a": "Executive Brief", "b": "Tremor Watch",
             "text": f"The brief's regime: {brief['regime']['label'][:1].lower() + brief['regime']['label'][1:]}. The families breaking most: {fam[0]['family']} and {fam[1]['family']}."},
        ],
        "watch": brief["watch"],
        "disclaimer": "From Antevo answers, each dated, assembled by a script with no opinion of its own. Tremor Watch describes, it does not forecast. Not investment advice.",
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default="workspace.json")
    ap.add_argument("--watch-name", help="also screen one name in the trademark registers (free)")
    a = ap.parse_args()
    ws = build(a.watch_name)
    json.dump(ws, open(a.out, "w"), ensure_ascii=False, indent=2)
    print(f"wrote {a.out}: {len(ws['tries']['items'])} panels, {len(ws['sections'])} board entries, {len(ws['steps']['items'])} dates")
