# Starter Sample Unit: Autonomous Agent Architecture & Deterministic Guardrails

This directory contains a complete, working, production-grade 31-slide unit presentation specification (`sample_unit_spec.py`) that demonstrates every single pedagogical and aesthetic standard in this repository.

---

## Why This Sample Exists

In a teacher workshop or when cloning this repository for the first time, educators need an immediate **"Quick Win"** to verify that their environment works and to see what a completed unit specification looks like before creating their own.

This sample serves as the golden standard reference:
- **31 Slides** (within the optimal 30-50 slide pacing target).
- **Slide 7: Measurable Learning Objectives** mapped to Bloom's Taxonomy.
- **Slide 8: The Battle Plan** explicitly connecting lecture objectives to the lab outcome.
- **Slide 31: Academic & Industry Bibliography** citing foundational research (ReAct, Toolformer, OWASP Top 10, Anthropic Blueprints).
- **100% Left-Aligned Code Snippets** (`PP_ALIGN.LEFT`) with syntax highlighting and defensive structure.
- **100% Complete Speaker Notes** (5-7 sentences per slide with classroom instructions, delivery tips, and discussion prompts).
- **Five Visual Archetypes**: Title, Split Concept, 3-Card Grid, Warning/Caution, and Code Demonstration.

---

## How to Compile the Sample Deck

From the root of this repository:

```bash
python starter_sample/sample_unit_spec.py
```

This will output `starter_sample/sample_unit_deck.pptx` in seconds.

---

## How to Audit the Sample Deck

To verify that the generated deck meets all institutional standards:

```bash
python engine/deck_auditor.py starter_sample/sample_unit_deck.pptx
```

The auditor will inspect all 31 slides and verify:
- Complete speaker notes coverage (0 missing notes)
- Presence of Learning Objectives and Battle Plan
- Left-aligned code blocks
- Final Bibliography slide
- Total slide count within bounds (30-50)
