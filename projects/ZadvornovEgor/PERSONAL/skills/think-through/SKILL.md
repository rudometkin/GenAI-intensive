---
name: think-through
description: This skill should be used when the user asks to "think through a problem", "let's think about this", "think through", "how best to", "help me decide", "let's figure out", or needs structured analysis of any non-code problem -- life decisions, business strategy, project planning, product analysis, career choices. Universal 6-phase methodology for any domain except code (for code use feature-dev instead).
---

# Think Through -- Universal Structured Thinking

6-phase structured thinking workflow for ANY non-code domain. The non-code equivalent of feature-dev.

## When to Use

- Life decisions, career choices, strategy questions
- Business strategy, pricing, positioning, partnerships
- Project planning, resource allocation, prioritization
- Product analysis (when not using /product-pipeline)
- Any "let's think about this" without code context

## When NOT to Use

- Code features, architecture, implementation -> use `/feature-dev`
- Quick factual questions (Level 0) -> answer directly
- Product pipeline -> use `/product-pipeline`

## Stop Rules

### Mandatory Stops (use AskUserQuestion tool)
- **After Phase 1 output** -> ALWAYS. Use AskUserQuestion: "Did I understand correctly? What did I miss? (or 'ok' to continue)"
- **After Phase 3 approaches** -> ALWAYS. Use AskUserQuestion: "Which approach do you choose? (A / B / C)"

### Adaptive Stops (Claude decides based on context)
- **Phase 2 questions** -> SKIP if user already provided goal, constraints, success criteria, and timeline. But MUST explain: "Skipping Phase 2 -- from your request I already know: [list what was provided]"
- **Phase 4 execution** -> STOP only if blocked or need clarification
- **Phase 6 summary** -> never stop, just present

### Rule: Never skip silently
If any phase is skipped or condensed -> explicitly state which phase and why.

## Optional Thinking Tools

Available as supplementary tools during phases. Invoke only when relevant, not every time.

| Tool | When | Phase |
|------|------|-------|
| `/thinking-partner` | Deep exploration through Socratic questioning | 1 |
| `/first-principles` | Decompose problem to fundamentals | 1 |
| `/pre-mortem` | "The idea already failed. Why?" | 1 |
| `/steel-manning` | Challenge assumptions, strongest counter-argument | 2 |
| `/inversion` | "What if we did the opposite?" | 3 |
| `/cynefin` | Determine problem type (clear/complicated/complex/chaotic) | 3 |
| `/regret-minimization` | Long-term decision (10 min / 10 months / 10 years) | 3 |
| `/ooda-loop` | Rapidly changing situation | 4 |

---

## Phase 1: Context Discovery

**Goal:** Understand the problem and confirm understanding with user.

### Steps

1. Launch research agents in parallel (skip agents that are clearly not needed):
   - Agent 1 (Explore): search project memory and knowledge base for relevant context
   - Agent 2 (general-purpose): web research on the topic (only if external info needed)
   - Agent 3 (Explore): read loaded project files (only if project loaded)
2. Read key files identified by agents to build deep understanding
3. If topic is complex and unfamiliar -> offer `/thinking-partner` or `/first-principles`
4. If topic involves risk -> offer `/pre-mortem`

### Output Format

Present to user:

```
Here is how I understood the task:
- Goal: [what we want to achieve]
- Context: [what I already know / found]
- Constraints: [what to consider -- time, budget, people, dependencies]
- Connections: [related projects, people, deadlines from knowledge base]

How I will proceed:
- Phase 2: will clarify [specific questions I see]
- Phase 3: will propose approaches for [directions]
- Tools: planning to use [/pre-mortem, /inversion, ...] (if applicable)

Did I understand correctly? What did I miss?
```

### MANDATORY STOP
Use AskUserQuestion: "Did I understand correctly? What did I miss? (or 'ok' -> Phase 2)"
DO NOT continue to Phase 2 until user responds.

---

## Phase 2: Clarifying Questions

**Goal:** Fill gaps and resolve ambiguities before proposing solutions.

### Adaptive Skip Rule

If user already provided goal, constraints, success criteria, and timeline in their initial request -> skip this phase. But MUST explain:
"Skipping Phase 2 -- from your request I already know: [list what was provided]."

### Rules (when NOT skipping)

- One question at a time
- Multiple choice preferred (A / B / C / D)
- Max 5 questions before moving to Phase 3
- Each question ends with: "Or something else?"
- Focus on: goal clarity, constraints, success criteria, timeline, stakeholders

### Optional Tool

If user's assumptions seem untested -> offer `/steel-manning` to challenge them.

### Output per Question

```
Question 2/5: [question text]

A) [option]
B) [option]
C) [option]
D) Or something else?
```

Collect all answers. Summarize before Phase 3:

```
Captured:
- Goal: [refined]
- Success criteria: [from answers]
- Constraints: [from answers]
- Timeline: [from answers]

Moving to solution options.
```

---

## Phase 3: Propose Approaches

**Goal:** Present 2-3 approaches with trade-offs. Get user's choice.

### Steps

1. Generate 2-3 distinct approaches
2. If decision is long-term -> offer `/regret-minimization`
3. If problem type unclear -> offer `/cynefin`
4. If stuck -> try `/inversion` ("what would guarantee failure?")

### Output Format

```
## Approach A: [name] (recommended)
[2-3 sentences]

## Approach B: [name]
[2-3 sentences]

## Approach C: [name] (optional)
[2-3 sentences]

| Criterion | A | B | C |
|-----------|---|---|---|
| Effort | Low | Medium | High |
| Risk | Medium | Low | High |
| Speed | Fast | Medium | Slow |
| [domain-specific] | ... | ... | ... |

I recommend A because [reasoning tied to user's criteria from Phase 2].

Which approach do you choose?
```

### MANDATORY STOP
Use AskUserQuestion: "Which approach do you choose? (A / B / C)"
DO NOT continue to Phase 4 until user responds.

---

## Phase 4: Execution

**Goal:** Execute the chosen approach.

### Steps

1. Execute the chosen approach step by step
2. May call other skills as needed (e.g., `/market-research`, `/jtbd-analysis`, web search)
3. Show progress at natural milestones, not just the final result
4. If blocked -> propose alternative approach, do not stall
5. If situation changes rapidly -> offer `/ooda-loop`

### Rules

- Deliver concrete output, not abstract advice
- If the task produces artifacts (documents, analyses, plans) -> create them
- If the task is a decision -> present the recommendation with full reasoning

---

## Phase 5: Validation

**Goal:** Verify the result matches the goal from Phase 2.

### Steps

1. Self-check: does the result address the goal and success criteria defined in Phase 2?
2. Run verification checks if applicable
3. If validation fails -> identify gap -> return to Phase 4 with specific fix
4. If validation passes -> proceed to Phase 6

### Output

```
Verification:
- Goal [from Phase 2]: [achieved / partially / not achieved]
- Criteria: [status of each]
- Gaps: [if any]
```

---

## Phase 6: Summary + Save

**Goal:** Document results, decisions, and lessons. Save to project if applicable.

### Output Format

```
## Done

**Goal:** [from Phase 2]
**Approach:** [chosen in Phase 3]
**Result:** [what was accomplished]
**Decisions:** [key choices made during execution]
**Lessons:** [if any cross-project insights]
```

### Save Logic

1. If a project is loaded in this session -> save to project directory
2. If Level 2+ task with no project loaded -> propose creating a new project
3. If cross-project lesson discovered -> save to shared knowledge base

---

## Error Handling

| Scenario | Behavior |
|----------|----------|
| User says "just do it" in Phase 2 | Provide best recommendation, confirm, proceed |
| User changes mind in Phase 4 | Acknowledge, return to Phase 3 with new context |
| Task turns out to be code-related | Redirect: "This is a code task -- use `/feature-dev` instead" |
| User wants faster process | Skip optional tools, reduce questions to 2-3, keep phases |
| Blocked with no alternative | Present blocker clearly, ask user for direction |
