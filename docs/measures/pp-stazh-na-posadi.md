# PP.Стаж на посаді

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _maxd = [PP.history_position_maxd]
VAR _seniority = 
    CALCULATE(
        SELECTEDVALUE(fact_Employee_History_Position[seniority_LAST_POSITION_HIRE_DATE]),
        'fact_Employee_History_Position'[PERIOD] = _maxd
    )
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

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `PERIOD`, `seniority_LAST_POSITION_HIRE_DATE`

Power Query: `fact_Employee_History_Position`

## Бізнес-суть

PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період; seniority_LAST_POSITION_HIRE_DATE → Стаж на посаді

Це дата нарахування/виплати премії Зірка МХП (accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' ) Поточний період Значення поля в місяцях потрібно перевести в роки та місяці. Наприклад, якшо seniority_LAST_POSITION_HIRE_DATE= 17, то в звіті треба відобразити 1 рік 5 місяців.

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Міри: [PP.history_position_maxd](../measures/pp-history-position-maxd.md)

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[PERIOD]`, `fact_Employee_History_Position[seniority_LAST_POSITION_HIRE_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Стаж на посаді"]
  M --> fact_Employee_History_Position
```

## Нотатки

_порожньо_
