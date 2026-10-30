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
    total, active, types, rows = 0, 0, collections.Counter(), []
    for s in latest_servers():
        total += 1
        srv = s["server"]
        status = s.get("_meta", {}).get(OFFICIAL, {}).get("status", "")
        active += status == "active"
        t = package_types(srv)
        for x in t:
            types[x] += 1
        if "cargo" not in t:
            continue
        repo = (srv.get("repository") or {}).get("url", "")
        crate = next((p.get("identifier") for p in srv.get("packages") or [] if p.get("registryType") == "cargo"), "")
        owner, otype, stars = github_info(repo)
        rows.append({
            "name": srv["name"], "version": srv.get("version", ""), "status": status, "first_cargo": first_cargo_date(srv["name"]),
            "packages": "+".join(t), "crate": crate, "repo": repo,
            "owner": owner, "owner_type": otype, "stars": stars,
            "description": (srv.get("description") or "").strip(),
        })
    rows.sort(key=lambda r: (r["first_cargo"], r["name"]))
    return {"date": datetime.date.today().isoformat(), "registry_servers": total, "registry_active": active,
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


def monday(date):
    d = datetime.date.fromisoformat(date)
    return (d - datetime.timedelta(days=d.weekday())).isoformat()


def pkgs(packages):
    return " + ".join(f"`{x}`" for x in packages.split("+"))


def readme(snap):
    deprecated = [r for r in snap["servers"] if r.get("status", "active") != "active"]
    rows = [r for r in snap["servers"] if r.get("status", "active") == "active"]
    n = len(rows)
    today = datetime.date.fromisoformat(snap["date"])
    week_ago = (today - datetime.timedelta(days=6)).isoformat()
    by_month = collections.Counter(r["first_cargo"][:7] for r in rows)
    by_week = collections.Counter(monday(r["first_cargo"]) for r in rows)
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
    day_label = f"{today.day} {today:%B %Y}"

    out = [f"# The Rust MCP Census", "",
           "Every server in the official [MCP Registry](https://registry.modelcontextprotocol.io) that ships a **cargo** (crates.io) package, counted each week.", "",
           f"## {day_label}: {n} servers", "",
           f"- **{n}** active servers list a cargo package, out of {snap['registry_active']:,} active servers in the registry ({snap['registry_servers']:,} entries, deprecated included)."
           + (f" {len(deprecated)} more cargo servers are deprecated." if deprecated else ""),
           f"- **{len(owners)}** owners: {people} people and {orgs} organisations on GitHub" + (f", {len(owners) - people - orgs} elsewhere." if len(owners) - people - orgs else "."),
           f"- Cargo has been accepted in production since registry v1.8.0 ({snap['cargo_live']}). The first cargo server arrived on {first}; the latest on {last} ({days} days).",
           f"- **+{sum(r['first_cargo'] >= week_ago for r in rows)}** new in the last 7 days ({week_ago} to {snap['date']}).", "",
           "## By week", "", "Weeks start on Monday.", "", "| Week of | New | Total |", "|---|---|---|"]
    total = 0
    for w in sorted(by_week):
        total += by_week[w]
        out.append(f"| {w}{' (so far)' if w == monday(snap['date']) else ''} | {by_week[w]} | {total} |")
    out += ["", "## By month", "", "| Month | New | Total |", "|---|---|---|"]
    total = 0
    for m in sorted(by_month):
        total += by_month[m]
        out.append(f"| {datetime.date.fromisoformat(m + '-01').strftime('%b %Y')} | {by_month[m]} | {total} |")
    out += ["", "## How they ship", "", "| Packages | Servers |", "|---|---|"]
    for k, v in mix.most_common():
        out.append(f"| {pkgs(k)} | {v} |")
    out += ["", "Many Rust MCP servers list another way (npm, an MCP bundle or a container) and don't appear here. This census counts servers that list a cargo package.", ""]
    new = [r for r in rows if r["first_cargo"] >= week_ago]
    out += [f"## New in the last 7 days ({len(new)})", "", "| First cargo | Server | What it does |", "|---|---|---|"]
    for r in reversed(new):
        link = f"[`{r['name']}`]({r['repo']})" if r["repo"] else f"`{r['name']}`"
        out.append(f"| {r['first_cargo']} | {link} | {cell(r['description'])} |")
    out += ["", f"## All {n}", "", "| # | First cargo | Server | Crate | Packages | ★ | What it does |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        link = f"[`{r['name']}`]({r['repo']})" if r["repo"] else f"`{r['name']}`"
        crate = f"[{r['crate']}](https://crates.io/crates/{r['crate']})" if r["crate"] else ""
        out.append(f"| {i} | {r['first_cargo']} | {link} | {crate} | {pkgs(r['packages'])} | {r['stars']} | {cell(r['description'])} |")
    if deprecated:
        out += ["", f"## Deprecated ({len(deprecated)})", "", "Marked deprecated in the registry, so not counted above.", ""]
        out += [f"- `{r['name']}` (first cargo {r['first_cargo']})" for r in deprecated]
    out += ["", "## Method", "",
            f"- **Source:** the registry API (`/v0/servers?version=latest`, then `/v0/servers/{{name}}/versions` for the first version with a cargo package). Owner and stars from the GitHub API. Snapshot taken {snap['date']}.",
            "- **Counted:** active servers whose latest version lists a package with `registryType: cargo`. Servers that list only `npm`, `pypi`, `oci` or `mcpb` are not counted, whatever language they are written in. A server that listed cargo in an earlier version but not its latest is not counted.",
            "- **Dates** are the registry's `publishedAt`, in UTC.",
            "- **What it does** is each author's own description from the registry, unedited.",
            "- **Stars** are shown, not ranked. Nothing here judges a server.",
            f"- **Data:** [`data/{snap['date']}.json`](data/{snap['date']}.json) and [`data/{snap['date']}.csv`](data/{snap['date']}.csv). One snapshot per day; earlier days are never overwritten.",
            "- **Run it yourself:** `python3 src/census.py` (Python 3, standard library; `gh` for owner and stars). One crawl a week (Sundays, 23:00 UTC, by [a GitHub Action](.github/workflows/weekly.yml)), with the User-Agent `rust-mcp-census`.",
            "- Cargo support in the registry: [modelcontextprotocol/registry#1207](https://github.com/modelcontextprotocol/registry/pull/1207).", "",
            "## Background", "",
            "[An MCP Story about Rust](https://wolfejam.dev/blog/rust-mcp-story): how cargo got into the registry.", ""]
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
