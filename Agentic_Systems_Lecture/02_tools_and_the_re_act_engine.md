# Module 2: Tools & The ReAct Engine
**Demystifying Function Calling, Tool Schemas, and the Thought-Action-Observation Loop**  
**Course Reference Series:** Agentic Software Engineering & Curriculum Design  

---

## 1. Demystifying Tools: What is a "Tool" in AI?

When newcomers hear that an AI agent is "using a tool," they often imagine something magical or science-fictional—as if the neural network has sprouted robotic arms or plugged directly into the motherboard.

The reality is vastly simpler, cleaner, and more elegant: **A tool is just a JSON Schema contract between the model and the host software harness.**

### 1.1 The Model Does NOT Execute Code Internally
A language model only ever generates text tokens. It has no physical connection to your CPU, hard drive, or terminal.

When an AI platform equips an LLM with tools:
1. The harness injects a list of **Tool Declarations** into the model's system prompt. Each tool declaration specifies the function's name, description, and expected parameters in JSON Schema.
2. When the model decides it needs to perform an action (e.g., read a file), it stops generating conversational text and generates a **structured tool call block**.
3. The host application (e.g., Google Antigravity) intercepts this structured block, pauses token generation, executes the function natively on your computer, captures the output, and feeds it back into the model's prompt as a **Tool Response (Observation)**.
4. The model reads the observation and continues reasoning!

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. LLM Generates Tool Call Request (JSON)                                │
│    {"name": "view_file", "parameters": {"AbsolutePath": "rubric.md"}}   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. Host Harness Intercepts Request                                      │
│    (Python/Go client running on your machine)                           │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. Native Operating System Execution                                    │
│    Reads "c:\dev\capstone_and_workforce\rubric.md" from NVMe drive      │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 4. Host Formats Observation & Appends to Context                        │
│    Role: TOOL_RESPONSE | Content: "# Comprehensive Course Rubric..."    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 5. LLM Reads Observation & Resumes Token Generation                     │
│    "I have analyzed the rubric. Now I will generate the slide deck..."  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Core Toolbelt Used in Our Course Build

Throughout our 8-week curriculum generation and template construction, our agent leveraged a precise, specialized toolbelt. Understanding these tools helps students see how software development is automated:

### Tool 1: `view_file` (Targeted File Inspection)
- **Why it exists:** Naively reading an entire 5,000-line codebase into an LLM will instantly blow past context window limits, degrading reasoning quality and wasting tokens.
- **How it works:** Accepts `AbsolutePath`, `StartLine`, and `EndLine`.
- **How we used it:** We used `view_file` to read the first 100 lines of `scripts/generate_unit06_deck.py` to inspect the slide data structure, and then read lines 860–935 to verify how code paragraphs were styled.

### Tool 2: `write_to_file` (Atomic File Creation & Overwrite)
- **Why it exists:** Enables the agent to create brand-new source code files, presentations, test suites, or documentation artifacts from scratch.
- **How it works:** Accepts `TargetFile`, `CodeContent`, `Overwrite` boolean, and `ArtifactMetadata`.
- **How we used it:** We used `write_to_file` to generate entire scripts (like `scripts/generate_unit07_deck.py` and `labs/unit07/unit07_code_lab.py`) in a single atomic disk operation.

### Tool 3: `replace_file_content` (Surgical Code Refactoring)
- **Why it exists:** When you only need to fix a 5-line bug inside an 800-line script, overwriting the entire file is slow and expensive.
- **How it works:** Uses exact string matching (`TargetContent` and `ReplacementContent`) bounded by a line range (`StartLine` and `EndLine`).
- **How we used it:** When fixing a small typographical error or tweaking an import path, `replace_file_content` surgically swaps the lines without touching the rest of the file.

### Tool 4: `run_command` (Terminal Subprocess Execution)
- **Why it exists:** Code that cannot be run cannot be verified. This tool gives the agent a live shell (PowerShell on Windows, Bash on Linux/macOS).
- **How it works:** Takes `CommandLine`, `Cwd`, and `WaitMsBeforeAsync`. Executes inside a sandboxed environment by default. Captures return codes, `stdout`, and `stderr`.
- **How we used it:**
  - Running deck generators: `python scripts/generate_unit06_deck.py`
  - Running automated audits: `python scripts/audit_any_deck.py output/week-6/...`
  - Running test labs: `python labs/unit07/unit07_code_lab.py`
  - Verifying alignment: Running Python one-liners to inspect PowerPoint paragraph shapes.

### Tool 5: `manage_task` (Asynchronous Job Supervision)
- **Why it exists:** Some commands take minutes or hours (e.g., training a deep neural network, compiling a massive Docker container, running 500 integration tests). An agent cannot block the UI indefinitely waiting for completion.
- **How it works:** Sends long-running processes to the background as background tasks (`task-xxx`). Provides `list`, `status`, `send_input`, and `kill` actions. The agent receives an automatic wakeup notification when the task terminates.

### Tool 6: `list_dir`, `find_by_name`, `grep_search` (Codebase Exploration)
- **Why they exist:** Allows the agent to explore unfamiliar repositories, locate files matching glob patterns (`*.pptx`, `unit*_code_lab.py`), and search for specific function names across thousands of files using ripgrep.

---

## 3. The ReAct Architecture: Thought -> Action -> Observation

The operational loop that ties all these tools together is called **ReAct** (Reasoning + Acting), first formalized by Yao et al. (ICLR 2023).

Before ReAct, AI models either:
- **Only Reasoned (Chain-of-Thought):** Great for solving math puzzles in isolation, but unable to interact with external databases or verify claims against reality.
- **Only Acted (Tool Use without Thinking):** Executed tools reflexively without forming a coherent, multi-step plan, frequently getting stuck in repetitive loops.

ReAct interleaves internal reasoning with external tool execution:

```
[ USER REQUEST: "Generate Unit 7 Deck and Audit It" ]
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 1 (Internal Reasoning):                        │
│ "I need to check if the Unit 7 instructional guide     │
│ and lab exist. Let me list the directories."           │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ ACTION 1 (Tool Call):                                  │
│ run_command: python -c "import os; print(os.listdir())"│
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ OBSERVATION 1 (Tool Response):                         │
│ output/week-7 exists: False, labs/unit07 exists: False │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ THOUGHT 2 (Internal Reasoning):                        │
│ "Neither directory exists. I must write the guide,     │
│ create the lab, then write the generator script."      │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ ACTION 2 (Tool Call):                                  │
│ write_to_file: output/week-7/instructional_guide.md    │
└────────────────────────────────────────────────────────┘
```

---

## 4. Real-World Case Study: Discovering the PowerPoint Centering Bug via ReAct

One of the most powerful demonstrations of the ReAct engine occurred during our Unit 6 slide deck generation:

1. **Human Critique:** The user pointed out: *"when you show code like you do in the hospital slide here, make sure it's left-aligned. Yours is center-justified and it's almost unreadable."*
2. **Agent Thought:** *"Why was the code center-aligned? Let me inspect the python-pptx script to see how the code box was constructed."*
3. **Action:** Call `view_file` on `scripts/generate_unit06_deck.py` around line 880.
4. **Observation:** The code container was created using `MSO_SHAPE.ROUNDED_RECTANGLE`.
5. **Thought:** *"Root cause identified: PowerPoint shapes default to center-alignment. In python-pptx, simply adding text to a shape centers it unless `p.alignment = PP_ALIGN.LEFT` is explicitly assigned to every paragraph."*
6. **Action:** Rewrite the generator loop to import `PP_ALIGN` and set `p.alignment = PP_ALIGN.LEFT` on every line.
7. **Action:** Run the generator, then run a Python verification one-liner inspecting slide paragraph shapes.
8. **Observation:** Console outputs: `Slide 18 code paragraph alignment: LEFT (1)`.
9. **Final Thought:** *"Bug resolved. The code is now strictly left-aligned."*

Without the ability to view files, write files, run terminal commands, and observe outputs in a continuous loop, fixing this subtle graphical bug would have required the human to manually search documentation, edit code in VS Code, and re-test by hand.

---

## 5. Key Takeaways for Students

1. **Tools are deterministic APIs.** The LLM is stochastic (probabilistic), but the tools it calls are deterministic (Python, bash, OS syscalls). Combining them gives you probabilistic creativity with deterministic precision.
2. **Context economy matters.** Good agent engineering requires surgical tool design. Never dump entire repositories into the prompt when targeted slices (`view_file` or `grep_search`) will do.
3. **The ReAct loop is self-correcting.** An agent's strength is not that it never makes mistakes—it's that it can observe its mistakes in the terminal and fix them autonomously before reporting back to the user.
