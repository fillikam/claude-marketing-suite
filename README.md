<div align="center">

# :rocket: Claude Marketing Suite

**AI-маркетолог внутри Claude Code. 10 скиллов. Одна экосистема.**

[![Skills](https://img.shields.io/badge/Skills-10-blue)]()
[![Language](https://img.shields.io/badge/Language-RU%20%2F%20EN-green)]()
[![Platform](https://img.shields.io/badge/Platform-Claude.ai-purple)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Download](https://img.shields.io/badge/⬇_Скачать_ZIP-все_10_скиллов-brightgreen?style=for-the-badge)](https://github.com/Fillikam/claude-marketing-suite/releases/download/v1.0.0/claude-marketing-suite-all-skills.zip)

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

### Способ 1: Для новичков (без терминала, без кода)

> Самый простой способ — скачать ZIP и попросить Claude всё установить.

1. **[⬇️ Скачайте ZIP-архив со всеми скиллами](https://github.com/Fillikam/claude-marketing-suite/releases/download/v1.0.0/claude-marketing-suite-all-skills.zip)** (108 KB)
2. **Откройте [claude.ai](https://claude.ai)** (нужна подписка Pro или выше)
3. **Прикрепите ZIP-файл** к чату (иконка 📎 скрепки)
4. **Напишите этот промпт:**

```
Установи все .skill файлы из этого архива. Это маркетинговый пакет
Claude Marketing Suite. Распакуй архив и установи каждый .skill файл
как скилл. После установки покажи список установленных скиллов.
```

5. **Готово!** Теперь можно использовать команды:
```
/aim audit https://your-site.com
```

---

### Способ 2: Установка скиллов по одному

Если не хотите ставить весь пакет — установите только нужные скиллы:

1. Откройте нужную папку в `skills/` (например, `skills/01-aim-audit/`)
2. Скачайте файл `.skill` (нажмите на файл → кнопка ⬇️ Download)
3. В [claude.ai](https://claude.ai) откройте **чат → прикрепите .skill файл → напишите:**
```
Установи этот скилл
```
4. Повторите для каждого нужного скилла

**Минимальный набор для старта:**
- `aim-audit.skill` — базовый аудит (начните с него)
- `aim-landing.skill` — CRO-анализ лендингов
- `aim-report.skill` — финальный сводный отчёт

---

### Способ 3: Установка одним промптом (Claude Code)

Если у вас есть Claude Code (CLI), скопируйте и вставьте:

```
Скачай репозиторий https://github.com/Fillikam/claude-marketing-suite
и установи из него все .skill файлы как скиллы.
```

---

### Способ 4: Автоматическая установка через терминал (для разработчиков)

Одна команда — устанавливает всё: скиллы, агентов, скрипты, шаблоны.

```bash
# Установка одной командой (через curl)
curl -fsSL https://raw.githubusercontent.com/fillikam/claude-marketing-suite/master/install.sh | bash

# Или если уже склонировали репо
git clone https://github.com/fillikam/claude-marketing-suite.git
cd claude-marketing-suite
bash install.sh
```

Для удаления:
```bash
bash uninstall.sh
```

Подробнее: [QUICK-START.md](QUICK-START.md)

---

## Примеры использования

- [SaaS-компания](examples/saas-company/workflow.md) -- полный цикл от аудита до рекламы
- [E-commerce](examples/ecommerce/workflow.md) -- оптимизация интернет-магазина
- [Агентство](examples/agency/workflow.md) -- работа с клиентскими проектами

---

## Что входит в пакет

| Компонент | Что это | Папка |
|-----------|---------|-------|
| 10 скиллов | `.skill` файлы + SKILL.md — основные команды `/aim` | `skills/` |
| Оркестратор | Главный роутер всех `/aim` команд | `aim/` |
| 5 агентов | Параллельные субагенты для `/aim audit` | `agents/` |
| 4 Python-скрипта | Анализ страниц, конкурентов, PDF, контент-план | `scripts/` |
| 6 шаблонов | Email-серии, контент-календарь, чеклист запуска, пропозал | `templates/` |

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

---

<div align="center">

### Сделано в Лаборатории ИИ-Маркетинга

Больше крутых AI-скиллов, связок, промптов и других крутых вещей можно найти в канале:

[![Telegram](https://img.shields.io/badge/Telegram-канал-blue?style=for-the-badge&logo=telegram)](https://t.me/moremarketingisaid)

**[@moremarketingisaid](https://t.me/moremarketingisaid)**

</div>
