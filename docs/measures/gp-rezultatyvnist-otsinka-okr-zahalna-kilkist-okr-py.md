# GP.Результативність.Оцінка OKR.Загальна кількість OKR.PY

*тека `Group_Profile\Результативність та оцінка\Оцінка OKR` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Результативність та оцінка\Оцінка OKR` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin

VAR _filter_admin = VALUES('dim_Admin_OS'[EMPLOYEE_ID])
VAR _filter_lt = 
CALCULATETABLE(
    VALUES('dim_Admin_OS'[EMPLOYEE_ID]), 
    TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), 'dim_Admin_OS'[USER_ACCESS_ID]))

VAR _admin = 
CALCULATE(
    COUNTA('fact_OKR_Goals'[OKR_OBJECTIVE_ID]),
    TREATAS(_filter_admin, 'fact_OKR_Goals'[EMPLOYEE_ID]),
    SELECTEDVALUE('fact_OKR_Goals'[PLAN_YEAR]) - 1 = 'fact_OKR_Goals'[PLAN_YEAR])

VAR _admin_lt = 
CALCULATE(
    COUNTA('fact_OKR_Goals'[OKR_OBJECTIVE_ID]),
    TREATAS(_filter_lt, 'fact_OKR_Goals'[EMPLOYEE_ID]),
    SELECTEDVALUE('fact_OKR_Goals'[PLAN_YEAR]) - 1 = 'fact_OKR_Goals'[PLAN_YEAR])

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)

RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_ID`, `Index`, `OKR_OBJECTIVE_ID`, `PLAN_YEAR`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_OKR_Goals`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_OKR_Goals[EMPLOYEE_ID]`, `fact_OKR_Goals[OKR_OBJECTIVE_ID]`, `fact_OKR_Goals[PLAN_YEAR]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Результативність.Оцінка OKR.Загальна кількість OKR.PY"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_OKR_Goals["fact_OKR_Goals"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md) — Результативність та оцінка › Оцінка ОКР

## Пов'язані міри

**Використовується в:** [GP.Результативність.Оцінка OKR.Середня кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-kr-py.md), [GP.Результативність.Оцінка OKR.Середня кількість OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-okr-py.md)

## Нотатки

_порожньо_
