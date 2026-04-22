---
name: exam-prep
description: Builds a personalized exam preparation plan — topics, priorities, and a week-by-week schedule up to the exam date. Use when a student has an upcoming exam (ЕГЭ, ОГЭ, or any test).
allowedTools:
  - Read
  - Bash
---

# Exam Prep Planner

Строит план подготовки к экзамену: темы, приоритеты и понедельный график до даты экзамена. Учитывает слабые места ученика и сколько времени осталось.

---

## Triggers

- "составь план подготовки к ЕГЭ", "помоги подготовиться к экзамену"
- "exam prep plan", "prepare for exam"
- `/exam-prep`

---

## Входные данные

- Предмет и тип экзамена (ЕГЭ / ОГЭ / внутренний тест)
- Дата экзамена
- Слабые темы ученика (опционально)
- Количество занятий в неделю

---

## Промпт для генерации

```
You are a tutor building an exam preparation plan.

Rules:
- Calculate weeks remaining from today to exam date
- Prioritize weak topics — allocate more time to them
- Structure by weeks: list 2–3 topics per week
- Include mock exam sessions in the last 2 weeks
- Add a final "revision week" before the exam
- Be specific — name actual topics from the syllabus
- Language: Russian

Exam: {EXAM}
Subject: {SUBJECT}
Exam date: {DATE}
Weak topics: {WEAK}
Sessions per week: {SESSIONS}
Today's date: {TODAY}
```

Модель: `claude-haiku-4-5-20251001`.

---

## Вывод пользователю

```
План подготовки к ЕГЭ по математике
Дата экзамена: 3 июня | Осталось: 7 недель
──────────────────────────────────────────
Неделя 1 (22–28 апр): Алгебра — основы
  — Квадратные уравнения и неравенства
  — Степени и логарифмы (базовый уровень)

Неделя 2 (29 апр – 5 мая): Функции
  — Свойства и графики: линейная, квадратичная
  — Показательная и логарифмическая функции

Неделя 3 (6–12 мая): Геометрия
  — Планиметрия: треугольники, окружности
  — Задачи на вычисление площадей

Неделя 4 (13–19 мая): Слабые места ★
  — Параметры и уравнения с параметром
  — Прогрессии

Неделя 5 (20–26 мая): Разбор заданий
  — Задания части 1 на скорость
  — Профильные задания части 2

Неделя 6–7: Пробные экзамены + разбор ошибок
  — 2 полных пробника в условиях реального экзамена
  — Финальный повтор слабых тем

Удачи на экзамене!
```
