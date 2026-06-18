# dim_Position_Category

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Position_Category` |
| Джерела | `DWH.t_SPO_HR_Position_Category_Matrix` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| Position_Category_Detail | string | Position_Category_Detail |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | POSITION_CATEGORY_DETAIL | `fact_Burnout_Indicators` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Employee_List` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_employee_seniority_by_month` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Metrics` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Mobile_Limit` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Monthly_Viva_Insights` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Repayment_Credit` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Sick_Leaves` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_TRS` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_TRS_Plan` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Vacation` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Vacation_Reserve` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Viva_Metrics` | Position_Category_Detail |
| to | POSITION_CATEGORY_DETAIL | `fact_Loss_of_Productivity` | Position_Category_Detail |

## Пов'язані міри

—

## Нотатки

_порожньо_
