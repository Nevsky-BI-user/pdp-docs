# AC.Export.Доля днів польових робіт (%)

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
SELECTEDVALUE('fact_Loss_of_Productivity'[Fieldwork_Share])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Fieldwork_Share`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Fieldwork_Share → Доля днів польових робіт (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Fieldwork_Share]`

## Схема

```mermaid
graph LR
  M["AC.Export.Доля днів польових робіт (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
