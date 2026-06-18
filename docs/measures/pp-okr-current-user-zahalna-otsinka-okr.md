# PP.OKR.Current_user.Загальна  оцінка OKR

*тека `Personal_Profile\Результативність та оцінка\OKR` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\OKR` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _employee_id = SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_ID])
VAR _main_position = 
	CALCULATE(
		VALUES('fact_OKR_Goals'[USER_ACCESS_ID]),
		REMOVEFILTERS('fact_OKR_Goals'),
		'fact_OKR_Goals'[EMPLOYEE_ID] = _employee_id
	)
VAR _filter0 = TREATAS({_main_position}, 'fact_OKR_Goals'[USER_ACCESS_ID])
VAR _res = 
	CALCULATE(
		AVERAGE('fact_OKR_Goals'[CALC_PERFORMANCE_STR_RATE]),
		_filter0
	)
RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `CALC_PERFORMANCE_STR_RATE`, `EMPLOYEE_ID`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_OKR_Goals`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_OKR_Goals[CALC_PERFORMANCE_STR_RATE]`, `fact_OKR_Goals[EMPLOYEE_ID]`, `fact_OKR_Goals[USER_ACCESS_ID]`

### Схема

```mermaid
graph LR
  M["PP.OKR.Current_user.Загальна  оцінка OKR"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_OKR_Goals["fact_OKR_Goals"]
```

---

## Бізнес-суть

CALC_PERFORMANCE_STR_RATE → Загальна оцінка ОКР; CALC_PERFORMANCE_STR_RATE → Загальна оцінка OKR; CALC_PERFORMANCE_STR_RATE → Оцінка OKR

Останнє НЕ пусте актуальне значення на дату (date) поточного запису

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [PP.OKR.SVG.Загальна колірна оцінка OKR](../measures/pp-okr-svg-zahalna-kolirna-otsinka-okr.md), [PP.SVG.OKR.Загальна оцінка](../measures/pp-svg-okr-zahalna-otsinka.md)

## Нотатки

_порожньо_
