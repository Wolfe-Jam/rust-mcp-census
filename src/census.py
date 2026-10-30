#!/usr/bin/env python3
"""The Rust MCP Census: every server in the official MCP Registry that ships a cargo (crates.io) package.

Usage:
    python3 src/census.py            # collect today's snapshot into data/, then rebuild README.md
    python3 src/census.py --readme   # rebuild README.md from the snapshots already in data/

Public data only: the MCP Registry API (registry.modelcontextprotocol.io) and, for owner and
stars, the GitHub API through the `gh` CLI when it is installed (skipped otherwise).
Standard library only.
"""
import collections
import csv
import datetime
import json
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

REGISTRY = "https://registry.modelcontextprotocol.io/v0/servers"
OFFICIAL = "io.modelcontextprotocol.registry/official"
CARGO_LIVE = "2026-07-13"  # registry v1.8.0, the release that added cargo
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "rust-mcp-census"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def latest_servers():
    """Every server in the registry, latest version only."""
    cursor = None
    while True:
        q = {"limit": "100", "version": "latest"}
        if cursor:
            q["cursor"] = cursor
        d = get(REGISTRY + "?" + urllib.parse.urlencode(q))
        yield from d.get("servers", [])
        cursor = d.get("metadata", {}).get("nextCursor")
        if not cursor:
            return


def package_types(server):
    return sorted({p.get("registryType") for p in server.get("packages") or [] if p.get("registryType")})


def first_cargo_date(name):
    """The publish date of the first version that shipped a cargo package."""
    d = get(f"{REGISTRY}/{urllib.parse.quote(name, safe='')}/versions")
    dates = [s.get("_meta", {}).get(OFFICIAL, {}).get("publishedAt", "")[:10]
             for s in d.get("servers", []) if "cargo" in package_types(s["server"])]
    return min(x for x in dates if x)


def github_info(repo_url):
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", repo_url or "")
    if not m or not shutil.which("gh"):
        return "", "", ""
    repo = m[2].removesuffix(".git")
    r = subprocess.run(["gh", "api", f"repos/{m[1]}/{repo}", "--jq", "[.owner.login,.owner.type,.stargazers_count]|@tsv"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return "", "", ""
    owner, otype, stars = r.stdout.strip().split("\t")
    return owner, otype, int(stars)


def collect():
    total, types, rows = 0, collections.Counter(), []
    for s in latest_servers():
        total += 1
        srv = s["server"]
        t = package_types(srv)
        for x in t:
            types[x] += 1
        if "cargo" not in t:
            continue
        repo = (srv.get("repository") or {}).get("url", "")
        crate = next((p.get("identifier") for p in srv.get("packages") or [] if p.get("registryType") == "cargo"), "")
        owner, otype, stars = github_info(repo)
        rows.append({
            "name": srv["name"], "version": srv.get("version", ""), "first_cargo": first_cargo_date(srv["name"]),
            "packages": "+".join(t), "crate": crate, "repo": repo,
            "owner": owner, "owner_type": otype, "stars": stars,
            "description": (srv.get("description") or "").strip(),
        })
    rows.sort(key=lambda r: (r["first_cargo"], r["name"]))
    return {"date": datetime.date.today().isoformat(), "registry_servers": total,
            "package_types": dict(types.most_common()), "cargo_live": CARGO_LIVE, "servers": rows}


def save(snap):
    DATA.mkdir(exist_ok=True)
    (DATA / f"{snap['date']}.json").write_text(json.dumps(snap, indent=1, ensure_ascii=False) + "\n")
    with open(DATA / f"{snap['date']}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(snap["servers"][0].keys()))
        w.writeheader()
        w.writerows(snap["servers"])


def cell(text):
    return str(text).replace("|", "/").replace("\n", " ")


def readme(snap):
    rows = snap["servers"]
    n = len(rows)
    month = snap["date"][:7]
    by_month = collections.Counter(r["first_cargo"][:7] for r in rows)
    owner_type = {}
    for r in rows:
        owner_type.setdefault(r["owner"] or r["name"].split("/")[0], r["owner_type"])
    owners = set(owner_type)
    people = sum(t == "User" for t in owner_type.values())
    orgs = sum(t == "Organization" for t in owner_type.values())
    first = rows[0]["first_cargo"]
    last = max(r["first_cargo"] for r in rows)
    days = (datetime.date.fromisoformat(last) - datetime.date.fromisoformat(snap["cargo_live"])).days
    mix = collections.Counter(r["packages"] for r in rows)
    month_label = datetime.date.fromisoformat(snap["date"]).strftime("%B %Y")

    out = [f"# The Rust MCP Census", "",
           "Every server in the official [MCP Registry](https://registry.modelcontextprotocol.io) that ships a **cargo** (crates.io) package, counted each month.", "",
           f"## {month_label}: {n} servers", "",
           f"- **{n}** servers list a cargo package, out of {snap['registry_servers']:,} in the registry.",
           f"- **{len(owners)}** owners: {people} people and {orgs} organisations on GitHub" + (f", {len(owners) - people - orgs} elsewhere." if len(owners) - people - orgs else "."),
           f"- Cargo became a registry package type on {snap['cargo_live']}. The first cargo server arrived on {first}; the latest on {last} ({days} days).",
           f"- **+{by_month.get(month, 0)}** new in {month_label}.", "",
           "## By month", "", "| Month | New | Total |", "|---|---|---|"]
    total = 0
    for m in sorted(by_month):
        total += by_month[m]
        out.append(f"| {datetime.date.fromisoformat(m + '-01').strftime('%b %Y')} | {by_month[m]} | {total} |")
    out += ["", "## How they ship", "", "| Packages | Servers |", "|---|---|"]
    for k, v in mix.most_common():
        out.append(f"| {k.replace('+', ' + ')} | {v} |")
    out += ["", "Many Rust MCP servers list another way (npm, an MCP bundle or a container) and don't appear here. This census counts servers that list a cargo package.", ""]
    new = [r for r in rows if r["first_cargo"].startswith(month)]
    out += [f"## New in {month_label} ({len(new)})", "", "| First cargo | Server | What it does |", "|---|---|---|"]
    for r in reversed(new):
        link = f"[`{r['name']}`]({r['repo']})" if r["repo"] else f"`{r['name']}`"
        out.append(f"| {r['first_cargo']} | {link} | {cell(r['description'])} |")
    out += ["", f"## All {n}", "", "| # | First cargo | Server | Crate | Packages | ★ | What it does |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        link = f"[`{r['name']}`]({r['repo']})" if r["repo"] else f"`{r['name']}`"
        crate = f"[{r['crate']}](https://crates.io/crates/{r['crate']})" if r["crate"] else ""
        out.append(f"| {i} | {r['first_cargo']} | {link} | {crate} | {r['packages'].replace('+', ' + ')} | {r['stars']} | {cell(r['description'])} |")
    out += ["", "## Method", "",
            f"- **Source:** the registry API (`/v0/servers?version=latest`, then `/v0/servers/{{name}}/versions` for the first version with a cargo package). Owner and stars from the GitHub API. Snapshot taken {snap['date']}.",
            "- **Counted:** servers whose latest version lists a package with `registryType: cargo`. Servers that list only npm, PyPI, OCI or a bundle are not counted, whatever language they are written in.",
            "- **Stars** are shown, not ranked. Nothing here judges a server.",
            f"- **Data:** [`data/{snap['date']}.json`](data/{snap['date']}.json) and [`data/{snap['date']}.csv`](data/{snap['date']}.csv). Every month gets its own snapshot; none is overwritten.",
            "- **Run it yourself:** `python3 src/census.py` (Python 3, standard library; `gh` for owner and stars).",
            "- Cargo support in the registry: [modelcontextprotocol/registry#1207](https://github.com/modelcontextprotocol/registry/pull/1207).", "",
            "## Background", "",
            "[An MCP Story about Rust](https://wolfejam.dev/blog/rust-mcp-story): how cargo got into the registry.", "",
            "---", "",
            "Know someone running an MCP server who'd like a hand? [The Worth-It Service](https://wolfejam.dev/#worth-it) starts with a free report.", ""]
    (ROOT / "README.md").write_text("\n".join(out))


def main():
    if "--readme" in sys.argv:
        snap = json.loads(sorted(DATA.glob("*.json"))[-1].read_text())
    else:
        snap = collect()
        save(snap)
    readme(snap)
    print(f"{snap['date']}: {len(snap['servers'])} cargo servers of {snap['registry_servers']}")


if __name__ == "__main__":
    main()
