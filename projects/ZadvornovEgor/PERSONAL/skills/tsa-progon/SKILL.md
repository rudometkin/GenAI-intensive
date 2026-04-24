---
name: tsa-progon
description: >
  Simulate audience reactions to any artifact (landing, post, feature, product, CustDev guide)
  through parallel multi-agent avatars. Each avatar provides honest first-person feedback.
  This skill should be used when the user says "audience test", "run through audience",
  "test on audience", "run through avatars", "what will audience think", "test on target audience",
  "synthetic custdev", "persona run".
---

# Audience Run -- Multi-Agent Audience Simulation

Run any artifact through N synthetic avatars (3-30). Each avatar is a separate agent with a unique position, providing honest first-person reaction.

## When to Use

- After creating a landing page, post, feature, commercial proposal, product card
- For synthetic CustDev (running an interview guide through personas)
- When you need not one evaluation but 5-30 different perspectives
- Before real interviews to calibrate questions

---

## Algorithm

### Phase 1: Task Capture

Read context. If the artifact is already in conversation (file, URL, text) -- use it. Otherwise request:

1. **What are we testing?** (file path / URL / text)
2. **What audience?** (if not obvious)
3. **How many avatars?** (default 5; range 3-30)
4. **What focus?** (general reaction / conversion / price / methodology / emotion)
5. **Response format?** (reaction to artifact / interview answers / scale rating)

### Phase 2: Avatar Design

Based on the target audience, generate N avatars with DIVERSITY across axes:
- Age / gender
- Grade / experience
- Segment (novice / expert / skeptic / evangelist)
- Context (geolocation, company size, budget, pain)
- Emotional position (enthusiastic / tired / cynical / curious)

If the project already has a persona file (e.g., `persona_templates.md`) -- use it instead of generating.

Avatar card:
```
Avatar N: Name, age, role (city, income)
- Who: 1 sentence
- Pain: what hurts right now
- Context: why they are here
- Stop words: what repels them
- What they want to see: expectation
```

Show avatars to user and ask for confirmation.

### Phase 3: Artifact Preparation

If artifact is a file, read it. If URL -- fetch it. Prepare a compact description (up to 2000 words) for passing to each agent.

Create a working folder in the current project:
```
{project_files_dir}/tsa_progon_YYYY-MM-DD/
  +-- 00_artifact.md       # copy of artifact
  +-- 01_avatars.md        # avatar cards
  +-- responses/           # avatar responses
  |   +-- avatar_01.md
  |   +-- ...
  +-- 02_raw_feedback.md   # all responses in sequence
  +-- 03_patterns.md       # patterns (observations)
  +-- 04_recommendations.md # recommendations (Phase 7)
```

### Phase 4: Parallel Run (multi-Agent)

Launch all avatars in ONE message with N parallel Agent calls (subagent_type: general-purpose).

#### Mode A: Artifact Reaction (landing, post, product)

Prompt for each agent:
```
You are [full avatar card]. Do not break character.

You have been shown the following artifact:
---
[artifact content]
---

Task: give a detailed honest reaction in first person.

Response structure:
1. **First reaction** (3 seconds -- what catches the eye)
2. **What I like** (specifics)
3. **What annoys / confuses / I don't believe** (specific quotes)
4. **What I want to see but don't**
5. **Action**: will share / will close / will buy / will ignore -- and why
6. **Rating 1-10**: relevance / trust / desire to share

Be sharp and honest. Don't flatter. If it's bad -- say "it's bad".
Use language appropriate for your role (slang, professional terms).
Format: markdown, ~400-600 words.
```

#### Mode B: Synthetic Interview (CustDev)

Prompt for each agent:
```
You are [full avatar card]. Do not break character.

A researcher is asking you questions. Answer in first person,
based ONLY on your experience (avatar card).

Rules:
- Answer like a real person, not like an LLM
- Use colloquial language, professional slang
- You can go off-topic, ask counter-questions
- Not all questions are relevant to you -- say "I don't know" / "haven't encountered"
- If a question is leading -- you can disagree
- Name specific numbers from your experience (amounts, timelines, quantities)

Questions:
---
[interview guide content]
---

Response format: for each question -- answer in first person (2-5 sentences).
At the end -- a block "What I would add myself" (1-3 topics that weren't asked).
~600-1000 words.
```

After each agent returns feedback -- save to `responses/avatar_N.md`.

### Phase 5: Collection and Analysis

Collect all responses into `02_raw_feedback.md` (without interpretation).

Create `03_patterns.md` -- observations only, not recommendations:
- Table "Topic x who mentioned x criticality"
- Anchor quotes (3-5 most vivid)
- What is unanimously praised
- What is unanimously criticized
- Where avatars disagree
- For CustDev mode: fill coding_spreadsheet if it exists in the project

Show user a summary:
- Ran N avatars
- Folder: ...
- Top-3 problems
- Top-3 things praised

### Phase 6: Stop -- Model Switch

Raw data is collected. Tell the user:

```
Raw data collected.
For recommendations, switch to Opus (/model opus).
When you switch, say "continue".
```

DO NOT generate recommendations in this message. Wait for explicit "continue".

### Phase 7: Recommendations (after model switch)

When user says to continue:
1. Re-read `02_raw_feedback.md` and `03_patterns.md`
2. Write `04_recommendations.md`:
   - **Fix urgently** (unanimous failures) -- 3-5 items
   - **Improve** (frequent complaints) -- 3-5 items
   - **Amplify** (what is praised, can make brighter) -- 2-3 items
   - **Strategic forks** (if feedback exposed a positioning problem)
   - **Specific edits** -- list of changes with priority

---

## Principles

- DO NOT generate avatars from templates ("Masha 25, marketer" 5 times). Each avatar is a unique person.
- DO NOT merge agent responses into one mega-avatar. Preserve individuality.
- DO NOT write recommendations before Phase 7.
- Parallel Agent calls in one message (not sequential).
- Save EVERYTHING to disk -- data must survive context compaction.
- Avatars can contradict each other -- that's normal, don't smooth it out.
- Include 1-2 contrarians and 1 anti-persona (someone the product is definitely NOT for).
