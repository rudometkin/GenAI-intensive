# CODEBASE

Сюда кладётся код, который мы готовы выложить публично.

Текущий статус: основной код живёт у меня локально в `D:\f2m` (пакет `food2mood-mvp v0.1.0`). Публично выкладывается не весь репозиторий, а:

- `app/` — доменная модель, репозитории, пайплайны, API, CLI;
- `db/migrations/001..003` — SQL-миграции Postgres;
- `tests/` — юнит-тесты на ключевые инварианты;
- `docs/` — master-spec, AGENTS, промпты для оффлайн-LLM, таксономия (`runtime_taxonomy_resolved_v1.json`);
- `pyproject.toml`, `requirements.txt`.

**Не выкладываем наружу:**
- `data/derived_real/` и `data/derived/` — они содержат сырые агрегаты из чеков пилотных клиентов, это их данные.
- `cust.json` — персональные данные гостей, только внутренний контур.
- `demo_profiles_output/` — маркетинговые артефакты под конкретные демо.

## Как запустить локально (для ревьюера)

```bash
pip install -e .[dev]
# 1. Прогнать таксономию-лок и базовые тесты
pytest
# 2. Построить feature layer из меню + анкеты
food2mood extract-questionnaire --users cust.json --out data/derived
food2mood build-dish-features --menu docs/menu_export.xlsx --out data/derived
# 3. Пересобрать профили и получить топ-N
food2mood rebuild-profiles --out data/derived
food2mood score-dishes --user-id 42 --top-k 10
# 4. Поднять API
food2mood serve --dsn postgresql://... --derived data/derived
```

## Ссылка на публичный репозиторий

TODO: после того как выделю `app/` + `tests/` + `db/` в отдельный GitHub-репо `food2mood-mvp`, ссылка встанет сюда.
