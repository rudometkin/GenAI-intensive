---
name: cddc-canvas
description: This skill should be used when the user asks to "create CDDC", "review CDDC", "improve CDDC", "customer development design canvas", "hypothesis validation", "custdev canvas", "CDDC for project", "review CDDC", "improve CDDC", "hypothesis decomposition", "from money backwards", or wants to plan, review, or improve hypothesis validation for a product/startup using the CDDC methodology (BTG-4, CustDev Lab).
---

# CDDC Canvas -- Customer Development Design Canvas

Create, improve, or review a CDDC (Customer Development Design Canvas) for hypothesis validation using BTG-4 methodology by CustDev Lab (Nevostruev).

## When to Use

- Creating a new CDDC for a product/startup
- Improving or expanding an existing CDDC
- Reviewing a CDDC for quality (benchmarks, chain linkage, data consistency)
- Decomposing a product hypothesis "from money backwards"

## Workflow

```
1. AUTO-ENRICH & GATHER CONTEXT
   |-- Accept SHORT prompt ("create CDDC for X")
   |-- Auto-read project files, interviews, existing artifacts
   |-- Construct full context internally (user doesn't need to specify file paths)
   |
2. STUDY METHODOLOGY (see BTG-4 methodology documentation for details)
   |
3. STUDY EXAMPLES (review bundled CDDC examples for patterns)
   |
4. BRAINSTORM with user *** HARD GATE -- NO WRITING BEFORE THIS ***
   |-- Ask 4-7 clarifying questions, ONE at a time
   |-- Use A/B/C format with recommendation (user often picks hybrid)
   |-- After questions: offer autonomous mode ("I'll work with agents, come back with result")
   |
5. DECOMPOSE "from money backwards"
   |-- Start with: "Who pays and for what?"
   |-- Work backwards: what must be true for them to pay?
   |-- Each "must be true" = one CDDC column
   |-- NO artificial column limits -- as many as needed
   |
6. WRITE CDDC (use CDDC template as base)
   |-- Fill ALL 13 fields per column (no empty cells)
   |-- One hypothesis per column (NEVER compound)
   |-- PASS + FAIL + INCONCLUSIVE benchmarks on every step
   |-- Early PASS/FAIL rules in Action Standards
   |-- Chain linkage: output of step N = input of step N+1
   |
7. QUALITY REVIEW (run quality checklist inline)
   |-- Go through every quality check mechanically
   |-- Fix all critical issues
   |
8. PRESENT to user
```

## Phase Details

### Phase 1: Auto-Enrich & Gather Context

The user should NOT need to write a detailed prompt with file paths, methodology rules, and format specs. Accept minimal input and auto-enrich.

**Minimal prompt examples:**
- "create CDDC for ProductX" -> auto-read project folder, extract all context
- "CDDC for my project, B2C, subscription model" -> use as base, ask 3-4 targeted questions
- "improve CDDC" + file attached -> read current CDDC, run quality checklist, identify gaps

**Auto-enrichment checklist:**
1. Identify project name from user's message
2. Read project folder if available:
   - PROJECT.md (product description, segment, stage)
   - files/ (interview transcripts, competitor analysis, existing CDDCs)
   - sessions.md (previous work context)
3. Read interview notes and transcripts (extract key quotes, pain ratings, WTP signals)
4. Read previous CDDC versions (if improving)
5. Read competitor/market research data

**Binary file extraction:** If user provides PDFs/XLSXs, extract using Python openpyxl or equivalent tools.

### Phase 2: Study Methodology

Internalize the BTG-4 methodology (see methodology documentation for details):
- 4 elements per column (hypotheses, methods, respondents, actions)
- 5 rules of CDDC
- Decomposition principle
- Discovery vs Validation distinction
- Action Standards methodology

### Phase 3: Study Examples

If user provides example CDDCs, extract key patterns:
- How many Discovery columns? How many Validation?
- What metrics and benchmarks are used?
- Where did hypotheses break? (most valuable learning)
- What are the proven column structures? (1D+3V for simple B2C, 3D+4V for B2B)

### Phase 4: Brainstorm

<HARD-GATE>
NEVER write CDDC before brainstorming. Not after "just reading the files." Not after "understanding the context." Not even if the prompt is very detailed. The first attempt without brainstorming WILL be rejected. This is a BLOCKING requirement -- no exceptions.
</HARD-GATE>

**Question format:** Offer 2-3 options (A/B/C) with a recommendation. The user often picks a hybrid of options -- that's the ideal outcome. ONE question per message. Wait for the answer before asking the next question.

**Minimum questions (skip only if answer is already clear from gathered context):**

1. **Pain framing:** "How to frame the core pain? A: [narrow/specific]. B: [broad/umbrella]. C: [split into parallel sub-hypotheses]." Recommend: start broad (D1), then split into specifics (D2, D3).
2. **Segment:** B2C or B2B? (separate CDDC for each)
3. **Money event:** How does the product make money? Who pays? (subscription / commission / one-time / hybrid). DO NOT assume from <5 interviews.
4. **Existing data:** Any interviews done? What preliminary signals? (Reference by R1, R2, etc.)
5. **COGS:** What does it cost to serve one user? Does it vary by architecture/deployment model?
6. **Unique barriers:** What's specific to this product? (trust/delegation of access, legal risks, tech feasibility, seasonality, ban risks)
7. **Structure validation:** Present proposed decomposition tree and ask: "Feels like something is missing or something is extra?"

**Critical rules during brainstorm:**
- NEVER limit columns artificially. "Only 3D" or "let's keep it compact" are anti-patterns. Write as many columns as the decomposition genuinely requires. 5D+4V+Final is fine if justified.
- NEVER draw conclusions about the business model from <5 interviews. Note early signals as "preliminary" only.
- NEVER pack multiple hypotheses into one column. If WTP, trust/delegation, and MVP requirements are separate unknowns -- they are separate columns.
- When user says "I don't care how many columns" -- take it literally.

**Autonomous mode handoff:** After clarifying questions, offer: "I'll brainstorm with agents, decompose, write the CDDC, and run quality review. I'll come back with the result." If user agrees, proceed through Phases 5-8 autonomously, then present the final reviewed result.

### Phase 5: Decompose

Build the "from money backwards" tree:
```
MONEY: [who pays what]
  <- Unit economics works (LTV/CAC >= 3, margin >= 40%)
    <- First payment collected
      <- [Conversion step N-1]
        <- ...
          <- [First validation: user actually uses the product]
            <- [Last discovery: willingness to pay confirmed]
              <- ...
                <- [First discovery: broad pain confirmed]
```

**Rules for decomposition:**
- Each arrow = one CDDC column
- Never skip steps (common mistake: jumping from "pain confirmed" to "payment")
- D2/D3 can be parallel if tested in same interviews
- Validation steps are always sequential
- Final column = always money
- If existing interview data challenges the original hypothesis -- reflect it in the decomposition (e.g., if R1 rated "speed" 5/5 but R2 rated it 2/5, the pain framing needs to be broader)
- Start D1 broad ("users experience disproportionate friction with X"), then split into specific sub-hypotheses in D2/D3

**Typical structures:**
- Simple B2C: 2-3D + 3-4V + Final (linear funnel, single pain dimension)
- Complex B2C: 4-5D + 4V + Final (multiple pain dimensions, delegation/trust questions, pricing complexity)
- B2B: 3D + 4-5V + Final (more Discovery for trust-building, separate column for buying process/budgets)

### Phase 6: Write CDDC

Use the CDDC template as a base and fill in the target location (usually `{project}/synthesis/cddc.md`).

**13 mandatory fields per column:**

| # | Field | Common Mistakes |
|---|-------|-----------------|
| 1 | Hypothesis | Compound hypotheses (2-3 crammed into one) |
| 2 | Goal | Too vague ("understand users") |
| 3 | Method | Missing specific questions/protocol |
| 4 | Metric | Not measurable ("satisfaction") |
| 5 | Benchmark PASS | No specific number |
| 6 | Benchmark FAIL | Missing or no consequence described |
| 7 | Benchmark INCONCLUSIVE | Missing entirely (most common gap) |
| 8 | Respondents | No filtering criteria |
| 9 | Action Standards | No early PASS/FAIL rules |
| 10 | Where to find | Generic ("social media") |
| 11 | What to do | Missing deliverables list |
| 12 | Budget | Not estimated |
| 13 | Result | Missing preliminary signals |

**Benchmark writing rules:**
- PASS: specific threshold + "AND" conditions (all must be true)
- FAIL: specific threshold + "OR" conditions (any one triggers fail) + **consequence** (pivot/kill/redesign)
- INCONCLUSIVE: zone between PASS and FAIL + **actions** (more data, different questions, narrower segment)

**Data integration:**
- Reference real interview data where available (R1, R2, etc.)
- Note preliminary signals in Result field
- Document anchoring points (competitor prices, current manual costs)
- Note seasonality if applicable

**Data caution rules:**
- If <5 interviews exist: frame ALL findings as "preliminary signal from R1-RN" -- never as confirmed
- If interview data contradicts the original hypothesis: flag it explicitly, propose hypothesis reformulation
- If respondents are a non-representative subset (e.g., all micro-businesses when targeting solo practitioners): note sampling bias in Result field
- Never assume the business model (subscription vs per-result vs commission) from <10 data points -- list it as an open question in the relevant D column

### Phase 7: Quality Review

Run the quality checklist inline -- go through every checkbox mechanically on the written CDDC. For complex CDDCs (7+ columns), delegate to a sub-agent for thorough review.

**Critical checks (must pass):**
1. Chain linkage: output N = input N+1
2. Number consistency: WTP matches pricing matches unit economics
3. No compound hypotheses
4. INCONCLUSIVE zones on every step
5. Architecture-dependent pricing (if applicable)
6. Monthly checkpoints in Unit Economics

Fix all critical issues before presenting to user.

### Phase 8: Present

Present the final CDDC with:
- Summary of structure (ND + NV + Final)
- Key design decisions and tradeoffs
- What data is already integrated
- What needs to happen next (usually: finish Discovery interviews)

## Common Patterns

### Parallel Discovery Columns
When D2/D3 test different aspects in the same interviews, mark them explicitly:
- Same respondents, same interview, different question blocks
- Budget = "0 (embedded in D1)"
- Action Standards reference D1's count

### Architecture-Dependent Pricing
When COGS varies by architecture (server vs mobile), reflect in ALL relevant columns:
- D5 hypothesis: mention both thresholds
- V4 benchmark: conditional PASS (server >= X, mobile >= Y)
- Unit Economics: separate margin calculations

### Seasonality
When the product has seasonal usage:
- Note in Unit Economics: "7 active months"
- Separate churn: "forever" vs "seasonal pause"
- LTV calculation on seasonal basis
- V3 timing: plan for peak season data collection

## Anti-Patterns

### CRITICAL (block delivery)

| Anti-Pattern | Fix |
|---|---|
| Writing CDDC without brainstorming | **HARD GATE.** Ask 4-7 clarifying questions with A/B/C options first. First attempt without brainstorming WILL be rejected. |
| Compound hypothesis ("A AND B AND C") | Split into separate columns. WTP, trust/delegation, MVP requirements = separate columns. |
| Artificial column limit ("only 3D" or "keep it compact") | NEVER limit columns. As many as the decomposition genuinely requires. 5D+4V+Final is fine. |
| Premature conclusions from <5 interviews | Frame as "preliminary signal," NOT confirmed finding. "R1 and R2 suggest X" != "X is confirmed." |
| Missing FAIL benchmark | Every PASS needs a FAIL + consequence (pivot/kill/redesign) |
| No INCONCLUSIVE zone | Add zone between PASS and FAIL thresholds with specific actions |

### IMPORTANT (fix before presenting)

| Anti-Pattern | Fix |
|---|---|
| Jumping from Discovery to money | Add intermediate Validation steps |
| Vague benchmarks ("good enough") | Use specific numbers with units |
| Same respondents across all Validation | Respondent pool narrows: V1 -> V2 -> V3 |
| No early stop rules | Add early PASS/FAIL after 50-70% of sample |
| Ignoring existing interview data | Reference R1, R2 etc. in Result fields |
| Architecture-dependent pricing not in all columns | If COGS varies by architecture, reflect in pricing Discovery, Validation, AND Unit Economics |
| Parallel Discovery columns not marked | When D2/D3 share interviews with D1, explicitly note "budget = 0, embedded in D1" |
| No seasonality adjustment in LTV/churn | If seasonal product, separate "forever churn" from "seasonal pause", adjust LTV |
| Assuming business model from limited data | "2 respondents said per-result payment" != "the model is per-result." Frame as hypothesis to test. |

## Resources

This skill relies on supporting methodology and example documents:
- **BTG-4 Methodology** -- Full BTG-4 methodology: 5 rules, 4 elements, decomposition, examples
- **Quality Checklist** -- Post-writing quality review checklist (structure, chain, numbers, data)
- **Example Filled Column** -- Annotated example of a well-filled Discovery column + quality criteria + column count patterns
- **Example CDDC: OneScore** -- Full CDDC (B2C, 1D+3V+Final). Key lesson: V3 FAIL (CR 0.1% at 45% target) -- engagement != monetization
- **Example CDDC: Apricot** -- Full CDDC (B2B EdTech, 3D+4V). Key lesson: 3 Discovery columns for B2B trust-building
- **Example CDDC: Smart Cork** -- Full CDDC (B2C IoT, 3D+4V). Key lesson: explicit FAIL conditions, physical product pilot dynamics
- **CDDC Template** -- Complete CDDC markdown template with all fields, sections, and placeholders
