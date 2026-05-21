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
After each chunk: ask "Got it? Yes / No / Branch deeper?". On "yes" → advance to the next sibling node. On no answer → wait. Never continue on the same node uninvited. (This is the v1.1 failure mode — see `tests/TC1-TC3`.)

*Affirmative tokens:* "yes", "y", "yep", "ok", "okay", "got it", "sure", "sounds good", a thumbs-up emoji, or any clear affirmative all count as Yes. Do not solicit a more elaborate confirmation. Do not preface the next chunk with a transition phrase or a recap of the prior node — open Node N+1's chunk directly.

**Rule 4 — Confusion → spawn child sub-branch.**
On "no" / "don't understand" / "explain more" / a specification request → open a child node (e.g., Node 2 → Node 2.1) with simpler scope or deeper focus. Do NOT rephrase in place. Resolve the child, then return to the parent's next sibling. Tree topology IS the determinism.

*Announce the branch operation aloud by name* — say *"Opening Node N.k — `<focus>`."* when descending, and *"Closing Node N.k. Back to Node N+1."* when returning. The verbal naming IS the tree-operation contract; silent branches do not count as compliance.

**N and N+1 are placeholder variables — always substitute the actual node numbers.** When closing Node 2.1 in a 3-node plan, say *"Closing Node 2.1. Back to Node 3."* — not the literal string *"Back to Node N+1."* Same substitution rule for the opening announcement.

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
