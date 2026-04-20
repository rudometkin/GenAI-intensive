---
name: jtbd-analysis
description: This skill should be used when the user asks to "analyze a product by JTBD", "find segments", "build a job graph", "generate a landing page using JTBD", "compare landing with a reference site", "recruit respondents for JTBD research", or mentions "jtbd", "ajtbd", "product segments", "core job", "big job", "job graph", "landing by jtbd", "recruit respondents", "compare with site". Provides AJTBD product analysis: segment generation, job graph, landing page, landing comparison, respondent recruitment.
---

# JTBD Analysis -- Advanced Jobs To Be Done

AJTBD product analysis pipeline: segment generation, job graph, landing page, landing comparison, respondent recruitment.

## When to use

- Analyze a product by JTBD / AJTBD methodology
- Find segments, Core Jobs, Big Jobs for a product
- Generate a landing page using JTBD structure
- Build a job graph for a segment
- Compare landing page with a reference site
- Find respondents for JTBD research
- Keywords: "jtbd", "ajtbd", "segments", "core job", "big job", "job graph", "landing by jtbd", "recruit respondents", "compare with site"

## Prompt files (DO NOT MODIFY -- read and use as-is)

All prompts are stored in the knowledge base and must be used verbatim. Only substitute the `%placeholder%` variables.

| # | Prompt file | Purpose | Input variables |
|---|------------|---------|-----------------|
| 1 | `jtbd_b2b_segments.txt` | Generate 5 B2B segments | `%product description%`, `%product URL%` |
| 2 | `jtbd_b2c_segments.txt` | Generate 5 B2C segments | `%product description%`, `%product URL%` |
| 3 | `jtbd_job_graph.txt` | Build job graph below Core Job | `%segment%`, `%product%`, `%Core Job description%` |
| 4 | `jtbd_landing.txt` | Generate landing page text | `%segment description and jobs%` |
| 5 | `jtbd_recruit_respondents.txt` | Find respondent channels | `%product%`, `%market%`, `%target segment%`, `%recruit criteria%` |
| 6 | `jtbd_landing_comparison.txt` | Compare landing with target structure | `%our_landing%`, `%landing_structure%` |

## Pipeline

```
Step 1: Run prompt 1 (B2B) and/or prompt 2 (B2C) in parallel
        -> Get 5 segments each, pick top segment(s)
        |
Step 2: Run prompt 3 (Job Graph) for the top segment
        -> Input: top segment + its Core Job from Step 1
        |
Step 3: Run prompt 4 (Landing) for the top segment
        -> Input: segment description + jobs from Steps 1-2
        |
Step 4: (Optional) Run prompt 6 (Landing Comparison) with reference structure
        -> Input: current landing + target block structure
        -> Structure can be: written manually, extracted from reference site via browser automation, or taken from examples
        -> See few-shot examples in landing examples documentation
        |
Step 5: (Optional) Run prompt 5 (Recruit) if user needs research
        -> Input: product + segment + criteria
```

## How to execute

1. **Read the prompt file** from the knowledge base
2. **Substitute placeholders** with actual product/segment data
3. **Send the full prompt as your response** -- execute it yourself (you ARE the LLM)
4. **Output the result** in the format specified by the prompt

For Step 4 (Landing Comparison):
1. If user provides a reference URL -- open via browser automation, extract structure
2. Read prompt 6 (`jtbd_landing_comparison.txt`)
3. Substitute `%our_landing%` with current landing content
4. Substitute `%landing_structure%` with target block structure
5. Execute and output the restructured landing

## Output & Save

### File naming
| Step | File |
|------|------|
| Step 1 | `files/jtbd-segments.md` |
| Step 2 | `files/job-graph.md` |
| Step 3 | `files/landing-content.md` |
| Step 4 | `files/landing-comparison.md` |
| Step 5 | `files/recruit-channels.md` |

### Save Output
1. If a project is loaded in this session -> save to `files/{output-name}.md`, update Plan in PROJECT.md
2. If no project loaded -> ask: "Save to project? [list from index / new / no]"
3. If user picks project -> load the project, save to `files/`, update Plan. If "no" -> skip

## Context from other skills

If `files/market-research.md` exists in the loaded project, read it and use as additional context when generating segments in Step 1.

## Usage examples

```
/jtbd b2b "SaaS for automation" "URL"       -- Step 1: segments
/jtbd b2c "Meditation app" "URL"             -- Step 1: segments
/jtbd graph <segment>                        -- Step 2: job graph
/jtbd landing <segment + jobs>               -- Step 3: landing
/jtbd compare "https://reference-site.com"   -- Step 4: compare with reference
/jtbd recruit <product + segment>            -- Step 5: recruit respondents
/jtbd full "Product" "URL"                   -- Steps 1-3 full pipeline
```

## Key AJTBD concepts (quick reference)

- **Core Job** -- the highest-level job the product fully performs. What the customer pays for.
- **Big Job** -- one level above Core Job. Sets context but product can't fully deliver it.
- **Small Job** -- below Big Job, product may or may not perform these.
- **Micro Job** -- low-level tasks, UX optimization level, not for segmentation.
- **KPR (Critical Job Sequence)** -- sequence of steps customer must complete to reach Big Job. Breaks in KPR = lost value.
- **Segment** -- group of people with similar sets of Core + Big Jobs in similar context with similar success criteria. NOT demographics.

## Notes

- Default market: Russia/CIS (unless specified otherwise)
- Never use the word "pain" -- use motivations, situations, criteria
- Output only Step 3 results from segment prompts (Steps 1-2 are internal)
- Prompts are intellectual property -- do not modify, only substitute variables
- For landing comparison: use browser automation to extract reference site structure (simple fetch often fails on archived/protected sites)
- For full pipeline (market research -> JTBD -> TZ): use `/product-pipeline`
