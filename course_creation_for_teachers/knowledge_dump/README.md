# Knowledge Dump Drop Zones & Intake Pipeline

Welcome to the **Course Knowledge Dump**. This directory is the raw intake hopper for all existing materials, brainstorms, syllabi, and legacy slide decks that will be transformed into enterprise-grade course units.

---

## Drop Zone Directory Structure

| Subfolder | Purpose & Permitted File Types | Processing Action |
| :--- | :--- | :--- |
| `raw_syllabi/` | Institutional syllabi, accreditation documents, program outcomes (`.md`, `.pdf`, `.docx`, `.txt`) | Scanned by `engine/intake_scanner.py` to extract unit counts, duration, and prerequisites. |
| `legacy_decks/` | Old PowerPoint slides, PDF slide exports, Keynote decks (`.pptx`, `.pdf`, `.txt`) | Scanned for slide titles, code snippets, visual diagrams, and speaker notes. |
| `transcripts_and_notes/` | Lecture recordings transcripts, meeting audio transcripts, educator notes (`.vtt`, `.srt`, `.txt`, `.md`) | Analyzed for educator voice, real-world examples, analogies, and classroom banter. |
| `reference_papers/` | Academic papers, vendor documentation, architecture blueprints (`.pdf`, `.md`, `.html`) | Scanned to produce accurate academic bibliographies and technical benchmarks. |
| `brainstorms/` | Scratchpad ideas, napkin sketches, project wishlists, lab ideas (`.md`, `.txt`, `.png`) | Categorized into potential lab challenges, discussion prompts, and capstone themes. |

---

## How to Run the Intake Scanner

Once you have dropped your files into any of the folders above, run the automated intake scanner:

```bash
python engine/intake_scanner.py
```

The scanner will:
1. Traverse all 5 drop zones.
2. Count total artifacts, file formats, and byte sizes.
3. Automatically generate a structured catalog in `knowledge_dump/course_intake_manifest.yaml`.
4. Provide immediate command-line recommendations on which unit templates to instantiate first.

---

## The Intake Workflow

```
[Drop Raw Files] ---> [Run intake_scanner.py] ---> [Inspect manifest.yaml] ---> [Generate Units]
  (PPTX/PDF/MD)        (Auto-cataloging)            (Review Scope)              (Use Templates)
```
