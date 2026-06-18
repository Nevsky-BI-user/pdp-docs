# GP.ОКР.Останній рік

*тека `Group_Profile\_Main\ОКР` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\ОКР` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
CALCULATE(MAX('fact_Employee_OKR'[PLAN_YEAR]), ALL('dim_OKR_Evalution'))
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Goals`

Колонки: `PLAN_YEAR`

Power Query: `fact_Employee_OKR`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_OKR`

Колонки: `fact_Employee_OKR[PLAN_YEAR]`

### Схема

```mermaid
graph LR
  M["GP.ОКР.Останній рік"]
  M --> fact_Employee_OKR["fact_Employee_OKR"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [GP.ОКР.Кількість співробітників (Останній період оцінки)](../measures/gp-okr-kilkist-spivrobitnykiv-ostannii-period-otsinky.md), [GP.ОКР.Назва графіка](../measures/gp-okr-nazva-hrafika.md), [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md), [GP.ОКР.Середня оцінка команди.Значення](../measures/gp-okr-serednia-otsinka-komandy-znachennia.md)

## Нотатки

_порожньо_
