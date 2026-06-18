# GP.ОКР.Оцінка керівника.Текстове поле

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
VAR _rate_value = [GP.ОКР.Оцінка керівника.Значення]
VAR _color = [GP.ОКР.Оцінка керівника.Колір]
RETURN 
    --"Оцінка керівника - " &
    IF(
        ISBLANK(_rate_value),
        "Дані відсутні",
         _color & ", " & ROUND(_rate_value,2)
    )
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md), [GP.ОКР.Оцінка керівника.Колір](../measures/gp-okr-otsinka-kerivnyka-kolir.md)


## Схема

```mermaid
graph LR
  M["GP.ОКР.Оцінка керівника.Текстове поле"]
```

## Нотатки

_порожньо_
