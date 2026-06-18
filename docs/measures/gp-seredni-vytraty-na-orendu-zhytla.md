# GP.Середні витрати на оренду житла

*тека `Group_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
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
	VAR _Employees =VALUES('dim_Admin_OS'[USER_ACCESS_ID])
	VAR _table0 = 
		ADDCOLUMNS(
			_Employees,
			"@Indicator",
			CALCULATE(
				MAX( fact_TRS_Plan[INIT_PAYMENT_PLAN_SUM] ),
				fact_TRS_Plan[IS_ACTUAL] = TRUE(),
				fact_TRS_Plan[ACCRUAL_ORG_CODE] = "00144"
			)
		)
	VAR _AverageOfSomeIndicator = 
		AVERAGEX(
			FILTER(
				_table0,
				NOT ISBLANK([@Indicator]) && [@Indicator] <> 0
			),
			[@Indicator]
		)
	RETURN _AverageOfSomeIndicator

/* *********** LT *********** */
VAR _admin_lt =
	VAR _table0 = 
		CALCULATETABLE(
			ADDCOLUMNS(
				VALUES( 'dim_Admin_OS'[USER_ACCESS_ID] ),
				"@Indicator",
				CALCULATE(
					MAX( fact_TRS_Plan[INIT_PAYMENT_PLAN_SUM] ),
					fact_TRS_Plan[IS_ACTUAL] = TRUE(),
					fact_TRS_Plan[ACCRUAL_ORG_CODE] = "00144"
				)
			),
			_filter_lt
		)
	VAR _AverageOfSomeIndicator = 
		AVERAGEX(
			FILTER(
				_table0,
				NOT ISBLANK([@Indicator]) && [@Indicator] <> 0
			),
			[@Indicator]
		)
	RETURN _AverageOfSomeIndicator

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)
RETURN 
COALESCE(
	_res, "-")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_TRS_Plan_PDP`

Колонки: `ACCRUAL_ORG_CODE`, `INIT_PAYMENT_PLAN_SUM`, `IS_ACTUAL`, `Index`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_TRS_Plan`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_TRS_Plan[ACCRUAL_ORG_CODE]`, `fact_TRS_Plan[INIT_PAYMENT_PLAN_SUM]`, `fact_TRS_Plan[IS_ACTUAL]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Середні витрати на оренду житла"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_TRS_Plan["fact_TRS_Plan"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

INIT_PAYMENT_PLAN_SUM → Цільовий розмір річної винагороди, до оподаткування; INIT_PAYMENT_PLAN_SUM → Оклад по годинах; INIT_PAYMENT_PLAN_SUM → Оклад по днях; INIT_PAYMENT_PLAN_SUM → Премія за місяць, %; INIT_PAYMENT_PLAN_SUM → Доплата за шкідливі умови праці, %; INIT_PAYMENT_PLAN_SUM → Роз'їзний характер роботи, %; INIT_PAYMENT_PLAN_SUM → Оренда житла; INIT_PAYMENT_PLAN_SUM → Середній цільовий розмір річної винагороди, до оподаткування; INIT_PAYMENT_PLAN_SUM → Середня зарплата (оклад); INIT_PAYMENT_PLAN_SUM → Доля команди з премією за місяць, %; INIT_PAYMENT_PLAN_SUM → Доля команди з доплатою за шкідливі умови праці, %; INIT_PAYMENT_PLAN_SUM → Доля команди з доплатою за роз’їзний характер роботи, %; INIT_PAYMENT_PLAN_SUM → Середній розмір доплати за шкідливі умови праці; INIT_PAYMENT_PLAN_SUM → Середній розмір доплати за роз’їзний характер роботи; INIT_PAYMENT_PLAN_SUM → Середні витрати на оренду житла; INIT_PAYMENT_PLAN_SUM → Річний цільовий дохід (РЦД); INIT_PAYMENT_PLAN_SUM → Оклад

Це сума по блокам Фіксована винагорода, всього х 12, Змінна винагорода (Щомісячна премія+ Квартальна премія+ Річний бонус) приведена до річної суми. <br> - **Фіксована винагорода** = Відібрати записи по працівнику [person_key], періоду [Period], організації [organization_key], підрозділу [division_key], де category_name = Фіксована винагорода, IS_ACTUAL  = "1",  TARIFF_RATE_TYPE_CODE <> "СДЕЛЬНАЯ", END_DATE > поточна дата, або END_DATE = "01.01.2001".  <br>Значення брати з INIT_PAYMENT_PLAN_SUM, якщо CALC_TYPE_CODE = "UAH", інакше - PAYMENT_PLAN_SUM.  <br> - **Змінна винагорода**(визначається 

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/РВІ.-Зміна-алгоритму-розрахунку-Річного-цільового-доходу`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
