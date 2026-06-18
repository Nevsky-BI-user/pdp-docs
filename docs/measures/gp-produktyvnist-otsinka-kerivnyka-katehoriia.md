# GP.Продуктивність.Оцінка керівника.Категорія

*тека `Group_Profile\_Main\Продуктивність`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Продуктивність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

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

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.Продуктивність.Оцінка керівника.Категорія"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md)

**Використовується в:** [GP.Продуктивність.Color.Оцінка керівника.Текстове поле](../measures/gp-produktyvnist-color-otsinka-kerivnyka-tekstove-pole.md), [GP.Продуктивність.Оцінка керівника.Текстове поле](../measures/gp-produktyvnist-otsinka-kerivnyka-tekstove-pole.md)

## Нотатки

_порожньо_
