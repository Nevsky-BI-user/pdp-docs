# AC.Зарплата (вилки)

*тека `Analytical Cases\Burnout_Risk\Main`*

## Бізнес-суть

SALARY_RANGE → Зарплата (вилки)

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Зарплата (вилки)](../measures/ac-switch-zarplata-vylky.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = 
	CALCULATE(
		SELECTEDVALUE('fact_Burnout_Indicators'[SALARY_RANGE])
	)
RETURN IF(_res = "Дані відсутні", "—", _res )
```

### Джерела даних


Колонки: `SALARY_RANGE`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[SALARY_RANGE]`

### Схема

```mermaid
graph LR
  M["AC.Зарплата (вилки)"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

## Нотатки

_порожньо_
