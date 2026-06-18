# GP.Середній стаж в команді, років

*тека `Group_Profile\_Main\Дані про команду`*

!!! abstract "Джерела даних"
    `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_employee_seniority_by_month_PDP`

## Бізнес-суть

seniority_LAST_DIVISION_HIRE_DATE → Стаж в команді; seniority_LAST_DIVISION_HIRE_DATE → <br>Середній стаж в команді

Значення поля в місяцях потрібно перевести в роки та місяці. Наприклад, якшо seniority_LAST_DIVISION_HIRE_DATE= 17, то в звіті треба відобразити 1 рік 5 місяців. Розрахункове поле: Х = (Х1 + Х2 + Х3.... + Xn )/С, де: - Х - середній стаж працівників команди; - Х1, Х2,Х3... Xn - стаж кожного працівника в підрозділі; - С - кількість працівників в команді  <br>На даний момент стаж буде розраховуватися однаково і для структурної одиниці (підрозділ), і для lead team.  <br>_Для  lead team потрібно буде рахувати стаж саме в цій команді по зв'яку Керівник - Підлеглий. Залежить від задачі по оновленню т

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Дані про команду` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),dim_Admin_OS[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin = 
	CALCULATE(
		AVERAGEX(
			VALUES('dim_Admin_OS'[USER_ACCESS_ID]),
			CALCULATE(AVERAGE(fact_employee_seniority_by_month[seniority_LAST_DIVISION_HIRE_DATE]))
		)
	)

/* *********** LT *********** */
VAR _admin_lt = 
	CALCULATE(
		AVERAGEX(
			VALUES('dim_Admin_OS'[USER_ACCESS_ID]),
			CALCULATE(AVERAGE(fact_employee_seniority_by_month[seniority_LAST_DIVISION_HIRE_DATE]))
		),
		_filter_lt
	)
	
VAR _seniority =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)
VAR _years = IF(_seniority/12 < 1, BLANK(), ROUNDDOWN(_seniority/12,0))
VAR _month = _seniority - COALESCE(_years,0) * 12
VAR _res = 
	IF(
		NOT ISBLANK( _seniority ),
		IF(
			NOT ISBLANK( _years ),
			_years & " р."
		) & " " &
		IF(
			NOT ISBLANK( _month ) && _month <> 0,
			ROUNDDOWN(_month,0) & " міс."
		)
	)
RETURN 
	COALESCE(
		TRIM(_res),
		"-"
	)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_employee_seniority_by_month_PDP`

Колонки: `Index`, `USER_ACCESS_ID`, `seniority_LAST_DIVISION_HIRE_DATE`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_employee_seniority_by_month`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_employee_seniority_by_month[seniority_LAST_DIVISION_HIRE_DATE]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Середній стаж в команді, років"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_employee_seniority_by_month["fact_employee_seniority_by_month"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

## Нотатки

_порожньо_
