---
name: clone-deployment
description: Production deployment -- Docker, CI/CD, domain, monitoring, launch checklist
category: clone-pipeline
trigger: "deploy clone", "production deployment", "launch clone", "clone deployment"
---

# Clone Deployment

## When to Use
- Testing complete, quality verdict is PASS (output of clone-testing)
- Ready to ship to production
- Need repeatable, automated deployment pipeline

## Process

1. **Containerization**:
   - Dockerfile per service (frontend, backend, worker)
   - docker-compose.yml for local orchestration
   - Multi-stage builds for minimal image size
   - Health check endpoints in each service
2. **CI/CD pipeline** (GitHub Actions):
   - On push: lint --> type-check --> unit tests --> build
   - On PR merge to main: full test suite --> build images --> push to registry
   - On release tag: deploy to production
   - Secrets managed via GitHub Secrets / Vault
3. **Domain and SSL**:
   - DNS A/CNAME records (Cloudflare or provider)
   - SSL via Let's Encrypt (auto-renewal)
   - Reverse proxy (nginx / Caddy)
4. **Monitoring**:
   - Uptime monitoring (UptimeRobot, Uptime Kuma)
   - Error tracking (Sentry)
   - Performance APM (response times, error rates)
   - AI cost tracking (tokens used, cost per request)
5. **Launch checklist**:
   - [ ] All ENV variables set in production
   - [ ] Database migrations applied
   - [ ] SSL certificate valid
   - [ ] Monitoring alerts configured
   - [ ] Backup strategy in place
   - [ ] Rate limiting enabled
   - [ ] CORS configured for production domain
6. **Post-launch verification**:
   - Smoke test critical path on production URL
   - Verify monitoring receives data
   - Check logs for errors in first 15 minutes

## Output
- Deployed application accessible via production URL
- CI/CD pipeline (green builds)
- Monitoring dashboard with alerts
- Deployment runbook for future releases

## Example
SlideDeck AI deployed: frontend on Vercel, backend on Railway (Docker), PostgreSQL on Supabase. CI/CD: GitHub Actions with 3 stages, ~4 min total. Domain: slidedeck.example.com with Cloudflare DNS + SSL. Monitoring: Sentry for errors, UptimeRobot for uptime, custom dashboard for AI token spend (~$0.03/generation).
