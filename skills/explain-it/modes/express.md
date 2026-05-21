# Explain-it — Express Mode (`/explain-it-now`)

Loaded by `explain-it` SKILL.md when the user invokes `/explain-it-now <concept>` or signals urgency mid-ceremony ("just give me the answer", "skip the rest").

Same tree topology as ceremony, minus the scope-interview and plan-approval gate. Speed is the trade.

Follow this protocol verbatim.

## Phase 1 — State the Shape, Skip the Gate

In ONE sentence, declare what you're about to teach and how many nodes:

> *"Quick walk: 3 nodes — setup, mechanism, consequence. Going."*

No interview. No approval gate. The user invoked express precisely to skip those.

If the concept clearly needs 5 nodes, you MAY use 5 — but state the shape upfront. If unsure between 1 and 3, default to 3.

*The shape statement MUST name the node count AND each node's one-word title* (e.g., *"3 nodes — setup, mechanism, consequence"*). *"Going."* alone is insufficient — the learner needs to anticipate the walk.

## Phase 2 — Tree Walk (same contract as ceremony)

For each node in order:

1. **Emit ONE chunk** — big picture only:
   - ≤5 sentences of prose
   - At least one non-prose visual element (see `references/visuals.md`)
   - Different visual pattern than the previous chunk
   - Zero unexplained jargon
2. **Stop-and-check:**
   > "Got it? Yes / No / Branch deeper?"
3. **Branch on response:**
   - **Yes** (or any affirmative token per `SKILL.md` Rule 3) → advance to next sibling, no preamble, no recap.
   - **No** → spawn child sub-branch Node N.1; announce *"Opening Node N.1 — `<focus>`."* Resolve, then announce *"Closing Node N.1. Back to Node N+1."*
   - **Branch deeper** → spawn child sub-branch Node N.k. Same announce-open + announce-close protocol.

## Phase 3 — Compact Synthesis (optional)

If the user wants closure, emit a one-sentence + one-visual synthesis. If the user already said "good, done" — stop. Express mode favors stopping early.

## Session-Budget Guard

Express mode max **5 chunks per express invocation** (lower than ceremony). The user picked express to be fast. If the lesson exceeds 5 chunks, ask:

> "Express budget hit (5 chunks). Switch to ceremony for the rest, or stop here?"

## When to Refuse Express

If the user invokes `/explain-it-now` on a concept that genuinely cannot fit in ≤5 chunks (e.g., "explain the entire CFA Level 1 curriculum"), say so in one line and recommend ceremony:

> *"This needs ceremony — too broad for express. Use `/explain-it` instead?"*

Do not silently try to compress an un-compressible topic.

## Hand-off to Ceremony

If the user signals they want depth mid-express ("actually, walk me through this properly"), switch to `modes/ceremony.md` from the current node forward. State the switch:

> *"Switching to ceremony for the rest — plan tree coming."*

## Anti-patterns — Express-Specific

- **Skipping the scope shape statement** — even express announces the tree shape; otherwise the user can't anticipate the walk.
- **Packing 2 nodes into 1 chunk because "it's express"** — express speeds up the gates, not the chunk contract.
- **Dropping the visual scaffold "to be quick"** — visual is the scaffold; prose alone fails. Use a compact pattern (boxed identity, causal arrow) if you need speed.
- **Continuing past 5 chunks without budget check** — express is a contract about scope, not a free pass.

## Return to SKILL.md

When the express walk completes or the user says "done" / "stop explain-it", revert to standard style. Acknowledge once: *"Express done."*
