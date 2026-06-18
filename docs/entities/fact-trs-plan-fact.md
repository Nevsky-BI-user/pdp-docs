# fact_TRS_plan_fact

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_TRS_plan_fact` |
| Джерела | `DM.vw_R27_fact_TRS_plan_fact` |

**Вимоги:** `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| period | dateTime | period |  |
| payment_budget | double | payment_budget |  |
| payment_budget_adjusted | double | payment_budget_adjusted |  |
| budget_year | string | budget_year |  |
| payment_fact | double | payment_fact |  |
| total_sum | double | total_sum |  |
| scenario | string | scenario |  |
| organization_key | string | organization_key |  |
| unit_key | string | unit_key |  |
| unit_direction | string | unit_direction |  |
| unit_sub_direction | string | unit_sub_direction |  |
| division_key | string | division_key |  |
| division_direction_Org | string | division_direction_Org |  |
| division_sub_direction_Org | string | division_sub_direction_Org |  |
| status_key | string | status_key |  |
| trs_category | string | trs_category |  |
| cost_centre_key | string | cost_centre_key |  |
| budget_code | string | budget_code |  |
| object_code | string | object_code |  |
| budget_cost_item | string | budget_cost_item |  |

## Зв'язки

—

## Пов'язані міри

—

## Нотатки

_порожньо_
