---
name: clone-testing
description: Comprehensive testing -- unit, E2E, visual comparison with original, performance, security
category: clone-pipeline
trigger: "test clone", "compare with original", "clone testing", "visual comparison"
---

# Clone Testing

## When to Use
- MVP implemented (output of clone-implementation)
- Need to verify correctness, performance, and visual fidelity
- Pre-deployment quality gate

## Process

1. **Unit tests** -- core business logic:
   - Model validation and transformations
   - Utility functions
   - AI prompt construction
   - Target: 80%+ coverage on core modules
2. **Integration tests** -- API layer:
   - Each endpoint: happy path + error cases
   - Auth flow end-to-end
   - Database state verification
   - AI provider mock for deterministic results
3. **E2E tests** (Playwright) -- user flows:
   - Critical path: registration --> create --> edit --> export
   - Navigation and routing
   - Form submissions and validation messages
   - Responsive behavior (desktop + mobile viewports)
4. **Visual comparison** -- clone vs original:
   - Screenshot same pages on original and clone
   - Side-by-side comparison (manual or pixel-diff tool)
   - Document deviations with rationale (intentional vs bug)
5. **Performance benchmark**:
   - Lighthouse score (Performance, Accessibility, SEO)
   - API response times (p50, p95, p99)
   - AI generation latency (time-to-first-token, total)
   - Bundle size analysis
6. **Security scan**:
   - Dependency audit (npm audit / pip-audit)
   - OWASP Top 10 checklist
   - Auth bypass attempts
   - Input injection tests (XSS, SQL injection, prompt injection)

## Output
- Test suite (runnable via `pytest` / `npx playwright test`)
- Visual comparison report (screenshots + diff annotations)
- Performance metrics table
- Security audit report with severity ratings
- Overall quality verdict: PASS / PASS WITH NOTES / FAIL

## Example
SlideDeck AI testing: 47 unit tests (92% coverage), 12 integration tests, 6 E2E flows. Visual comparison shows 85% fidelity to Gamma.app -- deviations in animation timing (intentional) and font rendering (browser difference). Lighthouse: 89 Performance, 95 Accessibility. Security: 0 critical, 2 medium (rate limiting missing on AI endpoint, CSP header incomplete).
