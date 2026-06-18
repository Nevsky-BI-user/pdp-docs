# PP.TRS_category_Y_axis_max_value_Доплати_за_суміщення

*тека `Personal_Profile\TRS`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[TT:Зміна фікс винагороди](../report/tt-zmina-fiks-vynahorody.md)

## Пов'язані міри

**Використовує:** [PP.Доплати за суміщення](../measures/pp-doplaty-za-sumishchennia.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
    MAXX(
        VALUES('dim_TRS_categories'[TRS_CATEGORY]),
        [PP.Доплати за суміщення]
    ) * 1.3
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_TRS_Plan_PDP`

Колонки: `TRS_CATEGORY`

Power Query: `dim_TRS_categories`

### Залежності (таблиці й колонки)

Таблиці: `dim_TRS_categories`

Колонки: `dim_TRS_categories[TRS_CATEGORY]`

### Схема

```mermaid
graph LR
  M["PP.TRS_category_Y_axis_max_value_Доплати_за_суміщення"]
  M --> dim_TRS_categories["dim_TRS_categories"]
```

## Нотатки

_порожньо_
