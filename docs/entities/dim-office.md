# dim_Office

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Office` |
| Джерела | `DM.vw_R27_dim_Office` |

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду/Редизайн-сторінки-Загальна-інформація`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| OFFICE_KEY | string | OFFICE_KEY |  |
| OFFICE_CODE | string | OFFICE_CODE |  |
| OFFICE | string | OFFICE |  |
| OFFICE_TYPE | string | OFFICE_TYPE |  |
| OFFICE_REGION | string | OFFICE_REGION |  |
| OFFICE_LOCALITY | string | OFFICE_LOCALITY |  |
| OFFICE_REGIONID | string | OFFICE_REGIONID |  |
| OFFICE_ADRESS | string | OFFICE_ADRESS |  |
| REGION_NAME | string | REGION_NAME |  |
| CITY_NAME | string | CITY_NAME |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | OFFICE_ON_POSITION_KEY | `fact_Burnout_Indicators` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Employee_List` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_employee_seniority_by_month` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Metrics` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Mobile_Limit` | OFFICE_KEY |
| to | office_on_position_key | `fact_Sick_Leaves` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Monthly_Viva_Insights` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_TRS_Plan` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Vacation` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Vacation_Reserve` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Viva_Metrics` | OFFICE_KEY |
| to | OFFICE_ON_POSITION_KEY | `fact_Loss_of_Productivity` | OFFICE_KEY |

## Пов'язані міри

—

## Нотатки

_порожньо_
