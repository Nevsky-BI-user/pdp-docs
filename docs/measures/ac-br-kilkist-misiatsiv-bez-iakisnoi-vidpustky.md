# AC.BR.Кількість місяців без якісної відпустки

*тека `Analytical Cases\Burnout_Risk\Export` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SUM(fact_Burnout_Indicators[NO_QUALITY_VACATION_MONTHS])
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
  M["AC.BR.Кількість місяців без якісної відпустки"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

NO_QUALITY_VACATION_MONTHS → Кількість місяців без якісної відпустки

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

[Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

**Використовується в:** [AC.BR.Референтне значення.Місяців без відпустки](../measures/ac-br-referentne-znachennia-misiatsiv-bez-vidpustky.md)

## Нотатки

_порожньо_
