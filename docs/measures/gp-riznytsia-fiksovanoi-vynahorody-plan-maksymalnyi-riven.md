# GP.Різниця фіксованої винагороди (план).Максимальний рівень

*тека `Group_Profile\TRS` · формат `#,0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),dim_Admin_OS[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin =
    VAR _Employees = VALUES('dim_Admin_OS'[USER_ACCESS_ID])
        VAR _table0 = 
            ADDCOLUMNS(
                _Employees,
                "@Indicator",
                CALCULATE(
                    SUM('fact_TRS_Plan'[PAYMENT_PLAN_SUM]),
                    'fact_TRS_Plan'[CATEGORY_NAME] = "Фіксована винагорода",
                    'fact_TRS_Plan'[IS_ACTUAL] = TRUE(),
                    ('fact_TRS_Plan'[END_DATE] > TODAY() || 'fact_TRS_Plan'[END_DATE] = DATE(2001, 01, 01)),
                    'dim_Admin_OS'[IS_MANAGER] = FALSE())
            )
        VAR _ShareOfSomeIndicator = 
            MAXX(
                FILTER(
                    _table0, 
                    NOT ISBLANK([@Indicator]) && [@Indicator] > 0
                ), [@Indicator]
            )

        RETURN _ShareOfSomeIndicator

/* *********** ADMIN LT *********** */
VAR _admin_lt =
    VAR _Employees =VALUES('dim_Admin_OS'[USER_ACCESS_ID])
        VAR _table0 = 
            CALCULATETABLE(
                ADDCOLUMNS(
                    _Employees,
                    "@Indicator",
                    CALCULATE(
                        SUM('fact_TRS_Plan'[PAYMENT_PLAN_SUM]),
                        'fact_TRS_Plan'[CATEGORY_NAME] = "Фіксована винагорода",
                        'fact_TRS_Plan'[IS_ACTUAL] = TRUE(),
                        ('fact_TRS_Plan'[END_DATE] > TODAY() || 'fact_TRS_Plan'[END_DATE] = DATE(2001, 01, 01)),
                        'dim_Admin_OS'[IS_MANAGER] = FALSE(),
                        'fact_TRS_Plan'[PAYMENT_PLAN_SUM] > 0)),
                _filter_lt
            )
        VAR _ShareOfSomeIndicator = 
            MAXX(
                FILTER(
                    _table0, 
                    NOT ISBLANK([@Indicator]) && [@Indicator] > 0
                ), [@Indicator]
            )

        RETURN _ShareOfSomeIndicator
    
VAR _res = 
	SWITCH(
		_roleIndex,
		0, _admin_lt,
		1, _admin
	)
RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_TRS_Plan_PDP`

Колонки: `CATEGORY_NAME`, `END_DATE`, `IS_ACTUAL`, `IS_MANAGER`, `Index`, `PAYMENT_PLAN_SUM`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_TRS_Plan`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[IS_MANAGER]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_TRS_Plan[CATEGORY_NAME]`, `fact_TRS_Plan[END_DATE]`, `fact_TRS_Plan[IS_ACTUAL]`, `fact_TRS_Plan[PAYMENT_PLAN_SUM]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Різниця фіксованої винагороди (план).Максимальний рівень"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_TRS_Plan["fact_TRS_Plan"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md) — TRS
- [Підсказка "Макc винагорода (план)"](../report/pidskazka-makc-vynahoroda-plan.md)

## Пов'язані міри

**Використовується в:** [GP.Різниця фіксованої винагороди (план).Різниця](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-riznytsia.md)

## Нотатки

_порожньо_
