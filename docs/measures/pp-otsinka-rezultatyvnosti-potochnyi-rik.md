# PP.Оцінка результативності поточний рік

*тека `Personal_Profile\Паспорт\Результативність` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Результативність` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SUM('fact_Burnout_Indicators'[LAST_YEAR_PERFORMANCE_DESC_RATE])
```

### Джерела даних


Колонки: `LAST_YEAR_PERFORMANCE_DESC_RATE`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[LAST_YEAR_PERFORMANCE_DESC_RATE]`

### Схема

```mermaid
graph LR
  M["PP.Оцінка результативності поточний рік"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [PP.SVG.Perfomance_Last_Year](../measures/pp-svg-perfomance-last-year.md), [PP.SVG.Performance.Last2Periods](../measures/pp-svg-performance-last2periods.md), [PP.Оцінка результативності поточний рік (пусто)](../measures/pp-otsinka-rezultatyvnosti-potochnyi-rik-pusto.md)

## Нотатки

_порожньо_
