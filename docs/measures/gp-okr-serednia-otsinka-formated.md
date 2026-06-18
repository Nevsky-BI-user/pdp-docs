# GP.ОКР.Середня Оцінка.Formated

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\ОКР` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res = [GP.ОКР.Середня оцінка команди.Значення]

RETURN
TRIM( 
        COALESCE( 
            SUBSTITUTE(FORMAT( _res, "#,0.00" ), ",", " "), "-"
        )
    )
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.ОКР.Середня оцінка команди.Значення](../measures/gp-okr-serednia-otsinka-komandy-znachennia.md)


## Схема

```mermaid
graph LR
  M["GP.ОКР.Середня Оцінка.Formated"]
```

## Нотатки

_порожньо_
