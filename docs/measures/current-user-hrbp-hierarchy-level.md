# Current_User_HRBP_Hierarchy_Level

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `USER` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
CALCULATE(
    MINX('dim_Admin_OS','dim_Admin_OS'[path_length_rls]),
    TREATAS({USERPRINCIPALNAME()},'dim_Admin_OS'[EMPLOYEE_EMAIL]),
    'dim_Admin_OS'[USER_ROLE] = "HRBP"
) - 1
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_EMAIL`, `USER_ROLE`, `path_length_rls`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length_rls]`

## Схема

```mermaid
graph LR
  M["Current_User_HRBP_Hierarchy_Level"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
