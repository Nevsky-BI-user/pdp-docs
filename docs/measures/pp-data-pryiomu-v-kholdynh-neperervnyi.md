# PP.Дата прийому в холдинг (неперервний)

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
VAR _res = SELECTEDVALUE('fact_employee_seniority_by_month'[LAST_HOLDING_HIRE_DATE])
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

Колонки: `LAST_HOLDING_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

## Бізнес-суть

LAST_HOLDING_HIRE_DATE → Дата останнього прийому працівника у холдинг; LAST_HOLDING_HIRE_DATE → Стаж в холдингу (останній)  <br>Дата прийому

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[LAST_HOLDING_HIRE_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Дата прийому в холдинг (неперервний)"]
  M --> fact_employee_seniority_by_month
```

## Нотатки

_порожньо_
