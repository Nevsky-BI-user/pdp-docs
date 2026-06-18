# AC.Export.Тренд Результативності по KPI (%)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SELECTEDVALUE('fact_Loss_of_Productivity'[Award_Trend])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Award_Trend`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Award_Trend → Тренд Результативності по KPI (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Award_Trend]`

## Схема

```mermaid
graph LR
  M["AC.Export.Тренд Результативності по KPI (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
