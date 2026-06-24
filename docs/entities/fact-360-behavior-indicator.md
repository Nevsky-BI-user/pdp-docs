# fact_360_Behavior_Indicator

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_360_Behavior_Indicator` |
| Джерела | `DM.vw_R27_fact_360_Behavior_Indicator` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| Employee_ID | string | Employee_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| IS_MAIN_POSITION | int64 | IS_MAIN_POSITION |  |
| WORK_FORMAT_ON_EMPLOYEE_KEY | string | WORK_FORMAT_ON_EMPLOYEE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| Form_Template_ID | string | Form_Template_ID |  |
| Form_Template_Name | string | Form_Template_Name |  |
| Competency_ID | string | Competency_ID |  |
| Competency_Name | string | Competency_Name |  |
| Behavior_ID | string | Behavior_ID |  |
| Behavior_Name | string | Behavior_Name |  |
| Assessment_Type_Code | string | Assessment_Type_Code |  |
| Participant_Category | string | Participant_Category |  |
| Employee_Participant_ID | string | Employee_Participant_ID |  |
| Behavior_Rate | double | Behavior_Rate |  |
| Competency_Rate | double | Competency_Rate |  |
| Comment | string | Comment |  |
| Section_Custom_Field_ID | string | Section_Custom_Field_ID |  |
| Question_Title | string | Question_Title |  |
| Value_Str | string | Value_Str |  |
| Assessment_Year | string | Assessment_Year |  |
| Form_Employee_ID | string | Form_Employee_ID |  |
| Form_Code | string | Form_Code |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |

## Пов'язані міри

—

## Нотатки

_порожньо_
