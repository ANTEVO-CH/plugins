"""Validate the marketplace the way a user's install would meet it.

Every JSON file parses; every marketplace entry points at a plugin whose manifest
agrees on name and version; every plugin wires an HTTPS connector on antevo.ch;
every skill's frontmatter names its own directory and carries a description and a
compatibility note; every SVG in assets/ is well-formed XML.
"""
import glob
import json
import re
import sys
import xml.dom.minidom
from urllib.parse import urlparse

fail = 0


def bad(msg):
    global fail
    print(f"FAIL {msg}")
    fail = 1


for path in sorted(glob.glob("**/*.json", recursive=True)):
    try:
        json.load(open(path))
    except Exception as e:
        bad(f"{path}: {e}")

market = json.load(open(".claude-plugin/marketplace.json"))
for entry in market["plugins"]:
    name = entry["name"]
    root = f"plugins/{entry['source'].lstrip('./')}"
    try:
        manifest = json.load(open(f"{root}/.claude-plugin/plugin.json"))
    except FileNotFoundError:
        bad(f"{name}: no {root}/.claude-plugin/plugin.json")
        continue
    if manifest.get("name") != name:
        bad(f"{name}: plugin.json name is {manifest.get('name')!r}")
    if manifest.get("version") != entry.get("version"):
        bad(f"{name}: marketplace says {entry.get('version')}, plugin.json says {manifest.get('version')}")
    servers = json.load(open(f"{root}/.mcp.json")).get("mcpServers", {})
    if not servers:
        bad(f"{name}: .mcp.json wires no connector")
    for server, cfg in servers.items():
        host = urlparse(cfg.get("url", "")).hostname or ""
        if not cfg.get("url", "").startswith("https://") or not (host == "antevo.ch" or host.endswith(".antevo.ch")):
            bad(f"{name}/{server}: {cfg.get('url')} is not an https antevo.ch address")
    skills = sorted(glob.glob(f"{root}/skills/*/SKILL.md"))
    for skill in skills:
        text = open(skill).read()
        fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        folder = skill.split("/")[-2]
        if not fm:
            bad(f"{skill}: no frontmatter")
            continue
        body = fm.group(1)
        if not re.search(rf"^name: {re.escape(folder)}$", body, re.M):
            bad(f"{skill}: frontmatter name does not match its directory")
        for field in ("description", "compatibility"):
            if not re.search(rf"^{field}:", body, re.M):
                bad(f"{skill}: no {field}")
    print(f"ok   {name} {entry.get('version')} — {len(servers)} connector(s), {len(skills)} skills")

for svg in sorted(glob.glob("assets/*.svg")):
    try:
        xml.dom.minidom.parse(svg)
        print(f"ok   {svg}")
    except Exception as e:
        bad(f"{svg}: {e}")

sys.exit(fail)
