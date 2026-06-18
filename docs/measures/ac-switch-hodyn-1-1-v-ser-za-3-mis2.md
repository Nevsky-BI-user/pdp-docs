# AC.Switch.Годин 1:1 в сер. за 3 міс2

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
VAR _indicator = SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator])
RETURN
SWITCH(
	_indicator,
	"Оцінка", [AC.Чи є ризик вигорання через відсутність спілкування з керівником?],
	"Дані", 
		VAR _value = [AC.Взаємодія з керівником]
		RETURN COALESCE(_value, 0)
)
```

## Джерела


Колонки: `Burnout_Indicator`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [AC.Взаємодія з керівником](../measures/ac-vzaiemodiia-z-kerivnykom.md), [AC.Чи є ризик вигорання через відсутність спілкування з керівником?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-vidsutnist-spilkuvannia-z-kerivnykom.md)

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

## Схема

```mermaid
graph LR
  M["AC.Switch.Годин 1:1 в сер. за 3 міс2"]
  M --> t_AC Burnout
```

## Нотатки

_порожньо_
