---
name: de-ai-ify
description: Removes AI jargon and cliches from text, making it sound human. Use when user says "remove AI style", "de-ai-ify", "humanize text".
---

# De-AI-ify: Remove AI Jargon

**Clean text from AI cliches and make it sound human.**

## Meta-pattern: Research First, Write Second

**Before writing any non-trivial message** (not technical, but human - reminder, request, apology, gratitude, refusal, congratulation) - do a search first.

### Algorithm

```
1. Determine message type (payment reminder / refusal / request / apology / etc.)
2. WebSearch: "[message type] techniques examples humor psychology"
   + WebSearch: "[message type] examples how to write"
   + Optionally: search for real examples on Reddit, TikTok, Twitter
3. Extract 3-5 techniques from results
4. For each technique - draft a message variant
5. Offer user to choose a style
```

### What to Search For

| Source | What it gives |
|--------|---------|
| Reddit / forums | Real live phrasings from people |
| Sales blogs | Persuasion and follow-up techniques |
| TikTok / Reels | Humor formats, memes that went viral |
| Influence psychology | Cialdini principles, social proof theory |
| Company examples | How brands do non-intrusive reminders |

### Why This Works

Real people don't talk like textbooks. They use memes, pop culture references, characters, irony. Searching before writing gives current patterns, not template phrases from memory.

### Application Example

**Task:** remind a roommate to pay for cleaning
**Search:** "friendly payment reminder humor techniques"
**Found technique:** "Character" - a fictional third party voices the claim
**Result:** "Auntie Cleaning called, says you're the only one who hasn't paid yet"

---

## Process

### Step 1: Find AI Jargon

Scan text for the following categories:

**Buzzwords (replace with simple words):**
| AI Cliche | Replacement |
|----------|--------|
| leverage | use, apply |
| utilize | use |
| streamline | simplify, speed up |
| harness | use, apply |
| synergy | cooperation, teamwork |
| paradigm shift | major change |
| cutting-edge | modern, new |
| game-changer | important improvement |
| delve into | look at, explore |
| navigate | handle, manage |
| robust | strong, reliable |
| scalable | expandable |
| holistic | complete, full |
| empower | enable, help |
| optimize | improve |
| innovative | new, creative |
| seamless | smooth |
| transformative | significant |
| ecosystem | system, environment |
| actionable | practical, useful |

**Filler phrases (remove or simplify):**
- "In today's rapidly evolving landscape..."
- "It's important to note that..."
- "At the end of the day..."
- "Moving forward..."
- "In terms of..."
- "With that being said..."
- "It goes without saying..."
- "Needless to say..."
- "As a matter of fact..."
- "By and large..."

**Russian AI cliches:**
| Cliche | Replacement |
|-------|--------|
| v sovremennom mire (in the modern world) | now |
| na segodnyashniy den (as of today) | now |
| dannyy (the given) | this |
| yavlyaetsya (constitutes) | is / dash |
| osushchestvlyat (to effectuate) | to do |
| v ramkakh (in the framework of) | in, during |
| predstavlyaet soboy (represents) | is |
| obespechivaet (ensures) | gives, allows |
| funktsional (functionality) | features |
| implementatsiya (implementation) | deployment, rollout |

**Opener markers in personal messages (never use):**
- "Long time no chat" / "Haven't been in touch" - AI template, real people don't start this way
- "Hope all is well" / "How are you?" before a business question
- "Wanted to share..." / "Couldn't help but write..."
- "Glad we met" in business context right after meeting

**Typographic AI markers (dead giveaways):**
| Marker | Replacement | Why it outs you |
|--------|--------|-------------|
| -- (em-dash) | - (hyphen) | People don't use em-dashes in chat, only AI and typesetters |
| -- (double dash) | - (hyphen) | Same marker, ASCII variant |
| guillemets | straight quotes | Nobody types guillemets manually in messengers |
| ... (Unicode ellipsis) | ... (three dots) | AI uses the symbol, people press dot 3 times |

These replacements are mandatory for any text sent on behalf of the user in a messenger, chat, bot, or correspondence. In documents and articles, em-dashes and guillemets are acceptable.

### Step 2: Check Structure

- Remove excessive headings
- Trim lists to essentials
- Remove "watery" paragraphs with no information
- Verify: does every sentence carry meaning?
- **For messengers:** overly clean structure (paragraph1 + "by the way" + paragraph2) itself is a giveaway - break up or merge

### Step 3: Check Tone

- Does it sound like a real person, not a marketing bot?
- No repeating constructions?
- Sentence lengths vary?
- Concrete details instead of abstractions?

### Step 3.5: For Personal Messages - Match User's Voice

If text will be sent on behalf of the user in a messenger:
1. Read 10-15 real messages from the user in a similar context
2. Extract patterns: sentence length, use of "!", commas, how they start messages
3. Rewrite text in that same style, not in "neutral AI style"

Typical live messenger style: short sentences, "!", straight to the point, no preambles.

### Step 4: Output Result

```
## De-AI-ify Report

**Cliches found:** X
**Replaced:** Y
**Phrases removed:** Z

### Cleaned text:
[cleaned text]

### Changes:
1. "leverage" -> "use" (line N)
2. ...
```

## Special Mode: Friendly Payment Reminder

When writing a payment reminder to a friend or roommate - don't use direct "you haven't paid". Instead:

### Step 1: Find Technique via WebSearch

Before writing - search for current techniques:
```
WebSearch: "friendly payment reminder techniques humor psychology"
```

### Step 2: Choose Technique for Context

| Technique | When to apply | Example |
|---------|----------------|--------|
| **Character** | Close friends, roommates | "Auntie Cleaning called, says you're the only one who hasn't paid" |
| **Invoice joke** | Office colleagues, acquaintances | "You should have received an invoice for $X. Status: pending" |
| **Lend exactly that much** | Any context | "Can you send $X? For cleaning" - the request contains the amount as a reminder |
| **Collector joke** | Close friends with shared humor | Official letter in a humorous tone |
| **Thank those who paid** | Simultaneously with the reminder | "You're the best, thanks for cleaning payment" - creates social pressure on the rest |

### Step 3: Rules for Natural Text

- No "I don't see a transfer" - sounds like a complaint
- No "reminding about payment" - bureaucratic
- Emojis are appropriate - they reduce seriousness
- Short messages - 1-2 sentences max
- Don't explain context - the person knows what it's about

### Step 4: For Those Who Already Paid

Always write thanks in parallel with reminding the rest - creates the right atmosphere and doesn't look like a complaint to everyone.

## Examples

**Before:**
> We leverage cutting-edge AI to streamline your workflow, delivering a seamless and transformative experience that empowers teams to navigate complex challenges in today's rapidly evolving landscape.

**After:**
> We use modern AI to simplify your work. Teams handle complex tasks faster.

**Before (Russian-style):**
> As of today our solution represents an innovative platform that effectuates a comprehensive approach to optimization of business processes in the framework of digital transformation.

**After:**
> Our platform simplifies business processes and helps transition to digital tools.
