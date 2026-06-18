# User_HRBP_Hierarchy_Level

*тека `USER` · формат `0`*

!!! abstract "Джерела даних"
    `DM.vw_R27_dim_Employee_Access_List`

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.LP.Nav.My_lead_team](../measures/ac-lp-nav-my-lead-team.md), [PP.Nav.My_lead_team](../measures/pp-nav-my-lead-team.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `USER` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
CALCULATE(
    MINX(ALL('dim_Admin_OS'),'dim_Admin_OS'[path_length_rls]),
    TREATAS({USERPRINCIPALNAME()},'dim_Admin_OS'[EMPLOYEE_EMAIL]),
    'dim_Admin_OS'[USER_ROLE] = "HRBP"
) - 1
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_EMAIL`, `USER_ROLE`, `path_length_rls`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length_rls]`

### Схема

```mermaid
graph LR
  M["User_HRBP_Hierarchy_Level"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

## Нотатки

_порожньо_
