# GP.Результативність.Оцінка результативності.К-ть працівників.Total

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Результативність та оцінка\Оцінка результативності` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt= TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), 'dim_Admin_OS'[USER_ACCESS_ID])

VAR _admin = 
CALCULATE(
    DISTINCTCOUNT('fact_Employee_Performance_Total'[USER_ACCESS_ID]))

VAR _admin_lt = 
CALCULATE(
    DISTINCTCOUNT('fact_Employee_Performance_Total'[USER_ACCESS_ID]),
    _filter_lt)

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)

RETURN _res
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Employee_Performance_General_PBI`

Колонки: `Index`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`, `fact_Employee_Performance_Total`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Employee_Performance_Total[USER_ACCESS_ID]`, `t_HierarchyTypes[Index]`

## Схема

```mermaid
graph LR
  M["GP.Результативність.Оцінка результативності.К-ть працівників.Total"]
  M --> dim_Admin_OS
  M --> fact_Employee_Performance_Total
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
