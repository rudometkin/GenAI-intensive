---
name: clone-discovery
description: Discovery phase -- compare 20+ competing services, build score matrix, select best clone target
category: clone-pipeline
trigger: "clone discovery", "find competitors", "what to clone", "score matrix", "compare services"
---

# Clone Discovery

## When to Use
- Starting a clone project from scratch -- need to pick the right target
- Have a product category but no specific product chosen
- Need structured comparison of GenAI market segment

## Process

1. **Define category** -- narrow down the product space (e.g. "AI presentation builders", "AI writing assistants")
2. **Web search** -- find 20+ products via Product Hunt, G2, AlternativeTo, GitHub Awesome lists, Reddit threads
3. **Build comparison table** -- for each product capture:
   - Name, URL, pricing (free tier / paid / enterprise)
   - Core features (bullet list)
   - Tech stack (frontend, backend, AI model)
   - Open-source availability (full OSS / partial / closed)
   - User base & traction (downloads, stars, reviews)
4. **Score matrix** -- rate each product 1-5 on:
   - **Openness** -- how much code/architecture is visible
   - **Complexity** -- effort to replicate (lower = better for cloning)
   - **Market fit** -- demand and willingness to pay
   - **Differentiation potential** -- room to improve over original
5. **Select target** -- pick the product with highest composite score
6. **Write rationale** -- 3-5 sentences explaining why this target was chosen

## Output
- Comparison table (markdown) with 20+ entries
- Score matrix with weighted scores
- Recommended target + rationale document
- List of runner-up alternatives

## Example
Category: "AI slide generators". Search yields Gamma.app, Beautiful.ai, Tome, SlidesAI, Decktopus, etc. Score matrix shows Gamma.app wins on market fit (4.8M users) + moderate complexity + partial API visibility. Recommendation: clone Gamma.app with focus on open-source LLM backend.
