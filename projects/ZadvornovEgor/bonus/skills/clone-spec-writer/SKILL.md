---
name: clone-spec-writer
description: Generate full technical specification (TZ) from architecture analysis
category: clone-pipeline
trigger: "write spec", "TZ from analysis", "technical specification", "clone spec"
---

# Clone Spec Writer

## When to Use
- Architecture analysis complete (output of clone-analysis)
- Ready to define what exactly to build
- Need a document a developer can implement from without ambiguity

## Process

1. **Feature inventory** -- extract every feature from analysis, tag as:
   - MVP (must-have for launch)
   - V2 (nice-to-have, post-launch)
   - Skip (not worth cloning)
2. **API contracts** -- for each endpoint define:
   - Method, path, auth requirement
   - Request body (JSON schema)
   - Response body (JSON schema)
   - Error codes and messages
3. **Data models** -- define all entities:
   - Fields, types, constraints
   - Relationships (1:1, 1:N, N:M)
   - Indexes and unique constraints
4. **UI wireframes description** -- for each screen:
   - Layout (text description or ASCII)
   - Components used
   - User interactions and state transitions
5. **Acceptance criteria** -- per feature, write testable AC:
   - Given / When / Then format
   - Edge cases explicitly listed
6. **Tech stack recommendation** -- based on analysis, recommend:
   - Framework, language, database
   - AI model provider and fallback
   - Hosting and deployment strategy

## Output
- Complete TZ document (markdown, 30-80 pages equivalent) containing:
  - Feature list with priorities
  - API contract catalog
  - Data model diagrams
  - UI descriptions per screen
  - Acceptance criteria per feature
  - Recommended tech stack with rationale

## Example
Gamma.app TZ: 18 MVP features (AI generation, template picker, slide editor, export PDF, share link), 9 V2 features (collaboration, analytics, custom fonts). Data models: User, Workspace, Presentation, Slide, Theme, Asset. API: 22 MVP endpoints. Stack recommendation: Next.js + FastAPI + PostgreSQL + Gemini API.
