# PP.Чи виплачено лікарняні від компанії

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Здоров'я та благополуччя` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _HasData =
	COALESCE([PP.Лікарняні], 0) > 0        -- числова версія, BLANK коли даних нема
VAR _Paid =
	CALCULATE(
		COUNTROWS(
			FILTER('fact_Metrics', 'fact_Metrics'[IS_SICK_LEAVE_PAID] = TRUE())
		)
	) 
RETURN
SWITCH(
	TRUE(),
	_Paid = 0, "-",
	_Paid >0 , "Так",
	"Ні"
)
```

## Джерела


Колонки: `IS_SICK_LEAVE_PAID`

Power Query: `fact_Metrics`

## Бізнес-суть

Чи виплачено лікарняні від компанії

Якщо is_sl_paid = 1 за останні 12 міс, то Так, is_sl_paid = 0, то Ні  <br>НЕ включаючи поточний місяць.

**Вимоги:** `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`

## Залежності

Міри: [PP.Лікарняні](../measures/pp-likarniani.md)

Таблиці: `fact_Metrics`

Колонки: `fact_Metrics[IS_SICK_LEAVE_PAID]`

## Схема

```mermaid
graph LR
  M["PP.Чи виплачено лікарняні від компанії"]
  M --> fact_Metrics
```

## Нотатки

_порожньо_
