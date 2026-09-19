# Educator Workshop: Autonomous Course Creation with AI
**1-Day Intensive Faculty Professional Development & Hands-On Training**  
**Audience:** Community College Faculty, University Instructors, High School CTE Educators, Industry Trainers  
**Prerequisites:** Laptop with Python 3.11+, Git, and VS Code / Antigravity installed (Zero AI background required)  

---

## 1. Workshop Mission & Objectives

By the end of this 1-day hands-on workshop, every educator in attendance will:
1. **Escape "Summary Mode":** Understand why unconstrained AI produces shallow outlines and how visual rubrics enforce rigorous curriculum depth.
2. **Master the Director Mindset:** Adopt the Human-in-the-Loop (HITL) methodology—acting as the executive taste-maker and architect while letting the AI agent handle repetitive file creation and testing.
3. **Ingest Existing Course Assets:** Stage their existing syllabi, old slide decks, and lecture transcripts into an automated intake pipeline.
4. **Publish Unit 1 of Their Own Course:** Author a complete, branded instructional guide, a working assertion-based Python lab, and a 30+ slide presentation deck with strictly left-aligned code and formal bibliographies.
5. **Establish Continuous Quality Assurance:** Run automated quality audit scripts that verify slide notes, code alignment, and anti-text-wall density before delivery.

---

## 2. Hour-by-Hour Workshop Flight Schedule

```
┌─────────────────────────────────────────────────────────────────────────┐
│ MORNING SESSION: FOUNDATIONS, INGESTION & COMPETENCY MAPPING            │
├─────────────────────────────────────────────────────────────────────────┤
│ 09:00 - 09:45 (45 min) | Module 1: The Paradigm Shift (Chatbots vs. Agents)
│   - Why ChatGPT in a browser fails at course creation.                  │
│   - Introducing the Agentic Operating System (Hands, Eyes, State).      │
│   - Hands-on: Cloning this repository and running the verification test.│
├─────────────────────────────────────────────────────────────────────────┤
│ 09:45 - 10:45 (60 min) | Module 2: The Raw Knowledge Ingestion Pipeline │
│   - Staging legacy syllabi and PowerPoint decks in `knowledge_dump/`.   │
│   - Configuring `knowledge_dump/course_intake_manifest.yaml`.          │
│   - Executing `python engine/intake_scanner.py`.                        │
├─────────────────────────────────────────────────────────────────────────┤
│ 10:45 - 11:00 (15 min) | Break & Workstation Assistance                 │
├─────────────────────────────────────────────────────────────────────────┤
│ 11:00 - 12:00 (60 min) | Module 3: Backward Design & Competency Mapping │
│   - The "Why -> What -> How" problem-first pedagogical cadence.         │
│   - Mapping Bloom's Taxonomy knowledge to concrete student deliverables.│
│   - Dual-Course Synchronization (Workforce Incubator + Capstone).       │
│   - Deliverable: Completing your 8-week `competency_map.md`.            │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│ LUNCH BREAK (12:00 - 01:00 PM)                                          │
└─────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────┐
│ AFTERNOON SESSION: CODE LABS, SLIDES & QUALITY AUDITING                 │
├─────────────────────────────────────────────────────────────────────────┤
│ 01:00 - 02:00 (60 min) | Module 4: Hands-On Lab Engineering & Toolkits │
│   - Building assertion-based Python test suites (`assert condition`).   │
│   - Running in pure standard library (zero paid third-party API keys).  │
│   - Clean ASCII reporting (`[PASS]` / `[FAIL]`) for console safety.     │
│   - Hands-on: Modifying and executing `templates/code_lab_template.py`. │
├─────────────────────────────────────────────────────────────────────────┤
│ 02:00 - 03:15 (75 min) | Module 5: Automated Presentation Engineering   │
│   - Customizing institutional brand colors and fonts in `engine/config.py`.
│   - The 5 slide archetypes (Title, Divider, Two-Column, Normal, Code).  │
│   - The Left-Aligned Code imperative (`p.alignment = PP_ALIGN.LEFT`).   │
│   - Mandatory Slides: Slide 7 (Objectives), Slide 8 (Battle Plan), Biblio│
│   - Hands-on: Compiling your Unit 1 deck using `engine/deck_generator.py`│
├─────────────────────────────────────────────────────────────────────────┤
│ 03:15 - 03:30 (15 min) | Afternoon Coffee Break                         │
├─────────────────────────────────────────────────────────────────────────┤
│ 03:30 - 04:30 (60 min) | Module 6: Automated Auditing & Peer Review     │
│   - Running `python engine/deck_auditor.py` on your generated `.pptx`.  │
│   - Fixing notes coverage, text-wall warnings, and code alignment live. │
│   - Conducting a 20-point peer review audit with a fellow educator.     │
├─────────────────────────────────────────────────────────────────────────┤
│ 04:30 - 05:00 (30 min) | Showcase, CI/CD GitHub Push & Graduation      │
│   - Pushing your new course repository to GitHub.                       │
│   - Observing the GitHub Actions CI workflow pass all tests in the cloud!
│   - Closing remarks & next steps for building Units 2 through 8.        │
└─────────────────────────────────────────────────────────────────────────┘
```
