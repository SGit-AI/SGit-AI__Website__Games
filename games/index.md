# The catalogue

> Every game this family has published, with a maturity rung that has a test behind it, and the vault each one ships in.

*Source: <https://games.sgit.ai/games/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The catalogue

# The catalogue

Three things in one vault, at three different stages. Nothing here is finished, and the rung on each card says how far off it is.

| What | Rung | What it measures | Where |
|---|---|---|---|
| [What Can It Do?](../games/what-can-it-do.md) | `scored` | Whether you can predict what your agent can do — scored for calibration, in both directions | [play](https://what-can-it-do.games.sgit.ai) |
| [Which Agent Is It?](../games/which-agent-is-it.md) | `playable` | Whether a handful of cheap questions can identify an agent, and how wrong your picture of its reach was | [open](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj) |
| [Ideas & feedback](../games/ideas.md) | `answered` | Not a game — the reply channel: what players argue with, and the position taken on it | [open](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj) |

## All three are one vault

Vault `4evnlwrj`, published under the name *Two games about what your agent can do*, at **v0.16.1** — 81 files across 28 releases at the time this page was written. The vault auto-opens the scoreboard; a menu on every page reaches the other two and the release history.

Publishing them as one vault rather than three sites is deliberate: they share a data snapshot, the same nine public profiles, and the same telemetry lane, and a player who finishes the floor plan is handed straight to the scoreboard with the matched profile already filled in. Splitting them would break that handover and give three copies of the data to drift apart.

> **Open it yourself.** Read key `f94c8b1d4235…111118:4evnlwrj` — the full string is on [the vault's page at sgit.ai](https://sgit.ai/demos/vaults/agent-permission-games/). [Open it read-only in a new tab](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj), or clone it with `sgit clone`. It is a read key: it cannot write, which is what makes publishing it safe.

## What is in the vault besides the games

- `what-can-it-do/source/` and `which-agent-is-it/source/` — each game's readable source: the engine as an ES module, `selftest.json`, the vendored data snapshot, the build script, and a README carrying a rules table and a *does-not-prove* list.
- `telemetry.html`, `telemetry.js`, `telemetry.config.json` — what the games send and the two write-only lanes they send it on. [Our page on it](../telemetry/index.md).
- `ideas/` — the reply channel: `ontology.json`, `ideas.json`, `signals.json`, and the `graph.json` compiled from them.
- `version.json` and `version.html` — the badge on every page and the release history behind it.

## Coming, and deliberately not built yet

The game authors' own *next* list is short and honest: fit the point values from play data, show a returning player their previous calibration, export the mandate draft into the probes' shape, and put a model at the game's three edges — free text for an unlisted setup, question generation, narration. **None built, on purpose.** A game that generates its own questions cannot be self-tested against a reference, and the self-test is what makes the score arguable.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/index.html)*
