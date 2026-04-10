# Выходные файлы скиллов

## Таблица выходных файлов

| Скилл | Выходной файл | Ключевые разделы |
|-------|---------------|------------------|
| `/aim report` | `MARKETING-REPORT.md` | Executive Summary, сводный скоринг, приоритеты, план действий |
| `/aim audit` | `MARKETING-AUDIT.md` | Скоринг по 12 категориям, проблемы, рекомендации, план 30/60/90 |
| `/aim landing` | `LANDING-CRO.md` | Посекционный разбор, конверсионные барьеры, A/B-тесты, revenue impact |
| `/aim competitors` | `COMPETITOR-REPORT.md` | Карта конкурентов, SWOT, стратегические окна, дифференциация |
| `/aim brand` | `BRAND-VOICE.md` | Архетип, тональность, словарь бренда, do/don't, примеры копирайтинга |
| `/aim audience` | `AUDIENCE-RESEARCH.md` | Макросегменты, микропортреты, JTBD, когнитивные триггеры, ценообразование |
| `/aim emails` | `EMAIL-SEQUENCES.md` | Welcome-серия, nurture, sales, retention, шаблоны писем |
| `/aim social` | `SOCIAL-CALENDAR.md` | 30 дней постов, рубрики, форматы, хэштеги, время публикации |
| `/aim ads` | `AD-CAMPAIGNS.md` | Кампании Google/Meta/LinkedIn/TikTok, аудитории, креативы, бюджеты |
| `/aim headlines` | `HEADLINES.md` | 100 заголовков, группировка по уровням осведомлённости, A/B-варианты |

---

## Кросс-ссылки между файлами

### Какие файлы использует каждый скилл

| Скилл | Читает файлы |
|-------|-------------|
| `/aim report` | Все файлы (оркестратор) |
| `/aim audit` | -- (независимый) |
| `/aim landing` | -- (независимый) |
| `/aim competitors` | -- (независимый) |
| `/aim brand` | `MARKETING-AUDIT.md`, `COMPETITOR-REPORT.md` |
| `/aim audience` | `MARKETING-AUDIT.md`, `COMPETITOR-REPORT.md`, `BRAND-VOICE.md` |
| `/aim emails` | `BRAND-VOICE.md`, `AUDIENCE-RESEARCH.md`, `MARKETING-AUDIT.md` |
| `/aim social` | `BRAND-VOICE.md`, `AUDIENCE-RESEARCH.md`, `MARKETING-AUDIT.md` |
| `/aim ads` | `AUDIENCE-RESEARCH.md`, `BRAND-VOICE.md`, `COMPETITOR-REPORT.md` |
| `/aim headlines` | `BRAND-VOICE.md`, `AUDIENCE-RESEARCH.md` |

### Рекомендуемый порядок генерации

```
1. audit, landing, competitors  (базовый слой -- независимые)
2. brand, audience              (средний слой -- используют базовый)
3. emails, social, ads, headlines (контентный слой -- используют все)
4. report                       (финальный -- собирает всё)
```

---

> Сделано в **Лаборатории ИИ-Маркетинга** | [Telegram-канал](https://t.me/moremarketingisaid) — больше крутых AI-скиллов, связок, промптов и других крутых вещей
