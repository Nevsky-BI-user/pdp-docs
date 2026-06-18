# text.My_lead_team

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Navigation\Group` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SWITCH(
    SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
    "HRBP", "Мої прямі підопічні",
    "Мої прямі підлеглі"
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ROLE`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[USER_ROLE]`

## Схема

```mermaid
graph LR
  M["text.My_lead_team"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
