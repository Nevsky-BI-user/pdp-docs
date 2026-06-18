# AC.Export.Тренд Оцінки рез-ті (%)

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
SELECTEDVALUE('fact_Loss_of_Productivity'[Performance_Rate_Trend])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Performance_Rate_Trend`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Performance_Rate_Trend → Тренд Оцінки рез-ті (%); Performance_Rate_Trend → Тренд оцінки результативності

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Performance_Rate_Trend]`

## Схема

```mermaid
graph LR
  M["AC.Export.Тренд Оцінки рез-ті (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
