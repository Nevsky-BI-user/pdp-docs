# GP.Середній розмір доплати за роз’їзний характер роботи, факт

*тека `Group_Profile\TRS` · формат `#,0`*

## Бізнес-суть

PAYMENTS_FACT_UAH → Зірка МХП; PAYMENTS_FACT_UAH → Наставництво (ост. 12 міс); PAYMENTS_FACT_UAH → Доплати за суміщення; PAYMENTS_FACT_UAH → Щомісячні премії; PAYMENTS_FACT_UAH → Квартальні премії; PAYMENTS_FACT_UAH → Річні бонуси; PAYMENTS_FACT_UAH → Інші доплати; PAYMENTS_FACT_UAH → Премія МХП Зірки; PAYMENTS_FACT_UAH → Проектний бонус за стратегічні ІТ проєкти; PAYMENTS_FACT_UAH → Інвестиційний проєктний бонус; PAYMENTS_FACT_UAH → Премія за збереження та розширення земельного банку; PAYMENTS_FACT_UAH → Разова премія за програмою визнання; PAYMENTS_FACT_UAH → Премія за внутрішнє тренерство; PAYMENTS_FACT_UAH → Доплата за наставництво; PAYMENTS_FACT_UAH → Премія за програмою «Приведи друга»; PAYMENTS_FACT_UAH → Премія за Банк ідей; PAYMENTS_FACT_UAH → Соціальна підтримка; PAYMENTS_FACT_UAH → Внутрішнє тренерство; PAYMENTS_FACT_UAH → Наставництво; PAYMENTS_FACT_UAH → Програма визнання; PAYMENTS_FACT_UAH → Сума нарахування; PAYMENTS_FACT_UAH → Місячний дохід з річним бонусом; PAYMENTS_FACT_UAH → Місячний дохід без річного бонусу; PAYMENTS_FACT_UAH → Доля команди із премією МХП Зірки, %; PAYMENTS_FACT_UAH → Доля команди із проектним бонусом за стратегічні ІТ проєкти, %; PAYMENTS_FACT_UAH → Доля команди із інвестиційним проєктним бонусом, %; PAYMENTS_FACT_UAH → Доля команди із премією за збереження та розширення земельного банку, %; PAYMENTS_FACT_UAH → Середній розмір премії МХП Зірки; PAYMENTS_FACT_UAH → Середній розмір проектного бонус за стратегічні ІТ проєкти; PAYMENTS_FACT_UAH → Середній розмір інвестиційного проєктного бонусу; PAYMENTS_FACT_UAH → Середній розмір премії за збереження та розширення земельного банку; PAYMENTS_FACT_UAH → Доля команди із разовою премією за програмою визнання, %; PAYMENTS_FACT_UAH → Доля команди із премією за внутрішнє тренерство, %; PAYMENTS_FACT_UAH → Доля команди із доплатою за наставництво, %; PAYMENTS_FACT_UAH → Доля команди із премією за програмою «Приведи друга», %; PAYMENTS_FACT_UAH → Доля команди із премією за Банк ідей, %; PAYMENTS_FACT_UAH → Середній розмір разової премії за програмою визнання; PAYMENTS_FACT_UAH → Середній розмір премії за внутрішнє тренерство; PAYMENTS_FACT_UAH → Середній розмір доплати за наставництво; PAYMENTS_FACT_UAH → Середній розмір премії за програмою «Приведи друга»; PAYMENTS_FACT_UAH → Середній розмір премії за Банк ідей; PAYMENTS_FACT_UAH → Доля команди з соціальними виплатами, %; PAYMENTS_FACT_UAH → Середній розмір соціальної підтримки; PAYMENTS_FACT_UAH → Середня заробітна плата; PAYMENTS_FACT_UAH → Діапазон фіксованої винагороди (факт); PAYMENTS_FACT_UAH → Доля команди з премією за місяць, % факт; PAYMENTS_FACT_UAH → Середній розмір премії за місяць факт; PAYMENTS_FACT_UAH → Доля команди з доплатою за шкідливі умови праці, % факт; PAYMENTS_FACT_UAH → Середній розмір доплати за шкідливі умови праці; PAYMENTS_FACT_UAH → Доля команди з доплатою за роз’їзний характер роботи, % факт; PAYMENTS_FACT_UAH → Середній розмір доплати за роз’їзний характер роботи факт; PAYMENTS_FACT_UAH → Доля команди із щомісячними преміями; PAYMENTS_FACT_UAH → Середній розмір щомісячних премій; PAYMENTS_FACT_UAH → Доля команди із квартальними преміями; PAYMENTS_FACT_UAH → Середній розмір квартальних премій; PAYMENTS_FACT_UAH → Доля команди із річними бонусами; PAYMENTS_FACT_UAH → Середній розмір річних бонусів; PAYMENTS_FACT_UAH → Доля команди із доплатами за суміщення; PAYMENTS_FACT_UAH → Середній розмір доплат за суміщення; PAYMENTS_FACT_UAH → Соціальні виплати; PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період

Потрібно відібрати останній запис по працівнику на дату, де  поле accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' Потрібно відібрати всі записи по працівнику, де  поле accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2'  <br>Рік визначати за полем period Якщо по працівнику [person_key], періоду [Period], організації [organization_key] , працевлаштуванню [employment_type_key] є значення по полю [ACCRUAL_TYPES_KEY] ='83ce68c2-8a36-d6d5-21bd-27fc6b970114" то Так. Інакше - Ні Відібрати записи за останні 12 

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Бейджики-під-фото-працівника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Доопрацювання-сторінки-ТРС`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`, `Командний-профіль/Паспортна-частина-групового-профілю/Сторінка-Картка-команди`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Доопрацювання-сторінки-TRS`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

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
| displayFolder | `Group_Profile\TRS` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),dim_Admin_OS[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin =
	VAR _Employees = VALUES('dim_Admin_OS'[USER_ACCESS_ID])
    VAR _Perionds = VALUES('fact_TRS'[PERIOD])
	VAR _table0 = 
		ADDCOLUMNS(
			CROSSJOIN(_Employees, _Perionds),
			"@Indicator",
			CALCULATE(
				SUM('fact_TRS'[PAYMENTS_FACT_UAH]),
				'fact_TRS'[ACCRUAL_TYPES_KEY] = "d8d58e4c-8800-ea51-9ff6-0bec21ff170f",
                'fact_TRS'[PAYMENTS_FACT_UAH] > 0,
                DATESINPERIOD( 'fact_TRS'[PERIOD], EOMONTH( TODAY(), - 1 ), - 12, MONTH )
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
    VAR _Employees = VALUES('dim_Admin_OS'[USER_ACCESS_ID])
    VAR _Perionds = VALUES('fact_TRS'[PERIOD])
	VAR _table0 = 
		CALCULATETABLE(
			ADDCOLUMNS(
				CROSSJOIN(_Employees, _Perionds),
				"@Indicator",
				CALCULATE(
					MAX('fact_TRS'[PAYMENTS_FACT_UAH]),
					'fact_TRS'[ACCRUAL_TYPES_KEY] = "d8d58e4c-8800-ea51-9ff6-0bec21ff170f",
                    'fact_TRS'[PAYMENTS_FACT_UAH] > 0,
					DATESINPERIOD( 'fact_TRS'[PERIOD], EOMONTH( TODAY(), - 1 ), - 12, MONTH )
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

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_TRS_PDP`

Колонки: `ACCRUAL_TYPES_KEY`, `Index`, `PAYMENTS_FACT_UAH`, `PERIOD`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_TRS`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_TRS[ACCRUAL_TYPES_KEY]`, `fact_TRS[PAYMENTS_FACT_UAH]`, `fact_TRS[PERIOD]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Середній розмір доплати за роз’їзний характер роботи, факт"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_TRS["fact_TRS"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

## Нотатки

_порожньо_
