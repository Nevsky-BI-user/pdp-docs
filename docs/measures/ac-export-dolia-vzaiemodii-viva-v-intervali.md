# AC.Export.Доля взаємодії (Viva) в інтервалі (%)

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
SELECTEDVALUE('fact_Loss_of_Productivity'[Collab_Hour_by_Span_Value])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Collab_Hour_by_Span_Value`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Collab_Hour_by_Span_Value → Доля взаємодії (Viva) в інтервалі (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Collab_Hour_by_Span_Value]`

## Схема

```mermaid
graph LR
  M["AC.Export.Доля взаємодії (Viva) в інтервалі (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
