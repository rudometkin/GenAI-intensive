---
name: product-pipeline
description: This skill should be used when the user asks to "run the full product pipeline", "from idea to product", "analyze the product fully", "product pipeline", "full product analysis", "from idea to product", or mentions running market research + JTBD + TZ as a combined workflow. Orchestrates the full product analysis pipeline by calling specialized skills in sequence, managing state via PROJECT.md Plan, and storing all outputs in a shared project folder.
---

# Product Pipeline -- Orchestrator

Orchestrator that runs the full product analysis pipeline by calling specialized skills (`/market-research`, `/jtbd-analysis`) in sequence. Manages state via PROJECT.md Plan checkboxes, passes context between steps, and stores all outputs in the project files directory.

## When to use

- Run the full product analysis pipeline (market research -> JTBD -> landing -> TZ)
- Resume a previously started pipeline
- Check status of a product project
- Keywords: "product pipeline", "from idea to product", "full analysis", "full pipeline", "analyze the product"

## Project Folder

All outputs are stored in the project directory:

```
{project-dir}/
+-- PROJECT.md              <- state: Plan section with checkboxes
+-- chronicle.md            <- event chronology
+-- decisions.md            <- decisions and lessons
+-- sessions.md             <- session log
+-- files/
    +-- market-research.md        <- Step 1 output
    +-- jtbd-segments.md          <- Step 2 output
    +-- job-graph.md              <- Step 3 output
    +-- landing-content.md        <- Step 4 output
    +-- landing-comparison.md     <- Step 5 output (optional)
    +-- recruit-channels.md       <- Step 6 output (optional)
    +-- tz.md                     <- Step 7 output (optional)
```

State is tracked via PROJECT.md Plan section:
```markdown
## Plan
- [x] Market Research -> files/market-research.md
- [x] JTBD Segments -> files/jtbd-segments.md
- [ ] Job Graph -> files/job-graph.md
- [ ] Landing Content -> files/landing-content.md
- [ ] Landing Comparison -> files/landing-comparison.md (optional)
- [ ] Recruit Channels -> files/recruit-channels.md (optional)
- [ ] TZ -> files/tz.md (optional)
```

## Pipeline

```
Step 1: (Optional) Market Research -> files/market-research.md
        Ask: "Run Market Research? (~15-30 min, token-heavy)
         1) Yes, run /market-research
         2) No, skip
         3) I already have one -- will send the file"
        -> If 1: invoke /market-research skill, save output to files/
        -> If 2: mark as skipped in Plan (remove line or add "skipped")
        -> If 3: copy user's file to files/
        |
Step 2: JTBD Segments -> files/jtbd-segments.md
        -> Invoke /jtbd b2c (or b2b) with product description
        -> If files/market-research.md exists, pass as context
        -> Save segments to files/
        -> ASK user to pick top segment
        |
Step 3: Job Graph -> files/job-graph.md
        -> Invoke /jtbd graph with selected segment
        -> Save to files/
        |
Step 4: Landing Content -> files/landing-content.md
        -> Invoke /jtbd landing with segment + jobs
        -> Save to files/
        |
Step 5: (Optional) Landing Comparison -> files/landing-comparison.md
        -> ASK: "Compare landing with a reference? If yes -- provide URL or structure"
        -> If yes: invoke /jtbd compare
        -> If no: skip
        |
Step 6: (Optional) Recruit Respondents -> files/recruit-channels.md
        -> ASK: "Need a respondent recruitment plan for CustDev?"
        -> If yes: invoke /jtbd recruit
        -> If no: skip
        |
Step 7: (Optional) TZ Generation -> files/tz.md
        -> ASK: "Generate a technical specification for developers?"
        -> If yes: invoke /jtbd tz
        -> If no: skip
```

## How to execute

### Starting a new pipeline

1. Create a new project (or load existing one if it exists)
2. Fill PROJECT.md Plan with pipeline steps (template above)
3. Run steps sequentially, asking before each optional step
4. After each step: save output to `files/`, mark completed step in Plan

### Resuming a pipeline

1. Load the project
2. Read Plan in PROJECT.md -> find first uncompleted item
3. Resume from that step
4. Show user what was already completed

### Passing context between steps

Each step receives outputs from all previous steps as context:
- Step 2 (JTBD) receives: files/market-research.md (if exists)
- Step 3 (Job Graph) receives: selected segment from Step 2
- Step 4 (Landing) receives: segment + jobs from Steps 2-3
- Step 7 (TZ) receives: all previous outputs

To pass context: read the relevant .md files from `files/` and include their content when invoking the next skill.

### Listing projects

Use the project dashboard command to see all projects.

## Usage

```
/project new "AI tutor agent"                  -- create project first
/product-pipeline ai-tutor-agent               -- start pipeline on existing project
/product-pipeline resume ai-tutor-agent        -- resume existing
/project                                       -- list all projects (dashboard)
/project ai-tutor-agent                        -- show project status
```

## Notes

- Default market: Russia/CIS (unless specified)
- Each optional step asks before running -- never auto-run expensive steps
- All output files use consistent naming within `files/` subdirectory
- The orchestrator does NOT contain its own prompts -- it delegates to `/market-research` and `/jtbd-analysis` skills
- PROJECT.md Plan allows seamless resume in a new session
- At the end of pipeline, save session state for future resumption
