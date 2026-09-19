# Module 2: The Educator Mindset: You Are the Director
**Transitioning from Manual Typist to Executive AI Course Architect**  
**Course Reference Series:** Teacher Professional Development Guide  

---

## 1. The Trap of the "AI Typist"

When teachers first experiment with AI tools (like ChatGPT or Claude), they almost always approach it as a **faster typewriter**:
- They type: *"Write me a syllabus for Introduction to Python."*
- The AI spits out a 2-page outline that looks vaguely plausible.
- The teacher reads it, notices it's too high-level, tweaks a few words, and then spends the next 6 hours manually building PowerPoint slides, finding graphics, writing lab exercises, and formatting documents by hand.

In this model, the teacher has not saved meaningful time. The teacher is still doing 95% of the heavy lifting.

---

## 2. The Mental Shift: You Are the Executive Director

To unlock the true power of autonomous agentic platforms (like Google Antigravity), you must completely redefine your role:

> **You are not the typist. You are the Film Director, and the AI Agent is your tireless, lightning-fast, junior production crew.**

```
┌────────────────────────────────────────┐
│      THE EDUCATOR (The Director)       │
├────────────────────────────────────────┤
│ • Decides the vision, theme, and tone  │
│ • Sets non-negotiable quality rubrics  │
│ • Enforces regional and domain context │
│ • Evaluates output with human "taste"  │
│ • Demands revisions when work is weak  │
└───────────────────┬────────────────────┘
                    │ High-Level Steerage
                    ▼
┌────────────────────────────────────────┐
│      THE AI AGENT (The Production Crew)│
├────────────────────────────────────────┤
│ • Writes 1,000 lines of Python code    │
│ • Compiles 40-slide presentation decks │
│ • Runs automated terminal test suites  │
│ • Fixes syntax bugs and indentation    │
│ • Generates complete instructor notes  │
└────────────────────────────────────────┘
```

---

## 3. The 3 Rules of Executive AI Direction

### Rule 1: Never Accept the First Draft
Large Language Models are probabilistic engines. Their first response to any prompt is almost always their **most statistical average response**—which means it is usually generic, superficial, and safe.
- When an agent generates a 20-slide deck, do not say *"Good enough."*
- Say: *"This is too shallow. We need at least 32 slides to cover this without text walls. Decompose each concept into a Why slide, a What diagram slide, and a How code slide. Loop until it's good."*

### Rule 2: Enforce Upfront Structural Rubrics
An agent cannot read your mind. If you tell it to *"make nice slides,"* it has no idea what "nice" means.
- Instead, give it an authoritative specification: [`playbooks/slide_design_playbook.md`](../playbooks/slide_design_playbook.md).
- Tell it: *"All slides must use the 5 archetypes in our playbook. Code must be strictly left-aligned in Consolas with `p.alignment = PP_ALIGN.LEFT`. Decks must end with formal APA bibliographies."*
- Now the agent has an explicit rubric to evaluate its own work against.

### Rule 3: Be the Taste-Maker and Real-World Grounding
The agent has read every computer science textbook in existence, but it has never taught a 19-year-old student who struggles with abstract math, nor does it know the local industries in your county.
- **Your Job:** Inject regional analogies (e.g., irrigation ditches, wind turbines, hospital triage).
- **Your Job:** Inspect typography to make sure titles aren't too small to read from the back of the lecture hall.
- **Your Job:** Ensure ethics, privacy, and local accreditation rules are respected.

---

## 4. The Anatomy of an Effective Teacher Directive

Compare these two prompts:

### The Amateur Prompt (Yields Generic Output):
> *"Make me a slide deck and lab for Unit 4 on Guardrails."*
> - Result: A 12-slide presentation with dense bulleted paragraphs and a non-functional pseudo-code lab.

### The Director's Directive (Yields Production Rigor):
> *"We are building Unit 4: Enterprise Guardrails for sophomore community college students. Use our LCCC brand colors from config.py. The deck must be at least 30 slides, featuring an upfront Objectives & Deliverables slide, followed immediately by the Unit Battle Plan slide. Every code snippet must be strictly left-aligned in Consolas. Build a companion Python lab in `labs/unit04/` that runs in pure standard library with zero paid API keys, testing regex injection filters and DLP canary redaction. Run the lab, run `deck_auditor.py`, and loop until all tests pass with [PASS]."*
> - Result: A 31-slide masterpiece with 100% speaker notes, left-aligned airlock code, an APA bibliography, and an automated test suite passing all assertions.

---

## 5. Key Takeaways

1. **Direct the architecture; delegate the typing.** Your time is too valuable to spend copying and pasting text into PowerPoint shapes.
2. **Hold the AI accountable.** If a script fails, make the agent debug its own traceback.
3. **Bring your authentic human voice.** The AI provides the machinery; you provide the soul, wisdom, and leadership of the course.
