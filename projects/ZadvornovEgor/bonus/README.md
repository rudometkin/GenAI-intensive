# Clone Pipeline: Reusable Methodology for Cloning GenAI Products

## Overview

6-phase pipeline that transforms "I want to build X" into a deployed, tested clone of any GenAI product. Each phase is a standalone skill with defined inputs, outputs, and methodology -- phases connect sequentially, where output of phase N becomes input for phase N+1.

```
Discovery --> Analysis --> Spec --> Implementation --> Testing --> Deployment
  (what)      (how it     (what    (build it)       (verify)    (ship it)
               works)      to build)
```

## Pipeline Phases

| # | Phase | Skill | Input | Output | Time Estimate |
|---|-------|-------|-------|--------|---------------|
| 1 | Discovery | `clone-discovery` | Product category | Score matrix + target selection | 2-4 hours |
| 2 | Analysis | `clone-analysis` | Selected target | Architecture document + API catalog | 4-8 hours |
| 3 | Spec | `clone-spec-writer` | Architecture document | Full TZ with acceptance criteria | 4-6 hours |
| 4 | Implementation | `clone-implementation` | TZ document | Working MVP codebase | 2-5 days |
| 5 | Testing | `clone-testing` | MVP codebase | Test suite + quality verdict | 1-2 days |
| 6 | Deployment | `clone-deployment` | Tested codebase | Production URL + CI/CD + monitoring | 4-8 hours |

**Total: 5-10 days from idea to production deployment.**

## How Phases Connect

```
[clone-discovery]
    |
    | comparison table + recommended target
    v
[clone-analysis]
    |
    | architecture doc (components, APIs, data flows, tech stack)
    v
[clone-spec-writer]
    |
    | full TZ (features, API contracts, data models, acceptance criteria)
    v
[clone-implementation]
    |
    | working MVP codebase (git repo, runnable locally)
    v
[clone-testing]
    |
    | test suite + quality verdict (PASS / FAIL)
    v
[clone-deployment]
    |
    | production URL + CI/CD pipeline + monitoring
    v
    DONE
```

Each phase can be re-entered independently. If testing reveals issues, loop back to implementation. If analysis shows the target is too complex, loop back to discovery and pick another.

## Applied Example: Gamma.app Clone

В рамках домашки пайплайн был применен в фазах 1-3 (Discovery, Analysis, Spec). Фазы 4-6 описаны как методология для будущих проектов.

1. **Discovery** -- через `/ai-search-free` сравнили 20+ AI-инструментов для презентаций. Gamma.app -- лучший по market fit + умере��ной сложности. Выбрали SlideDeck AI (346 stars, MIT, Python) как open-source базу.
2. **Analysis** -- агент `code-reviewer` провел аудит кода SlideDeck AI: структура, зависимости, безопасность. `/senior-architect` разобрал архитектуру: Streamlit UI, LiteLLM backend, python-pptx renderer.
3. **Spec** -- составлена таблица сравнения 5 решений по 6 критериям, декомпозиция на продуктовые модули, анализ рвов Gamma.app.
4. **Implementation** -- (методология) scaffolding + MVP из спецификации.
5. **Testing** -- (методология) unit + E2E + визуальное сравнение с оригиналом.
6. **Deployment** -- (методология) контейнеризация + CI/CD + мониторинг.

## Key Principles

- **Clone to learn, not to steal** -- the goal is understanding architecture patterns and building skills, not IP theft
- **MVP first** -- clone the core value prop (20% of features that deliver 80% of value), skip the rest
- **Open-source when possible** -- prefer targets with visible codebases for deeper analysis
- **AI-native** -- every phase uses AI tools (web search, code analysis, generation, testing)

## Meta

These skills were created using `/skill-creator` -- a skill that creates other skills. The pipeline itself is a demonstration of systematic approach to product cloning as a learning methodology.

## File Structure

```
bonus/
  README.md                              <-- this file
  skills/
    clone-discovery/SKILL.md             <-- phase 1: find and compare targets
    clone-analysis/SKILL.md              <-- phase 2: reverse-engineer architecture
    clone-spec-writer/SKILL.md           <-- phase 3: write technical specification
    clone-implementation/SKILL.md        <-- phase 4: build the MVP
    clone-testing/SKILL.md               <-- phase 5: test and compare
    clone-deployment/SKILL.md            <-- phase 6: ship to production
```
