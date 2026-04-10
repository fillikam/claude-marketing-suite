# Пример: Маркетинговое агентство

## Сценарий

Вы -- маркетинговое агентство. Новый клиент: фитнес-студия `https://ironpulse.com`. Нужно за один день подготовить стратегию и презентовать клиенту.

---

## Шаг 1: Полный отчёт одной командой

```
/aim report https://ironpulse.com
```

Мета-оркестратор последовательно запускает все 9 скиллов и собирает `MARKETING-REPORT.md` -- сводный документ для презентации клиенту.

## Альтернатива: пошаговый запуск

Если нужен контроль над каждым этапом:

### Аналитика (утро)

```
/aim audit https://ironpulse.com
/aim landing https://ironpulse.com
/aim competitors https://ironpulse.com
```

Три базовых отчёта для понимания текущей ситуации.

### Стратегия (день)

```
/aim brand https://ironpulse.com
/aim audience https://ironpulse.com
```

Голос бренда и портреты целевой аудитории.

### Контент и реклама (вечер)

```
/aim emails
/aim social
/aim ads
/aim headlines
```

Готовые материалы для реализации стратегии.

---

## Работа с несколькими клиентами

Создайте отдельную папку для каждого клиента:

```bash
mkdir -p clients/ironpulse clients/yogaflow clients/crossfit-lab
```

Запускайте скиллы из соответствующей папки:

```bash
cd clients/ironpulse
# Здесь запускаете /aim audit https://ironpulse.com
# Файлы создадутся в clients/ironpulse/

cd ../yogaflow
# Здесь запускаете /aim audit https://yogaflow.com
# Файлы создадутся в clients/yogaflow/
```

## Результат

Полный маркетинговый пакет для клиента за 1 день вместо 2-3 недель. 9 документов, готовых к презентации и реализации.
