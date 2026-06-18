# PP.Середня оцінка результативності річна

*тека `Personal_Profile\Паспорт\Spider`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Spider` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = 
LASTNONBLANKVALUE(
	VALUES('fact_Employee_Performance'[performance_PBI_order]),
	CALCULATE(
		AVERAGE('fact_Employee_Performance'[Official_Rate]),
		'fact_Employee_Performance'[Performance_Type] = "Річна"
	)
)
RETURN COALESCE(_res, "-")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_PBI`

Колонки: `Official_Rate`, `Performance_Type`, `performance_PBI_order`

Power Query: `fact_Employee_Performance`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_Performance`

Колонки: `fact_Employee_Performance[Official_Rate]`, `fact_Employee_Performance[Performance_Type]`, `fact_Employee_Performance[performance_PBI_order]`

### Схема

```mermaid
graph LR
  M["PP.Середня оцінка результативності річна"]
  M --> fact_Employee_Performance["fact_Employee_Performance"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
