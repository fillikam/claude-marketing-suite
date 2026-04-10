<div align="center">

# :rocket: Claude Marketing Suite

**AI-маркетолог внутри Claude Code. 10 скиллов. Одна экосистема.**

[![Skills](https://img.shields.io/badge/Skills-10-blue)]()
[![Language](https://img.shields.io/badge/Language-RU%20%2F%20EN-green)]()
[![Platform](https://img.shields.io/badge/Platform-Claude.ai-purple)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

</div>

---

## Что это такое

**Claude Marketing Suite** -- это набор из 10 взаимосвязанных скиллов для Claude Code, которые превращают AI в полноценный маркетинговый отдел. Каждый скилл запускается одной командой `/aim` и генерирует готовый к использованию `.md`-документ с профессиональной аналитикой, стратегиями и рекомендациями.

Не нужен ни один внешний сервис. Не нужны API-ключи. Только Claude Code и URL вашего сайта.

---

## Как работает одна команда

```
Вы: /aim audit https://example.com
```

Claude анализирует сайт, проверяет позиционирование, воронку, контент, SEO, конкурентов, CTA -- и создаёт файл `MARKETING-AUDIT.md` с:
- Скорингом по 12 категориям (0-100)
- Приоритезированным списком проблем
- Конкретными рекомендациями с оценкой revenue impact
- Готовым планом действий на 30/60/90 дней

---

## 10 скиллов

| # | Скилл | Команда | Выходной файл | Описание |
|---|-------|---------|---------------|----------|
| 0 | **Market Report** | `/aim report` | `MARKETING-REPORT.md` | Мета-оркестратор: запускает все скиллы и собирает единый отчёт |
| 1 | **Market Audit** | `/aim audit` | `MARKETING-AUDIT.md` | Полный маркетинговый аудит сайта с скорингом |
| 2 | **Landing CRO** | `/aim landing` | `LANDING-CRO.md` | CRO-аудит лендинга: посекционный разбор конверсий |
| 3 | **Competitors** | `/aim competitors` | `COMPETITOR-REPORT.md` | Конкурентная разведка и стратегический анализ |
| 4 | **Brand Voice** | `/aim brand` | `BRAND-VOICE.md` | Анализ голоса бренда, архетипы, тональность |
| 5 | **Audience Architect** | `/aim audience` | `AUDIENCE-RESEARCH.md` | Исследование ЦА через JTBD, когнитивные триггеры |
| 6 | **Email Sequences** | `/aim emails` | `EMAIL-SEQUENCES.md` | Генерация email-цепочек для воронки |
| 7 | **Social Calendar** | `/aim social` | `SOCIAL-CALENDAR.md` | 30-дневный контент-план для соцсетей |
| 8 | **Ad Campaigns** | `/aim ads` | `AD-CAMPAIGNS.md` | Рекламные кампании для Google/Meta/LinkedIn/TikTok |
| 9 | **Headlines** | `/aim headlines` | `HEADLINES.md` | 100 заголовков прямого отклика |

---

## Поток данных

```
                        /aim report
                            |
              +-------------+-------------+
              |             |             |
         /aim audit    /aim landing  /aim competitors
              |             |             |
              +------+------+------+------+
                     |             |
                /aim brand    /aim audience
                     |             |
              +------+------+------+------+
              |             |             |
         /aim emails   /aim social   /aim ads
                            |
                      /aim headlines
```

Каждый скилл может работать автономно, но при наличии выходных файлов других скиллов -- использует их данные для более точных результатов.

---

## Быстрый старт

### 1. Установите Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Склонируйте репозиторий

```bash
git clone https://github.com/anthropics/claude-marketing-suite.git
```

### 3. Установите скиллы

```bash
cd claude-marketing-suite
claude install-skills
```

### 4. Запустите первый аудит

```
/aim audit https://your-site.com
```

Подробнее: [QUICK-START.md](QUICK-START.md)

---

## Примеры использования

- [SaaS-компания](examples/saas-company/workflow.md) -- полный цикл от аудита до рекламы
- [E-commerce](examples/ecommerce/workflow.md) -- оптимизация интернет-магазина
- [Агентство](examples/agency/workflow.md) -- работа с клиентскими проектами

---

## Архитектура

Каждый скилл состоит из:
- **`.skill` файл** -- YAML-конфигурация с триггерами и метаданными
- **`SKILL.md`** -- промпт-инструкция для Claude

Скиллы используют:
- Структурированный Markdown-вывод
- Кросс-скилл интеграцию (автоматически подхватывают файлы друг друга)
- Guardrails для качества вывода
- Fallback-протоколы при недостатке данных

Подробнее: [docs/architecture.md](docs/architecture.md)

---

## Требования

- **Claude Code** (CLI) -- последняя версия
- **Claude Pro/Team/Enterprise** подписка
- Интернет-соединение (для анализа сайтов)
- Никаких API-ключей или внешних зависимостей

---

## Лицензия

MIT -- см. [LICENSE](LICENSE)
