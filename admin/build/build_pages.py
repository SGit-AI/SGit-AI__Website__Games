#!/usr/bin/env python3
"""games.sgit.ai — every page, as content. Run: python3 admin/build/build_pages.py

The nav, the footer and each page's blocks are defined once here and rendered to HTML and to
markdown by `shell.py`. Nothing under the site root is hand-edited: edit this file, run it,
then run `node admin/build/validate.js` before committing.

Release: bump VERSION, add a VERSION_LOG row, rebuild, validate, then
`git commit -am "site vX.Y.Z: ..." && git push origin dev`. CI checks version.txt against the
commit subject and tags the release.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shell  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()

# The games vault, read-only. This credential is PUBLISHED ON PURPOSE — it is what lets a
# reader open the vault, clone it, and check every claim on this site against the files. It
# cannot write. It is the same key sgit.ai publishes at /demos/vaults/agent-permission-games/.
# The vault key is not published and never will be; validate.js fails the build on anything
# shaped like one that is not on its allow-list.
VAULT = "4evnlwrj"
READKEY = "f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118"
VAULT_UI = f"https://dev.vault.sgraph.ai/#{READKEY}%3A{VAULT}"
PLAYER_SITE = "https://what-can-it-do.games.sgit.ai"

# RiskMandate — the project these games are part of, and the layer that starts where they
# stop. The games get a person to state their half of the mandate; RiskMandate turns the gap
# into a named owner and a time-bound decision. Deep links, so a nudge lands on the page that
# answers the question the game just raised.
RM = "https://riskmandate.ai"
RM_GRANT = "https://riskmandate.ai/v0/v0.11/v0.11.0/index.html"
RM_ACCEPT = "https://riskmandate.ai/v0/v0.10/v0.10.0/index.html"
RM_SCENARIOS = "https://riskmandate.ai/scenarios.html"
RM_HOW = "https://riskmandate.ai/how-it-works.html"
RM_LIBRARY = "https://riskmandate.ai/library.html"

# Licence to Operate — a published vault, read-only: one agent, a grant of 12 capabilities, a
# mandate of 4, and the 8-capability delta no policy covers, with every reply priced against a
# live policy. Not a game — no belief is stated before an answer — which is exactly why it
# earns a place on the grant-vs-mandate page rather than in the catalogue.
LTO_VAULT = "posrhzp3"
LTO_READKEY = "d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29"
LTO_UI = f"https://dev.vault.sgraph.ai/#{LTO_READKEY}%3A{LTO_VAULT}"
LTO_PAGE = "https://sgit.ai/demos/vaults/licence-to-operate/index.html"

SITE = {
    "host": "games.sgit.ai",
    "brand": ("games", ".sgit.ai"),
    "stage": "research site",
    "github": "https://github.com/SGit-AI/SGit-AI__Website__Games",
    "parent": "https://sgit.ai",
    "parent_label": "sgit.ai",
    "parent_title": "sgit.ai — the parent project: the vault layer the games ship in",
    "tagline": "A game is the only artefact that makes somebody state a belief before they "
               "are told the answer.",
    "blurb": 'Why this family builds games, and the games it has. Each one ships as an '
             'encrypted vault you can open, clone and argue with — '
             '<a href="{up}maturity/index.html" style="display:inline;padding:0">every one '
             'carries a maturity label with a test behind it</a>.',
    "netline": ('<a href="https://riskmandate.ai"><b>↗ RiskMandate.ai</b></a> — the business '
                'risk layer these games are part of · '
                '<a href="https://sgit.ai">↗ sgit.ai</a> — the vault layer the games '
                'ship in · <a href="https://pki.sgit.ai">↗ pki.sgit.ai</a> — the mesh and '
                'the profiles the questions come from · '
                f'<a href="{PLAYER_SITE}">↗ what-can-it-do.games.sgit.ai</a> — play the first '
                'game · <a href="https://sgit.ai/network/index.html">↗ the network</a>'),
    "telemetry_note": 'The games count usage anonymously while you play — no cookies, no '
                      'analytics script, nothing that identifies you. '
                      '<a href="{up}telemetry/index.html" style="display:inline;padding:0">'
                      'What is sent, and how to stop it</a>.',
}

NAV = [
    ("Games", "games/index.html", [
        ("The catalogue", "games/index.html"),
        ("What Can It Do?", "games/what-can-it-do.html"),
        ("Which Agent Is It?", "games/which-agent-is-it.html"),
        ("Ideas &amp; feedback", "games/ideas.html"),
    ], ("games/",)),
    ("Method", "method/index.html", [
        ("The four claims", "method/index.html"),
        ("Calibration, not knowledge", "method/calibration.html"),
        ("The ceiling", "method/the-ceiling.html"),
        ("Levels are distance", "method/levels.html"),
        ("Grant vs. mandate", "method/grant-vs-mandate.html"),
    ], ("method/",)),
    ("Maturity", "maturity/index.html", [], ("maturity/",)),
    ("Build one", "build/index.html", [
        ("Building a game as a vault", "build/index.html"),
        ("What our games send", "telemetry/index.html"),
    ], ("build/", "telemetry/")),
    ("Site", "admin/index.html", [
        ("The network", "network/index.html"),
        ("Release history", "admin/versions.html"),
        ("Admin &amp; engineering", "admin/index.html"),
    ], ("admin/", "network/")),
]

FOOTER = [
    ("Play", [
        ("&#8594; What Can It Do?", PLAYER_SITE),
        ("The catalogue", "games/index.html"),
        ("Which Agent Is It?", "games/which-agent-is-it.html"),
        ("Ideas &amp; feedback", "games/ideas.html"),
    ]),
    ("The method", [
        ("Calibration, not knowledge", "method/calibration.html"),
        ("The ceiling", "method/the-ceiling.html"),
        ("Levels are distance", "method/levels.html"),
        ("Grant vs. mandate", "method/grant-vs-mandate.html"),
    ]),
    ("Build one", [
        ("Building a game as a vault", "build/index.html"),
        ("What our games send", "telemetry/index.html"),
        ("The maturity ladder", "maturity/index.html"),
    ]),
    ("Site", [
        ("The network", "network/index.html"),
        ("Release history", "admin/versions.html"),
        ("Engineering", "admin/index.html"),
        ("llms.txt", "llms.txt"),
    ]),
]

VERSION_LOG = [
    ("v0.3.0", "2026-09-09",
     "This site goes back to being the generic one. It points at the games; the material "
     "specific to any single game belongs with that game. So the Licence to Operate embed and "
     "the long RiskMandate exposition move to what-can-it-do.games.sgit.ai, where a reader who "
     "has just played that game actually wants them, and grant vs. mandate keeps the method "
     "claim and links across. The telemetry notice also moves off the top of the front page to "
     "the foot of it: what it describes is less than a default web-server access log, and a "
     "notice a reader has to step over to reach the game treats something ordinary as an "
     "obstacle. Also fixes the nav, which prefixed the page's up-path to absolute hrefs and so "
     "emitted ../https://… for any off-site menu entry — the footer had always handled that "
     "and the nav had not; the link check caught it the moment one was added."),
    ("v0.2.0", "2026-09-09",
     "These games are part of RiskMandate, and the site now says so and shows where the join "
     "is. RiskMandate is the business risk layer for autonomous systems — it begins where "
     "security stops, its unit is the mandate (the right to act, granted by a named owner, "
     "scoped, time-bound rather than standing), and its signature mechanic is that a real risk "
     "has no deny button: the agent already has the access, so it can only be accepted, in a "
     "direction, for an interval, by somebody named, and underwritten upward. The games are "
     "the front end of one part of that — the bit that gets a real person to state what they "
     "wanted. Grant vs. mandate was rewritten around that model and now says plainly what is "
     "NOT built: the mandate draft exports into nothing, and the handover is a person "
     "retyping. Also embeds Licence to Operate, the published vault holding one agent's grant "
     "of 12, mandate of 4 and the 8-capability delta no policy covers, with every reply priced "
     "— the best worked example in this family, kept out of the catalogue because it is a "
     "simulation rather than a game and blurring that would cost the site its one distinction."),
    ("v0.1.1", "2026-09-09",
     "The telemetry notice got proportionate. It was an amber warning panel, which was the "
     "wrong size for what it says: anonymous counting with no cookies, no analytics script and "
     "nothing that identifies anyone is LESS than a default web-server access log and far less "
     "than the analytics on almost every site a reader will visit today. Dressing that as a "
     "hazard implies a risk that is not there, and a page that over-warns about something "
     "ordinary teaches people to skim the next notice. It is now one quiet line in the reading "
     "column, still before the thing it describes and still enforced by the release gate. The "
     "telemetry page states the comparison outright rather than leaving the reader to guess "
     "the scale, and says why the notice exists at all: not because the counting is invasive, "
     "but because a vault sending anything departs from a platform promise, and departures get "
     "stated."),
    ("v0.1.0", "2026-09-08",
     "First publish. The argument (a game is the only artefact that makes somebody state a "
     "belief before they are told the answer), the catalogue with a five-rung maturity ladder "
     "that has a test behind every rung, four method pages, the build guide, the telemetry "
     "page, and the network entry. The games are embedded rather than copied: the vault is "
     "the source, and assets/vault-app-embed.js opens it over the SG/Vault embed protocol "
     "with the vault-browser surface suppressed."),
]

# The one credential line, written once and reused, so the wording of how it is published
# cannot drift between pages.
KEY_NOTE = (f"**Open it yourself.** Read key `{READKEY[:12]}…{READKEY[-6:]}:{VAULT}` — the full "
            f"string is on [the vault's page at sgit.ai]"
            f"(https://sgit.ai/demos/vaults/agent-permission-games/). "
            f"[Open it read-only in a new tab]({VAULT_UI}), or clone it with `sgit clone`. "
            f"It is a read key: it cannot write, which is what makes publishing it safe.")

DISCLOSE = (
    "The games count usage anonymously while you play — which screens people reach, which "
    "answers are common. No cookies, no analytics script, no id, nothing that identifies you, "
    "and a pause switch on every screen. [What is sent, and why a vault doing it at all is "
    "unusual](/telemetry/index.html).")


def versions_table():
    rows = "".join(
        f'<tr><td class="vnum">{v}</td><td>{d}</td><td>{shell.inline_html(n)}</td></tr>'
        for v, d, n in VERSION_LOG)
    return ('<div class="tablewrap"><table><thead><tr><th>Version</th><th>Date</th>'
            f"<th>What changed</th></tr></thead><tbody>{rows}</tbody></table></div>")


PAGES = {
# ---------------------------------------------------------------------------
"index.html": {
  "title": "games.sgit.ai — a game makes you say what you think, before you are told",
  "description": "Why this family builds games: a game is the only artefact that makes "
                 "somebody state a belief before they are told the answer. The catalogue, "
                 "the method, and how to build one as a vault.",
  "blocks": [
    ("h1", "A game makes you say what you think — before you are told"),
    ("lead", "Everything else we publish can be nodded at. A graph, a standard, a report, a "
             "map: you read it, you agree, and neither of us learns whether you already knew. "
             "A game does not allow that. It makes you commit to an answer first, and the gap "
             "between what you said and what is true is data that could not have been "
             "collected any other way."),
    ("p", "That is the argument this site exists to make, and it is falsifiable: if play data "
          "shows people are as well calibrated as they think they are, the games measured "
          "nothing worth measuring. We publish the scores, so you will be able to tell."),
    ("h2", "The subject is what your agent can actually do"),
    ("p", "The first games ask one question in two directions. You have given an AI agent "
          "access to something — a machine, a repository, a mailbox, a cloud account. **Can it "
          "do X?** And, separately, **do you want it to?** Answer that forty times and you "
          "have written a draft mandate without meaning to, and the delta between what the "
          "agent can do and what you wanted it to do is the thing nobody has written down."),
    ("p", f"That delta is the whole subject of [**RiskMandate**]({RM}) — *the business risk "
          f"layer for autonomous systems* — which is the project these games are part of. "
          f"RiskMandate governs the right to act: what an agent may do, granted by whom, for "
          f"how long. A form would ask you for your half of that and you would answer "
          f"aspirationally. A game gets it out of you as a by-product of playing."),
    ("p", f"What happens to a delta once you have one is RiskMandate's answer rather than "
          f"this site's, and the game that produces one carries it: "
          f"[what to do next]({PLAYER_SITE}/what-next/index.html). Here, the relevant question "
          f"is the narrower one — [why a game gets it out of you at all]"
          f"(method/grant-vs-mandate.html)."),
    ("h2", "Play the first one"),
    ("embed", {"vault": VAULT, "readkey": READKEY, "open_url": VAULT_UI, "breakout": True,
               "label": "What Can It Do?, running out of the vault"}),
    ("p", f"That is the real game, running out of the encrypted vault it is published in — no "
          f"copy of it exists on this site. It has its own player-facing home at "
          f"[what-can-it-do.games.sgit.ai]({PLAYER_SITE}), which is the link to send someone "
          f"who just wants to play. This page is for the reader who wants to know why it "
          f"exists."),
    ("h2", "The games"),
    ("cards", [
      {"title": "What Can It Do? — the scoreboard",
       "sub": "Name your agent and where you run it. The board asks, capability by "
              "capability, *can it?* and *do you want it to?* You score for calibration, not "
              "for knowledge, and the end screen hands you the mandate you assembled without "
              "meaning to.",
       "foot": "{{rung:scored}} · [what it measures](games/what-can-it-do.html) · "
               f"[play it]({PLAYER_SITE})"},
      {"title": "Which Agent Is It? — the floor plan",
       "sub": "Think of an agent. Cheap questions narrow the field while you chalk which "
              "wings of the building you think it can enter. Then the doors open and the "
              "prediction gap is shown per capability.",
       "foot": "{{rung:playable}} · [what it measures](games/which-agent-is-it.html)"},
      {"title": "Ideas & feedback — the reply channel",
       "sub": "Not a game: the thing that turns one into a conversation. What players argue "
              "with becomes ideas, grouped into themes, answered with a published position — "
              "as a graph, in the same shape as the mesh the questions come from.",
       "foot": "{{rung:answered}} · [how it works](games/ideas.html)"},
    ]),
    ("h2", "Why a maturity label on every one"),
    ("p", "Games arrive half-built and stay that way for a while, and a catalogue that hides "
          "that is a catalogue nobody can use. Every game here carries one of five rungs, and "
          "**each rung has a test that moves it up** rather than a feeling: *playable* means a "
          "stranger finished a run without being told how; *measured* means a release note "
          "cites play data. [The ladder](maturity/index.html), stated once so a label means "
          "the same thing on every card."),
    ("h2", "What this site does not claim"),
    ("ul", [
      "**That a good score is safety.** Calibration is a property of the player, not of the "
      "environment they are describing. Somebody perfectly calibrated about a badly configured "
      "agent is still running a badly configured agent.",
      "**That the board is right about your setup.** Both games measure you against a "
      "*published profile* — what a vendor says a product does — which is the weakest tier of "
      "evidence there is. It is not an audit of your deployment and never claims to be.",
      "**That the points mean anything yet.** The values and cut-points are arbitrary until "
      "there is enough play data to fit them. That is stated inside the game too.",
      "**That the mandate is a mandate.** It is what one person said while playing, badged in "
      "the game itself as *a draft you wrote while playing*.",
    ]),
    ("note", "Everything on this site is checkable, because the games are published as a vault "
             "rather than described. " + KEY_NOTE),
    # Foot of the page, not between the reader and the game. See the note in the player site's
    # build_pages.py: this is anonymous counting, less than a default server log, and a notice
    # placed where you have to step over it treats an ordinary thing as an obstacle.
    ("disclose", DISCLOSE),
  ]},
# ---------------------------------------------------------------------------
"games/index.html": {
  "title": "The catalogue",
  "description": "Every game this family has published, with a maturity rung that has a test "
                 "behind it, and the vault each one ships in.",
  "blocks": [
    ("crumb", "[Home](index.html) / The catalogue"),
    ("h1", "The catalogue"),
    ("lead", "Three things in one vault, at three different stages. Nothing here is finished, "
             "and the rung on each card says how far off it is."),
    ("table",
     ["What", "Rung", "What it measures", "Where"],
     [["[What Can It Do?](games/what-can-it-do.html)", "{{rung:scored}}",
       "Whether you can predict what your agent can do — scored for calibration, in both "
       "directions",
       f"[play]({PLAYER_SITE})"],
      ["[Which Agent Is It?](games/which-agent-is-it.html)", "{{rung:playable}}",
       "Whether a handful of cheap questions can identify an agent, and how wrong your picture "
       "of its reach was",
       f"[open]({VAULT_UI})"],
      ["[Ideas & feedback](games/ideas.html)", "{{rung:answered}}",
       "Not a game — the reply channel: what players argue with, and the position taken on it",
       f"[open]({VAULT_UI})"]]),
    ("h2", "All three are one vault"),
    ("p", f"Vault `{VAULT}`, published under the name *Two games about what your agent can "
          f"do*, at **v0.16.1** — 81 files across 28 releases at the time this page was "
          f"written. The vault auto-opens the scoreboard; a menu on every page reaches the "
          f"other two and the release history."),
    ("p", "Publishing them as one vault rather than three sites is deliberate: they share a "
          "data snapshot, the same nine public profiles, and the same telemetry lane, and a "
          "player who finishes the floor plan is handed straight to the scoreboard with the "
          "matched profile already filled in. Splitting them would break that handover and "
          "give three copies of the data to drift apart."),
    ("note", KEY_NOTE),
    ("h2", "What is in the vault besides the games"),
    ("ul", [
      "`what-can-it-do/source/` and `which-agent-is-it/source/` — each game's readable source: "
      "the engine as an ES module, `selftest.json`, the vendored data snapshot, the build "
      "script, and a README carrying a rules table and a *does-not-prove* list.",
      "`telemetry.html`, `telemetry.js`, `telemetry.config.json` — what the games send and the "
      "two write-only lanes they send it on. [Our page on it](telemetry/index.html).",
      "`ideas/` — the reply channel: `ontology.json`, `ideas.json`, `signals.json`, and the "
      "`graph.json` compiled from them.",
      "`version.json` and `version.html` — the badge on every page and the release history "
      "behind it.",
    ]),
    ("h2", "Adjacent, and deliberately not listed above"),
    ("p", f"**Licence to Operate** ([open it]({LTO_UI}) · [write-up]({LTO_PAGE})) is a published "
          f"vault holding one agent's grant of 12 capabilities, its mandate of 4, and the "
          f"8-capability delta no policy covers — with every reply priced against a live "
          f"policy. It is the best demonstration in this family of what the games are pointing "
          f"at, and it is **not a game**: it never makes you commit to a belief before showing "
          f"you the answer. Listing it above would blur the one distinction this site is built "
          f"on. It is embedded on the player site instead, beside the game whose output it "
          f"prices: [what-can-it-do.games.sgit.ai/licence-to-operate]"
          f"({PLAYER_SITE}/licence-to-operate/index.html)."),
    ("h2", "Coming, and deliberately not built yet"),
    ("p", "The game authors' own *next* list is short and honest: fit the point values from "
          "play data, show a returning player their previous calibration, export the mandate "
          "draft into the probes' shape, and put a model at the game's three edges — free text "
          "for an unlisted setup, question generation, narration. **None built, on purpose.** "
          "A game that generates its own questions cannot be self-tested against a reference, "
          "and the self-test is what makes the score arguable."),
  ]},
# ---------------------------------------------------------------------------
"games/what-can-it-do.html": {
  "title": "What Can It Do? — the scoreboard",
  "description": "The scoreboard game: 40 questions, five levels, scored with a proper "
                 "scoring rule so that saying yes to everything loses. 17 of the 40 are "
                 "things no agent can do.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Games](games/index.html) / What Can It Do?"),
    ("h1", "What Can It Do? — the scoreboard"),
    ("lead", "You name the agent and where you run it. The board then asks, capability by "
             "capability, two questions back to back: **can it?** and **do you want it to?** "
             "The first is scored. The second quietly assembles a mandate."),
    ("p", f"[Play it at what-can-it-do.games.sgit.ai]({PLAYER_SITE}) — that is the "
          f"player-facing site, and the link to send to somebody who just wants to play. This "
          f"page is about how it works and what it is measuring."),
    ("h2", "Three marks, kept apart everywhere"),
    ("p", "The design decision the whole game rests on is that three different things are "
          "never drawn the same way: **your ink** (what you said), **the board's stamp** (what "
          "the profile says), and **the mandate mark** (what you wanted). Most assessment "
          "tools collapse the second and third — they ask what you want and then tell you "
          "whether you are compliant. Keeping them apart is what makes the delta visible."),
    ("h2", "The scoring, stated before you play"),
    ("table", ["You answer", "Scored as", "If right", "If wrong"],
     [["Yes", "0.75 confident", "+30", "−50"],
      ["No", "0.25 confident", "+30", "−50"],
      ["Don't know", "0.5", "0", "0"]]),
    ("p", "Under the hood that is a proper scoring rule — squared error, shifted so that *not "
          "sure* is worth nothing: `points = 160 × (¼ − (p − truth)²)`. The property that "
          "matters is that **a wrong answer costs more than a right one earns**, which is the "
          "only way to stop the winning strategy being *say yes to everything*. Real grants "
          "are wider than people expect, so yes-to-everything would otherwise score well while "
          "measuring nothing. The game's own self-test asserts it: answering *yes, definitely* "
          "to every question scores between −3,840 and −8,640 across the profiles in the set, "
          "against +3,840 for perfect knowledge."),
    ("p", "There is no forced guess. *Don't know* is always available and always worth zero — "
          "the headline figure the game reports is calibration, not score, and a player who "
          "knows what they do not know should not be punished for saying so."),
    ("h2", "The mandate points are a second, separate currency"),
    ("p", "After you answer *can it?*, a **but…** tick appears — *…but it shouldn't be able "
          "to* under a yes, *…but I'd want it to* under a no. Ticking it is worth ±20 mandate "
          "points, kept apart from the calibration points and reported separately: **+20 for "
          "flagging a real delta, −20 for flagging one that is not there.**"),
    ("p", "Every answer is then classed. The four delta classes are named in plain words, and "
          "the distinction inside each pair is the useful one:"),
    ("table", ["Class", "Means"],
     [["excess you flagged", "It can, you don't want it to — and you knew"],
      ["excess you did not see", "It can, you don't want it to — and you also had the grant wrong"],
      ["gap you knew of", "It cannot, you would want it to — and you knew"],
      ["gap you were counting on",
       "It cannot, you thought it could, and you wanted it — something you are relying on that "
       "is not there"]]),
    ("p", "That last row is the one worth the whole game. It is the only class that describes "
          "a thing you are currently depending on which does not exist."),
    ("h2", "The set spans both directions"),
    ("p", "**17 of the 40 questions are above the ceiling** — things no agent in any "
          "environment in the set can do, not even one running as an administrator with every "
          "confirmation switched off. They are there so the game measures over-crediting as "
          "well as underestimating, and the game's self-test fails if their share leaves the "
          "33–50% band. [Why the ceiling exists, and what bounds it](method/the-ceiling.html)."),
    ("h2", "What it does not prove"),
    ("ul", [
      "**Anything about your grant.** It measures you against a published profile — what a "
      "vendor says a product does — which is the weakest tier of evidence there is.",
      "**That the levels are right.** The derived ones come from a mesh snapshot that records "
      "no path at all for one capability; the above-the-ceiling ones are authored by one agent "
      "on one day, and each says so in the file.",
      "**That the points mean anything.** Values and cut-points are arbitrary until there is "
      "play data to fit them against.",
      "**That a good score is safety.** Calibration is about the player, not the environment.",
    ]),
    ("note", KEY_NOTE),
  ]},
# ---------------------------------------------------------------------------
"games/which-agent-is-it.html": {
  "title": "Which Agent Is It? — the floor plan",
  "description": "The floor-plan game: think of an agent, answer cheap questions, chalk which "
                 "wings of the building you think it can enter — then the doors open.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Games](games/index.html) / Which Agent Is It?"),
    ("h1", "Which Agent Is It? — the floor plan"),
    ("lead", "Think of an agent. A handful of cheap questions narrow the field while you chalk "
             "which wings of the building you believe it can enter. Then the doors open, and "
             "the prediction gap is shown capability by capability."),
    ("h2", "The board is the interesting part"),
    ("p", "Capabilities are drawn as rooms grouped into wings — filesystem, identity, process, "
          "code, network, communication, schedule, money, browser — and the legend keeps four "
          "states apart: **chalk** (asserted, you drew it), **pencil hatching** (inferred, the "
          "plan says so), **dotted** (possible, still consistent with what you have answered) "
          "and plain (no visitor above 5% likelihood holds a key). A belief column ranks the "
          "nine public profiles by likelihood, live, as you answer."),
    ("p", "The game is careful about what a drawing is, and says so on the board: *\"a room is "
          "a rendering choice, not a place — rooms are not ordered, sized or adjacent by "
          "anything in the data.\"* That sentence is doing real work. A floor plan invites you "
          "to read adjacency as meaning, and there is no adjacency in the underlying graph."),
    ("h2", "The question that measures nothing"),
    ("p", "Mid-game there is a question labelled `IDENTIFIES` which the board says *\"identifies "
          "and measures nothing\"*, and it never counts toward the prediction gap. It is there "
          "to narrow the belief column — to work out *which* agent you are thinking of — and "
          "keeping it out of the score is the honest thing to do: you should not lose points "
          "for a question asked to help the game, not to test you."),
    ("h2", "It hands you to the scoreboard"),
    ("p", f"The reveal screen links into [What Can It Do?](games/what-can-it-do.html) with the "
          f"matched profile already handed over, so the second game starts where the first "
          f"ended rather than asking you to name your agent again. It is the reason the two "
          f"ship in one vault."),
    ("p", "**Rung: `playable`.** It scores, and its engine is self-tested against a reference, "
          "but it has had far less play than the scoreboard and its reveal has not been "
          "reworked since the scoreboard's results page was. "
          "[What the rungs mean](maturity/index.html)."),
    ("note", KEY_NOTE),
  ]},
# ---------------------------------------------------------------------------
"games/ideas.html": {
  "title": "Ideas & feedback — the reply channel",
  "description": "What players argue with becomes ideas, grouped into themes and answered with "
                 "a published position — as a graph, joined to the mesh the questions come "
                 "from, naming nobody.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Games](games/index.html) / Ideas & feedback"),
    ("h1", "The reply channel — and why it is a graph"),
    ("lead", "A game that collects disagreement and never answers it is a survey. The thing "
             "that turns these games into a conversation is the third app in the vault: what "
             "players argue with, turned into ideas, grouped into themes, and answered with a "
             "position that is published rather than filed."),
    ("h2", "The answer comes back to where the argument happened"),
    ("p", "The by-product that matters most is `answers.json` — capability id to the position "
          "taken on it. The game inlines it at build time, so **a question somebody argued "
          "with now carries the answer**, folded above its 👍/👎. You disagree with a row, and "
          "the next player to reach that row sees what we said about it."),
    ("p", "That is a deliberately unaddressed reply. Answering the person who complained would "
          "require knowing who they were, and that is the option that costs privacy rather "
          "than the one that gains capability. Keying the answer to the question instead "
          "reaches everyone who cares about it and identifies nobody."),
    ("h2", "Published as a graph, under the mesh's own rules"),
    ("p", "The graph is compiled from three files by a builder that **refuses an edge whose "
          "type is not in the ontology, or whose ends are of the wrong type** — the same rule "
          "the mesh at [pki.sgit.ai](https://pki.sgit.ai) is built under. Node types are "
          "`idea`, `theme`, `signal`, `capability`, `decision` and `release`."),
    ("table", ["File", "What", "Written by"],
     [["`ontology.json`", "the taxonomy: node types, edge types, their direction and meaning", "hand"],
      ["`ideas.json`", "the authored half — ideas, themes, and the positions taken", "hand"],
      ["`signals.json`", "the received half — one entry per drained feedback record",
       "a person reading the feedback"]]),
    ("p", "**Capability ids are the mesh's own** (`capability:read.file.host`), so this graph "
          "joins onto that one with no mapping in between. That is the payoff of writing both "
          "under the same grammar: an argument about a question is attached to the same node "
          "the question was generated from."),
    ("h2", "What is deliberately not in it"),
    ("ul", [
      "**No player is named.** There are no person nodes and no identifiers of any kind.",
      "**Nobody's words are quoted** unless a quote was deliberately filled in on that signal. "
      "Paraphrase is the default, because quoting somebody back in a public file is a "
      "disclosure they did not choose to make.",
      "**The raw feedback stays in the private telemetry vault.** What is published is the "
      "reading of it.",
    ]),
    ("p", "Every row is arguable, which is the point of publishing a graph rather than a "
          "summary. [What is sent when you press 👍 or 👎](telemetry/index.html)."),
  ]},
# ---------------------------------------------------------------------------
"method/index.html": {
  "title": "The method — four claims",
  "description": "Four claims about how to build a game that measures something: score "
                 "calibration not knowledge, put a ceiling in the set, derive levels from a "
                 "graph, and treat the mandate as a by-product.",
  "blocks": [
    ("crumb", "[Home](index.html) / Method"),
    ("h1", "Four claims"),
    ("lead", "Each of these is a decision that could have gone the other way, and each names "
             "what would show it was wrong. They are the transferable part: nothing here is "
             "specific to agents, and all four apply to any game meant to measure a belief."),
    ("cards", [
      {"title": "1 — Score calibration, not knowledge",
       "sub": "A proper scoring rule, with a wrong answer costing more than a right one earns, "
              "and *don't know* always available and always worth zero.",
       "foot": "[The argument](method/calibration.html)"},
      {"title": "2 — Put a ceiling in the question set",
       "sub": "If every question has a real answer, the only error the game can measure is "
              "underestimating. Two fifths of these are things nothing can do.",
       "foot": "[The argument](method/the-ceiling.html)"},
      {"title": "3 — Derive levels from the graph, not from vibes",
       "sub": "A level is the number of hops to a one-way consequence, computed from the mesh "
              "— and it is distance, never a danger rating.",
       "foot": "[The argument](method/levels.html)"},
      {"title": "4 — Make the mandate a by-product",
       "sub": "Nobody fills in a mandate form honestly. Ask *do you want it to?* forty times "
              "and one falls out of the play.",
       "foot": "[The argument](method/grant-vs-mandate.html)"},
    ]),
    ("h2", "What they have in common"),
    ("p", "All four are ways of stopping a game from measuring the wrong thing while looking "
          "like it is working. A quiz with no ceiling, no scoring rule and hand-assigned "
          "levels still produces a number, still feels informative, and tells you nothing you "
          "did not put in. The four claims are what make the number arguable — and each one "
          "has a self-test in the vault that fails the build if it stops holding."),
  ]},
# ---------------------------------------------------------------------------
"method/calibration.html": {
  "title": "Calibration, not knowledge",
  "description": "Why the scoreboard scores how well you know what you know, with a proper "
                 "scoring rule that makes saying yes to everything a losing strategy.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Method](method/index.html) / Calibration"),
    ("h1", "Score calibration, not knowledge"),
    ("lead", "A quiz about agent capabilities would measure whether you have read the release "
             "notes. That is not the interesting question. The interesting question is whether "
             "the confidence you already act on is warranted."),
    ("h2", "The failure this avoids"),
    ("p", "Score bare accuracy and the game has a dominant strategy: **say yes to everything**. "
          "Real grants are wider than people expect, so a blanket yes scores well — and a "
          "player who wins that way has learned nothing and demonstrated nothing. Every "
          "capability quiz that scores one point per right answer has this hole."),
    ("h2", "The rule"),
    ("pre", "points = 160 x (1/4 - (p - truth)^2)\n\n"
            "  yes         -> p = 0.75\n"
            "  don't know  -> p = 0.5\n"
            "  no          -> p = 0.25\n\n"
            "  right       -> +30\n"
            "  wrong       -> -50\n"
            "  don't know  ->   0"),
    ("p", "This is the squared-error (Brier) rule, shifted so that the midpoint scores zero. "
          "Two properties follow, and both are load-bearing. It is **proper**: your best "
          "strategy is to report what you actually believe, because any other report lowers "
          "your expected score. And it is **asymmetric in the way that matters**: −50 against "
          "+30 means confident-and-wrong costs nearly twice what confident-and-right earns, so "
          "blanket confidence loses."),
    ("h2", "How we know it holds"),
    ("p", "It is asserted, not hoped for. The game's `selftest.json` plays *yes, definitely* to "
          "every question against every profile in the set and requires the result to land "
          "between −3,840 and −8,640, where perfect knowledge scores +3,840. If a change to "
          "the question set ever made blanket-yes profitable, the build fails."),
    ("h2", "The simplification that came from playing it"),
    ("p", "The brief asked for three confidence levels plus an always-present *not sure*. The "
          "built game has three answers and no confidence row at all, and the note in the "
          "source is worth quoting as a design finding: a confidence slider *\"confused the loop "
          "more than it measured\"*. Fewer, coarser answers that people actually use beat a "
          "finer scale they answer noisily — the rule stays proper either way, and the numbers "
          "a player sees (+30, −50, 0) are ones they can hold in their head."),
    ("h2", "What would show this is wrong"),
    ("p", "Play data where calibration scores cluster near the ceiling — meaning people already "
          "know what they know, and the game is measuring nothing. Or a wide spread with no "
          "relationship to how the player actually configured their agent, meaning it is "
          "measuring a trivia score after all. Neither can be checked yet: **no release has "
          "cited play data.** That is exactly why the scoreboard sits at `scored` on "
          "[the ladder](maturity/index.html) and not at `measured`."),
  ]},
# ---------------------------------------------------------------------------
"method/the-ceiling.html": {
  "title": "The ceiling",
  "description": "17 of the 40 questions are things no agent can do, because a control outside "
                 "the environment bounds them. Without them the game could only measure "
                 "underestimating.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Method](method/index.html) / The ceiling"),
    ("h1", "Put a ceiling in the question set"),
    ("lead", "If every question in a capability quiz has a real answer, then the only mistake "
             "the quiz can detect is underestimating. Somebody who believes their agent is "
             "less capable than it is gets caught. Somebody who believes it is a god does not."),
    ("h2", "The fix, and its size"),
    ("p", "**17 of the 40 questions are above the ceiling**: things no agent in any environment "
          "in the set can do — not even one running as an administrator on a desktop with every "
          "confirmation switched off. They are interleaved evenly through every level, and the "
          "self-test fails if their share leaves the 33–50% band. At 43% the set spans both "
          "directions, so the score measures over-crediting and underestimating alike."),
    ("h2", "The ceiling is a control, not the agent's restraint"),
    ("p", "This is the distinction that makes the whole idea work. Each above-the-ceiling row "
          "names the control that bounds it, and the control is always **outside the whole "
          "environment**: the provider's tenant boundary, an append-only log, cryptography, a "
          "second factor, a lockout, billing ownership, the provider's own isolation."),
    ("p", "So the answer is not *the agent is well behaved*. The answer is *there is a wall "
          "there, and it is not made of the agent's good intentions*. Thirteen of the "
          "seventeen are **attemptable**, and their verdicts say exactly that: what happens "
          "when the agent tries, that it fails, and that the attempt is visible."),
    ("h2", "They have to sound powerful"),
    ("p", "An above-the-ceiling question that reads as obviously silly teaches nothing and is "
          "spotted instantly, which turns the whole mechanism into a tell. These are written "
          "to sound like things a capable agent might well do — the player has to actually "
          "reason about the boundary rather than pattern-match on absurdity."),
    ("h2", "Where the levels for them come from"),
    ("p", "Nowhere derivable, and the game says so. The mesh records no exposure for a thing "
          "that cannot happen, so the levels of above-the-ceiling capabilities are **authored** "
          "— stated as a judgement in the file, by one agent on one day, with every verdict "
          "linking back to it. That is a weaker claim than the derived levels next to them, "
          "and it is labelled as one rather than blended in. "
          "[How the derived ones work](method/levels.html)."),
    ("h2", "What would show this is wrong"),
    ("p", "Somebody demonstrating an agent stepping over one of the seventeen. The game's own "
          "source calls that *\"a correction, not a quibble\"* — the row names its control, so a "
          "counter-example is a specific, checkable claim about that control, and the "
          "[reply channel](games/ideas.html) is where it would be answered in public."),
  ]},
# ---------------------------------------------------------------------------
"method/levels.html": {
  "title": "Levels are distance, not danger",
  "description": "A level is the number of hops from a capability to a one-way consequence, "
                 "computed from the mesh — and the game says on the rail that it is distance, "
                 "never a danger rating.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Method](method/index.html) / Levels"),
    ("h1", "Derive the levels from the graph"),
    ("lead", "Difficulty tiers in most assessments are assigned by whoever wrote them, which "
             "means the tiers encode the author's intuition and nothing else. These are "
             "computed, and the computation is published."),
    ("h2", "The definition"),
    ("p", "A **consequence** is a one-way exposure — an edge in the mesh marked `reversible: "
          "no`. A capability's level is the fewest hops from it to any consequence, moving "
          "through `at` edges (exposure → reach) and `runs-in` edges (reach → environment), "
          "within a single profile's exposures, minimised across every profile in the set."),
    ("table", ["Hops to a one-way consequence", "Level"],
     [["0", "1"], ["2", "2"], ["4", "3"], ["6 or more", "4"], ["no path found", "5"]]),
    ("p", "With the current snapshot that gives **13 / 3 / 5 / 1 / 1** derived capabilities "
          "across the five levels, plus **8 / 4 / 4 / 1 / 0** authored above-the-ceiling ones. "
          "The distribution is lumpy, which is a property of the mesh rather than of the game, "
          "and a long level is played in rounds of eight with a carry-on-or-finish card in "
          "between rather than being padded out."),
    ("h2", "The sentence on the rail"),
    ("p", "The level rail says what each level means **and that it is distance, not danger**. "
          "That caveat is not decoration. A capability zero hops from a one-way consequence is "
          "not necessarily more dangerous than one six hops away — it is closer, which is a "
          "different claim. Reading a distance as a risk rating is exactly the mistake a "
          "numbered tier invites, so the game refuses the reading in the place where the "
          "number appears."),
    ("h2", "The honest limits"),
    ("ul", [
      "**The mesh has a gap.** It records no path at all for one capability in the set, which "
      "lands that capability at level 5 by absence of evidence rather than by distance.",
      "**The data is a snapshot.** Taken 2026-09-06 from [pki.sgit.ai](https://pki.sgit.ai) and "
      "vendored into the vault, with the date shown in the header of every screen. A vendored "
      "snapshot is reproducible and gets stale; a live fetch is current and unreproducible. "
      "The game vendors and stamps the date, and takes `?live=1` for the other behaviour.",
      "**Levels unlock, but nothing is locked.** A level unlocks when the one before scored "
      "≥ 0; a locked level is dimmed and still tappable. Gating play on performance would "
      "measure persistence rather than calibration.",
    ]),
  ]},
# ---------------------------------------------------------------------------
"method/grant-vs-mandate.html": {
  "title": "Grant vs. mandate",
  "description": "The grant is what the agent can do. The mandate is what you wanted it to do. "
                 "The delta is the thing nobody writes down — so the game extracts it as a "
                 "by-product of play.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Method](method/index.html) / Grant vs. mandate"),
    ("h1", "Make the mandate a by-product"),
    ("lead", "Two different things get called permissions. The **grant** is what the system "
             "will actually allow. The **mandate** is what you intended to authorise. They are "
             "set in different places by different people at different times, and almost "
             "nobody has written the second one down."),
    ("h2", "Why not just ask"),
    ("p", "Because a mandate form is answered aspirationally. Asked in the abstract what an "
          "agent should be allowed to do, people describe a policy they would like to have. "
          "Asked forty times, concretely, whether they want *this* capability while they are "
          "busy trying to score points on a different question, they answer about the thing in "
          "front of them."),
    ("p", "So the game never asks for a mandate. It asks *do you want it to?* alongside every "
          "*can it?*, and the end screen hands over **the mandate you assembled without meaning "
          "to** — badged, accurately, as *a draft you wrote while playing*."),
    ("h2", "The delta is the output"),
    ("p", "With both halves collected per capability, the delta falls out as a 2×2 — it can / "
          "it cannot, against you want it / you don't. Two cells are alignment. The other two "
          "are the findings:"),
    ("ul", [
      "**Excess authority** — it can, and you did not want it to. Every one of these is a "
      "grant you would narrow if you knew about it.",
      "**Shortfall** — it cannot, and you wanted it to. Usually harmless, except for the "
      "variant the game calls *a gap you were counting on*: you thought it could, you wanted "
      "it to, and it cannot. That is a dependency on something that is not there.",
    ]),
    ("p", "Each is split again by whether you saw it coming: a delta you flagged with the "
          "**but…** tick is drawn outlined, and one you did not — because you also had the "
          "grant wrong — is drawn filled and loud. Hidden deltas are the ones worth acting on, "
          "and they are the ones a self-assessment questionnaire structurally cannot find, "
          "because it asks you about the things you already know about."),
    ("h2", "Where this comes from — and what happens to a delta"),
    ("p", f"These games are part of [**RiskMandate**]({RM}) — *the business risk layer for "
          f"autonomous systems* — and they exist at one specific point in its argument. "
          f"RiskMandate's own framing is that [the grant is not the mandate]({RM_GRANT}): a "
          f"mandate is *the right to act*, granted by a named accountable owner, scoped to what "
          f"the agent may do and reach, **time-bound, never standing**. The game is how you get "
          f"a real person to state their half of that without asking them to fill in a form."),
    ("p", f"What happens to the delta afterwards is the part the game deliberately does not do, "
          f"and RiskMandate's answer to it is the one mechanic worth borrowing whatever you "
          f"build: [**there is no deny button**]({RM_ACCEPT}). For a deployed agent the access "
          f"already exists, so a materialised risk cannot be denied — *\"pretending you can is "
          f"how risk registers drift into fiction.\"* It can only be **accepted**, in a "
          f"direction and for an interval, by somebody named, and underwritten upward until it "
          f"aggregates into one board-level view."),
    ("p", f"Which makes the interval the decision rather than a field on a form: accept "
          f"something for an hour and it is fixed within the hour. [How it works]({RM_HOW}) "
          f"reduces it to three verbs — **accept, fund, or fix** — and the "
          f"[risk scenarios]({RM_SCENARIOS}) ask *how long will you accept this?* about "
          f"situations, where this game asks *can it, and do you want it to?* about "
          f"capabilities. Same question, two ends of it."),
    ("h2", "The worked example lives with the game"),
    ("p", f"The strongest demonstration of all this is **Licence to Operate** — a published "
          f"vault holding one agent's grant of 12 capabilities, its mandate of 4, and the "
          f"8-capability delta in between, where every reply carries its cost before you "
          f"commit. It is not a game by this site's definition (it never makes you commit to a "
          f"belief before showing you the answer), and it is specific to the subject *What Can "
          f"It Do?* covers rather than to games in general — so it is embedded on the player "
          f"site, next to the game whose output it prices: "
          f"[what-can-it-do.games.sgit.ai/licence-to-operate]"
          f"({PLAYER_SITE}/licence-to-operate/index.html) · "
          f"[the write-up with its audit]({LTO_PAGE})."),
    ("h2", "What is not built"),
    ("p", "The mandate draft the game hands a player does not export into any of these shapes. "
          "It is copyable text. Turning it into something a policy engine, a risk register or "
          "RiskMandate itself could consume is on the game's own next list, and **saying it is "
          "done would be the easiest overclaim on this site to make.** Today the handover from "
          "a player's delta to a time-bound acceptance is a person retyping it."),
  ]},
# ---------------------------------------------------------------------------
"maturity/index.html": {
  "title": "The maturity ladder",
  "description": "Five rungs, each with a test that moves a game up, so a label on a catalogue "
                 "card is a claim rather than a mood.",
  "blocks": [
    ("crumb", "[Home](index.html) / Maturity"),
    ("h1", "Five rungs, each with a test"),
    ("lead", "Games arrive half-built. A catalogue that hides that is useless, and a catalogue "
             "whose labels mean whatever the author felt on the day is worse. So every rung "
             "here has a **test**, and a game moves up when the test passes — not when it "
             "feels ready."),
    ("table", ["Rung", "Means", "The test that moves it up"],
     [["{{rung:sketch}}", "an idea and a rules table, nothing playable", "—"],
      ["{{rung:playable}}", "you can finish a run",
       "a stranger finished it without being told how"],
      ["{{rung:scored}}", "the scoring is a stated rule, self-tested",
       "`selftest.json` passes and the rule is published where a player can read it"],
      ["{{rung:measured}}", "play data exists and has changed something",
       "a release whose notes cite play data"],
      ["{{rung:answered}}", "players argue with it and get answers back",
       "positions published in the [ideas graph](games/ideas.html)"]]),
    ("h2", "Where the games sit today"),
    ("table", ["Game", "Rung", "Why not the next one"],
     [["[What Can It Do?](games/what-can-it-do.html)", "{{rung:scored}}",
       "It has telemetry and a reply channel, but **no release note yet cites play data**. "
       "v0.16.1 moved the feedback controls on a bias argument — that is reasoning, and good "
       "reasoning, but it is not data."],
      ["[Which Agent Is It?](games/which-agent-is-it.html)", "{{rung:playable}}",
       "Its engine is self-tested against a reference, but it has had far less play than the "
       "scoreboard and its reveal predates the results redesign."],
      ["[Ideas & feedback](games/ideas.html)", "{{rung:answered}}",
       "Not a game, so the ladder fits it awkwardly. It is listed at the rung it enables for "
       "the others — it was seeded with the first three real pieces of feedback."]]),
    ("note", "These placements are **our reading of somebody else's work**, made by reading "
             "the vault rather than by asking. If a release did move because play data said "
             "so, name it and the rung moves — that is what the "
             "[reply channel](games/ideas.html) is for."),
    ("h2", "Why the rungs are ordered this way"),
    ("p", "The order is not effort, it is **how much the game can be argued with**. A "
          "`playable` game produces an experience. A `scored` one produces a number you can "
          "check the rule behind. A `measured` one has been changed by contact with players. "
          "An `answered` one has a public position on the objections. Each rung is a step "
          "further from *we made a thing* toward *we made a claim and defended it*."),
    ("p", "One consequence worth stating: **`measured` is the hard one**, and everything before "
          "it is under the author's control. A game can be built to `scored` in a weekend and "
          "then sit there for a year, because moving up needs other people to play it. That is "
          f"the honest reason the first game has its own domain at "
          f"[what-can-it-do.games.sgit.ai]({PLAYER_SITE}) — a link you can send to somebody is "
          f"the mechanism by which a rung gets earned."),
  ]},
# ---------------------------------------------------------------------------
"build/index.html": {
  "title": "Building a game as a vault",
  "description": "How to build a game that ships as an encrypted vault: the authoring "
                 "contract, the folder-manifest trap that cost this family four releases, the "
                 "telemetry lane, and what to publish beside the game.",
  "blocks": [
    ("crumb", "[Home](index.html) / Build one"),
    ("h1", "Building a game as a vault"),
    ("lead", "A vault app is one self-contained `index.html` plus an `app.json` that launches "
             "it. That is the whole deployment story: no build server, no hosting, no account "
             "for the reader. What follows is what this family learned building three of them, "
             "including the mistake that cost four releases."),
    ("h2", "1 — The authoring contract"),
    ("ul", [
      "One `index.html` with CSS and JS **inlined**. No `<link href>`, `<script src>` or "
      "`<img src>` pointing at vault paths — those resolve against an opaque origin and 404.",
      "Content read over the bridge with `sg.vfs.readText`, with an inlined fallback so the "
      "page still renders outside a vault host.",
      "Generative SVG rather than image files, where you can. It keeps the vault small and it "
      "survives the no-`<img src>` rule without an interceptor.",
      "Post `sg-app-ready` when you have rendered, so the host can drop its loading state.",
    ]),
    ("h2", "2 — The folder-manifest trap"),
    ("p", "This one is worth the whole page. **A folder-level `app.json` replaces the root one "
          "wholesale — nothing is inherited.**"),
    ("p", "The games vault declares `permissions.network` at the root, because the vault host's "
          "app frame ships a `connect-src blob: data:` content-security policy and a direct "
          "`fetch` to any API is blocked without it. That worked when the vault opened at its "
          "root. Opening a game *by its own path*, or reaching it from the vault's home page, "
          "resolved that folder's manifest instead — which had no `permissions` key — and the "
          "frame silently kept the restrictive CSP. Telemetry failed with *\"Load failed\"*, the "
          "bridge fallback answered *\"Permission denied\"*, and nothing said why."),
    ("p", "It took releases v0.12.1 through v0.12.5 to find, across two wrong theories. The fix "
          "is one line per folder: **every folder that can be opened as an app carries the "
          "same grants as the root.** Two related things the same investigation settled — a "
          "release pin makes `app.json` come from the pinned commit rather than HEAD, and the "
          "append checker only ever watches the *open* vault's own lane, so a `new-messages` "
          "grant on a vault that has no lane will never fire whatever you declare."),
    ("h2", "3 — If it phones home, one credential shape survives"),
    ("p", "A vault published with a read key is a vault whose entire contents are public. So a "
          "game that sends anything must carry a credential that is safe to publish, and there "
          "is exactly one shape that qualifies: a **write-only append token**, blind, whose "
          "answer is `{\"ok\":true}` and nothing else. It cannot read, list or decrypt "
          "anything, including what it wrote."),
    ("p", "Two lanes rather than one, because retention differs: anonymous counters on one "
          "token, deliberate feedback on the other, so a flood of the first cannot bury the "
          "second and the first can be purged without losing the second. "
          "[What ours send](telemetry/index.html)."),
    ("note", "**The audit is the part people skip.** When sgit.ai published this vault it "
             "grepped the whole tree for private key material, provider keys, `enum_key` / "
             "`write_key` / `vault_key` fields, and every 64-hex string. Exactly one 64-hex "
             "string existed and it was the append token — and it was then *tested*, not taken "
             "on trust: cloning the telemetry vault with it decrypts nothing, and a control run "
             "with an all-zeros key behaves identically. An append token and a read key are "
             "both 64 hex; a mistake between them would be invisible."),
    ("h2", "4 — Publish the source beside the game"),
    ("p", "Both games ship their readable source in the same vault: the engine as an ES module, "
          "`selftest.json`, the vendored data snapshot, the build script, and a README carrying "
          "a rules table and a **does-not-prove list**. The scoring rule a game claims and the "
          "rule its engine implements are different objects, and shipping both is what lets "
          "somebody check that they match."),
    ("p", "The self-test is the load-bearing artefact. It is what turns *\"saying yes to "
          "everything should lose\"* from a design intention into a build failure."),
    ("h2", "5 — Embedding it on a page"),
    ("p", "Two hosts exist, and they are not interchangeable. The **minimal host** decrypts the "
          "vault in the page and boots the app in a sandboxed `srcdoc` frame: small, fast, and "
          "**reads only** — no `sg.llm.*`, no `sg.append.*`, and it never reads `app.json`. The "
          "**embed protocol** loads the real SG/Vault host in an iframe and hands it the key by "
          "`postMessage` with a pinned target origin, so the credential never enters a URL — "
          "and the app gets the full bridge."),
    ("p", "This site uses the second, in `assets/vault-app-embed.js`, with the vault-browser "
          "surface suppressed. The games declare `llm.chat` for their chat panel and "
          "`append.write` for the telemetry fallback; under the minimal host the chat panel is "
          "dead and both grants are inert. If your game reads files and nothing else, the "
          "minimal host is the better trade."),
  ]},
# ---------------------------------------------------------------------------
"telemetry/index.html": {
  "title": "What our games send",
  "description": "The games send anonymous usage events over two write-only append lanes. "
                 "What is in an event, what is deliberately absent, what it proves, and how to "
                 "stop it.",
  "blocks": [
    ("crumb", "[Home](index.html) / What our games send"),
    ("h1", "What our games send"),
    ("disclose", DISCLOSE),
    ("h2", "The default this breaks — and the one it does not"),
    ("p", "Opening a vault does not normally send anything anywhere. That is the platform "
          "default and every other vault this family publishes honours it. These games do not, "
          "which is why the fact is stated wherever the games appear rather than left to a "
          "privacy page nobody opens."),
    ("p", "**It is worth being proportionate about the size of this.** What leaves is a count "
          "of how far people got and which answers are common. There is no cookie, no "
          "analytics script, no account, no id, no fingerprint, no URL and no referrer — which "
          "is **less than a default web-server access log**, and considerably less than the "
          "analytics running on almost every site a reader will visit today. The reason it is "
          "disclosed at all is not that it is invasive; it is that a vault sending anything is "
          "a departure from a platform promise, and departures get stated."),
    ("h2", "What is in an event"),
    ("table", ["Carried", "Deliberately absent"],
     [["which screen you reached", "your name, or any id for you"],
      ["the answers you gave, and the points", "any fingerprint"],
      ["the profile you picked from the public list", "the URL, and the referrer"],
      ["a 16-hex session id, minted in memory when the page opened and gone when the tab closes",
       "your IP, as far as the payload is concerned"],
      ["a coarse form factor, a language and a host", "your user-agent string and screen size"]]),
    ("p", "The `profile` field is which **public** profile you picked from a list of nine. It "
          "is not a description of your setup — the scoring is arithmetic over a published "
          "profile, and the schema is blunt about it: *\"Not a count of people (sessions are "
          "tabs). Not evidence.\"*"),
    ("h2", "How it travels"),
    ("p", "Batched: one batch per flush, at most every 4 seconds, at most 40 flushes and 50 "
          "events per flush in a session. The payload is an `sgit pki` v2 envelope — RSA-OAEP-"
          "SHA256 wrapping AES-256-GCM — built with Web Crypto in the browser against a public "
          "key that ships in the vault. **If there is no secure context there is no Web Crypto, "
          "and the sender disables itself rather than falling back to plaintext.**"),
    ("p", "It goes to a separate private vault over an append lane. The games hold a "
          "**write-only token**: it cannot read, list or decrypt anything on that lane, "
          "including what it just wrote."),
    ("h2", "What it proves — which is the part most analytics pages never write"),
    ("note", "**Nothing about anyone.** Anyone holding the games' read key holds the append "
             "token too — it is published with them, because it has to be — and could forge or "
             "flood the lane. So the receiving end treats every event as a claim, not as a "
             "fact. Counts from this lane are a lower bound on activity and evidence of "
             "nothing else."),
    ("h2", "Two lanes, not one"),
    ("p", "Anonymous counters travel on one token; **feedback you deliberately write** — the "
          "👍/👎 and the form behind *say more* — travels on a second, never batched with the "
          "counters. Different retention, and the counters can be purged without losing the "
          "feedback. Nothing is sent from the feedback lane without a press."),
    ("p", "What comes back out of it is [the ideas graph](games/ideas.html): paraphrased, "
          "keyed to the question rather than to the person, naming nobody."),
    ("h2", "How to stop it"),
    ("p", "Every page in the vault carries a **pause switch** next to the notice, and it works "
          "before the first question. `telemetry.html` inside the vault is the authoritative "
          "statement — it is reachable from every screen and it is more detailed than this "
          "page. This page exists so that a reader who never opens the vault still gets told."),
    ("p", "This site itself sends nothing. It is static files on GitHub Pages with no analytics "
          "and no server to receive anything — the only thing that sends is the game, in its "
          "frame, on its own lanes."),
  ]},
# ---------------------------------------------------------------------------
"network/index.html": {
  "title": "The network",
  "description": "Where games.sgit.ai sits in the sgit.ai family, and which sibling site "
                 "answers which question.",
  "blocks": [
    ("crumb", "[Home](index.html) / The network"),
    ("h1", "The network"),
    ("lead", "This is one of a family of focused sites on `*.sgit.ai`, each taking one question "
             "further than a section could. They share a design, a release discipline, and a "
             "habit of publishing the argument before the thing exists."),
    ("h2", "The project this site is part of"),
    ("p", f"[**RiskMandate.ai**]({RM}) — *the business risk layer for autonomous systems*. "
          f"*Agents act. You own the risk.* It begins where security stops: not the finding, "
          f"but who accepts it, who funds the fix, and who owns the consequence. Its unit is "
          f"the **mandate** — the right to act, granted by a named owner, scoped, and "
          f"time-bound rather than standing — and its signature mechanic is that a real risk "
          f"has [no deny button]({RM_ACCEPT}), only an interval and an owner."),
    ("p", f"These games are the front end of one part of that: getting a real person to state "
          f"what they wanted, so the gap against what was granted becomes visible and "
          f"countable. [How the two connect](method/grant-vs-mandate.html) · "
          f"[The grant is not the mandate]({RM_GRANT}) · [Library]({RM_LIBRARY})."),
    ("h2", "The ones this site leans on"),
    ("table", ["Site", "What it answers", "Why it matters here"],
     [["[sgit.ai](https://sgit.ai)", "the encrypted git for humans and AI agents",
       "The vault layer the games ship in, and the [page on this vault]"
       "(https://sgit.ai/demos/vaults/agent-permission-games/) with its credential audit"],
      ["[pki.sgit.ai](https://pki.sgit.ai)", "a key registry for agents",
       "The mesh, the capability primitives, the nine public profiles and the reductions both "
       "games run on"],
      ["[graphs.sgit.ai](https://graphs.sgit.ai)", "a node is just a node; meaning is in the edges",
       "The grammar the ideas graph and the mesh are both built under — which is why they join "
       "without a mapping"],
      ["[risks.sgit.ai](https://risks.sgit.ai)", "you cannot deny a risk, only accept it for a time",
       "Where the delta goes once you have one"],
      ["[llms.sgit.ai](https://llms.sgit.ai)", "calling a model without holding an API key",
       "The `sg.llm.*` bridge behind the games' chat panel — the reason we embed the real host"]]),
    ("h2", "And the one this site is for"),
    ("p", f"[**what-can-it-do.games.sgit.ai**]({PLAYER_SITE}) — the first game, player-facing. "
          f"It is the family's first fourth-level domain and its first site whose audience is "
          f"not a practitioner."),
    ("p", "The rule that produced it, stated once so the next game inherits it: **a game gets "
          "its own domain when it is meant to be shared, and the domain is the game's name so "
          "the link explains itself.** If more games reach `measured`, they get "
          "`<name>.games.sgit.ai` on the same rule. Everything below that bar lives on a page "
          "here."),
  ]},
# ---------------------------------------------------------------------------
"admin/index.html": {
  "title": "Admin & engineering",
  "description": "How games.sgit.ai is built and released: one content file, generated HTML "
                 "and markdown twins, and a seven-check gate.",
  "blocks": [
    ("crumb", "[Home](index.html) / Admin"),
    ("h1", "How this site is built"),
    ("lead", "Every page exists once, as content, in `admin/build/build_pages.py`. Nothing "
             "under the site root is hand-edited."),
    ("h2", "The build"),
    ("pre", "python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap\n"
            "node admin/build/validate.js          # the gate CI will run"),
    ("p", "`admin/build/shell.py` renders one block list to **both** the HTML page and its "
          "markdown twin. sgit.ai says of every twin that it *\"is generated from the same "
          "content as the page, so the two cannot drift\"* — a generator is the only way that "
          "sentence stays true."),
    ("h2", "The gate — seven checks"),
    ("ol", [
      "**Version agreement** — `version.txt` against every page's badge, the versions table "
      "and `llms.txt`, with each release appearing exactly once.",
      "**Internal links** — every relative `href`/`src` resolves to a file in the tree.",
      "**Canonical host** — every canonical and `og:url` is on the host in `CNAME`, and every "
      "page declares one.",
      "**Key-leak tripwire** — nothing may look like an sgit vault key. Extended here to catch "
      "the *short* vault-id shape (`<secret>:<8 alphanumerics>`) as well as the long form, "
      "with the published read key on an explicit allow-list of exact strings.",
      "**Every embed discloses** — a page that mounts a vault app must carry the telemetry "
      "notice. Mechanical, because this is the exact defect sgit.ai published against the "
      "vault: two pages saying *nothing sent* on the same screen as events being sent.",
      "**Maturity labels come from the ladder** — a card cannot invent a status.",
      "**Every page has its twin** — an HTML page with no `.md` beside it means the build "
      "was not run.",
    ]),
    ("h2", "Release"),
    ("pre", "# 1. bump admin/build/version.txt and add a VERSION_LOG row in build_pages.py\n"
            "python3 admin/build/build_pages.py && node admin/build/validate.js\n"
            'git commit -am "site vX.Y.Z: what changed" && git push origin dev'),
    ("p", "Every push to `dev` runs **validate → tag → deploy**. The tag is checked against "
          "`version.txt` *and* the release commit's subject, and the bump must be the next "
          "minor. Pull requests run validation only. Same pipeline as pki, graphs and "
          "wardley-maps."),
    ("h2", "Why the tripwire was extended"),
    ("p", "The inherited version matched `<secret>:<uuid>` — the long-form vault id. Every "
          "vault in this family uses the **short** form (`4evnlwrj`, `kqngdecz`), so the "
          "inherited check would have passed over a leaked key on either of these sites. It "
          "now matches both shapes, and the allow-list is a list of exact strings rather than "
          "a pattern: a pattern permissive enough to admit our read key would admit every "
          "credential of that shape, which is how a check comes to pass while meaning nothing."),
  ]},
# ---------------------------------------------------------------------------
"admin/versions.html": {
  "title": "Release history",
  "description": "Every release of games.sgit.ai. The site version bumps on every push to dev, "
                 "and CI refuses a push whose commit subject and version.txt disagree.",
  "blocks": [
    ("crumb", "[Home](index.html) / [Admin](admin/index.html) / Release history"),
    ("h1", "Release history"),
    ("lead", "The version badge in the nav links here. It bumps on every push to `dev`, and CI "
             "refuses a release whose `version.txt` and commit subject disagree."),
    ("raw", versions_table()),
    ("p", "The games have their own release history, in the vault and independent of this "
          f"site's: `version.html` inside vault `{VAULT}`, 28 releases at v0.16.1. This table "
          f"tracks the site that describes them."),
  ]},
}


def main():
    summary = shell.write_site(ROOT, SITE, NAV, FOOTER, PAGES, VERSION, VERSION_LOG)
    print(f"build_pages: {VERSION} — {summary}")


if __name__ == "__main__":
    main()
