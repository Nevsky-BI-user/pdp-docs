# PP.Колір приросту РЦД

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _Val = [PP.Приріст РЦД]
RETURN
    SWITCH(
        TRUE(),
        _Val > 0, "#1F7A47",
        _Val < 0, "#A82828",
        "#6B7B8E"
    )
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)


## Схема

```mermaid
graph LR
  M["PP.Колір приросту РЦД"]
```

## Нотатки

_порожньо_
