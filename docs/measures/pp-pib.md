# PP.PIB

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\_Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
COalesce(
	SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_NAME]),
	"-"
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_NAME`

Power Query: `dim_Admin_OS`

## Бізнес-суть

EMPLOYEE_NAME → ПІБ співробітника

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_NAME]`

## Схема

```mermaid
graph LR
  M["PP.PIB"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
