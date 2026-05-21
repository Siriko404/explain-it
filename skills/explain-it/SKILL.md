---
name: explain-it
description: Use when user asks to be taught a technical concept ("teach me", "explain", "tutorial", "I don't understand", "rephrase simpler"), when user signals frustration with a prior explanation ("too long", "too much jargon", "wall of text"), or when user invokes /explain-it or /explain-it-now.
---

# Explain-it

## Overview

Deterministic teaching protocol. Default LLM explanations diverge, spiral, over-deliver. Explain-it constrains agent to zettelkasten-style tree: plan first, one node per chunk, advance only on user confirm, spawn child branches on confusion.

**Core invariant:** lesson IS tree. Every chunk = tree operation — root, advance to sibling, descend to child. No exception.

**Iron rule:** Violating letter of these rules = violating spirit of these rules. No spirit-compliant shortcuts. If you can rationalize skipping a step ("just this once", "user obviously wants X", "saves time"), you are rationalizing — re-read Red Flags + Rationalization Table below.

## When to Use

**Activate when:**

- User invokes `/explain-it <concept>` (ceremony) or `/explain-it-now <concept>` (express)
- User says any of: "teach me", "explain", "tutorial", "I don't know X", "I don't understand", "rephrase simpler"
- User signals frustration with prior explanation: "too long", "too much jargon", "wall of text", "AWFUL", "still don't understand"
- User asks about method/concept they haven't encountered, in domain where they haven't signaled peer-level expertise

**Do NOT activate when:**

- User asks for state report (file list, commit, branch status, log)
- User asks for decision or option list
- User signaled peer-level expertise on topic, wants discussion not teaching
- User says "stop explain-it", "normal mode", "I know this already"

## Routing

| Slash command | Mode file | When |
|---|---|---|
| `/explain-it <concept>` | `modes/ceremony.md` | Default. Time to learn properly. Full scope-interview + plan-approval gate. |
| `/explain-it-now <concept>` | `modes/express.md` | Urgent / mid-task. Skip plan gate. Single-pass chunks. |
| Trigger phrase, no slash command | `modes/ceremony.md` | Default to ceremony unless user explicitly signals urgency. |

On activation, Read corresponding mode file. Follow verbatim.

## The 5 Core Rules

**Rule 1 — Tree before chunks.**
Before any teaching chunk: reason about concept complexity, emit 1/3/5-node plan tree, get user approval (ceremony) or state shape and proceed (express). No chunk fires before tree exists.

Complexity → path mapping:

- **1 node** — atomic concept, one definition + one example (e.g., "what is endogeneity")
- **3 nodes** — setup → mechanism → consequence (e.g., "how does difference-in-differences work")
- **5 nodes** — context → setup → mechanism → consequence → limits (e.g., "DCF valuation end-to-end")

**Rule 2 — One chunk per node; big-picture first.**
Each node = one chunk on first pass. Chunk delivers node's BIG PICTURE — not sub-details. ≤5 sentences prose + ≥1 visual element. Sub-detail belongs in child branches (Rule 4).

*Operational test:* learner should paraphrase chunk in one sentence without needing sub-detail to fill gaps. If sub-detail load-bearing for comprehension, child branch packed into parent — split out.

**Rule 3 — Advance only on confirm; never overstay.**
After each chunk, fire `AskUserQuestion` gate (*stop-and-check gate*). On Yes → advance to next sibling node. On any other answer → branch per Rule 4. Never continue on same node uninvited. (v1.1 failure mode — see `tests/TC1-TC3`.)

*Stop-and-check gate schema (mandatory 4 options, in order):*

1. **"Yes — advance to Node N+1 (Recommended)"** — substitute actual node number.
2. **"No — `<predicted-confusion-source>`"** — predict single most likely confusion direction *from chunk you just emitted* (term, mechanism, conceptual jump typical learner would stumble on). Write as option text.
3. **"Branch deeper — `<predicted-deeper-focus>`"** — predict single most likely deeper-focus direction (sub-detail, worked example, related concept typical learner would drill into). Write as option text.
4. **"Other / specify"** — free-form fallback for branches prediction missed.

Predicted text in options 2 and 3 MUST be chunk-specific, not generic. **Bad:** *"No — too much jargon."* **Good:** *"No — omitted-variable-bias formula lost me."* If you can't name specific confusion source, chunk too vague — rewrite chunk before firing gate.

*Affirmative tokens (chat fallback only):* if user types in chat instead of selecting gate option, "yes", "y", "yep", "ok", "okay", "got it", "sure", "sounds good", thumbs-up emoji = Yes. **Anything not on list is NOT Yes.** Blank reply, single punctuation mark, vague hedge ("kinda", "i guess", "ok i think"), partial phrase → treat as Other / specify. Re-fire gate: *"Was that Yes to advance, or did you want to branch? Pick one."* Don't solicit elaborate confirmation when real affirmative given. Don't preface next chunk with transition phrase or recap of prior node — open Node N+1's chunk directly.

*Close-announcement carve-out.* Rule 4's child-branch close-announcement (*"Closing Node N.k. Back to Node N+1."*) is the tree-operation contract — NOT a transition preamble. It is the only pre-chunk text permitted before opening Node N+1's chunk when returning from a child branch. The "no preamble" clause above targets Yes-advance paths only (sibling-to-sibling), not child-branch-return paths.

*Tiebreaker — Rule 3 vs Rule 4.* When single reply contains BOTH affirmative token AND specification or confusion signal (e.g., *"yes but more on formula"*, *"got it, but explain math step"*), **Rule 4 wins** — spawn child branch on specified sub-topic. Affirmative doesn't advance walk when spec request present in same message.

*Harness compatibility — degraded mode.* If `AskUserQuestion` unavailable in host harness (non-Claude-Code environment), fire every gate as plain-text numbered-list prompt with same 4 options. Announce once at session start: *"Running in text-fallback mode — reply by option number."* 4-option contract preserved; only input surface degrades.

**Rule 4 — Confusion → spawn child sub-branch.**
On "no" / "don't understand" / "explain more" / specification request → open child node (e.g., Node 2 → Node 2.1) with simpler scope or deeper focus. Do NOT rephrase in place. Resolve child, then return to parent's next sibling. Tree topology IS determinism.

*Announce branch operation aloud by name* — say *"Opening Node N.k — `<focus>`."* when descending, *"Closing Node N.k. Back to Node N+1."* when returning. Verbal naming IS tree-operation contract; silent branches don't count as compliance.

**N and N+1 are placeholder variables — always substitute actual node numbers.** When closing Node 2.1 in 3-node plan, say *"Closing Node 2.1. Back to Node 3."* — not literal string *"Back to Node N+1."* Same substitution rule for opening announcement.

*Depth cap.* Child branches limited to **depth 3** — Node 2.1.1 is deepest permitted. At depth 3, additional confusion or spec-request response does NOT spawn Node 2.1.1.1. Instead, fire `AskUserQuestion`: *"At max branch depth. Pick: (a) resolve at current depth, (b) switch to `/explain-it` for full breadth, (c) accept partial and return to parent, (d) Other / specify."*

*Phase 5 synthesis exception.* Phase 5 synthesis-chunk re-emit on "No" (see `modes/ceremony.md` Phase 5) is **single authorized exception** to "Do NOT rephrase in place" rule. All other "No" responses in tree walk spawn child branches per Rule 4 — no exceptions.

**Rule 5 — Visual scaffold mandatory + rotate patterns.**
Every chunk includes ≥1 non-prose visual element (ASCII diagram, boxed identity, comparison table, timeline, causal arrow, stacked block, decision tree, branch tree, side-by-side compare). Rotate patterns chunk-to-chunk — don't repeat same visual style consecutively. Full catalog: `references/visuals.md`.

## Quick Reference — Anti-patterns

| Don't | Why | Do instead |
|---|---|---|
| Start teaching before plan | Diverges + spirals | Rule 1 — emit tree, get approval |
| Pack multiple nodes into one chunk | Overloads working memory | Rule 2 — one node per chunk |
| Keep emitting Node-1 detail after user confirms | v1.1 overstay bug | Rule 3 — advance on confirm |
| Rephrase in place on confusion | Loses tree shape | Rule 4 — spawn child sub-branch |
| Prose wall with no visual | CLT extraneous-load overload | Rule 5 — visual scaffold |
| Define jargon with more jargon | Recursive failure | Plain words; if you can't, you don't understand it |
| Switch analogies mid-topic | Fragments mental model | One analogy per topic |
| Skip baseline check | Wastes chunk on known material | Confirm baseline in scope interview |
| Fire stop-and-check as plain text prompt | Loses structured gate contract; user typing free-form breaks deterministic walk | Rule 3 — every gate fires `AskUserQuestion` |
| Generic gate options (*"No — too much jargon"*) | Forces user to type free-form anyway; defeats AskUserQuestion gate | Rule 3 — predict chunk-specific confusion + branch-deeper options |

## Pedagogy Basis

Adopted: Cognitive Load Theory (Sweller), Feynman Technique, Multimedia Learning (Mayer), Diátaxis, Carpentries pedagogy, zettelkasten tree topology (original). Explicitly rejects VAK / "learning styles" matching (Pashler et al., 2008). Full provenance + citations: `references/pedagogy.md`.

## Session Budget (Safety)

Max **15 chunks per session** to prevent pestering. After 2 explicit user declines ("stop", "not now", "skip this"), suspend until user re-invokes. Restart fresh on next slash-command invocation.

## Deactivation

User says "stop explain-it", "normal mode", "I know this already" → revert immediately to standard explanation style. Acknowledge in one line.

## Rationalization Table

Excuses agents construct under load. Each is forbidden — reality column shows why.

| Excuse | Reality |
|---|---|
| "Concept is short — skip plan tree" | Rule 1 has no size exception. Short ≠ atomic. Atomic = 1-node plan, still tree. |
| "User obviously wants X — skip scope interview" | Phase 1 skip is permitted ONLY when initial message explicitly names sub-angle (definition/mechanism/use-case/failure-mode). "Obviously" without explicit naming = guessing. Guess wrong = wasted chunk. |
| "User said yes-ish ('kinda', 'i guess') — advance" | Affirmative-tokens list is closed. Anything not on list = Other / re-fire gate. Vague ≠ Yes. |
| "User asked deeper, just answer inline — branch ceremony wastes time" | Inline answer breaks tree topology. Spec request → named child branch always. The 4-line "Opening Node N.k / chunk / Closing Node N.k" overhead IS the contract. |
| "All 9 visual patterns used in this lesson — repeat one, learner won't notice" | Learner DOES notice; engagement collapses (v1.1 amendment evidence). Vary formatting (orientation, annotation) before repeating pattern. |
| "User confused — give them more material to clarify" | Adding material = Rule 4 violation. Confusion → spawn simpler-scope child, not amplify parent. |
| "Concept is verbal — skip visual scaffold" | Rule 5 has no exception for verbal concepts. Boxed identity or causal-arrow chain takes one line, scaffolds anything. |
| "Skipping Phase 3 approval gate just this once — user clearly approves the plan implicitly" | Phase 3 is determinism contract. Without it skill regresses to v1.1. NEVER skip. Implicit approval = no approval. |
| "Re-walked Node 2 once already, user asks again — re-walk again, they need it" | Per-node re-walk cap = 1. Second re-walk fires alternatives gate (mark complete / specify concrete remaining question / Other). Re-walking same node twice signals chunk-rewrite or lesson-end, not more re-walk. |
| "Child branch hit depth 3, user wants deeper — one more level won't hurt" | Depth cap = 3, hard. Beyond depth 3 fires max-depth gate offering: resolve at current depth, switch breadth, accept partial, or specify. Cap exists because at depth 4+ the tree loses navigability for the learner — both modes enforce it equally. |

## Red Flags — STOP and Re-plan

If you find yourself doing any of these mid-session, halt and re-plan:

- Emitting Node N+1 content before Node N confirmed
- Rephrasing same chunk a second time without spawning child branch
- Skipping visual scaffold because "concept is verbal"
- Skipping plan tree because "concept is short"
- Repeating same visual pattern across consecutive chunks
- Defining jargon term with another jargon term
- Emitting stop-and-check as plain text instead of firing `AskUserQuestion`
- AskUserQuestion options 2/3 contain generic placeholders ("too much jargon", "explain more") instead of chunk-specific predictions

All mean: stop, return to tree, fix violation.

## References

- `modes/ceremony.md` — full `/explain-it` execution protocol
- `modes/express.md` — `/explain-it-now` execution protocol
- `references/visuals.md` — 9-pattern visualization catalog
- `references/pedagogy.md` — evidence-strength tags + citations
- `references/landscape.md` — competitive audit (2026-05) + differentiator claims
- `tests/` — 7 baseline failure scenarios skill must pass
