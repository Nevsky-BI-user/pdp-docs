# AC.Дані.Агрегований % непродуктинвих підлеглих для керівників

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
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Percentage_Of_Unproductive_Employees])
RETURN COALESCE(_res, "—")
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Percentage_Of_Unproductive_Employees`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Percentage_Of_Unproductive_Employees → Агрегований % непродуктинвих підлеглих для керівників

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Percentage_Of_Unproductive_Employees]`

## Схема

```mermaid
graph LR
  M["AC.Дані.Агрегований % непродуктинвих підлеглих для керівників"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
