# PP.Наявність довгих відпусток

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
VAR _qty = [PP.Кількість довгих відпусток]
VAR _days = [PP.Тривалість довгих відпусток]
VAR _res = 
	_qty & 
	IF(
		OR(ISBLANK(_days), _days = 0), 
		BLANK(), 
		" (" & _days & " дн.)"
	)
RETURN _res
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Кількість довгих відпусток](../measures/pp-kilkist-dovhykh-vidpustok.md), [PP.Тривалість довгих відпусток](../measures/pp-tryvalist-dovhykh-vidpustok.md)


## Схема

```mermaid
graph LR
  M["PP.Наявність довгих відпусток"]
```

## Нотатки

_порожньо_
