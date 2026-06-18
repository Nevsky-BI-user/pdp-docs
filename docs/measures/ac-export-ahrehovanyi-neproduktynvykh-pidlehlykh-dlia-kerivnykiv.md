# AC.Export.Агрегований % непродуктинвих підлеглих для керівників

*тека `Analytical Cases\Loss_Productivity\Export`*

## Бізнес-суть

Percentage_Of_Unproductive_Employees → Агрегований % непродуктинвих підлеглих для керівників

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

[Продуктивність працівників](../report/produktyvnist-pratsivnykiv.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Loss_of_Productivity'[Percentage_Of_Unproductive_Employees])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Percentage_Of_Unproductive_Employees`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Percentage_Of_Unproductive_Employees]`

### Схема

```mermaid
graph LR
  M["AC.Export.Агрегований % непродуктинвих підлеглих для керівників"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
