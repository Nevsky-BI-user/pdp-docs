# GP._Manager_ID

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | так |

## DAX

```dax
			
FIRSTNONBLANKVALUE(
	'dim_Admin_OS'[ORDER_NUM_2],
	MIN('dim_Admin_OS'[USER_ACCESS_ID])
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `ORDER_NUM_2`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[ORDER_NUM_2]`, `dim_Admin_OS[USER_ACCESS_ID]`

## Схема

```mermaid
graph LR
  M["GP._Manager_ID"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
