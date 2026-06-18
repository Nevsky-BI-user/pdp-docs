# AC.Зарплата (вилки)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res = 
	CALCULATE(
		SELECTEDVALUE('fact_Burnout_Indicators'[SALARY_RANGE])
	)
RETURN IF(_res = "Дані відсутні", "—", _res )
```

## Джерела


Колонки: `SALARY_RANGE`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

SALARY_RANGE → Зарплата (вилки)

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[SALARY_RANGE]`

## Схема

```mermaid
graph LR
  M["AC.Зарплата (вилки)"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
