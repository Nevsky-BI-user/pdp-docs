# fact_Vacation

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Vacation` |
| Джерела | `DM.vw_R27_fact_Vacation_Fact_PDP` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| PERIOD | dateTime | PERIOD |  |
| DOC_VACATION_NUM | string | DOC_VACATION_NUM |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| FIRST_DAY_OF_VACATION | dateTime | FIRST_DAY_OF_VACATION |  |
| LAST_DAY_OF_VACATION | dateTime | LAST_DAY_OF_VACATION |  |
| DOC_VACATION_START_DATE | dateTime | DOC_VACATION_START_DATE |  |
| DOC_VACATION_END_DATE | dateTime | DOC_VACATION_END_DATE |  |
| VAC_BEGIN_DATE | dateTime | VAC_BEGIN_DATE |  |
| VAC_END_DATE | dateTime | VAC_END_DATE |  |
| UTILIZED | int64 | UTILIZED |  |
| UTILIZED_FACT | int64 | UTILIZED_FACT |  |
| IS_VACATION_CALCULATED | int64 | IS_VACATION_CALCULATED |  |
| VACATION_TYPE | string | VACATION_TYPE |  |
| VACATION_TYPE_KEY | string | VACATION_TYPE_KEY |  |
| VACATION_TYPE_DETALIZATION | string | VACATION_TYPE_DETALIZATION |  |
| STATUS_KEY | string | STATUS_KEY |  |
| STATUS_CODE | string | STATUS_CODE |  |
| FTE_FACT | double | FTE_FACT |  |
| IS_RATE_RELEASE | boolean | IS_RATE_RELEASE |  |
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
| DIVISION_ID | string | DIVISION_ID |  |
| DOC_DATE | dateTime | DOC_DATE |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERSON_KEY | string | PERSON_KEY |  |
| PERMANENT_TEMPORARY_DETAILS_ID | int64 | PERMANENT_TEMPORARY_DETAILS_ID |  |

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

—

## Нотатки

_порожньо_
