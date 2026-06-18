# PP.Частка OKR за кросфункційністю

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\OKR` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _employee_id = CALCULATETABLE(VALUES('dim_Admin_OS'[EMPLOYEE_ID]))
VAR _res = 
CALCULATE(
    COUNTROWS(VALUES('fact_OKR_Goals'[OKR_OBJECTIVE_ID])),
    TREATAS(_employee_id,'fact_OKR_Goals'[EMPLOYEE_ID])
)
RETURN _res
```

## Джерела

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_ID`, `OKR_OBJECTIVE_ID`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`, `fact_OKR_Goals`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_OKR_Goals[EMPLOYEE_ID]`, `fact_OKR_Goals[OKR_OBJECTIVE_ID]`

## Схема

```mermaid
graph LR
  M["PP.Частка OKR за кросфункційністю"]
  M --> dim_Admin_OS
  M --> fact_OKR_Goals
```

## Нотатки

_порожньо_
