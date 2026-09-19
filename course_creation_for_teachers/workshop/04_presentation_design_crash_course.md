# Module 4: Presentation Design Crash Course for Educators
**The 5 Visual Archetypes, Assertion-Evidence Headlines & The Left-Aligned Code Standard**  
**Course Reference Series:** Teacher Professional Development Guide  

---

## 1. Why PowerPoint Slide Design Matters

In higher education and workforce training, slide presentations are often an afterthought: walls of black text dumped onto default white backgrounds, tiny unreadable code blocks, and bullet points read verbatim by the instructor.

This creates cognitive fatigue and disengages students.

By contrast, an **enterprise-grade instructional deck**:
- Uses **Assertion-Evidence headlines** to deliver clear takeaways.
- Houses content in **visual card containers** with high contrast.
- Formats code strictly with **left-aligned monospaced typography**.
- Embeds rich **speaker notes** so any instructor or substitute can teach the material seamlessly.

---

## 2. The 5 Universal Slide Archetypes

Every presentation generated in our curriculum uses a combination of 5 proven layout archetypes:

```
┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐
│   1. SPLIT-HERO TITLE   │  │   2. SECTION DIVIDER    │  │  3. TWO-COLUMN CARDS    │
│ ┌─────┐ ┌─────────────┐ │  │ ┌─────────────────────┐ │  │ ┌─────────┐ ┌─────────┐ │
│ │ NAVY│ │ Main Title  │ │  │ │ SECTION 02          │ │  │ │ Card A   │ │ Card B   │ │
│ │ HERO│ │ Subtitle    │ │  │ │ Dark Navy Background│ │  │ │ Option A │ │ Option B │ │
│ └─────┘ └─────────────┘ │  │ └─────────────────────┘ │  │ └─────────┘ └─────────┘ │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
┌─────────────────────────┐  ┌─────────────────────────┐
│   4. NORMAL FULL-CARD   │  │   5. LEFT-ALIGNED CODE  │
│ ┌─────────────────────┐ │  │ ┌─────────┐ ┌─────────┐ │
│ │ Sequential Flow /   │ │  │ │ Spec    │ │ Consolas│ │
│ │ 4-Step Checklist    │ │  │ │ Points  │ │ Code    │ │
│ └─────────────────────┘ │  │ └─────────┘ └─────────┘ │
└─────────────────────────┘  └─────────────────────────┘
```

### Archetype 1: Split-Hero Title Slide
Features an institutional brand block on the left (64pt white acronym, gold accent band, program name) paired with a high-impact course title (40pt bold navy) and academic metadata on the right.

### Archetype 2: Section Divider Slide
Full dark section navy (`#002055`) background with a vertical gold accent bar, section number in gold (14pt), and section title in white (36pt). Signals clear cognitive transitions between modules.

### Archetype 3: Two-Column Comparison Cards
The workhorse of technical presentations: Left card (Ice Blue `#F3F7FC`) and Right card (Warm Cream/Gold `#FFDF0`). Perfect for comparing Traditional vs. Modern, Objectives vs. Outcomes, or Domain Track specializations.

### Archetype 4: Normal Full-Width Content Card
A single rounded container (Width: 11.7") with 3 to 4 scannable bold anchor items. Ideal for sequential 4-step execution flows, course trajectories, or failure mode anatomies.

### Archetype 5: The Usable Code & Runbook Slide (Strictly Left-Aligned)
Left card explains the algorithm logic in 3–4 bold anchor points. Right card is a dark midnight slate container (`#111827`) displaying 10–20 lines of clean, usable code in Consolas.

---

## 3. The Assertion-Evidence Headline Standard

Never use passive, generic topic titles on slides:
- **Weak Topic Title:** *"Circuit Breakers"*
- **Strong Assertion Headline:** *"Circuit Breakers Prevent Cascading Infrastructure Collapse"*

- **Weak Topic Title:** *"Latency Analysis"*
- **Strong Assertion Headline:** *"Tail Latency (p95) Matters Far More Than Arithmetic Averages"*

- **Weak Topic Title:** *"Docker Security"*
- **Strong Assertion Headline:** *"Dropping Root Privileges via Dedicated System Users Prevents Container Escapes"*

**The Rule:** A student sitting in the back row who only reads the headlines should understand the entire core narrative of the lecture!

---

## 4. The Critical Left-Aligned Code Standard

### The PowerPoint Centering Bug
> [!WARNING]
> In `python-pptx`, any shape created via `shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE)` **DEFAULTS TO CENTER-JUSTIFIED PARAGRAPHS**.
> If you add code without setting alignment, your code will render center-justified, destroying indentation and rendering it unreadable!

### The Solution:
Every paragraph in a code container must explicitly enforce:
```python
p.alignment = PP_ALIGN.LEFT
p.font.name = "Consolas"
p.font.size = Pt(10.5)
p.font.color.rgb = CODE_TEXT
p.space_after = Pt(1.5)
```
This guarantees crisp, left-aligned syntax with preserved 4-space indentation.

---

## 5. Pacing & Slide Count: The 30–50 Slide Sweetspot

- Presentations with fewer than 25 slides almost always compress complex ideas into unreadable text walls.
- Aim for **30 to 50 slides** per unit.
- Spread ideas across sequential visual slides:
  - Slide 1: The Problem (The Why)
  - Slide 2: The Architecture (The What)
  - Slide 3: The Left-Aligned Code (The How)
  - Slide 4: The Empirical Benchmark Results

---

## 6. Mandatory Academic Bibliography Slide

Every presentation deck must conclude with a formal `References & Further Reading` slide:
- **Left Column:** Foundational peer-reviewed academic papers (APA format).
- **Right Column:** Recognized industry specifications, regulatory standards (NIST, OWASP, ISO), and engineering whitepapers.
- **Purpose:** Gives students scholarly grounding and provides citable sources for their capstone dossiers.
