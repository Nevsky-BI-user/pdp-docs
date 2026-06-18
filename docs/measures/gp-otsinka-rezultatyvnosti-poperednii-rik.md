# GP.Оцінка результативності попередній рік

*тека `Group_Profile\_Main\SVG`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\SVG` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),'dim_Admin_OS'[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin = 
	CALCULATE(
		AVERAGEX(
			VALUES('dim_Admin_OS'[USER_ACCESS_ID]),
			CALCULATE(
				SUM('fact_Burnout_Indicators'[PREV_YEAR_PERFORMANCE_DESC_RATE])
			)
		)
	)

/* *********** LT *********** */
VAR _admin_lt =
	CALCULATE(
		AVERAGEX(
			VALUES('dim_Admin_OS'[USER_ACCESS_ID]),
			CALCULATE(
				SUM('fact_Burnout_Indicators'[PREV_YEAR_PERFORMANCE_DESC_RATE])
			)
		),
		_filter_lt
	)

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)
RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Index`, `PREV_YEAR_PERFORMANCE_DESC_RATE`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Burnout_Indicators`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Burnout_Indicators[PREV_YEAR_PERFORMANCE_DESC_RATE]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Оцінка результативності попередній рік"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

PREV_YEAR_PERFORMANCE_DESC_RATE → Оцінка результативності за передостанній рік в цифровому форматі; PREV_YEAR_PERFORMANCE_DESC_RATE → Оцінка результативності (ОР) за попередній рік; PREV_YEAR_PERFORMANCE_DESC_RATE → Загальна оцінка співробітника за передостанній період (рік); PREV_YEAR_PERFORMANCE_DESC_RATE → Середня оцінка результативності команди за передостанній рік в цифровому форматі

Для розрахунку метрики "Тренд оцінки рез-ті" Ці дані виводяться в деталізацію по тренду оцінки результативності Потрібно вирахувати середнє значення по команді = сума значень всіх оцінок членів команди станом на поточний момент поділити на кіл-сть таких членів команди (кількість записів). Тобто, якщо в складі команди є працівники, які не оцінювалися, вони участі в розрахунку не приймають.  <br>В розрахунок беремо оцінку всіх працівників, які станом на поточний момент є членами команди. На те, що вони могли працювати та оцінюватися на інших підприємствах/підрозділах не заважати.

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Додати-інформацію-про-оцінку-результативності-працівника-в-Картку-працівника`, `Кейс-Втрати-Продуктивності-Працівників/Деталізація-метрик-в-кейсі-Продуктивність`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`, `Командний-профіль/Паспортна-частина-групового-профілю/Додати-інформацію-про-ОКР-команди-та-середню-оцінку-результативності-по-команді`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [GP.SVG.Оцінка результативності команди](../measures/gp-svg-otsinka-rezultatyvnosti-komandy.md), [GP.Оцінка результативності пусто](../measures/gp-otsinka-rezultatyvnosti-pusto.md)

## Нотатки

_порожньо_
