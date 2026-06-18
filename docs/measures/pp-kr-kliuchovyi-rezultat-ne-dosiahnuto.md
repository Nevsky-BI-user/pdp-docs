# PP.KR.Ключовий результат НЕ досягнуто

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
		VALUES('fact_OKR_Key_Results'[USER_ACCESS_ID]),
		REMOVEFILTERS('fact_OKR_Key_Results'),
		'fact_OKR_Key_Results'[EMPLOYEE_ID] = _employee_id
	)
VAR _filter0 = TREATAS({_main_position}, 'fact_OKR_Key_Results'[USER_ACCESS_ID])
VAR _res = 
	CALCULATE(
        COUNTROWS('fact_OKR_Key_Results'),
        'fact_OKR_Key_Results'[KR_COLOR_RATE] < 25,
        'fact_OKR_Key_Results'[KR_WEIGHT] >0,
        'fact_OKR_Key_Results'[KR_CHANGE] <> "DELETE",
		_filter0
	)
VAR _blank_check = 
CALCULATE(
    COUNTROWS('fact_OKR_Key_Results'),
    'fact_OKR_Key_Results'[KR_COLOR_RATE] < 25
)
RETURN IF(NOT(ISBLANK(_blank_check)), _res)
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Key_Results`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_ID`, `KR_CHANGE`, `KR_COLOR_RATE`, `KR_WEIGHT`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_OKR_Key_Results`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_OKR_Key_Results[EMPLOYEE_ID]`, `fact_OKR_Key_Results[KR_CHANGE]`, `fact_OKR_Key_Results[KR_COLOR_RATE]`, `fact_OKR_Key_Results[KR_WEIGHT]`, `fact_OKR_Key_Results[USER_ACCESS_ID]`

### Схема

```mermaid
graph LR
  M["PP.KR.Ключовий результат НЕ досягнуто"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_OKR_Key_Results["fact_OKR_Key_Results"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Результативність та оцінка › OKR.детально

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
