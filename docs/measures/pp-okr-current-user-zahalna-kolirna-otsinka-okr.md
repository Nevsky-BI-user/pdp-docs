# PP.OKR.Current_user.Загальна колірна оцінка OKR

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

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
		SELECTEDVALUE('fact_OKR_Goals'[Calc_Performance_Desc_Rate]),
		_filter0
	)
RETURN _res
```

## Джерела

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Calc_Performance_Desc_Rate`, `EMPLOYEE_ID`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

## Бізнес-суть

Calc_Performance_Desc_Rate → Колірна оцінка ОКР; Calc_Performance_Desc_Rate → Загальна колірна оцінка ОКР; Calc_Performance_Desc_Rate → Загальна колірна оцінка OKR; Calc_Performance_Desc_Rate → Ціль виконана; Calc_Performance_Desc_Rate → Ціль не виконана; Calc_Performance_Desc_Rate → Колірна оцінка OKR за останній період; Calc_Performance_Desc_Rate → Колірна оцінка OKR за передостанній період; Calc_Performance_Desc_Rate → Загальний колір ОКР; Calc_Performance_Desc_Rate → Колірна оцінка OKR

Останнє НЕ пусте актуальне значення на дату (date) поточного запису Якщо поле Calc_Performance_Desc_Rate має значення Супер зелений, або Жовто-зелений, або Зелений, або Жовтий, або Жовто-червоний Якщо поле Calc_Performance_Desc_Rate має значення Червоний

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## Залежності

Таблиці: `dim_Admin_OS`, `fact_OKR_Goals`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_OKR_Goals[Calc_Performance_Desc_Rate]`, `fact_OKR_Goals[EMPLOYEE_ID]`, `fact_OKR_Goals[USER_ACCESS_ID]`

## Схема

```mermaid
graph LR
  M["PP.OKR.Current_user.Загальна колірна оцінка OKR"]
  M --> dim_Admin_OS
  M --> fact_OKR_Goals
```

## Нотатки

_порожньо_
