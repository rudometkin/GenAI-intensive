# GenAI-Intensive: Итоговая работа

**Задворнов Егор** | МФТИ | Апрель 2026

---

## Навигация

| Блок | Директория | Описание |
|------|-----------|----------|
| 1. OpenClaw | [OpenClaw/](OpenClaw/) | ПрофиАссистент -- AI-ассистент для репетиторов на Profi.ru. Архитектура, отчет, продукт, план, AJTBD |
| 2. PERSONAL | [PERSONAL/](PERSONAL/) | Personal AI OS -- 10 скиллов Claude Code, которые производят реальные проектные артефакты |
| 3. PROJECTCLONE | [PROJECTCLONE/](PROJECTCLONE/) | Клон Gamma.app -- MVP генератора AI-презентаций + аналитическое сравнение 5 open-source решений |
| 4. BONUS | [bonus/](bonus/) | Clone Pipeline -- 6 переиспользуемых скиллов для систематического клонирования GenAI-продуктов |

---

## Dogfooding: как это было сделано

Эта работа создана с помощью системы, описанной в Блоке 2. 9 из 10 скиллов использовались при подготовке:

| Артефакт | Скилл | Доказательство |
|----------|-------|----------------|
| Струк��ура и план домашки | `/think-through` | Этот README |
| 5 AJTBD-сегментов | `/tsa-progon` | [OpenClaw/AJTBD.md](OpenClaw/AJTBD.md) |
| Пивот монетизации 7500 -> гибрид | `/cddc-canvas` | [OpenClaw/REPORT.md](OpenClaw/REPORT.md), решение #3 |
| Продуктовый анализ OpenClaw | `/product-pipeline` | [OpenClaw/PRODUCT.md](OpenClaw/PRODUCT.md) |
| Конкурентный анализ Gamma + 20 аналогов | `/market-research` | [PROJECTCLONE/README.md](PROJECTCLONE/README.md), секция 5 |
| 6 clone-pipeline скиллов | `/skill-creator` | [bonus/skills/](bonus/skills/) |
| Промпты для AI-генерации | `/senior-prompt-engineer` | PROJECTCLONE/gamma-clone/prompts.py |
| Quality gates артефактов | `/code-reviewer` | Аудит всех файлов перед коммитом |
| Очистка текстов от AI-маркеров | `/de-ai-ify` | Все markdown-файлы |

---

## Технический стек

- **Claude Code (Opus 4.6)** -- основная среда разработки
- **164 скилла, 40+ агентов, 80+ команд** -- библиотека переиспользуемых AI-операций
- **Routing table** -- автоматический маршрут задача -> скилл по триггерам
- **Quality gates** -- автоматическая верификация перед завершением каждого этапа

---

## Автор

Задворнов Егор | МФТИ | @egor_zadvornov | github.com/LoveMyWork
