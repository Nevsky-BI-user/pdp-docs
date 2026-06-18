# AC.Burnout_Risk.c_rows

*тека `Analytical Cases\Burnout_Risk\Main` · формат `0`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SWITCH(
	SELECTEDVALUE('t_IS_FIRED'[IS_FIRED]),
	0, 
	CALCULATE(
		COUNTROWS('fact_Burnout_Indicators'),
		'fact_Burnout_Indicators'[IS_FIRED] = FALSE()
	),
	1,
	CALCULATE(
		COUNTROWS('fact_Burnout_Indicators'),
		'fact_Burnout_Indicators'[IS_FIRED] = TRUE()
	)
)
```

### Джерела даних


Колонки: `IS_FIRED`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`, `t_IS_FIRED`

Колонки: `fact_Burnout_Indicators[IS_FIRED]`, `t_IS_FIRED[IS_FIRED]`

### Схема

```mermaid
graph LR
  M["AC.Burnout_Risk.c_rows"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
  M --> t_IS_FIRED["t_IS_FIRED"]
```

## Нотатки

_порожньо_
