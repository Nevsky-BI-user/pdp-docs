# PP.Ризик.Довгі відпустки 12м

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Ризики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _v = [PP.Кількість довгих відпусток]
RETURN
	IF(ISBLANK(_v) || _v = 0, "Дані відсутні", FORMAT(_v, "0") & " шт.")
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Кількість довгих відпусток](../measures/pp-kilkist-dovhykh-vidpustok.md)


## Схема

```mermaid
graph LR
  M["PP.Ризик.Довгі відпустки 12м"]
```

## Нотатки

_порожньо_
