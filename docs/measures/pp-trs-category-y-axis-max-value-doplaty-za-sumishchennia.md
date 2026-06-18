# PP.TRS_category_Y_axis_max_value_Доплати_за_суміщення

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
    MAXX(
        VALUES('dim_TRS_categories'[TRS_CATEGORY]),
        [PP.Доплати за суміщення]
    ) * 1.3
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_TRS_Plan_PDP`

Колонки: `TRS_CATEGORY`

Power Query: `dim_TRS_categories`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Доплати за суміщення](../measures/pp-doplaty-za-sumishchennia.md)

Таблиці: `dim_TRS_categories`

Колонки: `dim_TRS_categories[TRS_CATEGORY]`

## Схема

```mermaid
graph LR
  M["PP.TRS_category_Y_axis_max_value_Доплати_за_суміщення"]
  M --> dim_TRS_categories
```

## Нотатки

_порожньо_
