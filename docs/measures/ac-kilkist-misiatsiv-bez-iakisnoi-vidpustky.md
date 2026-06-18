# AC.Кількість місяців без якісної відпустки

*тека `Analytical Cases\Burnout_Risk\Main` · формат `#,0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = SUM(fact_Burnout_Indicators[NO_QUALITY_VACATION_MONTHS])
RETURN _res
```

### Джерела даних


Колонки: `NO_QUALITY_VACATION_MONTHS`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[NO_QUALITY_VACATION_MONTHS]`

### Схема

```mermaid
graph LR
  M["AC.Кількість місяців без якісної відпустки"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

NO_QUALITY_VACATION_MONTHS → Кількість місяців без якісної відпустки

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Кількість місяців без якісної відпустки за ост. 3 роки](../measures/ac-switch-kilkist-misiatsiv-bez-iakisnoi-vidpustky-za-ost-3-roky.md)

## Нотатки

_порожньо_
