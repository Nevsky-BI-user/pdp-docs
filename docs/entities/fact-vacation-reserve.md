# fact_Vacation_Reserve

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Vacation_Reserve` |
| Джерела | `DM.vw_R27_fact_Vacation_Reserve_PDP` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| RESERVE_START_OF_MONTH | double | RESERVE_START_OF_MONTH |  |
| ACCRUED | double | ACCRUED |  |
| UTILIZED | double | UTILIZED |  |
| RESERVE_END_OF_MONTH | double | RESERVE_END_OF_MONTH |  |
| LAST_DAY_OF_VACATION | dateTime | LAST_DAY_OF_VACATION |  |
| NO_VACATION_DURATION_MONTHS | double | NO_VACATION_DURATION_MONTHS |  |
| IS_YEAR_NO_VACATION | int64 | IS_YEAR_NO_VACATION |  |
| VACATION_TYPE | string | VACATION_TYPE |  |
| VACATION_TYPE_KEY | string | VACATION_TYPE_KEY |  |
| VACATION_TYPE_DETALIZATION | string | VACATION_TYPE_DETALIZATION |  |
| STATUS_KEY | string | STATUS_KEY |  |
| STATUS_CODE | string | STATUS_CODE |  |
| IS_RATE_RELEASE | int64 | IS_RATE_RELEASE |  |
| EMP_HEAD_ADMIN_ID | string | EMP_HEAD_ADMIN_ID |  |
| EMP_HEAD_FUNCTIONAL_ID | string | EMP_HEAD_FUNCTIONAL_ID |  |
| EMP_HRBP_ID | string | EMP_HRBP_ID |  |
| EMP_FINBP_ID | string | EMP_FINBP_ID |  |
| TENURE_ALT_BOX_KEY | string | TENURE_ALT_BOX_KEY |  |
| AGE_BOX_KEY | string | AGE_BOX_KEY |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| WORK_FORMAT_ON_POSITION_KEY | string | WORK_FORMAT_ON_POSITION_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| WORK_FORMAT_ON_PERSON_KEY | string | WORK_FORMAT_ON_PERSON_KEY |  |
| OFFICE_ON_PERSON_KEY | string | OFFICE_ON_PERSON_KEY |  |
| IS_GREEN | int64 | IS_GREEN |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| EMPLOYEE_STATUS_ID | string | EMPLOYEE_STATUS_ID |  |
| DOC_VACATION_ID | string | DOC_VACATION_ID |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| PERSON_KEY | string | PERSON_KEY |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERMANENT_TEMPORARY_DETAILS_ID | int64 | PERMANENT_TEMPORARY_DETAILS_ID |  |
| PERMANENT_TEMPORARY_ADVANCED_KEY | int64 | PERMANENT_TEMPORARY_ADVANCED_KEY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | DIVISION_PERSON_ID | `dim_Person` | PERSON_KEY |
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | JOB_TITLE_ID | `dim_Position` | POSITION_CODE_KEY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: 2.
- [PP.Залишок відпустки](../measures/pp-zalyshok-vidpustky.md)
- [PP.Місяці без відпустки](../measures/pp-misiatsi-bez-vidpustky.md)

## Нотатки

_порожньо_
