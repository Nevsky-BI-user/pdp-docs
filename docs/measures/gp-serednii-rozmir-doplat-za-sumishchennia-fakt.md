# GP.Середній розмір доплат за суміщення, факт

*тека `Group_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),dim_Admin_OS[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin = 
CALCULATE(
    AVERAGE('fact_TRS'[PAYMENTS_FACT_UAH]),
    'fact_TRS'[PAYMENTS_FACT_UAH] > 0,
    'fact_TRS'[ACCRUAL_TYPES_KEY] IN { "00b34057-6d79-2141-77d6-3f280e312196", "e48a6efe-4040-3d6c-4fab-7d9671f8a6c6",  "0b8a5246-2403-aea0-b64c-a76dfc32b115", "fbffac97-52df-2478-0a58-c4b4fe8f25a4"},
    'fact_TRS'[TAX_PIT_ID] = BLANK(),
    DATESINPERIOD( 'fact_TRS'[PERIOD], EOMONTH( TODAY(), - 1 ), - 12, MONTH ))

/* *********** LT *********** */
VAR _admin_lt =
CALCULATE(
    AVERAGE('fact_TRS'[PAYMENTS_FACT_UAH]),
    'fact_TRS'[PAYMENTS_FACT_UAH] > 0,
    'fact_TRS'[ACCRUAL_TYPES_KEY] IN { "00b34057-6d79-2141-77d6-3f280e312196", "e48a6efe-4040-3d6c-4fab-7d9671f8a6c6",  "0b8a5246-2403-aea0-b64c-a76dfc32b115", "fbffac97-52df-2478-0a58-c4b4fe8f25a4"},
    'fact_TRS'[TAX_PIT_ID] = BLANK(),
    DATESINPERIOD( 'fact_TRS'[PERIOD], EOMONTH( TODAY(), - 1 ), - 12, MONTH ),
    _filter_lt)

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)
RETURN 
COALESCE(_res, "-")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_TRS_PDP`

Колонки: `ACCRUAL_TYPES_KEY`, `Index`, `PAYMENTS_FACT_UAH`, `PERIOD`, `TAX_PIT_ID`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_TRS`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_TRS[ACCRUAL_TYPES_KEY]`, `fact_TRS[PAYMENTS_FACT_UAH]`, `fact_TRS[PERIOD]`, `fact_TRS[TAX_PIT_ID]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Середній розмір доплат за суміщення, факт"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_TRS["fact_TRS"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md) — TRS

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
