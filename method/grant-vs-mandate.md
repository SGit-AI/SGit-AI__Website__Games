# Grant vs. mandate

> The grant is what the agent can do. The mandate is what you wanted it to do. The delta is the thing nobody writes down — so the game extracts it as a by-product of play.

*Source: <https://games.sgit.ai/method/grant-vs-mandate.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Method](../method/index.md) / Grant vs. mandate

# Make the mandate a by-product

Two different things get called permissions. The **grant** is what the system will actually allow. The **mandate** is what you intended to authorise. They are set in different places by different people at different times, and almost nobody has written the second one down.

## Why not just ask

Because a mandate form is answered aspirationally. Asked in the abstract what an agent should be allowed to do, people describe a policy they would like to have. Asked forty times, concretely, whether they want *this* capability while they are busy trying to score points on a different question, they answer about the thing in front of them.

So the game never asks for a mandate. It asks *do you want it to?* alongside every *can it?*, and the end screen hands over **the mandate you assembled without meaning to** — badged, accurately, as *a draft you wrote while playing*.

## The delta is the output

With both halves collected per capability, the delta falls out as a 2×2 — it can / it cannot, against you want it / you don't. Two cells are alignment. The other two are the findings:

- **Excess authority** — it can, and you did not want it to. Every one of these is a grant you would narrow if you knew about it.
- **Shortfall** — it cannot, and you wanted it to. Usually harmless, except for the variant the game calls *a gap you were counting on*: you thought it could, you wanted it to, and it cannot. That is a dependency on something that is not there.

Each is split again by whether you saw it coming: a delta you flagged with the **but…** tick is drawn outlined, and one you did not — because you also had the grant wrong — is drawn filled and loud. Hidden deltas are the ones worth acting on, and they are the ones a self-assessment questionnaire structurally cannot find, because it asks you about the things you already know about.

## Where this comes from — and what happens to a delta

These games are part of [**RiskMandate**](https://riskmandate.ai) — *the business risk layer for autonomous systems* — and they exist at one specific point in its argument. RiskMandate's own framing is that [the grant is not the mandate](https://riskmandate.ai/v0/v0.11/v0.11.0/index.html): a mandate is *the right to act*, granted by a named accountable owner, scoped to what the agent may do and reach, **time-bound, never standing**. The game is how you get a real person to state their half of that without asking them to fill in a form.

What happens to the delta afterwards is the part the game deliberately does not do, and RiskMandate's answer to it is the one mechanic worth borrowing whatever you build: [**there is no deny button**](https://riskmandate.ai/v0/v0.10/v0.10.0/index.html). For a deployed agent the access already exists, so a materialised risk cannot be denied — *"pretending you can is how risk registers drift into fiction."* It can only be **accepted**, in a direction and for an interval, by somebody named, and underwritten upward until it aggregates into one board-level view.

Which makes the interval the decision rather than a field on a form: accept something for an hour and it is fixed within the hour. [How it works](https://riskmandate.ai/how-it-works.html) reduces it to three verbs — **accept, fund, or fix** — and the [risk scenarios](https://riskmandate.ai/scenarios.html) ask *how long will you accept this?* about situations, where this game asks *can it, and do you want it to?* about capabilities. Same question, two ends of it.

## The worked example: when the delta has a price

The strongest demonstration of all this is not a game and does not pretend to be. **Licence to Operate** is a published vault holding one agent's grant of **12 capabilities**, its mandate of **4** — read the customer's record, search the help centre, generate, and *draft, never send* — and the **8-capability delta** in between, which includes `mail:send` and `shell:exec`. Nobody asked for those; nothing insures them; the agent can reach them.

Then it prices the gap. A customer cannot log in, you pick the reply, and every option carries its cost before you commit: one inside the band, one that draws on the pool, one outside cover entirely. Underneath is a real rate table — a normal band, an ask-above threshold, a per-action ceiling, a pool with an untouchable reserve. It answers *does this agent have the licence to operate* by letting you spend it.

> Unlike the games, this vault sends **nothing at all** — no telemetry of any kind. It also declares read and no write at any path, so the app that simulates spending against a policy is structurally incapable of editing the policy it is spending against. Not because it is well behaved: because it never asked for the grant that would let it.

*[A live vault surface here in the HTML page — the game running out of vault `posrhzp3`. In this markdown twin, [open it in the vault UI](https://dev.vault.sgraph.ai/#d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29%3Aposrhzp3).]*

[Open it in its own tab](https://dev.vault.sgraph.ai/#d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29%3Aposrhzp3) — it is an interactive simulation and has far more room there — or read [the full write-up with its audit](https://sgit.ai/demos/vaults/licence-to-operate/index.html).

### Why it is not in the catalogue

Because it is a **simulation, not a game**, by this site's own definition: it never makes you commit to a belief before showing you the answer. You explore a priced space and learn the shape of it, which is valuable and is a different thing. [The catalogue](../games/index.md) lists things that score a stated prediction; putting this beside them would blur the one distinction the site is built on.

## What is not built

The mandate draft the game hands a player does not export into any of these shapes. It is copyable text. Turning it into something a policy engine, a risk register or RiskMandate itself could consume is on the game's own next list, and **saying it is done would be the easiest overclaim on this site to make.** Today the handover from a player's delta to a time-bound acceptance is a person retyping it.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/method/grant-vs-mandate.html)*
