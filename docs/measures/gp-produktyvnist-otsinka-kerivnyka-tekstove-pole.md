# GP.Продуктивність.Оцінка керівника.Текстове поле

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
VAR _category = [GP.Продуктивність.Оцінка керівника.Категорія]
VAR _rate_value = [GP.Продуктивність.Оцінка керівника.Значення]
RETURN 
    --"Оцінка керівника - " &
    IF(
        ISBLANK(_rate_value),
        "Дані відсутні",
         _category & ", " & ROUND(_rate_value,2)
    )
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md), [GP.Продуктивність.Оцінка керівника.Категорія](../measures/gp-produktyvnist-otsinka-kerivnyka-katehoriia.md)


## Схема

```mermaid
graph LR
  M["GP.Продуктивність.Оцінка керівника.Текстове поле"]
```

## Нотатки

_порожньо_
