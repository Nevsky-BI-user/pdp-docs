# AC.Дані.Результативність по KPI (%)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Award_Norm_Pct])
RETURN COALESCE(_res, "—")
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Award_Norm_Pct`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Award_Norm_Pct → Результативність по KPI (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Award_Norm_Pct]`

## Схема

```mermaid
graph LR
  M["AC.Дані.Результативність по KPI (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
