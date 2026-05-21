# Pedagogy Basis + Explicit Exclusions

Reference for `explain-it` design provenance. Not operational — agents executing the skill do not need to read this file.

## Adopted (evidence-strength noted)

- **Strong** — Cognitive Load Theory worked-examples (Sweller); concrete-first sequencing. Reduces extraneous load by giving learners worked solutions before asking them to construct mental models from scratch.
- **Strong** — Feynman Technique (sixth-grade-simplicity test). Operationalized as Rule 3's jargon prohibition and Rule 2's paraphrase test.
- **Strong** — Multimedia Learning (Mayer). Graphical organizers reduce extraneous load when they make spatial relationships explicit. Operationalized as Rule 5 (visual scaffold mandatory + rotate patterns).
- **Moderate** — Diátaxis (Procida) — tutorial ≠ explanation distinction. Operationalized as the choice to make `/explain-it` a tutorial-mode skill rather than a reference-lookup skill.
- **Moderate** — Carpentries one-idea-per-chunk pedagogy. Operationalized as Rule 2 (one chunk per node).
- **Original** — Zettelkasten-style tree topology applied to live tutoring. The named-node branching contract (Rule 4) is novel — competitor surveys found no other tutoring skill or framework that promotes confusion to a structural tree operation rather than an in-place rephrase.

## Explicitly rejected

- **VAK / "learning styles" matching** — no robust evidence the technique improves learning outcomes (Pashler et al., 2008). Explain-it does not ask the learner about their "preferred learning style" and does not adapt presentation style on that basis. It adapts on scope (the seed question's A/B/C/D angle) and on confusion-signal (the chunk-tailored gate predictions), both of which have evidence backing.
- **Single-pass dump of "key concepts" lists** as a substitute for teaching. A bulleted recap is reference material, not pedagogy. Explain-it's chunks must *teach* the node's big picture, not list its parts.
- **"Adapt style to learner" without a scope-interview evidence base.** Explain-it's only adaptation channels are (a) the scope interview's seed question, (b) the on-the-fly chunk-tailored gate predictions, and (c) confusion → child branch. Free-floating "adapt to learner" instructions are excluded as they enable post-hoc rationalization.

## Sources

- [Cognitive Load Theory practice guide — NSW Dept of Education](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory-practice-guide.pdf)
- [Feynman Technique — Farnam Street](https://fs.blog/feynman-technique/)
- [Diátaxis framework](https://diataxis.fr/)
- [Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning Styles: Concepts and Evidence.](https://journals.sagepub.com/doi/10.1111/j.1539-6053.2009.01038.x) *Psychological Science in the Public Interest, 9*(3), 105–119.
- [Mayer, R. E. — Multimedia Learning principles](https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/8E317F6353F710E69BA62F4856D8FAE9). Cambridge Handbook of Multimedia Learning.
- [Sweller, J., Ayres, P., & Kalyuga, S. (2011). Cognitive Load Theory](https://link.springer.com/book/10.1007/978-1-4419-8126-4). Explorations in the Learning Sciences, Instructional Systems and Performance Technologies.
