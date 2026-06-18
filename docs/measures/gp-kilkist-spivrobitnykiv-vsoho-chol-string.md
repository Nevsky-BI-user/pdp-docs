# GP.Кількість співробітників всього, чол. - String

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Дані про команду` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
			
TRIM(
	FORMAT(
		COALESCE([GP.Кількість співробітників всього, чол. - Integer], "-"),
		"### ###"
	))
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md)


## Схема

```mermaid
graph LR
  M["GP.Кількість співробітників всього, чол. - String"]
```

## Нотатки

_порожньо_
