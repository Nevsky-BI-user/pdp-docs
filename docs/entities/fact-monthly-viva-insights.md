# fact_Monthly_Viva_Insights

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Monthly_Viva_Insights` |
| Джерела | `DM.vw_R27_fact_Monthly_Viva_Insights_PDP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Holding_PDP`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| PERSON_KEY | string | PERSON_KEY |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| UNIT_KEY | string | UNIT_KEY |  |
| PERIOD | dateTime | PERIOD |  |
| EMPLOYEE_LOGIN | string | EMPLOYEE_LOGIN |  |
| EMPLOYEE_MANAGER_LOGIN | string | EMPLOYEE_MANAGER_LOGIN |  |
| SUPERVISOR_INDICATOR | string | SUPERVISOR_INDICATOR |  |
| COLLABORATION_SPAN | double | COLLABORATION_SPAN |  |
| COLLABORATION_HOUR | double | COLLABORATION_HOUR |  |
| AFTER_HOUR_COLLABORATION_HOUR | double | AFTER_HOUR_COLLABORATION_HOUR |  |
| INTERNAL_NETWORK_SIZE | double | INTERNAL_NETWORK_SIZE |  |
| NETWORK_OUTSIDE_ORGANIZATION | double | NETWORK_OUTSIDE_ORGANIZATION |  |
| MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR | double | MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR |  |
| MEETING_HOUR | double | MEETING_HOUR |  |
| OPEN_ONE_BLOCK_HOUR | double | OPEN_ONE_BLOCK_HOUR |  |
| UNINTERRUPTED_HOUR | double | UNINTERRUPTED_HOUR |  |
| MANAGER_COACHING_ONE_TO_ONE_HOUR | double | MANAGER_COACHING_ONE_TO_ONE_HOUR |  |
| MEETING_AND_CALL_WITH_SKIP_LEVEL_ONE_TO_ONE_HOUR | double | MEETING_AND_CALL_WITH_SKIP_LEVEL_ONE_TO_ONE_HOUR |  |
| CALL_HOUR | double | CALL_HOUR |  |
| CHAT_HOUR | double | CHAT_HOUR |  |
| EMAIL_HOUR | double | EMAIL_HOUR |  |
| CHANNEL_MESSAGE_HOUR | double | CHANNEL_MESSAGE_HOUR |  |
| CONFLICTING_MEETING_HOUR | double | CONFLICTING_MEETING_HOUR |  |
| MEETING_AND_CALL_WITH_MANAGER_HOUR | double | MEETING_AND_CALL_WITH_MANAGER_HOUR |  |
| TOTAL_AFTER_HOURS | double | TOTAL_AFTER_HOURS |  |
| COLLABORATION_WITH_MANAGER | double | COLLABORATION_WITH_MANAGER |  |
| TOTAL_WITHOUT_SICKLEAVES_AND_VACATIONS | int64 | TOTAL_WITHOUT_SICKLEAVES_AND_VACATIONS |  |
| WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS | int64 | WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS |  |
| WORKED_ON_WEEKENDS | int64 | WORKED_ON_WEEKENDS |  |
| WORKED_IN_SICKLEAVES | int64 | WORKED_IN_SICKLEAVES |  |
| WORKED_IN_VACATION | int64 | WORKED_IN_VACATION |  |
| VIVA_DAYS | int64 | VIVA_DAYS |  |
| CALENDAR_DAYS | int64 | CALENDAR_DAYS |  |
| TOTAL_WORKDAYS | int64 | TOTAL_WORKDAYS |  |
| TOTAL_WEEKENDS | int64 | TOTAL_WEEKENDS |  |
| EMP_SICKLEAVES | int64 | EMP_SICKLEAVES |  |
| EMP_VACATIONS | int64 | EMP_VACATIONS |  |
| EMP_WORKDAYS | int64 | EMP_WORKDAYS |  |
| EMP_WEEKENDS | int64 | EMP_WEEKENDS |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | PERSON_KEY | `dim_Person` | PERSON_KEY |
| from | UNIT_KEY | `dim_Unit` | UNIT_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

—

## Нотатки

_порожньо_
