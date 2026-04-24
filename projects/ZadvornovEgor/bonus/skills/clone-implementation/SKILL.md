---
name: clone-implementation
description: Scaffold project and implement MVP from spec -- boilerplate, core features, AI integration
category: clone-pipeline
trigger: "implement clone", "scaffold project", "build MVP", "clone implementation"
---

# Clone Implementation

## When to Use
- Technical specification ready (output of clone-spec-writer)
- Time to write actual code
- Goal: working MVP, not perfect product

## Process

1. **Scaffold project** -- generate boilerplate:
   - Initialize repo with chosen framework (Next.js, FastAPI, etc.)
   - Configure linters, formatters, pre-commit hooks
   - Set up environment variables template (.env.example)
   - Create folder structure matching spec's component map
2. **Implement data layer** -- database first:
   - Define models/schemas (SQLAlchemy, Prisma, etc.)
   - Write and run migrations
   - Seed development data
   - Add CRUD repository layer
3. **Implement API** -- endpoints from spec:
   - Auth flow (JWT/OAuth)
   - Core business endpoints
   - Input validation (Pydantic, Zod)
   - Error handling middleware
4. **Implement UI** -- screens from spec:
   - Layout components (header, sidebar, main)
   - Page components per route
   - Forms with validation
   - State management (zustand, Redux, etc.)
5. **Integrate AI components** -- the GenAI core:
   - LLM provider client (Gemini, OpenAI, Anthropic)
   - Prompt templates with variable injection
   - Streaming response handling
   - Fallback chain (primary model --> fallback model)
6. **Wire together** -- connect all layers:
   - Frontend calls API, API calls AI, results render in UI
   - End-to-end smoke test of critical path

## Output
- Working MVP codebase in git repository
- README with setup instructions
- .env.example with all required variables
- Development seed data
- At least one end-to-end flow working (e.g. "create presentation from prompt")

## Example
SlideDeck AI MVP: Next.js frontend scaffolded with 8 pages, FastAPI backend with 22 endpoints, PostgreSQL with 6 tables, Gemini integration for slide content generation. Critical path works: user enters topic --> AI generates outline --> slides render in editor --> export to PDF.
