---
name: clone-analysis
description: Deep architecture analysis of selected target -- UI audit, code audit, API reverse-engineering
category: clone-pipeline
trigger: "analyze target", "reverse engineer", "architecture analysis", "clone analysis"
---

# Clone Analysis

## When to Use
- Target product selected (output of clone-discovery)
- Need full technical understanding before writing spec
- Want to map every component, API call, and data flow

## Process

1. **UI walkthrough** -- open target in Playwright, screenshot every screen and interaction flow
   - Map all pages/routes
   - Capture modal dialogs, dropdowns, edge states
   - Note animations, transitions, loading states
2. **Code audit** (if open-source) -- clone repo, analyze:
   - Project structure and framework choices
   - Core algorithms and business logic
   - Database schema and migrations
   - Third-party dependencies
3. **API analysis** -- open DevTools Network tab via Playwright:
   - Capture all API endpoints (REST/GraphQL/WebSocket)
   - Document request/response shapes
   - Identify authentication flow (JWT, OAuth, API keys)
   - Map rate limits and error handling patterns
4. **Component tree** -- build hierarchical map of UI components
5. **Data flow diagram** -- trace how data moves: user input --> frontend --> API --> AI model --> response --> UI
6. **Tech stack identification** -- confirm: framework, language, hosting, AI provider, database, CDN

## Output
- Architecture document (markdown) with:
  - Component map (hierarchical)
  - Tech stack summary table
  - Data flow diagram (text-based or Mermaid)
  - API endpoint catalog
  - Screenshots archive (numbered, annotated)

## Example
Target: Gamma.app. UI walkthrough reveals 12 core screens. Network analysis shows REST API at api.gamma.app with 34 endpoints. Tech stack: React + Next.js frontend, Python backend, GPT-4 for content generation, Unsplash for images. Component tree: Editor (BlockEditor, SlideCanvas, AIPanel, ThemePicker).
