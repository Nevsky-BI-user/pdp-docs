# PP.Оцінка результативності.Самооцінка.Total

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\Результативність` |
| formatString | `0.00` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
CALCULATE(AVERAGE('fact_Employee_Performance_Total'[General_Self_Rate]))
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_General_PBI`

Колонки: `General_Self_Rate`

Power Query: `fact_Employee_Performance_Total`

## Бізнес-суть

General_Self_Rate → Загальна самооцінка працівника

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди`

## Залежності

Таблиці: `fact_Employee_Performance_Total`

Колонки: `fact_Employee_Performance_Total[General_Self_Rate]`

## Схема

```mermaid
graph LR
  M["PP.Оцінка результативності.Самооцінка.Total"]
  M --> fact_Employee_Performance_Total
```

## Нотатки

_порожньо_
