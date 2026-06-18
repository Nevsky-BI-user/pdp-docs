# AC.Burnout.Tooltip

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
	SWITCH(
		TRUE(),
		ISSELECTEDMEASURE([AC.Ризик]), "Підказка"
	)
RETURN COALESCE(_res, "")
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [AC.Ризик](../measures/ac-ryzyk.md)


## Схема

```mermaid
graph LR
  M["AC.Burnout.Tooltip"]
```

## Нотатки

_порожньо_
