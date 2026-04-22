# Food2Mood — PRODUCT

## 1. Что это

Food2Mood — это **движок цифрового вкусового профиля** для сетевых кафе и ресторанов. Система смотрит на меню, историю заказов гостя и его анкету и возвращает **персонализированные рекомендации блюд** с объяснением «почему именно это».

Формат доставки — не «ещё одно приложение для гостя», а backend для ресторанного digital-продукта (QR-меню, приложение сети, кассир с планшетом, Telegram-бот). Ресторан платит нам **за выручку, которую движок достаёт из хвоста меню и из повторных визитов**.

### Ключевые свойства

- **local-first MVP**: работает на файлах (`cust.json`, `menu_export.xlsx`), Postgres как опция;
- **closed taxonomy**: все теги в профиле и блюде — из словаря, новых в рантайме никто не выдумывает;
- **три слоя состояния гостя**: `hard_constraints` (аллергии, пост, безопасность), `long_term` (устойчивые предпочтения), `short_term` (последние 2–4 недели, быстрое затухание);
- **LLM только оффлайн** — извлечение признаков блюд, аудит анкеты. В request path модели не вызываются;
- **explainable score**: каждое блюдо в топ-10 раскладывается на слагаемые (`ingredient_match`, `format_texture_match`, `restaurant_context`, `repeat_bonus`, `novelty`, `venue_boost`, penalties) — можно показать менеджеру.

## 2. Целевая аудитория

Мы строим двухстороннюю ЦА: **ресторан платит**, **гость пользуется**.

### 2.1 Покупатель (кто платит)

**Head of Digital / Head of Marketing в сетевом ресторане на 5–50 точек.** Такие сети:
- уже имеют приложение или Telegram-бота;
- видят, что CRM шлёт всем одну и ту же рассылку, и понимают, что это грубо;
- имеют кассовую систему, откуда можно выгрузить чеки (iiko, r_keeper, Poster).

Боль: «рассылки отваливаются по open-rate, гость приходит, берёт одно и то же, чек не растёт».

### 2.2 Пользователь (кто ест)

Три сегмента, по убыванию частоты в истории заказов:

| Сегмент | Частота | Характер |
|---|---|---|
| **«Постоянник-рутинер»** | 3–8 раз в месяц в одну сеть | ест 2–3 блюда по кругу, редко пробует новое, чувствителен к повторному привкусу |
| **«Исследователь вкуса»** | 2–5 раз в месяц | хочет нового, но боится неудачи, читает описания долго |
| **«Осознанный»** | 1–4 раза в месяц | аллергии / диета / пост / «без глютена» — принимает решение через ограничения, а не через предпочтения |

Для каждого сегмента система ведёт себя по-разному: для первого давим на `repeat_bonus` и контекст времени дня, для второго — на `novelty`, для третьего — на `hard_constraints` как первый фильтр.

## 3. Продуктовые модули

```
[Menu ingest] ─▶ [Dish feature pipeline (stage A rules + stage B offline LLM)] ─▶ dish_feature_values
[cust.json / Questionnaire UI] ─▶ [Questionnaire extractor] ─▶ seed profile
[Orders / events] ─▶ [Event ingest] ─▶ events + event_items
                                              ▼
                                  [Profile rebuild] ─▶ user_profile (long_term + short_term + hard_constraints)
                                              ▼
                        [Deterministic scoring + explain] ─▶ top-N + rationale
                                              ▼
                               [Ranking dataset + outcome logger] (для будущей ML-модели)
```

## 4. Агрегаторы нейросетей и зачем

| Инструмент | Зачем используем |
|---|---|
| **OpenRouter** | единая точка входа к разным моделям (GPT-4o, Claude, Llama-3.1-70B, Qwen) при оффлайн-разметке блюд и аудите анкет. Даёт fallback и контроль стоимости по провайдеру. |
| **Replicate / Together** (резерв) | когда нужен open-source (`qwen2.5-72b`, `llama-3.3`) для разметки массивов меню — дешевле на объёме. |
| **Anthropic API (Claude)** | длинные контексты при анализе всего меню ресторана в одном промпте (Stage B dish features); лучший follow-instruction на разметочных промптах. |
| **OpenAI API (GPT-4o)** | structured output (JSON mode) для questionnaire extractor, когда нужен железный контракт полей. |
| **Yandex GPT / GigaChat** (резерв) | если клиенту важно, чтобы оффлайн-разметка не выходила за пределы РФ — для pilot-ов в чувствительных сетях. |

Правило: **агрегатор не вызывается в request path**. Он крутится в cron/worker ночью, результаты лежат в `dish_feature_values` и кэше.

## 5. Парсеры и зачем

| Парсер | Источник | Что извлекает | Где в коде |
|---|---|---|---|
| **Menu TXT/XLSX parser** | `menu_export.xlsx`, текстовые экспорты из iiko/r_keeper | `dish / semi_finished / ingredient` nodes, состав, выход, ккал, БЖУ | `app/pipelines/txt_data_layer.py` |
| **Ingredient alias extractor** | `ingredient_phrase_inventory.csv`, freeform ingredient_text | нормализация «масло сливочное», «слив. масло», «butter» → единый canonical id | `docs/ingredient_alias_extractor_prompt_v1.txt` + `app/pipelines/txt_data_layer.py` |
| **Dish feature tagger (stage A)** | описания блюд + словарь | детерминированные признаки: методы (`fried`, `grilled`), форматы (`soup`, `salad`, `bowl`), рестораны/меню | `app/pipelines/dish_features_stage_a.py` |
| **Dish feature tagger (stage B, оффлайн-LLM)** | описания + stage A | мягкие семантические признаки (`hearty`, `light`, `romantic`, `comfort_food`) | prompt в `docs/menu_tagger_prompt_v1.txt` |
| **Questionnaire extractor** | `cust.json` freeform-ответы | `hard_constraints`, `explicit_features` (taste/cuisine preferences), dislikes | `app/pipelines/questionnaire_seed.py` + `docs/questionnaire_extractor_prompt_v1.txt` |
| **Order item parser** | чеки из кассы | food/drink/service, матчинг строки чека к `dish_id` | `app/pipelines/real_purchase_recommender.py` (`ingest_real_orders`) |
| **Event ingestor** | будущие логи UI/бота | `view / long_view / add_to_cart / purchase_paid / ...`, идемпотентно по `event_uuid` | `app/api.py` → `repo.upsert_event` |

### Что парсеры умышленно **не** делают

- не создают новых тегов вне `runtime_taxonomy_resolved_v1.json`;
- не додумывают состав блюда, если нет источника;
- не вызывают LLM на hot-path — только в пайплайне.

## 6. Как выглядит результат для ресторана

Ресторан получает:
1. `dish_feature_values.csv` — размеченное меню (для Marketing/CRM);
2. `user_profiles` — sparse-векторы гостей (для сегментации рассылок);
3. `recommendations_sample.csv` + `recommendation_examples.md` — top-N для конкретного гостя с раскладкой по слагаемым;
4. `backtest_summary.csv` — hit-rate на hold-out, по каким сегментам работает, где проваливается.

## 7. Пример объяснения рекомендации (живой кусок `recommendation_examples.md`)

```
#1 Пикадильо (node_00480): 6.014
    ingredient_match=0.097
    format_texture_match=1.289
    restaurant_context=4.028
    novelty=0.350
    venue_boost=0.250
```

У гостя в профиле высокий вес `restaurant.venue:gc` (он регулярный в этой точке) и `format_texture.bowl / hearty`; блюдо это подсвечивает. Дальше мы показываем менеджеру буквально эти строки — и это главный барьер входа для тех, кто пытается продать ресторану «магическую коробку».
