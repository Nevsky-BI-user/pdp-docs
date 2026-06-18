# Administrative_role_filter

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `_Technical` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
COUNTROWS(
    FILTER(
        'dim_Admin_OS', 
        SEARCH(USERPRINCIPALNAME(), dim_Admin_OS[path_column_email], , 0) > 0
    )
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `path_column_email`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[path_column_email]`

## Схема

```mermaid
graph LR
  M["Administrative_role_filter"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
