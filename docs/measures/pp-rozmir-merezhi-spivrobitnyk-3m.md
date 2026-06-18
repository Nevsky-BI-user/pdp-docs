# PP.Розмір мережі (співробітник, 3м)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Networks` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR employee = 
FIRSTNONBLANKVALUE(
		VALUES('dim_Admin_OS'[ORDER_NUM]),
		CALCULATE(SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_ID])))

VAR __val =
CALCULATE(
	[PP.Розмір мережі (Холдинг, 3м)],
	fact_Viva_Metrics[EMPLOYEE_ID] = employee)

RETURN __val
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_ID`, `ORDER_NUM`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Розмір мережі (Холдинг, 3м)](../measures/pp-rozmir-merezhi-kholdynh-3m.md)

Таблиці: `dim_Admin_OS`, `fact_Viva_Metrics`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `dim_Admin_OS[ORDER_NUM]`, `fact_Viva_Metrics[EMPLOYEE_ID]`

## Схема

```mermaid
graph LR
  M["PP.Розмір мережі (співробітник, 3м)"]
  M --> dim_Admin_OS
  M --> fact_Viva_Metrics
```

## Нотатки

_порожньо_
