# PP.Nav.My_lead_team

*тека `Navigation\Personal` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Navigation\Personal` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

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

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ROLE`, `path_length_rls`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length_rls]`

### Схема

```mermaid
graph LR
  M["PP.Nav.My_lead_team"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [User_Admin_Hierarchy_Level](../measures/user-admin-hierarchy-level.md), [User_HRBP_Hierarchy_Level](../measures/user-hrbp-hierarchy-level.md)

## Нотатки

_порожньо_
