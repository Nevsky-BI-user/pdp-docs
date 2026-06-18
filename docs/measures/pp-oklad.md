# PP.Оклад

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SUM(fact_Employee_History_Position[Salary])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `Salary`

Power Query: `fact_Employee_History_Position`

## Бізнес-суть

Salary → Оклад

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`

## Залежності

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[Salary]`

## Схема

```mermaid
graph LR
  M["PP.Оклад"]
  M --> fact_Employee_History_Position
```

## Нотатки

_порожньо_
