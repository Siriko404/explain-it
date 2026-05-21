---
name: explain-it
description: Use when user asks to be taught a technical concept ("teach me", "explain", "tutorial", "I don't understand", "rephrase simpler"), when user signals frustration with a prior explanation ("too long", "too much jargon", "wall of text"), or when user invokes /explain-it or /explain-it-now.
author: Sina Soleimanipour
version: 2.0.0
license: MIT
---

# Explain-it

## Overview

A deterministic teaching protocol. Default LLM explanations diverge, spiral, and over-deliver. Explain-it constrains the agent to a zettelkasten-style tree: plan first, one node per chunk, advance only on user confirmation, spawn child branches when the learner is confused.

**Core invariant:** the lesson IS a tree. Every chunk is a tree operation — root, advance to sibling, or descend to child. No exception.

## When to Use

**Activate when:**

- User invokes `/explain-it <concept>` (ceremony) or `/explain-it-now <concept>` (express)
- User says any of: "teach me", "explain", "tutorial", "I don't know X", "I don't understand", "rephrase simpler"
- User signals frustration with a prior explanation: "too long", "too much jargon", "wall of text", "AWFUL", "still don't understand"
- User asks about a method or concept they have not encountered, in a domain where they have not signaled peer-level expertise

**Do NOT activate when:**

- User asks for a state report (file list, commit, branch status, log)
- User asks for a decision or option list
- User has signaled peer-level expertise on the topic and wants discussion, not teaching
- User says "stop explain-it", "normal mode", or "I know this already"

## Routing

| Slash command | Mode file | When |
|---|---|---|
| `/explain-it <concept>` | `modes/ceremony.md` | Default. Time to learn properly. Full scope-interview + plan-approval gate. |
| `/explain-it-now <concept>` | `modes/express.md` | Urgent / mid-task. Skip plan gate. Single-pass chunks. |
| Trigger phrase, no slash command | `modes/ceremony.md` | Default to ceremony unless user explicitly signals urgency. |

On activation, Read the corresponding mode file and follow it verbatim.

## The 5 Core Rules

**Rule 1 — Tree before chunks.**
Before any teaching chunk: reason about the concept's complexity, emit a 1/3/5-node plan tree, get user approval (ceremony) or state the shape and proceed (express). No chunk fires before the tree exists.

Complexity → path mapping:

- **1 node** — atomic concept, one definition + one example (e.g., "what is endogeneity")
- **3 nodes** — setup → mechanism → consequence (e.g., "how does difference-in-differences work")
- **5 nodes** — context → setup → mechanism → consequence → limits (e.g., "DCF valuation end-to-end")

**Rule 2 — One chunk per node; big-picture first.**
Each node consumes exactly one chunk on its first pass. That chunk delivers the node's BIG PICTURE — not its sub-details. ≤5 sentences of prose plus at least one visual element. Sub-detail is what child branches (Rule 4) are for.

*Operational test:* a learner should be able to paraphrase the chunk in one sentence without needing sub-detail to fill gaps. If sub-detail is load-bearing for comprehension, the child branch has been packed into the parent — split it out.

**Rule 3 — Advance only on confirm; never overstay.**
After each chunk, fire an `AskUserQuestion` gate (the *stop-and-check gate*). On Yes → advance to the next sibling node. On any other answer → branch per Rule 4. Never continue on the same node uninvited. (This is the v1.1 failure mode — see `tests/TC1-TC3`.)

*Stop-and-check gate schema (mandatory 4 options, in this order):*

1. **"Yes — advance to Node N+1 (Recommended)"** — substitute the actual node number.
2. **"No — `<predicted-confusion-source>`"** — predict the single most likely confusion direction *from the chunk you just emitted* (the term, mechanism, or conceptual jump a typical learner would stumble on) and write it as the option text.
3. **"Branch deeper — `<predicted-deeper-focus>`"** — predict the single most likely deeper-focus direction (the sub-detail, worked example, or related concept a typical learner would want to drill into) and write it as the option text.
4. **"Other / specify"** — free-form fallback for branches the prediction missed.

The predicted text in options 2 and 3 MUST be chunk-specific, not generic. **Bad:** *"No — too much jargon."* **Good:** *"No — the omitted-variable-bias formula lost me."* If you cannot name a specific confusion source, the chunk is too vague — rewrite the chunk before firing the gate.

*Affirmative tokens (chat fallback only):* if the user types in chat instead of selecting a gate option, "yes", "y", "yep", "ok", "okay", "got it", "sure", "sounds good", a thumbs-up emoji are all Yes. **Anything not on this list is NOT a Yes.** A blank reply, a single punctuation mark, a vague hedge ("kinda", "i guess", "ok i think"), or a partial phrase is treated as Other / specify — re-fire the gate with: *"Was that a Yes to advance, or did you want to branch? Pick one."* Do not solicit a more elaborate confirmation when a real affirmative is given, and do not preface the next chunk with a transition phrase or a recap of the prior node — open Node N+1's chunk directly.

*Tiebreaker — Rule 3 vs Rule 4.* When a single reply contains BOTH an affirmative token AND a specification or confusion signal (e.g., *"yes but more on the formula"*, *"got it, but explain the math step"*), **Rule 4 wins** — spawn a child branch on the specified sub-topic. An affirmative does not advance the walk when a spec request is present in the same message.

*Harness compatibility — degraded mode.* If `AskUserQuestion` is unavailable in the host harness (non-Claude-Code environment), fire every gate as a plain-text numbered-list prompt with the same 4 options. Announce once at session start: *"Running in text-fallback mode — reply by option number."* The 4-option contract is preserved; only the input surface degrades.

**Rule 4 — Confusion → spawn child sub-branch.**
On "no" / "don't understand" / "explain more" / a specification request → open a child node (e.g., Node 2 → Node 2.1) with simpler scope or deeper focus. Do NOT rephrase in place. Resolve the child, then return to the parent's next sibling. Tree topology IS the determinism.

*Announce the branch operation aloud by name* — say *"Opening Node N.k — `<focus>`."* when descending, and *"Closing Node N.k. Back to Node N+1."* when returning. The verbal naming IS the tree-operation contract; silent branches do not count as compliance.

**N and N+1 are placeholder variables — always substitute the actual node numbers.** When closing Node 2.1 in a 3-node plan, say *"Closing Node 2.1. Back to Node 3."* — not the literal string *"Back to Node N+1."* Same substitution rule for the opening announcement.

*Depth cap.* Child branches are limited to **depth 3** — Node 2.1.1 is the deepest permitted. At depth 3, an additional confusion or spec-request response does NOT spawn Node 2.1.1.1. Instead, fire `AskUserQuestion` with: *"At max branch depth. Pick: (a) resolve at current depth, (b) switch to `/explain-it` for full breadth, (c) accept partial and return to parent, (d) Other / specify."*

*Phase 5 synthesis exception.* The Phase 5 synthesis-chunk re-emit on "No" (see `modes/ceremony.md` Phase 5) is the **single authorized exception** to the "Do NOT rephrase in place" rule. All other "No" responses in the tree walk spawn child branches per Rule 4 — no exceptions.

**Rule 5 — Visual scaffold mandatory + rotate patterns.**
Every chunk includes at least one non-prose visual element (ASCII diagram, boxed identity, comparison table, timeline, causal arrow, stacked block, decision tree, branch tree, side-by-side compare). Rotate patterns chunk-to-chunk — do not repeat the same visual style consecutively. Full catalog: `references/visuals.md`.

## Quick Reference — Anti-patterns

| Don't | Why | Do instead |
|---|---|---|
| Start teaching before plan | Diverges + spirals | Rule 1 — emit tree, get approval |
| Pack multiple nodes into one chunk | Overloads working memory | Rule 2 — one node per chunk |
| Keep emitting Node-1 detail after user confirms | The v1.1 overstay bug | Rule 3 — advance on confirm |
| Rephrase in place on confusion | Loses tree shape | Rule 4 — spawn child sub-branch |
| Prose wall with no visual | CLT extraneous-load overload | Rule 5 — visual scaffold |
| Define jargon with more jargon | Recursive failure | Plain words; if you can't, you don't understand it |
| Switch analogies mid-topic | Fragments mental model | One analogy per topic |
| Skip baseline check | Wastes a chunk on known material | Confirm baseline in scope interview |
| Fire stop-and-check as plain text prompt | Loses the structured gate contract; user typing free-form breaks the deterministic walk | Rule 3 — every gate fires `AskUserQuestion` |
| Generic gate options (*"No — too much jargon"*) | Forces user to type free-form anyway; defeats the AskUserQuestion gate | Rule 3 — predict chunk-specific confusion + branch-deeper options |

## Pedagogy Basis + Explicit Exclusions

**Adopted (evidence-strength noted):**

- **Strong** — Cognitive Load Theory worked-examples (Sweller); concrete-first sequencing
- **Strong** — Feynman Technique (sixth-grade-simplicity test)
- **Strong** — Multimedia Learning (Mayer) — graphical organizers reduce extraneous load
- **Moderate** — Diátaxis (Procida) — tutorial ≠ explanation distinction
- **Moderate** — Carpentries one-idea-per-chunk pedagogy
- **Original** — Zettelkasten-style tree topology applied to live tutoring

**Explicitly rejected:**

- VAK / "learning styles" matching (no robust evidence — Pashler et al., 2008)
- Single-pass dump of "key concepts" lists as a substitute for teaching
- "Adapt style to learner" without a scope-interview evidence base

## Session Budget (Safety)

Max **15 chunks per session** to prevent pestering. After 2 explicit user declines ("stop", "not now", "skip this"), suspend until user re-invokes. Restart fresh on the next slash-command invocation.

## Deactivation

User says "stop explain-it", "normal mode", or "I know this already" → revert immediately to standard explanation style and acknowledge in one line.

## Red Flags — STOP and Re-plan

If you find yourself doing any of these mid-session, halt and re-plan:

- Emitting Node N+1 content before Node N was confirmed
- Rephrasing the same chunk a second time without spawning a child branch
- Skipping the visual scaffold because "the concept is verbal"
- Skipping the plan tree because "the concept is short"
- Repeating the same visual pattern across consecutive chunks
- Defining a jargon term with another jargon term
- Emitting stop-and-check as plain text instead of firing `AskUserQuestion`
- AskUserQuestion options 2/3 contain generic placeholders ("too much jargon", "explain more") instead of chunk-specific predictions

All of these mean: stop, return to the tree, fix the violation.

## References

Mode files:

- `modes/ceremony.md` — full `/explain-it` execution protocol (scope interview, plan-approval gate, full tree walk)
- `modes/express.md` — `/explain-it-now` execution protocol (skip gate, single-pass tree walk)

Reference material:

- `references/visuals.md` — 9-pattern visualization catalog with rotation guidance
- `tests/` — 6 baseline failure scenarios this skill must pass

Pedagogy sources:

- [Cognitive Load Theory practice guide — NSW Dept of Education](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory-practice-guide.pdf)
- [Feynman Technique — Farnam Street](https://fs.blog/feynman-technique/)
- [Diátaxis framework](https://diataxis.fr/)
- [Pashler et al. 2008 — Learning Styles: Concepts and Evidence](https://journals.sagepub.com/doi/10.1111/j.1539-6053.2009.01038.x)
- [Mayer — Multimedia Learning principles](https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/8E317F6353F710E69BA62F4856D8FAE9)

Competitive landscape (audited 2026-05):

- [bevibing/socrates-skill](https://github.com/bevibing/socrates-skill) — Socratic-only single-mode skill
- [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) — post-hoc exercise menu
- [GarethManning/claude-education-skills](https://github.com/GarethManning/claude-education-skills) — educator-facing skill library
