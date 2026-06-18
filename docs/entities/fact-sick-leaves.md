# fact_Sick_Leaves

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Sick_Leaves` |
| Джерела | `DM.vw_R27_fact_Sick_Leaves_PDP` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| period | dateTime | period |  |
| FTE_num | double | FTE_num |  |
| sick_leave_days | int64 | sick_leave_days |  |
| sick_leave_work_days | double | sick_leave_work_days |  |
| FTE_weighted_sick_leave_work_days | double | FTE_weighted_sick_leave_work_days |  |
| is_sl_start_month | int64 | is_sl_start_month |  |
| payments_from_company | double | payments_from_company |  |
| company_paid_days | double | company_paid_days |  |
| payments_from_FSC | double | payments_from_FSC |  |
| FSC_paid_days | double | FSC_paid_days |  |
| is_sl_paid | int64 | is_sl_paid |  |
| organization_key | string | organization_key |  |
| person_key | string | person_key |  |
| unit_key | string | unit_key |  |
| position_key | string | position_key |  |
| sick_leave_duration_box_key | string | sick_leave_duration_box_key |  |
| sick_leave_id_key | string | sick_leave_id_key |  |
| sick_leave_type_key | string | sick_leave_type_key |  |
| status_key | int64 | status_key |  |
| sl_start_date | int64 | sl_start_date |  |
| sl_end_date | dateTime | sl_end_date |  |
| sl_diagnosis | string | sl_diagnosis |  |
| is_pregnancy | string | is_pregnancy |  |
| emp_head_id | string | emp_head_id |  |
| emp_head_admin_id | string | emp_head_admin_id |  |
| emp_head_functional_id | string | emp_head_functional_id |  |
| emp_hrbp_id | string | emp_hrbp_id |  |
| emp_finbp_id | string | emp_finbp_id |  |
| tenure_alt_box_key | string | tenure_alt_box_key |  |
| age_box_key | string | age_box_key |  |
| employment_type_key | string | employment_type_key |  |
| permanent_temporary_key | int64 | permanent_temporary_key |  |
| work_format_on_position_key | int64 | work_format_on_position_key |  |
| office_on_position_key | string | office_on_position_key |  |
| work_format_on_person_key | string | work_format_on_person_key |  |
| office_on_person_key | string | office_on_person_key |  |
| Employee_ID | string | Employee_ID |  |
| Doc_Job_Application_ID | string | Doc_Job_Application_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| sl_status | string | sl_status |  |
| FTE_weighted_sick_leave_days | double | FTE_weighted_sick_leave_days |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | person_key | `dim_Person` | PERSON_KEY |
| from | unit_key | `dim_Unit` | UNIT_KEY |
| from | status_key | `dim_Employee_Status` | STATUS_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | employment_type_key | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | office_on_position_key | `dim_Office` | OFFICE_KEY |
| from | position_key | `dim_Position` | POSITION_CODE_KEY |
| from | period | `dim_Date` | Date |

## Пов'язані міри

—

## Нотатки

_порожньо_
