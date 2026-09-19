---
name: Unit Development Checklist
about: Track the creation, lab verification, and presentation audit for a new unit
title: "Unit [XX]: [Topic Name]"
labels: ["curriculum-unit"]
assignees: ""
---

## Unit [XX]: [Topic Name] Development Checklist

### 1. Ingestion & Scoping
- [ ] Raw syllabus requirements / lecture notes placed in `knowledge_dump/`
- [ ] Problem formulation defined using the "Why -> What -> How" cadence
- [ ] Learning Objectives (Bloom's Taxonomy) & Concrete Deliverables documented

### 2. Instructional Materials
- [ ] Created `output/week-XX/instructional_guide.md` using `templates/instructional_guide_template.md`
- [ ] Embedded regional / physical world analogies
- [ ] Added formal academic bibliography (peer-reviewed papers & industry standards)

### 3. Hands-On Code Lab
- [ ] Created `labs/unitXX/unitXX_code_lab.py` using `templates/code_lab_template.py`
- [ ] Pure standard library execution verified (zero paid API dependencies)
- [ ] Clean ASCII test output (`[PASS]` / `[FAIL]`) verified
- [ ] Automated verification suite passing 100% assertions locally

### 4. Slide Deck Presentation
- [ ] Created unit specification script (targeting 30–50 slides)
- [ ] Compiled presentation using `engine/deck_generator.py`
- [ ] Slide 7 (Learning Objectives & Measurable Deliverables) present
- [ ] Slide 8 (The Unit Battle Plan Alignment) present
- [ ] Strictly left-aligned code blocks verified (`p.alignment = PP_ALIGN.LEFT`)
- [ ] Slide 35 (References & Further Reading) bibliography present
- [ ] 100% speaker notes coverage verified

### 5. Quality Assurance Gate
- [ ] Executed `python engine/deck_auditor.py path/to/deck.pptx` -> **PASS**
- [ ] Git committed and pushed to GitHub
- [ ] GitHub Actions CI passing cleanly
