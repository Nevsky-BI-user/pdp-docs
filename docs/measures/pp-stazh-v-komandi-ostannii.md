# PP.Стаж в команді (останній)

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
VAR _seniority = SELECTEDVALUE(fact_employee_seniority_by_month[seniority_LAST_DIVISION_HIRE_DATE])
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

Колонки: `seniority_LAST_DIVISION_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

## Бізнес-суть

seniority_LAST_DIVISION_HIRE_DATE → Стаж в команді; seniority_LAST_DIVISION_HIRE_DATE → <br>Середній стаж в команді

Значення поля в місяцях потрібно перевести в роки та місяці. Наприклад, якшо seniority_LAST_DIVISION_HIRE_DATE= 17, то в звіті треба відобразити 1 рік 5 місяців. Розрахункове поле: Х = (Х1 + Х2 + Х3.... + Xn )/С, де: - Х - середній стаж працівників команди; - Х1, Х2,Х3... Xn - стаж кожного працівника в підрозділі; - С - кількість працівників в команді  <br>На даний момент стаж буде розраховуватися однаково і для структурної одиниці (підрозділ), і для lead team.  <br>_Для  lead team потрібно буде рахувати стаж саме в цій команді по зв'яку Керівник - Підлеглий. Залежить від задачі по оновленню т

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[seniority_LAST_DIVISION_HIRE_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Стаж в команді (останній)"]
  M --> fact_employee_seniority_by_month
```

## Нотатки

_порожньо_
