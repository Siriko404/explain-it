# eval-01 — novice general concept (full ceremony)

**Skill:** explain-it
**Query:** "Teach me what difference-in-differences is. I'm not familiar with it."
**Inputs:** none (general concept, no repo)

**expected_behavior:**
- P0 recon is SKIPPED (concept is not repo-anchored)
- P1 scope interview runs via AskUserQuestion (goal/depth/baseline), not prose
- P2 assigns complexity and an N-step path with N in {1,3,5}
- P3 presents the path and waits for explicit approval before teaching
- P4 teaches node-by-node using the 10-rule protocol; renders a MOC
  "you are here" anchor every turn
- A "give me an example" request spawns a CHILD node (branch), not a rework
- An "I don't understand" spawns a REWORK of the same node, no new material
- No spiral / no over-teaching past the approved path
- P5 writes the lesson tree to ./explain-it-vault/
