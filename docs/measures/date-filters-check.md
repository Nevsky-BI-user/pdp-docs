# date_filters_check

*тека `_Technical`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `_Technical` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _period =                                               //Сюди підставляємо фільтр контексту
	VAR __Win =         
		VAR __EndMonth = EOMONTH( TODAY(), -1 ) 
	RETURN DATESINPERIOD( dim_Date[Date], __EndMonth, -3, MONTH )
RETURN 
	CALCULATETABLE(
		VALUES('dim_Date'[Date]),
		__Win
	)
VAR _mind = 
	CALCULATE(
		MIN('dim_Date'[Date]),
		
		_period
	)
VAR _maxd = 
	CALCULATE(
		MAX('dim_Date'[Date]),
		_period
	)
VAR result = 
FORMAT(_mind, "dd.mm.yyyy") & " - " & FORMAT(_maxd, "dd.mm.yyyy")
RETURN result
```

### Джерела даних


Колонки: `Date`

Power Query: `dim_Date`

### Залежності (таблиці й колонки)

Таблиці: `dim_Date`

Колонки: `dim_Date[Date]`

### Схема

```mermaid
graph LR
  M["date_filters_check"]
  M --> dim_Date["dim_Date"]
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
