# dim_Employment_Type

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employment_Type` |
| Джерела | `DM.vw_R27_dim_Employment_Type` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| CODE | string | CODE |  |
| NAME | string | NAME |  |
| SORT_NUM | int64 | SORT_NUM |  |
| EMPLOYMENT_TYPE | string | EMPLOYMENT_TYPE |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | EMPLOYMENT_TYPE_KEY | `fact_Employee_List` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Burnout_Indicators` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_employee_seniority_by_month` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Metrics` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Mobile_Limit` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Monthly_Viva_Insights` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Repayment_Credit` | EMPLOYMENT_TYPE_KEY |
| to | employment_type_key | `fact_Sick_Leaves` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_TRS` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Vacation` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_ID | `fact_TRS_Plan` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Vacation_Reserve` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Viva_Metrics` | EMPLOYMENT_TYPE_KEY |
| to | EMPLOYMENT_TYPE_KEY | `fact_Loss_of_Productivity` | EMPLOYMENT_TYPE_KEY |

## Пов'язані міри

—

## Нотатки

_порожньо_
