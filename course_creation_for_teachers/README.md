# The Autonomous Course Factory: Turnkey GitHub Template for Educators

> **A battle-tested, zero-cost curriculum engineering framework for secondary, post-secondary, and vocational educators to build production-grade, lab-backed technical courses from soup to nuts.**

[![Course Validation CI](https://github.com/your-org/github_course_creation_for_teachers/actions/workflows/validate_course.yml/badge.svg)](https://github.com/your-org/github_course_creation_for_teachers/actions/workflows/validate_course.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Cloud Budget: $0.00](https://img.shields.io/badge/Cloud%20Budget-%240.00-success.svg)](workshop/05_zero_cost_infrastructure_guide.md)

---

## The Educator's Challenge

Building a modern, rigorous technical curriculum—especially in fast-moving fields like Artificial Intelligence, Cloud Architecture, or Agentic Software—normally requires hundreds of hours:
- Wrestling with PowerPoint alignment, blurry screenshots, and wall-of-text slides.
- Debating vague learning outcomes that fail accreditation audits.
- Debugging student environment issues caused by broken third-party library dependencies.
- Dealing with cloud billing surprises or students without credit cards.
- Scrambling when live classroom demos fail due to campus Wi-Fi drops.

**The Course Factory changes the paradigm.** Instead of acting as a manual typist formatting bullet points, you act as the **Instructional Director**. You provide the domain expertise, learning milestones, and raw knowledge; this repository provides the automated compilation engines, pedagogical guardrails, and deterministic testing infrastructure to produce world-class course deliverables.

---

## What This Repository Contains

```
github_course_creation_for_teachers/
├── .github/
│   ├── workflows/validate_course.yml     # Automated CI quality gate
│   └── ISSUE_TEMPLATE/unit_creation.md   # Step-by-step GitHub issue checklist
├── engine/                               # THE GENERATION & AUDITING ENGINE
│   ├── config.py                         # Single-file institutional rebranding
│   ├── deck_generator.py                 # Universal 16:9 widescreen PPTX compiler
│   ├── deck_auditor.py                   # Automated compliance & accessibility checker
│   └── intake_scanner.py                 # Ingestion scanner for raw syllabi and notes
├── knowledge_dump/                       # 5 ASSET DROP ZONES
│   ├── raw_syllabi/                      # Syllabi, course descriptions, accreditation
│   ├── legacy_decks/                     # Old PPTX, PDF, Keynote slides
│   ├── transcripts_and_notes/            # Lecture recordings, speech-to-text, notes
│   ├── reference_papers/                 # Whitepapers, literature, documentation
│   ├── brainstorms/                      # Napkin sketches, lab ideas, project wishlists
│   └── course_intake_manifest.yaml       # Structured YAML catalog of all assets
├── templates/                            # PRODUCTION-GRADE PEDAGOGICAL TEMPLATES
│   ├── competency_map_template.md        # ABET / Bloom's aligned competency matrix
│   ├── instructional_guide_template.md   # Comprehensive educator delivery guide
│   ├── code_lab_template.py              # Pure standard-library Python lab scaffold
│   ├── peer_review_rubric_template.md    # 20-Point double-blind student rubric
│   ├── capstone_defense_rubric_template.md # 100-Point summative jury rubric
│   └── demo_contingency_runbook_template.md # 3-Tier failover for classroom presentations
├── workshop/                             # 1-DAY PROFESSIONAL DEVELOPMENT SYLLABUS
│   ├── 01_workshop_syllabus_and_schedule.md # Hour-by-hour educator training plan
│   ├── 02_educator_mindset_the_director.md # Mental shift: Human-as-Director
│   ├── 03_the_why_what_how_pedagogy_guide.md # Bloom's verbs, Problem-First flow
│   ├── 04_presentation_design_crash_course.md # 5 visual archetypes & left-aligned code
│   └── 05_zero_cost_infrastructure_guide.md # Running on $0.00 with Ollama/Gemini/Groq
├── starter_sample/                       # TURNKEY REFERENCE IMPLEMENTATION
│   ├── sample_unit_spec.py               # Working 31-slide unit presentation spec
│   ├── sample_unit_deck.pptx             # Pre-compiled reference presentation
│   └── README.md                         # Quickstart guide for the sample
├── requirements.txt                      # Zero bloat: only python-pptx
└── README.md                             # You are here
```

---

## 5-Minute Quickstart

### 1. Clone & Install Dependencies
Clone this repository to your local computer or classroom lab machine:

```bash
git clone https://github.com/your-org/github_course_creation_for_teachers.git
cd github_course_creation_for_teachers
pip install -r requirements.txt
```

### 2. Verify with the Starter Sample (Immediate "Quick Win")
Compile the reference 31-slide unit presentation and run the automated auditor:

```bash
# 1. Compile the 31-slide starter presentation
python starter_sample/sample_unit_spec.py

# 2. Audit the generated presentation for quality & pedagogical compliance
python engine/deck_auditor.py starter_sample/sample_unit_deck.pptx
```

You should see:
```text
Slide Count Pacing (>=30):        [PASS]
100% Speaker Notes Coverage:      [PASS]
Objectives & Outcomes Slide:      [PASS]
Battle Plan Alignment Slide:      [PASS]
Strict Left-Aligned Code:         [PASS]
References & Bibliography Slide:  [PASS]
Anti-Text-Wall Density Check:     [PASS]
======================================================================
OVERALL AUDIT STATUS: [PASS] DECK APPROVED FOR DELIVERY
======================================================================
```

### 3. Rebrand to Your Institution in 60 Seconds
Open `engine/config.py` and customize your institutional metadata:

```python
INSTITUTION_NAME = "Cascadia Institute of Technology"
INSTITUTION_ACRONYM = "CIT"
DEPARTMENT_NAME = "Department of Computer Science & Artificial Intelligence"
COURSE_CODE = "CS-401"
COURSE_TITLE = "Autonomous Agent Systems & Control Loops"
```

Now, every presentation compiled by `engine/deck_generator.py` will automatically adopt your institution's name, brand colors, and header/footer metadata.

---

## The Course Creation Workflow

```
+-----------------------------------------------------------------------------------+
|                           THE 5-STEP COURSE PIPELINE                              |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  1. INTAKE            Drop raw syllabi, old PPTs, and notes into knowledge_dump/  |
|                       Run: python engine/intake_scanner.py                        |
|                                                                                   |
|  2. MAP & PLAN        Copy templates/competency_map_template.md                   |
|                       Define Bloom's Level 3-6 measurable competencies           |
|                                                                                   |
|  3. CODE LABS         Copy templates/code_lab_template.py                         |
|                       Build pure standard-library, assertion-tested exercises     |
|                                                                                   |
|  4. SLIDE SPEC        Write unit spec following starter_sample/sample_unit_spec.py|
|                       Compile: python engine/deck_generator.py                    |
|                                                                                   |
|  5. AUDIT & GATE      Verify quality: python engine/deck_auditor.py <deck.pptx>   |
|                       Push to GitHub; automated CI validates integrity            |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## Key Pedagogical & Technical Standards

### 1. The Mandatory Slide 7 & Slide 8 Contract
Every presentation generated in this framework enforces an instructional contract with students:
- **Slide 7 (Learning Objectives & Measurable Outcomes)**: Stated in unambiguous language using Bloom's Taxonomy action verbs (e.g., *Analyze*, *Synthesize*, *Construct*—never vague verbs like *understand*).
- **Slide 8 (The Battle Plan)**: Explicitly explains how the slides will connect the theory directly to today's lab outcomes and graded deliverables.

### 2. Strict Left-Aligned Code Typography
Standard presentation templates default to centering all text in shapes, rendering indented Python code completely illegible. The `engine/deck_generator.py` compiler programmatically enforces:
- Dark slate code container (`#0F172A`)
- Crisp monospace typography (`Consolas` or `Courier New`)
- **Strict Left Alignment (`p.alignment = PP_ALIGN.LEFT`)** across 100% of code lines
- Syntax-friendly font sizing (11pt to 13pt) with explicit line-height buffers

### 3. Five Visual Archetypes (Anti-Boredom Pacing)
Never present 30 identical bulleted slides. The generator provides 5 distinct visual archetypes:
1. **Title & Hero Slide**: Split navy/gold institutional branding.
2. **Split Concept Slide**: Comparative two-column cards with dark navy and teal accents.
3. **Three-Card Grid**: Balanced horizontal cards for 3-phase pipelines or architecture tiers.
4. **Warning & Trap Slide**: High-visibility rose/crimson card alerting students to critical failure modes.
5. **Code Demonstration Slide**: Left-hand concept card paired with right-hand left-aligned syntax container.

### 4. 100% Speaker Notes Coverage
Slides are visual anchors for students, not teleprompters for educators. Every slide must contain 5–7 sentences of complete speaker notes detailing:
- The verbal narrative script
- Classroom delivery instructions
- Socratic discussion prompts
- Common student misconceptions to address

### 5. Academic & Industry Bibliographies
Every unit concludes with a formal bibliography citing foundational academic papers (e.g., ReAct, Toolformer, Constitutional AI) and industry architecture blueprints (e.g., Anthropic, OWASP, NIST).

### 6. Zero-Cost Infrastructure ($0.00 Cloud Budget)
Detailed in `workshop/05_zero_cost_infrastructure_guide.md`:
- **Local Sovereign Compute**: Run quantized models (Llama 3.2 3B, Qwen 2.5-Coder 1.5B/7B) offline via Ollama.
- **Zero-Credit-Card Cloud Tiers**: Leverage Google AI Studio (Gemini Flash, 15 RPM) and GroqCloud LPUs.
- **Deterministic CI Testing**: Use Python standard library mock fixtures for offline, cost-free student grading.

---

## Using This Repository in a Workshop

This repository is ready to be used as a hands-on Professional Development workshop for teachers. See `workshop/01_workshop_syllabus_and_schedule.md` for the complete 1-day (6-hour) or 5-evening schedule:

| Time | Session | Hands-On Deliverable |
| :--- | :--- | :--- |
| **09:00 - 10:00** | The Mindset Shift: Teacher as Instructional Director | Configure `engine/config.py` |
| **10:00 - 11:15** | Knowledge Intake & Competency Architecture | Run `engine/intake_scanner.py` & draft competency map |
| **11:30 - 12:30** | Presentation Engineering & Visual Archetypes | Compile & audit `sample_unit_deck.pptx` |
| **13:30 - 14:45** | Deterministic Code Labs & Zero-Cost Infrastructure | Build an assertion-based standard library lab |
| **15:00 - 16:00** | Rubrics, Summative Defenses & Continuous Delivery | Push to GitHub; pass GitHub Actions CI |

---

## Automated GitHub Actions CI Gate

When you or your students push to this repository, `.github/workflows/validate_course.yml` automatically executes:
1. Syntax and lint verification across all Python scripts.
2. Compilation test of starter unit specifications.
3. Automated compliance audit of generated presentations using `engine/deck_auditor.py`.
4. Verification that lab templates pass standard library `unittest` suites.

---

## Contributing & License

This template is open-source under the **MIT License**. Educators, instructional designers, and curriculum engineers are encouraged to fork, adapt, and share this framework across schools and universities worldwide.
