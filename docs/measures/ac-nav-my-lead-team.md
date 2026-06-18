# AC.Nav.My_lead_team

*тека `Analytical Cases\Burnout_Risk\Main` · формат `0`*

!!! abstract "Джерела даних"
    `DM.vw_R27_dim_Employee_Access_List`

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [Current_User_Admin_Hierarchy_Level](../measures/current-user-admin-hierarchy-level.md), [Current_User_HRBP_Hierarchy_Level](../measures/current-user-hrbp-hierarchy-level.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SWITCH(
	CALCULATE(
		SELECTEDVALUE('dim_Admin_OS'[path_length_rls]),
		TREATAS(VALUES('fact_Burnout_Indicators'[USER_ACCESS_ID]), 'dim_Admin_OS'[USER_ACCESS_ID])
	)  <= 
    SWITCH(
        SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
        "Адміністративний керівник", [Current_User_Admin_Hierarchy_Level],
        "HRBP", [Current_User_HRBP_Hierarchy_Level]
    ) + 2,
	TRUE(), 1,
	0
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ACCESS_ID`, `USER_ROLE`, `path_length_rls`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Burnout_Indicators`

Колонки: `dim_Admin_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length_rls]`, `fact_Burnout_Indicators[USER_ACCESS_ID]`

### Схема

```mermaid
graph LR
  M["AC.Nav.My_lead_team"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

## Нотатки

_порожньо_
