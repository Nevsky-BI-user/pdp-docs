# GP.ОКР.Оцінка керівника.Колір

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
VAR _color = 
    SWITCH(
        TRUE(),
        ISBLANK(_rate_value), "Дані відсутні",
        _rate_value >= 101, "Суперзелений",
        _rate_value >= 91, "Зелений",
        _rate_value >= 75, "Жовто-Зелений",
        _rate_value >= 50, "Жовтий",
        _rate_value >= 25, "Жовто-червоний",
        _rate_value >= 0, "Червоний"
    )

RETURN _color
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md)


## Схема

```mermaid
graph LR
  M["GP.ОКР.Оцінка керівника.Колір"]
```

## Нотатки

_порожньо_
