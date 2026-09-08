# Plan — `games.sgit.ai` and `what-can-it-do.games.sgit.ai`

**Status:** draft for review. Nothing in this plan has been built yet.
**Written:** 8 September 2026, by Claude Code, from the state of the sgit.ai network and of
vault `4evnlwrj` as read on that date.
**For review by:** the agent that built the games vault (`4evnlwrj`), and anyone working on
the RiskMandate.ai side of the same idea.
**What is wanted back:** corrections to §1 (I read your vault rather than asking you), a
decision on §4 (the embed choice is yours to veto — it changes what your app can do), and
answers to §9.

Everything below is arguable. Where I state a fact I got from the vault, the file it came
from is named, so you can tell a fact from a guess.

---

## 0. The short version

Two sites, two audiences, one game.

| | `games.sgit.ai` | `what-can-it-do.games.sgit.ai` |
|---|---|---|
| Reader | colleagues, practitioners, agents | **players**, sent a link |
| Question it answers | *why are we building games at all?* | *want to find out what your agent can do?* |
| Voice | house voice — sourced claims, stated status, honest edges | plain, warm, no jargon above the fold |
| Front page | the argument, then the catalogue | **the game, playable, immediately** |
| Vault chrome | visible, explained, part of the point | hidden |
| Maturity | catalogue carries a maturity label per game | one game, at its own maturity |
| Repo | `SGit-AI/SGit-AI__Website__Games` | `SGit-AI/SGit-AI__Website__Game__What-Can-It-Do` |

Both repos exist and are empty apart from a README. **Both DNS names already resolve** to
`sgit-ai.github.io` (checked 8 Sep; `games.sgit.ai` and `what-can-it-do.games.sgit.ai` both
have CNAME records, and `sgit.ai` has no wildcard, so somebody created them deliberately).
So the infrastructure question is already answered and the work is content and embedding.

---

## 1. What already exists — read from the vault, not assumed

I opened vault `4evnlwrj` read-only with the key published on
`sgit.ai/demos/vaults/agent-permission-games/`, using the same derivation
`sgit.ai/assets/vault-embed.js` uses. What follows is from that read, and may be a commit or
two behind you.

**Version `0.16.1`** (`version.json`, release entry dated 7 September 2026), **81 files**,
under the name *"Two games about what your agent can do"*.

**Three apps, not two.** The root `app.json` auto-opens `what-can-it-do/index.html`. Each of
the three folders carries its own manifest, because — as your `_why_this_file` note records —
a folder-level `app.json` replaces the root one wholesale rather than inheriting from it:

- `what-can-it-do/` — the scoreboard. 40 questions, 5 levels, `+30 / −50 / 0`, yes scored at
  0.75 and no at 0.25, `points = 160 × (¼ − (p − truth)²)`; `±20` mandate points for the
  "but…" tick; **17 of 40 questions above the ceiling** (43%, self-test fails outside 33–50%);
  nine public profiles; data snapshot taken 2026‑09‑06 from pki.sgit.ai.
- `which-agent-is-it/` — the floor plan. Reveal links into the scoreboard with the matched
  profile handed over.
- `ideas/` — Ideas & feedback, added at v0.16.0. The reply channel: a graph of themes, ideas,
  decisions and counted signals, with `answers.json` folded back into the game so a question
  someone argued with now carries the position taken on it. **This is the piece the sgit.ai
  page does not yet describe, and it is the best argument for the player site existing** — it
  is the thing that turns a game into a conversation.

**Permissions the root and both game manifests declare:**

```json
{ "permissions": { "append": { "write": true }, "network": true, "llm": { "chat": true } } }
```

Three consequences that drive §4:

1. `network: true` exists because the vault host's app frame ships
   `connect-src blob: data:`, so a direct `fetch` to the telemetry API is blocked without it
   (v0.12.3).
2. `append.write` is the bridge fallback, `sg.append.write` (v0.11.2, v0.12.1).
3. `llm.chat` is the chat panel added at v0.14.0 — **the model runs in the host and the
   vault's key never enters the frame**. This one is the constraint that decides the embed.

**Telemetry** (`telemetry.config.json`): two lanes on vault `kqngdecz` — `append_token` for
anonymous counters, `feedback_token` for what a player deliberately writes, deliberately kept
apart so retention can differ and one cannot flood the other. RSA‑OAEP‑SHA256 wrapping
AES‑256‑GCM; flush every 4 s, at most 40 flushes and 50 events per flush per session. Both
tokens are write-only and blind. `telemetry.html` is reachable from every page.

**Already published on sgit.ai:** `/demos/vaults/agent-permission-games/` describes the vault
at v0.8.1, carries the credential audit, and publishes two findings. It predates `ideas/`, the
chat panel, the picker, the synthetic users and the results redesign — roughly nine releases of
drift. That page is a *vault* page and stays where it is; these two sites are not a replacement
for it and should link to it rather than restate it.

---

## 2. `games.sgit.ai` — the concept site

### The argument it makes

The house style is that a site exists to take **one question** further than a section could.
The question here:

> **A game is the only artefact that makes somebody state a belief before they are told the
> answer — which is the only way to measure what they actually think.**

Everything else we publish (a graph, a standard, a report, a map) can be nodded at. A player
of *What Can It Do?* has to commit to *can it?* before the board stamps it, and the delta
between the two is data that could not have been collected any other way. That is the claim,
and it is falsifiable: if play data shows players are as well calibrated as they think, the
game measured nothing worth measuring.

Second claim, and the one the network cares about: **the mandate is a by-product.** A player
answers *do you want it to?* forty times and walks away holding a draft mandate they did not
set out to write. That is the RiskMandate.ai idea — grant vs. mandate, and the delta nothing
covers — arrived at by playing rather than by filling in a form.

### Site map

```
/                          the argument: why games, what a game measures, the catalogue
/games/                    the catalogue — every game, with a maturity label
/games/what-can-it-do/     what it measures, how it scores, → play it (player site)
/games/which-agent-is-it/  the floor plan, the prediction gap
/games/ideas/              the reply channel: how an argument becomes a published position
/method/                   the four method pages:
  · calibration.html       why a proper scoring rule, and why yes-to-everything must lose
  · the-ceiling.html       17 of 40 questions no agent can do — measuring over-crediting
  · levels.html            a level is distance from a consequence, derived from a mesh
  · grant-vs-mandate.html  the delta, and where it comes from (RiskMandate.ai)
/build/                    how to build a game as a vault: the contract, the manifest trap,
                           the telemetry lane, what to publish beside it
/telemetry/                what our games send, and the disclosure obligation that follows
/maturity/                 the ladder, stated once, so a label on a card means something
/network/                  siblings; /admin/, /agents/ (llms.txt), the usual house furniture
```

### The maturity ladder

The user's brief asks for games "which will have different levels of maturity". The network
already has stage vocabulary (`beta`, `research site`, `published soon`) but nothing for a
game. Proposed — five rungs, each with a **test**, so a label is a claim rather than a mood:

| Rung | Means | The test that moves it up |
|---|---|---|
| **sketch** | an idea and a rules table, nothing playable | — |
| **playable** | you can finish a run | a stranger finished it without being told how |
| **scored** | the scoring is a stated rule, self-tested | `selftest.json` passes and the rule is published |
| **measured** | play data exists and has changed something | a release whose notes cite play data |
| **answered** | players argue with it and get answers back | positions published in the ideas graph |

Against that ladder today: *What Can It Do?* is **scored**, one release short of **measured**
(it has telemetry and an ideas graph, but I found no release note yet that says "we changed X
because the data said Y" — v0.16.1 changes the feedback UI because of a bias argument, which
is close but is reasoning, not data). *Which Agent Is It?* is **playable/scored**. *Ideas* is
not a game; it is listed as the reply channel. **This is a claim about your work made from the
outside — correct it.**

### How games.sgit.ai shows a game

Small, inline, honest: a card per game with a screenshot, the maturity rung, one sentence, and
**a live preview** using the minimal embed (§4, option B) that a reader can expand. The
concept site is allowed to show the seams — the vault id, the read key, the `sgit clone`
command — because showing the seams *is* the argument on this domain. The player site is not.

---

## 3. `what-can-it-do.games.sgit.ai` — the player site

### The rule that governs every decision on this domain

**A player arrives from a link somebody sent them. They have no idea what a vault is and they
should not need to find out.** Every word on the first screen either gets them into the game
or explains what they will get out of it. Everything else lives below the fold or on another
page.

### The front page, top to bottom

1. **One line:** *"You gave an AI agent access to your machine. Do you know what it can
   actually do?"*
2. **The game, mounted and playable, without a click.** Full-bleed. Not a button that reveals
   a button.
3. Under it, in small type: what this is, how long it takes (~5 minutes), **that it sends
   anonymous usage events and how to stop it** — see below, this one is not optional — and
   that nothing is stored and nothing identifies you.
4. **What you get at the end:** the score, the calibration, and the mandate draft. Shown as a
   real screenshot of the end screen, not described.
5. **Share.** The single thing this domain exists for. A short, memorable URL and a copy
   button, plus the score card the game already generates.

### The rest of the site — four pages, no more

- `/how-it-is-scored/` — +30 / −50 / 0, in plain words, and *why a wrong answer costs more
  than a right one earns*. Players will ask; the answer is interesting; and stating the rule
  before play is what makes the score mean anything.
- `/the-ceiling/` — "some of these questions are things **no** agent can do". Publish this.
  A player who guesses wrong on those and is not told why will conclude the game is broken.
- `/what-we-learn/` — what is sent, what is not, who sees it, and the ideas graph as the
  reply. Links to `telemetry.html` in the vault rather than paraphrasing it.
- `/about/` — the one page that says "this is built by sgit.ai, here is the vault, here is
  the key, you can clone it". The vault mechanics get exactly one page on this domain, at the
  bottom of the funnel, for the player who got curious.

### The disclosure obligation moves with the game

The vault carries a notice with a pause switch on every page, and `telemetry.html` behind it.
**Putting the game on a public domain does not discharge that; it extends it.** The sgit.ai
page already names this in its first finding: two of four pages once said "nothing sent" while
events were being sent, and it called that out precisely because the vault's subject is
informed consent.

So on the player site: the notice is **on the front page, visible without scrolling**, not in
a footer, and the pause switch works before the first question. A site about whether you know
what your agent can do cannot be coy about what *it* is doing. If the in-frame notice is
sufficient and duplicating it outside is worse (two switches, one of which does nothing), say
so — that is a real design question and you own the answer.

---

## 4. The embed — the decision this plan needs a verdict on

The network has two working embed hosts. They are not equivalent, and the difference lands
squarely on features you shipped in the last four releases.

### Option A — the official SG/Vault UI, over the embed protocol

`sgit.ai/assets/vault-ui-embed.js`. Loads `https://dev.vault.sgraph.ai/?embed=1&parent=<origin>`
in an iframe, waits for `{sg:'vault-embed-ready'}` **from that frame**, then posts
`{sg:'vault-open', key, mode}` with `targetOrigin` pinned. The key never appears in a URL and
is never written to the frame's storage.

- **You get the real host.** `sg.llm.chat` works, so the chat panel added at v0.14.0 works.
  `sg.append.write` works, so the telemetry fallback works. `app.json` permissions are read
  and honoured, so `network: true` means what it means everywhere else.
- **Cost:** the SG/Vault chrome, two stacked surfaces (App Mode *and* the vault browser), and
  a slower first paint — the component deliberately opens the browser surface only after the
  app reports ready.
- **It needs one small change for the player site.** Reading the component: `if (hasApp)
  push('app'); push('vault')` — the vault-browser surface is *always* added. A player site
  needs App Mode alone, chromeless. That is a `data-browser="0"` attribute and two lines. I
  would add it to a copy of the component in this repo rather than patching sgit.ai's,
  unless the sgit.ai maintainers want it upstream.

### Option B — the minimal host

`sgit.ai/assets/vault-embed.js` (~170 lines). Derives the ref id with HMAC-SHA256, fetches
ciphertext over CORS, decrypts with Web Crypto, and boots the app's `index.html` into a
`srcdoc` iframe with `sandbox="allow-scripts"` (opaque origin), serving `sg.vfs.readText`,
`sg.vfs.read`, `sg.loadCss`, `sg.loadJs` over postMessage.

- **Clean and fast**, no chrome, and it cannot write by construction — the page only ever
  holds a read key.
- **But the bridge is reads only.** There is no `sg.llm.*` and no `sg.append.*` in it. So:
  **the chat panel would not work**, and telemetry would fall back to the direct `fetch`
  path — which *should* succeed here, because the page is served from GitHub Pages with no
  restrictive CSP, unlike the vault host's frame. That inverts the v0.12.3 situation and is
  worth testing before anyone relies on it.
- It also does not read `app.json` at all, so your permission declarations are inert.

### Option C — link out

`https://dev.vault.sgraph.ai/#<key>` in a new tab. Zero risk, zero embedding, and the sgit.ai
page already recommends it for the full-width board.

### Recommendation

- **`what-can-it-do.games.sgit.ai` → Option A, with the app-only flag added.** The player
  site is the one that most needs the chat panel and a telemetry lane that works the same way
  it does everywhere else, and it is the one place where losing five releases of features to
  save some chrome would be the wrong trade. The domain is dedicated, so App Mode can be
  full-bleed and the chrome cost mostly disappears.
- **`games.sgit.ai` → Option B for the small inline previews on catalogue cards**, plus
  Option C ("open it full-width") everywhere. Previews are illustrative; a card that cannot
  chat is fine.
- **Both sites publish the credential and the `sgit clone` line**, on the pages where that
  belongs — always as a read key, never as a vault key, per the house rule.

**Which credential?** Two forms are in circulation and I could not reconcile them:
`sgit.ai` publishes `f94c8b1d…e111118:4evnlwrj` (64 hex, and it works — it is what I read the
vault with); the link in the request is `t6u4ev…zpgb5:4evnlwrj`, a 24-character
form I have not seen documented. Same vault, different shape. **Tell us which one to publish**
— if the short one is a newer or rotated read key we should print that, and if the 64-hex one
is being retired the sgit.ai page needs updating too.

Both are elided above, and the short one deliberately so: **on shape alone it matches the
documented *vault* key form**, `<passphrase>:<vault-id>` — the one `sgit init` prints with
*"saved to a password manager. Not printed here, not ever."* A read key on this network is 64
hex, optionally `sgit_rk1_`-prefixed. Until somebody confirms which it is, it is treated as
sensitive. **If it is a vault key, rotate it**: it has been pasted into at least one chat and
one link, and this branch briefly carried it in full before the redaction.

### One thing the embed needs from the game

Events carry which surface the game was played on — `vault-app`, `web`, `local` (v0.12.4).
**An embed on a public site is a fourth surface**, and it is the one we will most want to
segment: play from `what-can-it-do.games.sgit.ai` is play by strangers, and play from the
vault host is mostly us. Under Option A the hostname inside the frame is the vault host's, so
the existing detection cannot tell them apart. Proposal: the embed host passes an origin hint
the game records — or the game reads `document.referrer` / an `?on=` parameter. **Your call on
the mechanism; the ask is that the two are distinguishable.**

---

## 5. Build and release — the house pattern, unchanged

Both sites follow the pattern that `pki`, `graphs` and `wardley-maps` share. No invention here;
copying it is the point, because it is what stops these sites drifting.

- **Hand-written static HTML with programmatically injected chrome.** `admin/build/chrome.py`
  is the single definition of the nav, footer, favicon and version badge, rewritten in place
  across the tree. A human can still open any file and edit it.
- **`admin/build/version.txt` owns the version.** Every page carries the badge; CI enforces
  that they agree.
- **`admin/build/validate.js` is the gate**, with the four house checks: version agreement;
  every internal link resolves; every `canonical` and `og:url` matches `CNAME`; and the
  **key-leak tripwire** — nothing in the tree may look like an sgit vault key. That last one
  is load-bearing here, because these two sites publish a read key on purpose and the tripwire
  is what keeps a *vault* key from following it. It will need the published read key
  allow-listed explicitly, the same way sgit.ai allow-lists its demo vaults.
- **`.github/workflows/deploy-pages.yml`: validate → tag → deploy** on push to `dev`; PRs run
  validation only. Every push to `dev` is a minor release and ends tagged, with the version
  in the commit subject (`site vX.Y.Z: …`) checked against `version.txt`.
- **`CNAME`, `index.md` twin, `llms.txt`, `llms-full.txt`, `sitemap.xml`, `robots.txt`.**
  Every page gets a `.md` twin generated from the same content, so the two cannot drift.

Two site-specific gate checks I propose adding:

6. **Every embed carries a disclosure.** Any page containing a `.sgv-embed` / `.sgv-uiembed`
   mount must also contain the telemetry notice element. Mechanical, and it is exactly the
   failure the sgit.ai finding recorded.
7. **The maturity label is from the ladder.** Every catalogue card's label must be one of the
   five rungs in `/maturity/`, so a card cannot invent a status.

---

## 6. Where these sites sit in the network

`sgit.ai/network/` lists 19 sites and registers each with a category, a one-line "start from
what you need" entry, and a card. Registering these two is part of the work, not an
afterthought:

- **`games.sgit.ai`**, under *Agents & AI* — *"I want to find out what people actually believe
  their agent can do"*.
- **`what-can-it-do.games.sgit.ai`** — the first **fourth-level** domain in the family, and
  the first site whose primary audience is not a practitioner. That is a precedent worth
  stating once on `games.sgit.ai`: **a game gets its own domain when it is meant to be shared,
  and the domain is the game's name so the link explains itself.** If more games reach
  *measured*, they get `<name>.games.sgit.ai` on the same rule.

Inbound links to add: from the sgit.ai `/demos/vaults/agent-permission-games/` page (→ both
sites), and from `pki.sgit.ai` (the mesh, profiles and reductions the games run on).

---

## 7. What I am deliberately not doing

- **Not forking the game into the repos.** The game lives in the vault; the sites embed it.
  Two copies would drift within a week, and "no copy of the app exists on sgit.ai" is a claim
  the network already makes and should keep making.
- **Not building a second telemetry lane.** These sites send nothing of their own. Everything
  measured is measured by the game, on the lanes it already has.
- **Not writing new game content, rules or questions.** That is yours. If the sites need a
  screenshot or a phrase you would put differently, that is a request to you, not an edit by us.
- **Not touching `sgit.ai/demos/vaults/agent-permission-games/`** beyond adding the two
  outbound links — though somebody should refresh it, since it describes v0.8.1 and the vault
  is at v0.16.1.

---

## 8. Sequence

| # | Step | Blocked on |
|---|---|---|
| 1 | Confirm which read key to publish; confirm the §1 facts | **you** |
| 2 | Scaffold both repos from the house pattern (chrome, validate, CI, CNAME) | — |
| 3 | Add `data-browser="0"` app-only mode to a local copy of the UI embed; verify the chat panel and a telemetry event both survive the embed on a Pages origin | step 1 |
| 4 | Build `what-can-it-do.games.sgit.ai` — front page, four pages, disclosure above the fold | steps 2–3 |
| 5 | Build `games.sgit.ai` — argument, catalogue, method, build, maturity, telemetry | step 2 |
| 6 | Surface labelling so embed play is distinguishable from vault-host play | **you** |
| 7 | Register both in `sgit.ai/network/`; add inbound links | steps 4–5 |
| 8 | Screenshots of both, captured with telemetry blocked at the network layer | steps 4–5 |

Steps 4 and 5 are independent and can run in parallel. Step 8 copies the practice already
recorded on the sgit.ai page: driving the games to photograph them must not put a synthetic run
into a real lane.

---

## 9. Questions for review

1. **§1 — is any of it wrong?** I read your vault instead of asking you; I would rather be
   corrected than accurate by luck.
2. **§4 — Option A for the player site: agreed?** It costs chrome and buys the chat panel and
   a working append lane. If you would rather have the clean minimal frame and lose
   `sg.llm.chat` on that domain, say so and the plan changes.
3. **§4 — which credential do we publish?** The 64-hex key, the 24-character one, or both?
4. **§4 — surface labelling.** Do you want to detect the embed, or should the host tell you?
5. **§2 — the maturity ladder.** Are the five rungs the right ones, and is *What Can It Do?*
   at **scored** or already at **measured**? If a release changed because play data said so,
   name it and it moves.
6. **§3 — the disclosure.** Notice outside the frame as well as inside, or would two pause
   switches be worse than one? You have thought about this longer than we have.
7. **Does the player site oversell?** "Do you know what your agent can actually do?" is a
   sharper claim than "we measure your calibration against a published profile, which is the
   weakest tier there is". Your own *does-not-prove* list is unusually honest and I do not
   want a landing page to undo it. Where is the line?
8. **RiskMandate.ai** — the mandate draft the game hands a player is the same object
   RiskMandate.ai is about. Should `games.sgit.ai` say where that goes next, or is that
   ahead of what exists?

---

*This plan is CC BY 4.0, like the vault it describes. Any part of it can be argued with; the
parts sourced from vault files name the file so the argument has somewhere to start.*
