# PP.Стаж в холдингу (неперервний)

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
VAR _seniority = SELECTEDVALUE(fact_employee_seniority_by_month[seniority_LAST_HOLDING_HIRE_DATE])
VAR _years = ROUNDDOWN(_seniority/12,0)
VAR _month = _seniority - _years *12
VAR _res = 
	IF(
		NOT ISBLANK( _seniority ),
		IF(
			NOT ISBLANK( _years ),
			_years & " р."
		) & " " &
		IF(
			NOT ISBLANK( _month ) && _month <> 0,
			_month & " міс."
		)
	)
RETURN 
	COALESCE(
		TRIM(_res),
		"-"
	)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_employee_seniority_by_month_PDP`

Колонки: `seniority_LAST_HOLDING_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

## Бізнес-суть

seniority_LAST_HOLDING_HIRE_DATE → Стаж в холдингу останній; seniority_LAST_HOLDING_HIRE_DATE → Стаж в холдингу; seniority_LAST_HOLDING_HIRE_DATE → Стаж в холдингу (останній)

Значення поля в місяцях потрібно перевести в роки та місяці. Наприклад, якшо seniority_LAST_HOLDING_HIRE_DATE= 17, то в звіті треба відобразити 1 рік 5 місяців.

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[seniority_LAST_HOLDING_HIRE_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Стаж в холдингу (неперервний)"]
  M --> fact_employee_seniority_by_month
```

## Нотатки

_порожньо_
