---
name: market-research
description: This skill should be used when the user asks to "research a market", "analyze competitors", "estimate market size", "find market problems", "validate business model", "analyze search demand", or mentions "market research", "competitors", "market size", "unit economics", "demand analysis", "TAM SAM SOM", "go-to-market", "demand testing", "CustDev", "business model". Provides comprehensive market research pipeline: market sizing, competitor analysis, BM validation prep, search demand analysis, customer research, demand testing, and GTM strategy.
---

# Market Research

Comprehensive market research pipeline based on Ninja Marketing 7 methodology + AI tools. All steps execute automatically by default. Steps that are "manual" in the original course are performed via internet research, with a MANUAL UPGRADE option for higher accuracy.

## Modes

| Mode | Steps | Duration | Use case |
|------|-------|----------|----------|
| **quick** | 0-2 | ~15 min | Fast hypothesis check: TAM + competitors |
| **standard** | 0-4 | ~30 min | Full automated analysis with search demand |
| **full** | 0-7 | ~45 min | Complete pipeline including CustDev proxy, demand testing, GTM |

Default: **standard**. Default market: Russia/CIS unless specified.

## Prompt Files

| # | File | Variables | Tool | Used in |
|---|------|-----------|------|---------|
| 1 | `prompt_01_market_analysis.txt` | `{industry}`, `{country}` | Manus/ChatGPT | Step 1 |
| 2 | `prompt_02_business_idea.txt` | `{product}`, `{audience}`, `{problem}` | ChatGPT/Manus | Step 1 |
| 3 | `prompt_03_demand_check.txt` | `{product}`, `{date_from}` | Grok | Step 2 |
| 4 | `prompt_04_competitors_top10.txt` | `{category}`, `{persona}`, `{our_brand}` | Perplexity | Step 2 |
| 5 | `prompt_05_competitors_expanded.txt` | `{category}`, `{persona}`, `{our_brand}` | Perplexity | Step 2 |
| 6 | `prompt_06_competitor_deep.txt` | `{industry}` | Manus/Perplexity | Step 2 |
| 7 | `prompt_07_mckinsey_strategy.txt` | `{industry}` | Claude | Step 3 |
| 8 | `prompt_08_pains_gains.txt` | `{competitor_product}` | Perplexity | Step 2 |
| 9 | `prompt_09_influencers.txt` | `{niche}`, `{brand_description}` | Perplexity | Step 7 |

## Pipeline

```
Step 0: INPUT
    |
Step 1: MARKET SIZING ----------- 2 agents parallel ---- quick+
    |
Step 2: COMPETITORS ------------- 2 agents parallel ---- quick+
    |
Step 3: BM VALIDATION PREP ------ 2 agents parallel ---- standard+
    |
Step 4: SEARCH DEMAND ----------- 1 agent -------------- standard+
    |
Step 5: CUSTOMER RESEARCH ------- 1 agent -------------- full
    |
Step 6: DEMAND TESTING ---------- 1 agent -------------- full
    |
Step 7: GO-TO-MARKET ------------ 1 agent -------------- full
```

### Step 0: Input Gathering

Collect from user:
- Product/service description
- Target audience
- Problem being solved
- Target market/country (default: Russia/CIS)
- Mode (quick/standard/full)
- Business model type (if known)

Map input to variables: `{product}`, `{audience}`, `{problem}`, `{industry}`, `{country}`, `{category}`, `{persona}`, `{our_brand}`.

### Step 1: Market Sizing [AUTO] - 2 agents parallel

**Agent A** (general-purpose, WebSearch):
1. Use business idea analysis prompt, substitute variables
2. Execute the 8-block analysis prompt via WebSearch
3. Calculate TAM/SAM/SOM with sources (reference: ChatGPT TAM/SAM/SOM Calculator GPT)
4. Identify growth rate, key trends, market drivers

**Agent B** (general-purpose, WebSearch):
1. Use market analysis prompt, substitute variables
2. Search consulting reports (McKinsey, BCG, Bain, Deloitte, PwC, EY, KPMG)
3. Build Country Score Card if multi-country
4. Macro analysis: GDP, digital penetration, market maturity

### Step 2: Competitors [AUTO] - 2 agents parallel

**Agent C** (general-purpose, WebSearch):
1. Use the 3x3 question framework for competitor research
2. Find top 10 competitors using competitor discovery prompt
3. Deep dive top 5 with expanded analysis prompt
4. Comprehensive analysis with deep competitor prompt
5. Output: competitor table (name, URL, pricing, positioning, weakness, estimated revenue)

**Agent D** (general-purpose, WebSearch):
1. Extract pains/gains from reviews using pains/gains prompt
2. Check demand signals using demand check prompt
3. Search forums, Reddit, Telegram, social media for real user quotes
4. Collect user language patterns (for marketing copy)

### Step 3: BM Validation Prep [AUTO] - 2 agents parallel

**Agent E** (general-purpose, WebSearch):
1. Find 10 companies with similar business model - CEO/founder names, LinkedIn profiles
2. Find 5 VC funds via Crunchbase WebSearch - partner contacts
3. Analyze investor landscape for the industry

**Agent F** (business-analyst):
1. McKinsey-style strategic analysis using strategy prompt
2. Build unit economics model: CAC, LTV, payback period, channel costs
3. Risk analysis: country risks, dependencies, personal blind spots
4. Generate personalized outreach letters for founders (pitch formula)
5. Prepare interview questions table (6 blocks: viability, competition, economics, structure, scale, mistakes)
6. Investor talking points based on data from Steps 1-2

> MANUAL UPGRADE: This is a manual step in the original methodology. For more accurate data, prepare a script for 10 calls to founders and 5 funds. Requires approximately 5 hours of calls.

### Step 4: Search Demand [AUTO] - 1 agent

**Agent G** (general-purpose, WebSearch + Playwright):
1. Use search demand methodology guide
2. Google Trends analysis: trend direction, compare up to 5 themes, regional breakdown, YouTube trends
3. Yandex Wordstat via Playwright (RU/CIS): absolute search volumes
4. Build keyword clustering matrix (rows = topics/professions, columns = semantic modifiers)
5. Normalize data (0-1) for cross-market comparison if multiple countries
6. Estimate search competition (CPC, organic difficulty)
7. Verify findings against consulting reports (Big 3 + Big 4)

### Step 5: Customer Research [AUTO] - 1 agent

**Agent H** (general-purpose, WebSearch):
1. Proxy CustDev: analyze forums, Reddit, Quora, review sites (G2, TripAdvisor, etc.)
2. Collect real user quotes with sources
3. Identify patterns: pains, JTBD, audience language, decision criteria
4. Find respondent channels (Respondent.io, LinkedIn groups, competitor communities)
5. Analyze audience questions (Quora, Reddit, StackExchange) for unmet needs

> MANUAL UPGRADE: This is a manual step in the original methodology - CustDev interviews. Prepare: CustDev script (6 JTBD questions), quantitative research form, verifying survey, respondent channel list. Requires: 5-10 hours of interviews, budget $3-7K.

### Step 6: Demand Testing [AUTO] - 1 agent

**Agent I** (general-purpose, WebSearch + Playwright):
1. Analyze competitor landing pages via Playwright (structure, CTA, positioning, copy)
2. Estimate CPQL by industry benchmarks
3. Compare positioning strategies across competitors
4. Recommend test hypotheses (which positionings to A/B test)
5. Suggest landing page structure based on best-performing competitors

> MANUAL UPGRADE: In the original methodology, create several landing pages, run traffic, compare real CPQL. Prepare: headline variants and positionings, testing plan, budget ~$2K.

### Step 7: Go-to-Market [AUTO] - 1 agent

**Agent J** (business-analyst):
1. Positioning strategy based on all data from Steps 1-6
2. Channel strategy (WebSearch: what works in this niche, CAC benchmarks)
3. Sales scripts (benchmarked against competitor approaches)
4. Trust-building plan (Google Business, PR Newswire, YouTube, conferences, Medium)
5. B2C vs B2B decision: automation vs live sales (by average check)
6. Hiring channels for sales team + salary benchmarks in the niche
7. Influencer strategy using influencer prompt
8. Scaling playbook: which channels to scale first

> MANUAL UPGRADE: In the original methodology, real actions needed: hire bizdev ($1-2K/month), 6 advisors (0.1% equity), sales ($5K+). Prepare: full checklist with tactics: 60 call attempts, write in WhatsApp/Telegram immediately after lead, different telephony.

## Execution Pattern

For each prompt file:
1. Read the prompt file
2. Substitute `{variables}` with actual data from Step 0
3. Execute as the search/analysis prompt (Claude IS the LLM)
4. Output in the format specified in the prompt file

Tip: ask Claude to improve a prompt before sending to Perplexity for better results.

## Output & Save

### Report format:

```markdown
# Market Research: {Product Name}
> Date: {date} | Market: {country} | Mode: {mode}

## Executive Summary
3-5 key findings + go/no-go recommendation

## 1. Market Overview
### TAM / SAM / SOM (table with calculations)
### Market Trends (growth rate, drivers, consulting report citations)
### Macro Analysis (Country Score Card if multi-country)

## 2. Competitor Landscape
### Top Competitors (table: name, URL, pricing, positioning, weakness)
### Competitive Matrix (feature comparison grid)
### White Space (underserved areas, differentiation opportunities)

## 3. User Problems & Demand
### Pain Points (quotes, sources, frequency)
### Demand Signals (search volumes, trend direction, community sizes)

## 4. Search Demand Analysis (standard+)
### Trend Analysis (Google Trends / Wordstat data)
### Keyword Clusters (matrix with volumes)
### Competition in Search (CPC, organic difficulty)

## 5. Strategic Analysis
### McKinsey-style Overview (industry picture, key players, white space)
### Unit Economics (CAC, LTV, payback, channel costs)
### Risk Assessment (country, dependency, personal blind spots)

## 6. BM Validation Package (standard+)
### Founders to Contact (10 companies, CEO names, LinkedIn)
### VC Funds (5 funds, partner contacts)
### Outreach Templates (personalized letters)
### Interview Questions (6-block table)

## 7. Customer Insights (full)
### Proxy CustDev Findings (forum/review analysis)
### Audience Language Patterns
### Respondent Channels

## 8. Demand Testing Plan (full)
### Competitor Landing Analysis
### CPQL Benchmarks
### Test Hypotheses

## 9. GTM Strategy (full)
### Positioning
### Channel Strategy
### Sales Approach
### Trust Building Plan
### Influencer Strategy

## Sources
All URLs and reports cited
```

## Integration

- **JTBD skill**: Step 0 of JTBD analysis can call market-research for market context
- **Step 5** references 6 JTBD questions by Ivan Zamesin for CustDev script
- **WebSearch**: primary data tool for all automated steps
- **Playwright**: fallback for Wordstat, Google Trends, competitor landing pages
- External tools (guidance only): Manus, Grok, Perplexity, Segmentable, ChatGPT GPTs

## Usage

```
/market-research "AI courses for marketers"
/market-research "SaaS for HR analytics" --mode full
/market-research "EdTech platform in India" --mode quick
```
