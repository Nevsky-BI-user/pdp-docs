# AC.Дані.Чистий час в офісі Тренд (%)

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
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Trend_Net_Office_Time_Pct])
RETURN COALESCE(_res, "—")
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Trend_Net_Office_Time_Pct`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Trend_Net_Office_Time_Pct → Чистий час в офісі Тренд (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Trend_Net_Office_Time_Pct]`

## Схема

```mermaid
graph LR
  M["AC.Дані.Чистий час в офісі Тренд (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
