# TC6 — Specification Request Spawns Child Branch

**Rule under test:** Rule 4 — *Confusion → spawn child sub-branch.* ("Branch deeper" / specification request half.)
**Maps to painpoint:** #6 (specification request → child branch missing).

## User simulation

Learner invokes `/explain-it CAPM`.
Plan approved as 3 nodes: `[Node 1: what beta is | Node 2: the CAPM equation | Node 3: when CAPM fails]`.
After Node 1's chunk, learner replies: **"Wait — explain how beta is actually calculated in practice."**

## v1.1 baseline failure

Skill answered the specification inline as a free-form tangent and then either (a) forgot to return to the planned tree, or (b) returned ambiguously without indicating which node was now active. The lesson lost structural coherence.

## v2 pass criterion

On a specification request (any "explain X deeper", "how exactly does Y work", "what about Z"), the skill MUST:

1. Recognize the request as a *branch-deeper* signal, equivalent to clicking the third option in the stop-and-check prompt.
2. Open and name a child sub-branch — e.g., *"Opening Node 1.1 — how beta is calculated in practice."*
3. Emit the child's big-picture chunk under the chunk contract (≤5 sentences, one visual, different visual pattern from Node 1's chunk).
4. Stop-and-check after the child chunk.
5. On the child's "yes", return EXPLICITLY to the parent's NEXT sibling: *"Closing Node 1.1. Back to plan — Node 2: the CAPM equation."*

## Verdict

- **PASS** if a named child branch opens and the explicit return-to-plan announcement follows its resolution.
- **FAIL** if the skill answers inline without naming a child branch, or fails to announce the return to the parent's next sibling.
