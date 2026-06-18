# dim_Employee_Status

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employee_Status` |
| Джерела | `DM.vw_R27_dim_Employee_Status` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Паспортна-частина-групового-профілю/Сторінка-Картка-команди`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| STATUS_KEY | string | STATUS_KEY |  |
| CODE | string | CODE |  |
| NAME | string | NAME |  |
| SORT_NUM | int64 | SORT_NUM |  |
| STATUS_SHORT | string | STATUS_SHORT |  |
| STATUS | string | STATUS |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | STATUS_KEY | `fact_Employee_List` | STATUS_KEY |
| to | STATUS_KEY | `fact_TRS` | STATUS_KEY |
| to | STATUS_KEY | `fact_Vacation` | STATUS_KEY |
| to | STATUS_KEY | `fact_Vacation_Reserve` | STATUS_KEY |
| to | status_key | `fact_Sick_Leaves` | STATUS_KEY |
| to | STATUS_KEY | `fact_Metrics` | STATUS_KEY |
| to | STATUS_KEY | `fact_Burnout_Indicators` | STATUS_KEY |
| to | STATUS_KEY | `fact_employee_seniority_by_month` | STATUS_KEY |
| to | STATUS_KEY | `fact_Mobile_Limit` | STATUS_KEY |
| to | STATUS_KEY | `fact_Monthly_Viva_Insights` | STATUS_KEY |
| to | STATUS_KEY | `fact_Repayment_Credit` | STATUS_KEY |
| to | STATUS_KEY | `fact_TRS_Plan` | STATUS_KEY |
| to | STATUS_KEY | `fact_Viva_Metrics` | STATUS_KEY |
| to | STATUS_KEY | `fact_Loss_of_Productivity` | STATUS_KEY |

## Пов'язані міри

Усього: **1**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Group Profile](../report/group-profile.md) — 1

**Інші візуали:** [GP.Плинність (%)](../measures/gp-plynnist.md)

**Версія 1:** [GP.Плинність (%)](../measures/gp-plynnist.md)

## Нотатки

_порожньо_
