# GP.К-ть співробітників, що отримують виплати на мобільний зв’язок

*тека `Group_Profile\TRS` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
| formatString | `0` |
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
    COUNTA('fact_Mobile_Limit'[USER_ACCESS_ID]),
    FILTER(
        'fact_Mobile_Limit',
        NOT ISBLANK('fact_Mobile_Limit'[PHONE_CORP_LIMIT]) && 'fact_Mobile_Limit'[PHONE_CORP_LIMIT] <> 0))
        
/* *********** LT *********** */
VAR _admin_lt =
    CALCULATE(
        COUNTA('fact_Mobile_Limit'[USER_ACCESS_ID]),
        FILTER(
            'fact_Mobile_Limit',
            NOT ISBLANK('fact_Mobile_Limit'[PHONE_CORP_LIMIT]) && 'fact_Mobile_Limit'[PHONE_CORP_LIMIT] <> 0),
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

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Mobile_Limit_PDP`

Колонки: `Index`, `PHONE_CORP_LIMIT`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Mobile_Limit`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Mobile_Limit[PHONE_CORP_LIMIT]`, `fact_Mobile_Limit[USER_ACCESS_ID]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.К-ть співробітників, що отримують виплати на мобільний зв’язок"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Mobile_Limit["fact_Mobile_Limit"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовується в:** ['GP.Мобільний зв''язок, % факт.SVG'](../measures/gp-mobilnyi-zviazok-fakt-svg.md)

## Нотатки

_порожньо_
