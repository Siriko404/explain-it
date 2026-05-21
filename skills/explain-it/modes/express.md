# Explain-it — Express Mode (`/explain-it-now`)

Loaded by `explain-it` SKILL.md when user invokes `/explain-it-now <concept>` or signals urgency mid-ceremony ("just give me the answer", "skip the rest").

Same tree topology as ceremony, minus scope-interview and plan-approval gate. Speed is trade.

Follow protocol verbatim.

## Phase 1 — State Shape, Skip Gate

In ONE sentence, declare what you're about to teach and how many nodes:

> *"Quick walk: 3 nodes — setup, mechanism, consequence. Going."*

No interview. No approval gate. User invoked express precisely to skip those.

If concept clearly needs 5 nodes, MAY use 5 — but state shape upfront. If unsure between 1 and 3, default to 3.

*Shape statement MUST name node count AND each node's one-word title* (e.g., *"3 nodes — setup, mechanism, consequence"*). *"Going."* alone insufficient — learner needs to anticipate walk.

## Phase 2 — Tree Walk (same contract as ceremony)

For each node in order:

1. **Emit ONE chunk** — big picture only:
   - ≤5 sentences prose
   - ≥1 non-prose visual element (see `references/visuals.md`)
   - Different visual pattern than previous chunk
   - Zero unexplained jargon
2. **Stop-and-check gate** — fire `AskUserQuestion` per `SKILL.md` Rule 3 schema (same 4-option pattern as ceremony; same chunk-tailored prediction requirement):
   - **"Yes — advance to Node N+1 (Recommended)"**
   - **"No — `<predicted-confusion>`"** — chunk-specific, not generic
   - **"Branch deeper — `<predicted-focus>`"** — chunk-specific, not generic
   - **"Other / specify"**
3. **Branch on response:**
   - **Yes** (or any affirmative token per `SKILL.md` Rule 3) → advance to next sibling, no preamble, no recap.
   - **No** → spawn child sub-branch Node N.1; announce *"Opening Node N.1 — `<focus>`."* Resolve, then announce *"Closing Node N.1. Back to Node N+1."*
   - **Branch deeper** → spawn child sub-branch Node N.k. Same announce-open + announce-close protocol.

## Phase 3 — Compact Synthesis (optional)

If user wants closure, emit one-sentence + one-visual synthesis. If user already said "good, done" — stop. Express mode favors stopping early.

## Session-Budget Guard

Express mode max **5 chunks per express invocation** (lower than ceremony). User picked express to be fast. If lesson exceeds 5 chunks, halt and fire `AskUserQuestion`:

- **"Stop here — concept covered enough for express (Recommended)"**
- **"Switch to ceremony for the remaining material"**
- **"Extend express by 3 more chunks"**
- **"Other / specify"**

## When to Refuse Express

If user invokes `/explain-it-now` on concept that genuinely can't fit in ≤5 chunks (e.g., "explain entire CFA Level 1 curriculum"), say so in one line and recommend ceremony:

> *"This needs ceremony — too broad for express. Use `/explain-it` instead?"*

Don't silently try to compress un-compressible topic.

## Hand-off to Ceremony

If user signals they want depth mid-express ("actually, walk me through this properly"), switch to `modes/ceremony.md` from current node forward. State switch:

> *"Switching to ceremony for the rest — plan tree coming."*

## Anti-patterns — Express-Specific

- **Skipping scope shape statement** — even express announces tree shape; otherwise user can't anticipate walk.
- **Packing 2 nodes into 1 chunk because "it's express"** — express speeds up gates, not chunk contract.
- **Dropping visual scaffold "to be quick"** — visual IS scaffold; prose alone fails. Use compact pattern (boxed identity, causal arrow) if you need speed.
- **Continuing past 5 chunks without budget check** — express is contract about scope, not free pass.

## Return to SKILL.md

When express walk completes or user says "done" / "stop explain-it", revert to standard style. Acknowledge once: *"Express done."*
