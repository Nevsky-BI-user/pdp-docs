# PP.Y_axis_rcd

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
MAXX(
    VALUES('dim_Date'[Date]),
    [PP.РЦД]
) * 1.3
```

## Джерела


Колонки: `Date`

Power Query: `dim_Date`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.РЦД](../measures/pp-rtsd.md)

Таблиці: `dim_Date`

Колонки: `dim_Date[Date]`

## Схема

```mermaid
graph LR
  M["PP.Y_axis_rcd"]
  M --> dim_Date
```

## Нотатки

_порожньо_
