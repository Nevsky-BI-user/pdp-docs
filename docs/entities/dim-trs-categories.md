# dim_TRS_categories

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_TRS_categories` |
| Джерела | `DM.vw_R27_fact_TRS_Plan_PDP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| TRS_CATEGORY | string | TRS_CATEGORY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | ACCRUAL_ORG_NAME | `fact_TRS_Plan` | TRS_CATEGORY |
| to | ACCRUAL_TYPE_NAME | `fact_TRS` | TRS_CATEGORY |

## Пов'язані міри

Усього: **1**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [TT:Зміна фікс винагороди](../report/tt-zmina-fiks-vynahorody.md) — 1

**Інші візуали:** [PP.TRS_category_Y_axis_max_value_Доплати_за_суміщення](../measures/pp-trs-category-y-axis-max-value-doplaty-za-sumishchennia.md)

## Нотатки

_порожньо_
