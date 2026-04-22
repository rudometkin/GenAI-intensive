# Food2Mood — REPORT

Что изменилось за последние ~2 недели на уровне архитектуры. Снимок сделан 2026-04-22 на основе состояния репозитория `D:\f2m` (`food2mood-mvp v0.1.0`).

---

## 1. Короткий итог

Проект из «скрипта, который парсит меню и cust.json и выдаёт что-то похожее на профиль» превратился в **модульный локальный MVP с явной доменной моделью, закрытой таксономией и полноценным бэктестом**. Появилось API (FastAPI), CLI, две параллельные реализации репозитория (файловая и Postgres) и оффлайн-пайплайн обогащения блюд. Заложена почва, на которой уже можно ставить эксперименты.

## 2. Слои архитектуры (стало)

```
app/
├── domain/              # модели и политики предметки (не знают про хранилище)
│   ├── models.py        # Event, EventItem, UserFeatureValue, UserConstraint, ...
│   └── policy.py        # правила: decay, hard vs soft, modifiers-patch
├── config/
│   └── taxonomy.py      # загрузка closed taxonomy из docs/runtime_taxonomy_resolved_v1.json
├── repositories/        # адаптеры хранилища, оба за единым интерфейсом
│   ├── base.py
│   ├── file_repository.py
│   └── postgres_repository.py
├── pipelines/           # пайплайны построения признаков
│   ├── txt_data_layer.py          # меню → nodes (dish/semi/ingredient)
│   ├── dish_features_stage_a.py   # детерминированные признаки блюд
│   ├── questionnaire_seed.py      # анкета → профиль
│   ├── questionnaire_audit.py     # аудит качества анкеты
│   ├── profile_rebuild.py         # пересборка профиля из событий
│   ├── seed_events.py             # исторические заказы → events
│   ├── real_purchase_recommender.py  # рекомендации на реальных меню/заказах
│   ├── recommendation_dataset.py  # датасет для ранжирующей модели + логи
│   └── scoring_deterministic.py   # детерминированный scoring/explain
├── services/
│   ├── repository_sync.py         # двунаправленный sync file ↔ postgres
│   └── api_smoke.py               # smoke-тесты API и идемпотентности
├── api.py                          # FastAPI
└── cli.py                          # единая консоль всех пайплайнов
```

## 3. Ключевые архитектурные решения за 2 недели

| # | Что | Почему | Последствие |
|---|---|---|---|
| 1 | Разнесли **domain / pipelines / repositories / services** | раньше всё было перемешано в одном скрипте, нельзя было тестировать | тесты теперь есть на 9 пайплайнах (`tests/test_*.py`), замена файлового хранилища на Postgres не ломает пайплайны |
| 2 | Ввели **closed taxonomy** (`runtime_taxonomy_resolved_v1.json`) + `test_taxonomy_lock` | раньше каждая часть генерировала свои ярлыки, пересечение не было возможно | модель «пользователь ↔ блюдо» стала sparse и сравнимой; пайплайны не имеют права выдумывать теги в рантайме |
| 3 | Разделили **hard_constraints / long_term / short_term** | по спеке это три независимых слоя, но фактически они слипались | безопасность (аллергии, религия) теперь фильтрует до скоринга, а не «учитывается весом» |
| 4 | Сделали **двунаправленный sync file ↔ postgres** (`services/repository_sync.py`) | по DoD MVP должен работать на файлах, но Postgres нужен для масштаба | можно дампить derived в Postgres для экспериментов и обратно, без переписывания доменной логики |
| 5 | Ввели **stage A** для dish features (детерминированные правила без LLM) и оставили hook под stage B (offline LLM) | нельзя вызывать LLM в рантайме, но нужно извлекать `fried/grilled/soup/...` из описаний | предсказуемая база + возможность постепенно улучшать без регрессий |
| 6 | Разделили **events** и **event_items** (idempotent ingest) | один чек — много позиций; нужна идемпотентность по `event_uuid` | api `/events/ingest` можно дёргать повторно, история не дублируется |
| 7 | Добавили **questionnaire_audit** отдельным пайплайном | анкета плохо заполняется, без аудита профиль шумит | видно, где именно протекает извлечение, можно выборочно чинить prompt |
| 8 | Реализовали **real_purchase_recommender** и **backtest** на отдельном реальном датасете (`data/derived_real/`) | синтетика лжёт; только живые чеки показывают, что скоринг работает | есть `backtest_summary.csv`, `recommendations_sample.csv`, `recommendation_examples.md` — можно предметно обсуждать качество |
| 9 | Вынесли **scoring_deterministic.py** (ingredient_match + method_cuisine_match + format_texture_match + restaurant_context + novelty/repeat + venue_boost + penalties) | скоринг, разнесённый по файлам, не читался; нельзя было объяснить, почему top-1 именно такой | теперь `explain_dish_for_user` возвращает раскладку по слагаемым — показываем ресторану буквально формулу |
| 10 | Миграции Postgres (`db/migrations/001..003`) лежат в репо и применяются из CLI | ручные `psql` неповторимы | развернуть проект на новой машине — один `food2mood apply-migrations` |

## 4. Что переделали (регрессы и честные откаты)

- **Отказались от дэнс-векторных профилей.** Пробовали embeddings — на MVP-объёме они лишь усложнили отладку и не дали прирост. Возврат к sparse `taxonomy`. Возвращаться к dense — только после 10k+ пользователей и своего корпуса сигналов.
- **Отказались от Redis / Kafka / Clickhouse** в MVP (как и записано в `codex_master_spec_v2.md § 2`). JSON-кэш + Postgres хватает до первых 1–2 ресторанов.
- **Перетащили LLM с рантайма в оффлайн.** В первых версиях были попытки подтянуть LLM на каждый запрос рекомендации — убрали жёстко, `api_smoke` теперь проверяет, что в request path LLM-вызовов нет.
- **Переосмыслили `ingredient_dictionary`.** Строили словарь «из меню», получался шум и typo (см. `ingredient_typo_clusters.csv`). Ввели ручной ревью `manual_curation/` + `ingredient_alias_review`. Стало хуже по ощущению «сделано быстро», стало лучше по качеству матчинга.
- **Кэш блюд.** Пришлось держать **два** файла (`dish_features_cache.json` и `dish_feature_cache.json`) из-за исторической несовместимости; тех-долг — свести в один; не делали сейчас, потому что на него завязаны демо-отчёты.

## 5. Что заложили на будущее (в план)

- **Stage B — оффлайн-LLM разметка мягких семантических тегов** (romantic, comfort, hearty). Сейчас она руками в stage A по ключевым словам.
- **Ranking-модель** поверх `ranking_dataset_rows.jsonl`. Сейчас скор детерминированный, датасет уже накапливается.
- **Модуль модификаторов** (`policy.py` принимает modifiers, но `event_items.modifiers_json` ещё не патчит consumed items в полную силу).
- **Questionnaire UI / веб-анкета** — пока seed идёт из cust.json.
- **Event logger** как отдельный сервис (сейчас всё через `/events/ingest`, без батчей и без backpressure).
- **UI для ресторана** — pilot-кабинет, где видно recommendations sample и explanation, чтобы менеджер ресторана мог сам читать объяснения.

## 6. Тесты и фактическое состояние

- `tests/test_taxonomy_lock.py` — инвариант «никто не плодит теги в рантайме»;
- `tests/test_dish_features_stage_a.py` — детерминированные признаки не ломаются при добавлении новой таксономии;
- `tests/test_file_repository.py` — CRUD, idempotency;
- `tests/test_profile_rebuild.py` — пересборка профиля из событий;
- `tests/test_scoring_deterministic.py` — эталонные пары user×dish дают ожидаемый score;
- `tests/test_recommendation_dataset.py` — формат ranking-датасета;
- `tests/test_questionnaire_audit.py` — аудит не молчит при пустых ответах;
- `tests/test_seed_events_pipeline.py` — seed от чеков до events;
- `tests/test_txt_data_layer.py` — меню → nodes.

## 7. DoD на сейчас

MVP-требование из `AGENTS.md`:
- [x] loads `menu_export.xlsx`
- [x] loads `cust.json`
- [x] builds dish features (stage A)
- [x] rebuilds user profiles
- [x] exposes profile JSON via API (FastAPI, `POST /events/ingest`, `POST /score`) и CLI (`food2mood`)
- [x] tests for safety, decay, modifiers, idempotency — основа есть; глубину по модификаторам ещё добираем.
