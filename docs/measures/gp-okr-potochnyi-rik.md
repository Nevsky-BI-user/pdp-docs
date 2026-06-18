# GP.OKR  поточний рік

*тека `Group_Profile\_Main\SVG` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\SVG` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
CALCULATE(
	SUM('fact_Burnout_Indicators'[OKR_LAST_YEAR_RATE]),
	TREATAS({[GP._Manager_ID]}, 'fact_Burnout_Indicators'[USER_ACCESS_ID])
)
```

### Джерела даних


Колонки: `OKR_LAST_YEAR_RATE`, `USER_ACCESS_ID`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[OKR_LAST_YEAR_RATE]`, `fact_Burnout_Indicators[USER_ACCESS_ID]`

### Схема

```mermaid
graph LR
  M["GP.OKR  поточний рік"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP._Manager_ID](../measures/gp-manager-id.md)

**Використовується в:** [GP.OKR пусто](../measures/gp-okr-pusto.md), [GP.SVG.OKR команди](../measures/gp-svg-okr-komandy.md)

## Нотатки

_порожньо_
