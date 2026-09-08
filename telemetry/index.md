# What our games send

> The games send anonymous usage events over two write-only append lanes. What is in an event, what is deliberately absent, what it proves, and how to stop it.

*Source: <https://games.sgit.ai/telemetry/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / What our games send

# What our games send

> **These games phone home, and you should know before you play.** Opening a vault does not normally send anything anywhere — that is the platform default, and every other vault this family publishes honours it. These send **anonymous usage events** while you play: which screens you reach, the answers you give, your score. No name, no id, no fingerprint, no URL, no referrer. Every page carries a notice and a pause switch. [What is sent, exactly](../telemetry/index.md).

## The default this breaks

Opening a vault does not normally send anything anywhere. That is the platform default and every other vault this family publishes honours it. These games do not, and the notice belongs above the fold rather than in a footnote — particularly in a vault whose own subject is informed consent.

## What is in an event

| Carried | Deliberately absent |
|---|---|
| which screen you reached | your name, or any id for you |
| the answers you gave, and the points | any fingerprint |
| the profile you picked from the public list | the URL, and the referrer |
| a 16-hex session id, minted in memory when the page opened and gone when the tab closes | your IP, as far as the payload is concerned |
| a coarse form factor, a language and a host | your user-agent string and screen size |

The `profile` field is which **public** profile you picked from a list of nine. It is not a description of your setup — the scoring is arithmetic over a published profile, and the schema is blunt about it: *"Not a count of people (sessions are tabs). Not evidence."*

## How it travels

Batched: one batch per flush, at most every 4 seconds, at most 40 flushes and 50 events per flush in a session. The payload is an `sgit pki` v2 envelope — RSA-OAEP-SHA256 wrapping AES-256-GCM — built with Web Crypto in the browser against a public key that ships in the vault. **If there is no secure context there is no Web Crypto, and the sender disables itself rather than falling back to plaintext.**

It goes to a separate private vault over an append lane. The games hold a **write-only token**: it cannot read, list or decrypt anything on that lane, including what it just wrote.

## What it proves — which is the part most analytics pages never write

> **Nothing about anyone.** Anyone holding the games' read key holds the append token too — it is published with them, because it has to be — and could forge or flood the lane. So the receiving end treats every event as a claim, not as a fact. Counts from this lane are a lower bound on activity and evidence of nothing else.

## Two lanes, not one

Anonymous counters travel on one token; **feedback you deliberately write** — the 👍/👎 and the form behind *say more* — travels on a second, never batched with the counters. Different retention, and the counters can be purged without losing the feedback. Nothing is sent from the feedback lane without a press.

What comes back out of it is [the ideas graph](../games/ideas.md): paraphrased, keyed to the question rather than to the person, naming nobody.

## How to stop it

Every page in the vault carries a **pause switch** next to the notice, and it works before the first question. `telemetry.html` inside the vault is the authoritative statement — it is reachable from every screen and it is more detailed than this page. This page exists so that a reader who never opens the vault still gets told.

This site itself sends nothing. It is static files on GitHub Pages with no analytics and no server to receive anything — the only thing that sends is the game, in its frame, on its own lanes.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/telemetry/index.html)*
