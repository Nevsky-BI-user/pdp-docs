# GP.Продуктивність.Середня оцінка команди.Текстове поле

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
VAR _res = [GP.Продуктивність.Середня оцінка команди.Значення]
VAR _color = [GP.Продуктивність.Середня оцінка команди.Категорія]
RETURN 
    --"Оцінка керівника - " &
    IF(
        ISBLANK(_res),
        "Дані відсутні",
         _color & ", " & TRIM(_res)
    )
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Продуктивність.Середня оцінка команди.Значення](../measures/gp-produktyvnist-serednia-otsinka-komandy-znachennia.md), [GP.Продуктивність.Середня оцінка команди.Категорія](../measures/gp-produktyvnist-serednia-otsinka-komandy-katehoriia.md)


## Схема

```mermaid
graph LR
  M["GP.Продуктивність.Середня оцінка команди.Текстове поле"]
```

## Нотатки

_порожньо_
