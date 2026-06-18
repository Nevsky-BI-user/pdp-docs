# GP.Продуктивність.Оцінка керівника.Категорія

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Продуктивність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _rate_value = [GP.Продуктивність.Оцінка керівника.Значення]
VAR _category = 
    SWITCH(
        TRUE(),
        _rate_value > 4.3, "Категорія ТОР А",
        _rate_value > 3.90, "Категорія А",
        _rate_value > 3.4, "Категорія B",
        _rate_value > 3.0, "Категорія C",
        _rate_value > 0, "Категорія D"
    )

RETURN _category
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md)


## Схема

```mermaid
graph LR
  M["GP.Продуктивність.Оцінка керівника.Категорія"]
```

## Нотатки

_порожньо_
