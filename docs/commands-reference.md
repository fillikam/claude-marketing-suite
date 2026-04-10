# Справочник команд

Полный список команд Claude Marketing Suite с префиксом `/aim`.

---

## Все команды

| Команда | Аргументы | Выходной файл | Описание |
|---------|-----------|---------------|----------|
| `/aim report` | `<URL>` | `MARKETING-REPORT.md` | Мета-оркестратор. Запускает все скиллы последовательно и собирает сводный отчёт |
| `/aim audit` | `<URL>` | `MARKETING-AUDIT.md` | Полный маркетинговый аудит: позиционирование, воронка, контент, SEO, CTA |
| `/aim landing` | `<URL>` | `LANDING-CRO.md` | CRO-аудит лендинга: посекционный анализ с рекомендациями по конверсии |
| `/aim competitors` | `<URL>` | `COMPETITOR-REPORT.md` | Конкурентная разведка: анализ 3-5 конкурентов, SWOT, стратегические окна |
| `/aim brand` | `<URL>` | `BRAND-VOICE.md` | Анализ голоса бренда: архетипы, тональность, словарь, гайдлайны |
| `/aim audience` | `<URL>` | `AUDIENCE-RESEARCH.md` | Исследование ЦА: JTBD, сегменты, когнитивные триггеры, ценообразование |
| `/aim emails` | `[URL]` | `EMAIL-SEQUENCES.md` | Email-последовательности: welcome, nurture, sales, retention |
| `/aim social` | `[URL]` | `SOCIAL-CALENDAR.md` | 30-дневный контент-план для соцсетей с рубриками и форматами |
| `/aim ads` | `[URL]` | `AD-CAMPAIGNS.md` | Рекламные кампании: Google, Meta, LinkedIn, TikTok |
| `/aim headlines` | `[URL]` | `HEADLINES.md` | 100 заголовков прямого отклика по шаблонам Шварца |

---

## Обозначения аргументов

- `<URL>` -- обязательный аргумент (URL сайта для анализа)
- `[URL]` -- опциональный. Если не указан, скилл использует данные из ранее созданных файлов

---

## Примеры использования

### Базовый аудит
```
/aim audit https://myapp.com
```

### Полный отчёт одной командой
```
/aim report https://myapp.com
```

### Генерация контента после аудита
```
/aim audit https://myapp.com
/aim brand https://myapp.com
/aim audience https://myapp.com
/aim emails
/aim social
/aim headlines
```

---

## Флаги и модификаторы

Скиллы не используют CLI-флаги. Все параметры передаются через текст запроса. Примеры:

```
/aim audit https://myapp.com на русском языке
/aim headlines для курса по Python
/aim social для B2B SaaS в финтехе
```

---

> Сделано в **Лаборатории ИИ-Маркетинга** | [Telegram-канал](https://t.me/moremarketingisaid) — больше крутых AI-скиллов, связок, промптов и других крутых вещей
