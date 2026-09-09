# Which Agent Is It? — the floor plan

> The floor-plan game: think of an agent, answer cheap questions, chalk which wings of the building you think it can enter — then the doors open.

*Source: <https://games.sgit.ai/games/which-agent-is-it.html> · site v0.3.2 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / [Games](../games/index.md) / Which Agent Is It?

# Which Agent Is It? — the floor plan

Think of an agent. A handful of cheap questions narrow the field while you chalk which wings of the building you believe it can enter. Then the doors open, and the prediction gap is shown capability by capability.

## The board is the interesting part

Capabilities are drawn as rooms grouped into wings — filesystem, identity, process, code, network, communication, schedule, money, browser — and the legend keeps four states apart: **chalk** (asserted, you drew it), **pencil hatching** (inferred, the plan says so), **dotted** (possible, still consistent with what you have answered) and plain (no visitor above 5% likelihood holds a key). A belief column ranks the nine public profiles by likelihood, live, as you answer.

The game is careful about what a drawing is, and says so on the board: *"a room is a rendering choice, not a place — rooms are not ordered, sized or adjacent by anything in the data."* That sentence is doing real work. A floor plan invites you to read adjacency as meaning, and there is no adjacency in the underlying graph.

## The question that measures nothing

Mid-game there is a question labelled `IDENTIFIES` which the board says *"identifies and measures nothing"*, and it never counts toward the prediction gap. It is there to narrow the belief column — to work out *which* agent you are thinking of — and keeping it out of the score is the honest thing to do: you should not lose points for a question asked to help the game, not to test you.

## It hands you to the scoreboard

The reveal screen links into [What Can It Do?](../games/what-can-it-do.md) with the matched profile already handed over, so the second game starts where the first ended rather than asking you to name your agent again. It is the reason the two ship in one vault.

**Rung: `playable`.** It scores, and its engine is self-tested against a reference, but it has had far less play than the scoreboard and its reveal has not been reworked since the scoreboard's results page was. [What the rungs mean](../maturity/index.md).

> **Open it yourself.** Read key `f94c8b1d4235…111118:4evnlwrj` — the full string is on [the vault's page at sgit.ai](https://sgit.ai/demos/vaults/agent-permission-games/). [Open it read-only in a new tab](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj), or clone it with `sgit clone`. It is a read key: it cannot write, which is what makes publishing it safe.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/games/which-agent-is-it.html)*
