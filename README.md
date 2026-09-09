# SGit-AI__Website__Games

Repo for **[games.sgit.ai](https://games.sgit.ai)** — why this family builds games, and the
games it has, each with a maturity label that has a test behind it.

The games are **not** copied into this repo. *What Can It Do?* lives in encrypted vault
`pg87npy3` (v1.0.0, 9 September 2026) and reads its data from the player site; *Which Agent Is
It?* and the home page live in the games vault `4evnlwrj` (v0.26.0), which also holds the 9
September version of both games on branch `release-2026-09-09`. The site opens the vaults live
over the SG/Vault embed protocol with the vault-browser surface suppressed. One source, no drift.

Sibling site: **[what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai)**
([repo](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do)) — the first game,
player-facing.

## Structure

- `index.html` — the argument; `games/` — the catalogue and a page per game
- `method/` — four claims: calibration, the ceiling, levels, grant vs. mandate
- `maturity/` — the five-rung ladder, and where each game sits
- `build/` — how to build a game as a vault, including the folder-manifest trap
- `telemetry/` — what our games send, and how to stop it
- `network/`, `admin/` — the usual house furniture
- `briefs/00__PLAN.md` — the plan these sites were built from
- `briefs/01__PLAN__vaults-and-packs.md` — the plan for the vault split, question packs and
  the Mavs PoC — open for review

## Build

Every page exists once, as content, in `admin/build/build_pages.py`. Nothing under the site
root is hand-edited — `admin/build/shell.py` renders one block list to both the HTML page and
its markdown twin, so the two cannot drift.

```bash
python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap, robots
node admin/build/validate.js          # the gate CI will run
```

## Release

```bash
# bump admin/build/version.txt and add a VERSION_LOG row in build_pages.py
python3 admin/build/build_pages.py && node admin/build/validate.js
git commit -am "site vX.Y.Z: what changed" && git push origin dev
```

Every push to `dev` runs **validate → tag → deploy**. Same pipeline as
[PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI),
[Graphs](https://github.com/SGit-AI/SGit-AI__Website__Graphs) and
[Wardley-Maps](https://github.com/SGit-AI/SGit-AI__Website__Wardley-Maps).

### The gate

The four house checks — version agreement, internal links, canonical/CNAME agreement, and a
key-leak tripwire — plus three of our own: a page that mounts a vault app must carry the
telemetry disclosure; a maturity label must be one of the five rungs; and every HTML page must
have its markdown twin.

The tripwire is **extended** relative to the sibling sites. Theirs matches
`<secret>:<uuid>`; every vault in this family uses the short id form (`4evnlwrj`), so that
check would have passed over a leaked key here. It now matches both shapes, with the published
read key on an allow-list of exact strings.

## Credentials

The read keys for vaults `pg87npy3` and `4evnlwrj` are published on purpose — it is what lets a reader open the
vault and check every claim on the site against the files. It cannot write. The vault key is
not published and never will be.

## Licence

Content CC BY 4.0. Code under the repository licence.
