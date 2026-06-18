# PP.Nav.My_lead_team

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Navigation\Personal` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res = 
IF(
	SELECTEDVALUE('dim_Admin_OS'[path_length_rls]) <= 
    SWITCH(
        SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
        "Адміністративний керівник", [User_Admin_Hierarchy_Level],
        "HRBP", [User_HRBP_Hierarchy_Level]
    ) + 2,
	1,
	0
)
RETURN _res
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ROLE`, `path_length_rls`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [User_Admin_Hierarchy_Level](../measures/user-admin-hierarchy-level.md), [User_HRBP_Hierarchy_Level](../measures/user-hrbp-hierarchy-level.md)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length_rls]`

## Схема

```mermaid
graph LR
  M["PP.Nav.My_lead_team"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
