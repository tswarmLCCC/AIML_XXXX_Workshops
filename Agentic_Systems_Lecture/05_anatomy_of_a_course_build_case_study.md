# Module 5: Anatomy of a Course Build (A Live Case Study)
**Forensic Retrospective: How an 8-Week Workforce Curriculum & Reusable Template Were Built from Scratch**  
**Course Reference Series:** Agentic Software Engineering & Curriculum Design  

---

## 1. Executive Summary: What Was Accomplished

Over the course of this development journey, an instructor and an autonomous AI agent collaborated to modernize and produce a complete, accredited, 8-week technical curriculum for **Laramie County Community College (LCCC)** entitled:
**"AI in the Workforce: Technical Implementation & Industry Tracks"** (Concurrent Corequisite with `AI ML 2060 Capstone`).

### The Final Deliverables Inventory:
- **8 Production Presentation Decks:** Fully styled, branded `.pptx` files totaling **297 slides** (average 37 slides per unit, all >= 30 slides).
- **8 Hands-On Python Code Labs:** Verified, deterministic assertion-based test suites running in pure Python without paid API hurdles.
- **8 Comprehensive Instructional Guides:** Complete pedagogical guides with executive summaries, Why->What->How modules, and formal APA bibliographies.
- **2 Institutional Rubrics:** A 20-point Capstone Peer Review Audit Rubric and a 100-point Official Capstone Defense Evaluation Rubric.
- **1 Live Demo Contingency Runbook:** A 3-minute live demonstration flight script with a 3-tier failover matrix.
- **1 Portable Course Creation Factory:** A completely modularized, reusable template folder (`course_creation_template/`) that can be taken to any future subject.

This module provides a **forensic step-by-step deconstruction** of how this monumental project was engineered from raw prompts to verified production.

---

## 2. Phase-by-Phase Forensic Breakdown

```
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: FOUNDATION & STANDARDS SETTING                                 │
│ - Legacy benchmarking & initial template analysis                       │
│ - Authoring `rubric.md` and `course_slide_design_playbook.md`           │
│ - Establishing LCCC Golden Eagles branding & WCAG AAA contrast          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: UNITS 1 - 5 (CORE TECHNICAL DEVELOPMENT)                       │
│ - Unit 1: Sovereign Silicon, Quantization & Infrastructure (50 slides)   │
│ - Unit 2: Industry Tracks & Intel 4Ws Problem Formulation (45 slides)   │
│ - Unit 3: Agent Foundations I (ReAct & Claude Blueprints) (36 slides)   │
│ - Unit 4: Agent Foundations II (Enterprise Guardrails & Airlocks) (31s) │
│ - Unit 5: Agent Foundations III (Multi-Agent Swarms & Sandboxes) (30s)  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: UNITS 6 - 8 (HARDENING, INTEGRATION & DEFENSE)                 │
│ - Unit 6: Chaos Engineering, Circuit Breakers & Stress Fuzzing (35s)    │
│ - Unit 7: Capstone Integration Sprint & 20-Pt Peer Review Audit (35s)   │
│ - Unit 8: Capstone Defense Rehearsal (Zero New Tech Concepts) (35s)     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: MASTER VERIFICATION & REGRESSION AUDITING                      │
│ - Running automated auditor `audit_any_deck.py` across all 8 decks      │
│ - Executing all 8 Python code lab assertion test suites                 │
│ - Verifying 100% pass status across notes, code alignment & biblios     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 5: SYSTEM-LEVEL GENERALIZATION & TEMPLATE EXTRACTION              │
│ - 5-loop analytical review of the entire curriculum                     │
│ - Authoring `course_creation_template/` with knowledge_dump drop zones  │
│ - Writing parameterized `config.py`, universal generator & auditor      │
│ - End-to-end verification of the 31-slide reference implementation      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Deep Dive into Critical Engineering Turning Points

### Turning Point 1: Overcoming "Summary Mode" via Visual Scaffolding
In early prototype attempts, LLM slide generators produced 15-to-20 slide decks. These decks suffered from severe cognitive overload: 8 bullets crammed onto a slide, unformatted code, and generic bullet points.

The human intervened, establishing the rule that **complex engineering units require 30 to 50 slides**. By expanding the slide count, the agent was able to decompose concepts progressively:
1. Slide A: The Historical Bottleneck / Real-World Problem (The "Why")
2. Slide B: The High-Level Architectural Solution (The "What")
3. Slide C: The Usable Left-Aligned Code Implementation (The "How")
4. Slide D: The Empirical Benchmarks & Fault Injection Results

### Turning Point 2: Stripping Master Layouts & Enforcing Brand Identity
The workspace contained legacy presentation templates from prior corporate partnerships (e.g., Intel AI). The human directed the agent to strip away legacy third-party branding and establish an authentic collegiate brand:
- The agent wrote an automated cleaner in python-pptx that inspected `prs.slide_masters`, detected `Picture` shapes (shape type 13) and logo names, and cleanly removed them from XML layouts.
- It then introduced the **LCCC Golden Eagles** color system: Deep Navy (`#003278`), Dark Section Navy (`#002055`), Bright Gold (`#FFC001`), Warm Gold (`#BE8700`), and Charcoal Body Text (`#1F2937`), delivering a stunning 11:1 contrast ratio against white.

### Turning Point 3: The Left-Aligned Code Discovery
When displaying technical code on slides (e.g., Python airlocks, circuit breakers, and Dockerfiles), the code was initially rendering center-justified, destroying indentation.

By investigating `python-pptx`, the agent discovered that `MSO_SHAPE.ROUNDED_RECTANGLE` defaults to centered paragraph text. To solve this permanently, the agent built a dedicated **Code Container Archetype**:
```python
lines = code_snippet.strip().split("\n")
for l_idx, line in enumerate(lines):
    p = tf_c.paragraphs[0] if l_idx == 0 else tf_c.add_paragraph()
    p.text = line if line else " "
    p.font.name = "Consolas"
    p.font.size = Pt(10.5)
    p.font.color.rgb = CODE_TEXT
    p.alignment = PP_ALIGN.LEFT  # <--- Strictly enforced left-alignment
    p.space_after = Pt(1.5)
```
This single standard made all code slides across Units 1 through 8 crisp, readable, and professional.

### Turning Point 4: Enforcing the Unit 8 Boundary
When approaching the final week of the curriculum, many instructors and AI models make the fatal mistake of introducing more technical topics (e.g., advanced neural network topics or new frameworks).

The human established a strict, non-negotiable pedagogical boundary:
> **Unit 8 introduces ZERO new technical concepts.**

Instead, Unit 8 was engineered as an intensive **Capstone Defense Rehearsal**:
- Teaching the 15-minute presentation architecture (3 min problem ROI, 4 min architecture, 3 min live demo, 5 min Q&A).
- Creating the 3-minute live demonstration flight script.
- Implementing the 3-tier contingency failover matrix (Local live -> Mock replay -> Video trace) so students never panic when live demos fail.
- Drilling responses to hostile panel cross-examination questions.

---

## 4. The Creation of `course_creation_template/`

In the final phase, the human directed the agent to package the entire methodology into a portable, reusable template folder.

Rather than hastily copying files, the agent conducted **five systematic review loops**:
1. **Review Loop 1 (Pedagogy & Scaffolding):** Captured the "Why->What->How" cadence, Bloom's taxonomy mapping, Slide 7 (Objectives & Deliverables), and Slide 8 (The Battle Plan).
2. **Review Loop 2 (Visual Design & Layouts):** Captured the 5 slide archetypes, assertion-evidence headlines, and WCAG AAA contrast standards.
3. **Review Loop 3 (Code Formatting & Usability):** Captured the strict left-alignment recipe, monospaced Consolas styling, and usable code standards.
4. **Review Loop 4 (Lab Toolkits & Sovereign Compute):** Captured the assertion-based testing harness, pure Python standard library design, and clean ASCII reporting (`[PASS]`).
5. **Review Loop 5 (Quality Assurance & Ingestion):** Captured the automated auditor (`audit_deck.py`), the `knowledge_dump/` drop-zone intake pipeline, and the 20-point/100-point rubrics.

The resulting template was tested out-of-the-box by compiling and auditing a 31-slide reference unit presentation with 100% passing checks.

---

## 5. Master Verification Metrics

To prove the production integrity of the entire curriculum, a master test runner was executed across the entire repository:

```
======================================================================
MASTER CURRICULUM AUDIT RESULTS
======================================================================
[PASS] Unit01_Enterprise_Infrastructure.pptx (50 slides) - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit02_Industry_Tracks.pptx (45 slides)           - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit03_Agent_Foundations_I.pptx (36 slides)       - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit04_Agent_Foundations_II.pptx (31 slides)      - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit05_Agent_Foundations_III.pptx (30 slides)     - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit06_Hardening_Stress_Testing.pptx (35 slides)  - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit07_Capstone_Integration.pptx (35 slides)      - 100% Notes, Left-Aligned Code, Biblio
[PASS] Unit08_Capstone_Defense.pptx (35 slides)          - 100% Notes, Left-Aligned Code, Biblio
----------------------------------------------------------------------
TOTAL BRANDED SLIDES GENERATED: 297 SLIDES

=== ALL HANDS-ON CODE LABS VERIFICATION ===
[PASS] Unit 1 (unit01_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 2 (unit02_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 3 (unit03_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 4 (unit04_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 5 (unit05_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 6 (unit06_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 7 (unit07_code_lab.py)       - 100% Assertions Passed
[PASS] Unit 8 (unit08_rehearsal_lab.py)  - 100% Assertions Passed
======================================================================
ALL 8 WEEKS FULLY GENERATED, TESTED & AUDITED!
======================================================================
```

---

## 6. What This Means for the Future of Computer Science Education

For decades, creating a new high-rigor, accredited, 8-week computer science course required an entire committee of faculty working for 6 to 12 months: drafting syllabi, writing slide decks by hand, creating sample code labs, and writing rubrics.

By pairing a human subject-matter director with an autonomous agentic development platform:
1. **Development time collapsed from 9 months to hours.**
2. **Quality increased:** Every slide has explicit speaker notes, high contrast, left-aligned code, and formal academic citations.
3. **Reproducibility is guaranteed:** Every lab is backed by automated test suites that students can run on their own hardware without paid API subscriptions.
4. **The process is institutionalized:** By creating `course_creation_template/`, the college now possesses an enduring curriculum factory that can produce future courses across any domain with identical rigor.

This is the true promise of Agentic AI: not replacing the educator, but **amplifying the educator's reach, standards, and impact by orders of magnitude.**
