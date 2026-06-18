# AC.Взаємодія з керівником

*тека `Analytical Cases\Burnout_Risk\Main` · формат `#,0.00`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | `#,0.00` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = SUM('fact_Burnout_Indicators'[MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR])
RETURN _res
```

### Джерела даних


Колонки: `MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR]`

### Схема

```mermaid
graph LR
  M["AC.Взаємодія з керівником"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Годин 1:1 в сер. за 3 міс.](../measures/ac-switch-hodyn-1-1-v-ser-za-3-mis.md), [AC.Switch.Годин 1:1 в сер. за 3 міс2](../measures/ac-switch-hodyn-1-1-v-ser-za-3-mis2.md)

## Нотатки

_порожньо_
