# fact_Viva_Metrics

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `fact_Viva_Metrics` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| PERIOD | dateTime | PERIOD |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| STATUS_KEY | string | STATUS_KEY |  |
| IS_MAIN_POSITION | boolean | IS_MAIN_POSITION |  |
| VACATION_DAY | double | VACATION_DAY |  |
| WEEKEND_DAY | double | WEEKEND_DAY |  |
| VACATION_NUMBER | double | VACATION_NUMBER |  |
| LONG_VACATION | double | LONG_VACATION |  |
| LONG_VACATION_BY_MAIN_POSITION | double | LONG_VACATION_BY_MAIN_POSITION |  |
| LONG_VACATION_TOTAL_DAY | double | LONG_VACATION_TOTAL_DAY |  |
| LONG_VACATION_TOTAL_DAY_BY_MAIN_POSITION | double | LONG_VACATION_TOTAL_DAY_BY_MAIN_POSITION |  |
| SICK_LEAVE_DAY_WITHOUT_PREGNANCY | double | SICK_LEAVE_DAY_WITHOUT_PREGNANCY |  |
| WORK_DAY_FOR_ABSENTEEISM_СNT | double | WORK_DAY_FOR_ABSENTEEISM_СNT |  |
| FTE_WEIGHTED_WORK_DAY_FOR_ABSENTEEISM | double | FTE_WEIGHTED_WORK_DAY_FOR_ABSENTEEISM |  |
| WORK_DAYS_PER_MONTH_YEAR_CNT | double | WORK_DAYS_PER_MONTH_YEAR_CNT |  |
| FTE_WEIGHTED_WORK_DAYS_PER_MONTH_YEAR_CNT | double | FTE_WEIGHTED_WORK_DAYS_PER_MONTH_YEAR_CNT |  |
| SICK_LEAVE_ID_CNT | double | SICK_LEAVE_ID_CNT |  |
| IS_SICK_LEAVE_PAID | boolean | IS_SICK_LEAVE_PAID |  |
| SICK_LEAVE_DAY_TOTAL | double | SICK_LEAVE_DAY_TOTAL |  |
| INTERNAL_NETWORK_SIZE | double | INTERNAL_NETWORK_SIZE |  |
| NETWORK_OUTSIDE_ORGANIZATION | double | NETWORK_OUTSIDE_ORGANIZATION |  |
| COLLABORATION_HOUR | double | COLLABORATION_HOUR |  |
| COLLABORATION_SPAN | double | COLLABORATION_SPAN |  |
| TOTAL_AFTER_HOUR | double | TOTAL_AFTER_HOUR |  |
| UNINTERRUPTED_HOUR | double | UNINTERRUPTED_HOUR |  |
| MEETING_HOUR | double | MEETING_HOUR |  |
| MEETING_AND_CALL_WITH_MANAGER_HOUR | double | MEETING_AND_CALL_WITH_MANAGER_HOUR |  |
| MANAGER_COACHING_ONE_TO_ONE_HOUR | double | MANAGER_COACHING_ONE_TO_ONE_HOUR |  |
| WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION | double | WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION |  |
| CONFLICTING_MEETING_HOUR | double | CONFLICTING_MEETING_HOUR |  |
| MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR | double | MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR |  |
| IS_EXIST_VIVA_INFO | boolean | IS_EXIST_VIVA_INFO |  |
| IS_FIRED | boolean | IS_FIRED |  |
| FIRED_UNIT_CNT | int64 | FIRED_UNIT_CNT |  |
| EMPLOYEE_UNIT_AVERAGE | double | EMPLOYEE_UNIT_AVERAGE |  |
| FULL_NAME | string | FULL_NAME |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| POSITION | string | POSITION |  |
| DISMISSAL_DATE | dateTime | DISMISSAL_DATE |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |

## Пов'язані міри

Усього: 22.
- [PP.Годин взаємодії з керівником (Холдинг)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-kholdynh.md)
- [PP.Годин взаємодії з керівником (співробітник)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-spivrobitnyk.md)
- [PP.Годин взаємодії по нарадах (Холдинг)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kholdynh.md)
- [PP.Годин взаємодії по нарадах (співробітник)](../measures/pp-hodyn-vzaiemodii-po-naradakh-spivrobitnyk.md)
- [PP.Годин взаємодії у неробочий час (Холдинг)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kholdynh.md)
- [PP.Годин взаємодії у неробочий час (співробітник)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-spivrobitnyk.md)
- [PP.Годин для фокусної роботи (Холдинг)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kholdynh.md)
- [PP.Годин для фокусної роботи (співробітник)](../measures/pp-hodyn-dlia-fokusnoi-roboty-spivrobitnyk.md)
- [PP.Годин загальної взаємодії (Холдинг)](../measures/pp-hodyn-zahalnoi-vzaiemodii-kholdynh.md)
- [PP.Годин загальної взаємодії (співробітник)](../measures/pp-hodyn-zahalnoi-vzaiemodii-spivrobitnyk.md)
- [PP.Годин керівника на взаємодію із безпосередніми підлеглими (Холдинг)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kholdynh.md)
- [PP.Годин керівника на взаємодію із безпосередніми підлеглими (співробітник)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-spivrobitnyk.md)
- [PP.Годин нарад 1:1 з керівником (Холдинг)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kholdynh.md)
- [PP.Годин нарад 1:1 з керівником (співробітник)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-spivrobitnyk.md)
- [PP.Довжина (границі) робочого дня (Холдинг)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-kholdynh.md)
- [PP.Довжина (границі) робочого дня (співробітник)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-spivrobitnyk.md)
- [PP.Доля Conflicting meeting hours (Холдинг)](../measures/pp-dolia-conflicting-meeting-hours-kholdynh.md)
- [PP.Доля Conflicting meeting hours (співробітник)](../measures/pp-dolia-conflicting-meeting-hours-spivrobitnyk.md)
- [PP.Розмір мережі (Холдинг, 3м)](../measures/pp-rozmir-merezhi-kholdynh-3m.md)
- [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md)
- [PP.Ширина мережі (Холдинг, 3м)](../measures/pp-shyryna-merezhi-kholdynh-3m.md)
- [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

## Нотатки

_порожньо_
