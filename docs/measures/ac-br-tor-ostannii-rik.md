# AC.BR.ТОР останній рік

*тека `Analytical Cases\Burnout_Risk\Export` · формат `#,0.00`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | `#,0.00` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Burnout_Indicators'[LAST_YEAR_PERFORMANCE_DESC_RATE])
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
  M["AC.BR.ТОР останній рік"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
