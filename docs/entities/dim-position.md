# dim_Position

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Position` |
| Джерела | `DM.vw_R27_dim_Position` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Індивідуальний-профіль-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| POSITION_CODE_KEY | string | POSITION_CODE_KEY |  |
| CODE | string | CODE |  |
| POSITION | string | POSITION |  |
| POSITION_CODE_STATE | string | POSITION_CODE_STATE |  |
| POSITION_JOB_SPECIFICATION | string | POSITION_JOB_SPECIFICATION |  |
| POSITION_CATEGORY_STATE | string | POSITION_CATEGORY_STATE |  |
| ID | string | ID |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | POSITION_KEY | `fact_Employee_List` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Burnout_Indicators` | ID |
| to | POSITION_KEY | `fact_employee_seniority_by_month` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Metrics` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Mobile_Limit` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Monthly_Viva_Insights` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Repayment_Credit` | POSITION_CODE_KEY |
| to | position_key | `fact_Sick_Leaves` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_TRS` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_TRS_Plan` | POSITION_CODE_KEY |
| to | POSITION_KEY | `fact_Viva_Metrics` | POSITION_CODE_KEY |
| to | JOB_TITLE_ID | `fact_Vacation_Reserve` | POSITION_CODE_KEY |
| to | JOB_TITLE_ID | `fact_Vacation` | POSITION_CODE_KEY |
| to | JOB_TITLE_ID | `fact_Loss_of_Productivity` | POSITION_CODE_KEY |

## Пов'язані міри

—

## Нотатки

_порожньо_
