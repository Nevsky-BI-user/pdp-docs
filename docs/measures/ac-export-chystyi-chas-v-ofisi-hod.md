# AC.Export.Чистий час в офісі, год.

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
SELECTEDVALUE('fact_Loss_of_Productivity'[Net_Office_Time_AVG_3month])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Net_Office_Time_AVG_3month`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Net_Office_Time_AVG_3month → Чистий час в офісі, год.

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Net_Office_Time_AVG_3month]`

## Схема

```mermaid
graph LR
  M["AC.Export.Чистий час в офісі, год."]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
