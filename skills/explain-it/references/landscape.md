# Competitive Landscape (audited 2026-05)

Reference for `explain-it` differentiator claims. Not operational — agents executing the skill do not need to read this file. Maintained for release-time positioning and to justify the "what we do that no one else does" section of the README.

## Competitors surveyed

- **[bevibing/socrates-skill](https://github.com/bevibing/socrates-skill)** — Socratic-only single-mode skill. Enforces one absolute rule: never give a direct answer. 5-step workflow (read silently → assess level → progressive questioning → adapt → confirm via user summary). 73 lines. Missing: tree topology, chunk-per-node contract, complexity-to-path mapping, visualization catalog, dual entry split, plan-approval gate.
- **[DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)** — Single-mode interruption layer triggered post-architectural-work. Six evidence-based exercise types (prediction/generation/trace/debug/teach-back/retrieval). 10–15 min budget; suppression after 2 declines or 2 completions. Borrow: post-hoc exercise menu pattern; decline-suppression heuristic. Missing: reactive (not on-demand), no Socratic dialog, no scope interview, no branching.
- **[GarethManning/claude-education-skills](https://github.com/GarethManning/claude-education-skills)** — 152 skills across 19 domains. Typed I/O schema; evidence-strength rated (Strong/Moderate/Emerging/Original); explicit exclusion list. Borrow: typed I/O, evidence-strength tagging, transparent exclusions. Missing: educator-facing not student-facing; no live tutoring loop.
- **[vuciv Socratic Tutor gist](https://gist.github.com/vuciv/1d2864e73306f490aaeaa023cd3600fa)** — ~250 words, single prompt. Five rules (delayed revelation, on-demand explanation, question-driven, quiz often, error-focused). Borrow: opening line *"What part do you understand least right now?"*; delayed retrieval practice. Missing: no architecture beyond a flat rule list.
- **[linexjlin Code Tutor](https://github.com/linexjlin/GPTs/blob/main/prompts/Code%20Tutor.md)** — Hard constraint "never write code"; one-question-per-turn; pseudo-code only as last resort. Borrow: explicit boundary repetition; emotional-support clause. Missing: no topology, no chunking spec, single mode.
- **[Khanmigo](https://blog.khanacademy.org/khan-academys-7-step-approach-to-prompt-engineering-for-khanmigo/)** — GPT-4-backed, Socratic, 7-step prompt-engineering recipe. Personalizes by pulling learner's course/language/interests. Borrow: persona-test matrix; "meet students where they are" hook (we have scope-interview — make it learner-state-aware, not just topic-scope-aware). Missing: closed-source, no public visualization catalog.
- **[Anthropic Claude Learning Mode](https://www.anthropic.com/news/introducing-claude-for-education)** — Projects-template dropdown. Patterns: guided discovery, scaffolding, connection-building, metacognitive prompts. [Northeastern guide](https://learning.northeastern.edu/ai-student-guides-using-claude-learning-mode-to-study/) notes Learning Mode has no progressive hint system, no formal comprehension checks, no branching framework, no visualization generation — all four are explain-it's v2 differentiators.

## Top-3 patterns borrowed from competitors

1. **Evidence-strength tags + explicit-exclusion list** (GarethManning) — implemented in `references/pedagogy.md`.
2. **Decline-suppression + session budget** (learning-opportunities) — implemented in `modes/ceremony.md` Session-Budget Guard.
3. **Persona seed question** (Khanmigo + vuciv) — implemented in `modes/ceremony.md` Phase 1 scope interview.

## Top-3 things no surveyed competitor does (the moat)

1. **Deterministic zettelkasten/mindmap tree topology with complexity-to-path mapping (1/3/5).** Every surveyed competitor is a flat dialog loop. None pre-commit to a tree before teaching; none scale node count to complexity.
2. **Chunk-per-node execution contract with advance-on-confirm + confusion-spawns-named-child-branch.** bevibing has "adapt"; learning-opportunities has fixed exercise types; explain-it promotes confusion to a structural tree operation, not a rewrite.
3. **Two-entry-point split (`/explain-it` ceremony vs `/explain-it-now` express) with scope-interview + plan-approval gate + 9-pattern visualization rotation contract.** Northeastern explicitly calls out Claude Learning Mode's lack of any of these.
