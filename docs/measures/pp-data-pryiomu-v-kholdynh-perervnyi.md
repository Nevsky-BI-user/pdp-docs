# PP.Дата прийому в холдинг (перервний)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res = SELECTEDVALUE('fact_employee_seniority_by_month'[FIRST_HOLDING_HIRE_DATE])
RETURN 
	COALESCE(
		FORMAT(
			_res,
			"dd.mm.yyyy"
		),
		"-"
	)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_employee_seniority_by_month_PDP`

Колонки: `FIRST_HOLDING_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

## Бізнес-суть

FIRST_HOLDING_HIRE_DATE → Стаж в холдингу (загальний)  <br>Дата прийому

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[FIRST_HOLDING_HIRE_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Дата прийому в холдинг (перервний)"]
  M --> fact_employee_seniority_by_month
```

## Нотатки

_порожньо_
