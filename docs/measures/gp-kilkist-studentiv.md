# GP.Кількість студентів

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | `0;-0;0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
"В розробці"
// VAR _set =
//  CALCULATE(
//     COUNTROWS(VALUES('fact_Employee_List'[person_key])),
//     KEEPFILTERS('fact_Employee_List'[STATUS_KEY] = 11)
// )
```

## Джерела


Колонки: `STATUS_KEY`, `person_key`

Power Query: `fact_Employee_List`

## Бізнес-суть

Кількість студентів

Деталі підрахунку будуть додані після доробки відповідного довідника та оновлення алгоритму розрахунку.  <br>Потрібно рахувати унікальну к-ть, щоб двічі не рахували тих, в кого осн місце і сумісництво.

**Вимоги:** `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[STATUS_KEY]`, `fact_Employee_List[person_key]`

## Схема

```mermaid
graph LR
  M["GP.Кількість студентів"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
