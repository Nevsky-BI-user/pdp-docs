# dim_Person

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Person` |
| Джерела | `DM.vw_R27_dim_Person_PDP` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| PERSON_KEY | string | PERSON_KEY |  |
| FULL_NAME | string | FULL_NAME |  |
| FIRST_NAME | string | FIRST_NAME |  |
| LAST_NAME | string | LAST_NAME |  |
| SHORT_NAME | string | SHORT_NAME |  |
| EMPLOYEE_CODE | string | EMPLOYEE_CODE |  |
| TAX_CODE | string | TAX_CODE |  |
| GENDER | string | GENDER |  |
| DATE_OF_BIRTH | dateTime | DATE_OF_BIRTH |  |
| INDIVIDUAL_CODE | string | INDIVIDUAL_CODE |  |
| PHONE_PERSONAL | string | PHONE_PERSONAL |  |
| PHONE_WORK | string | PHONE_WORK |  |
| EMAIL | string | EMAIL |  |
| EDUCATION | string | EDUCATION |  |
| EDUCATION_LVL | string | EDUCATION_LVL |  |
| UNIVERSITY | string | UNIVERSITY |  |
| IS_TG_SUBSCRIBER | int64 | IS_TG_SUBSCRIBER |  |
| IS_VETERAN_NEWMAN | int64 | IS_VETERAN_NEWMAN |  |
| WAR_UBD | string | WAR_UBD |  |
| IS_VETERAN | int64 | IS_VETERAN |  |
| ADDRESS_REGISTRATION | string | ADDRESS_REGISTRATION |  |
| ADDRESS_FACT | string | ADDRESS_FACT |  |
| MARITAL_STATUS | string | MARITAL_STATUS |  |
| DISABILITY_PERIOD_DATE | dateTime | DISABILITY_PERIOD_DATE |  |
| URL_FOTO | string | URL_FOTO |  |
| FinalImage | — | — | так |
| DISABILITY_GROUP | string | DISABILITY_GROUP |  |
| DISABILITY_START_DATE | dateTime | DISABILITY_START_DATE |  |
| DISABILITY_COMMENT | string | DISABILITY_COMMENT |  |
| WORK_HOUR_START_TIME | dateTime | WORK_HOUR_START_TIME |  |
| WORK_HOUR_END_TIME | dateTime | WORK_HOUR_END_TIME |  |
| CHILDREN_UNDER_18_AMOUNT | int64 | CHILDREN_UNDER_18_AMOUNT |  |
| CHILDREN_UNDER_14_AMOUNT | int64 | CHILDREN_UNDER_14_AMOUNT |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | PERSON_KEY | `fact_Employee_List` | PERSON_KEY |
| to | PERSON_KEY | `fact_TRS` | PERSON_KEY |
| to | DIVISION_PERSON_ID | `fact_TRS_Plan` | PERSON_KEY |
| to | DIVISION_PERSON_ID | `fact_Vacation` | PERSON_KEY |
| to | DIVISION_PERSON_ID | `fact_Vacation_Reserve` | PERSON_KEY |
| to | person_key | `fact_Sick_Leaves` | PERSON_KEY |
| to | PERSON_KEY | `fact_Repayment_Credit` | PERSON_KEY |
| to | PERSON_KEY | `fact_Mobile_Limit` | PERSON_KEY |
| to | PERSON_KEY | `fact_Monthly_Viva_Insights` | PERSON_KEY |
| to | DIVISION_PERSON_ID | `fact_Metrics` | PERSON_KEY |
| to | EMPLOYEE_ID | `fact_Burnout_Indicators` | EMPLOYEE_CODE |
| to | EMPLOYEE_ID | `fact_Loss_of_Productivity` | PERSON_KEY |
| to | EMPLOYEE_ID | `fact_Employee_Performance_Total` | PERSON_KEY |

## Пов'язані міри

Усього: **6**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Group Profile](../report/group-profile.md) — 3

**Інші візуали:** [GP.Доля заброньованих чоловіків(%)](../measures/gp-dolia-zabronovanykh-cholovikiv.md) · [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md)

**Версія 1:** [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md)

**Загальна інформація:** [GP.Доля заброньованих чоловіків(%)](../measures/gp-dolia-zabronovanykh-cholovikiv.md) · [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md) · [GP.Кількість Ветеранів](../measures/gp-kilkist-veteraniv.md)

### [Під ризиком мобілізації](../report/pid-ryzykom-mobilizatsii.md) — 2

**Інші візуали:** [GP.Кількість чоловіків БЕЗ ризику мобілізації(%)](../measures/gp-kilkist-cholovikiv-bez-ryzyku-mobilizatsii.md) · [GP.Кількість чоловіків під ризиком мобілізації(%)](../measures/gp-kilkist-cholovikiv-pid-ryzykom-mobilizatsii.md)

### Поза звітом / службові — 1

[button_detalization.Personal_profile](../measures/button-detalization-personal-profile.md)

## Нотатки

_порожньо_
