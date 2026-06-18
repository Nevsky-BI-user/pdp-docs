# fact_employee_seniority_by_month

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_employee_seniority_by_month` |
| Джерела | `DM.vw_R27_fact_employee_seniority_by_month_PDP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/Додаткові-вимоги-до-вітрини-Плинність`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| PERSON_KEY | string | PERSON_KEY |  |
| DOC_JOB_APPLICATION_KEY | string | DOC_JOB_APPLICATION_KEY |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYMENT_TYPE_CODE | string | EMPLOYMENT_TYPE_CODE |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| FIRST_HOLDING_HIRE_DATE | dateTime | FIRST_HOLDING_HIRE_DATE |  |
| seniority_FIRST_HOLDING_HIRE_DATE | int64 | seniority_FIRST_HOLDING_HIRE_DATE |  |
| LAST_HOLDING_HIRE_DATE | dateTime | LAST_HOLDING_HIRE_DATE |  |
| seniority_LAST_HOLDING_HIRE_DATE | int64 | seniority_LAST_HOLDING_HIRE_DATE |  |
| LAST_ORGANIZATION_HIRE_DATE | dateTime | LAST_ORGANIZATION_HIRE_DATE |  |
| seniority_LAST_ORGANIZATION_HIRE_DATE | int64 | seniority_LAST_ORGANIZATION_HIRE_DATE |  |
| LAST_DIVISION_HIRE_DATE | dateTime | LAST_DIVISION_HIRE_DATE |  |
| seniority_LAST_DIVISION_HIRE_DATE | int64 | seniority_LAST_DIVISION_HIRE_DATE |  |
| LAST_POSITION_HIRE_DATE | dateTime | LAST_POSITION_HIRE_DATE |  |
| seniority_LAST_POSITION_HIRE_DATE | int64 | seniority_LAST_POSITION_HIRE_DATE |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |

## Пов'язані міри

Усього: 14.
- [AC.BR.Стаж в холдингу (неперервний)](../measures/ac-br-stazh-v-kholdynhu-neperervnyi.md)
- [AC.BR.Стаж на посаді (останній)](../measures/ac-br-stazh-na-posadi-ostannii.md)
- [AC.LP.Стаж на посаді (останній)](../measures/ac-lp-stazh-na-posadi-ostannii.md)
- [GP.Середній стаж в команді, років](../measures/gp-serednii-stazh-v-komandi-rokiv.md)
- [PP.Дата прийому в команду (останній)](../measures/pp-data-pryiomu-v-komandu-ostannii.md)
- [PP.Дата прийому в організацію (останній)](../measures/pp-data-pryiomu-v-orhanizatsiiu-ostannii.md)
- [PP.Дата прийому в холдинг (неперервний)](../measures/pp-data-pryiomu-v-kholdynh-neperervnyi.md)
- [PP.Дата прийому в холдинг (перервний)](../measures/pp-data-pryiomu-v-kholdynh-perervnyi.md)
- [PP.Дата прийому на посаду (останній)](../measures/pp-data-pryiomu-na-posadu-ostannii.md)
- [PP.Стаж в команді (останній)](../measures/pp-stazh-v-komandi-ostannii.md)
- [PP.Стаж в організації (останній)](../measures/pp-stazh-v-orhanizatsii-ostannii.md)
- [PP.Стаж в холдингу (неперервний)](../measures/pp-stazh-v-kholdynhu-neperervnyi.md)
- [PP.Стаж в холдингу (перервний)](../measures/pp-stazh-v-kholdynhu-perervnyi.md)
- [PP.Стаж на посаді (останній)](../measures/pp-stazh-na-posadi-ostannii.md)

## Нотатки

_порожньо_
