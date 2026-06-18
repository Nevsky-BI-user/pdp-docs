# fact_Metrics

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `fact_Metrics` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| PERIOD | dateTime | PERIOD |  |
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
| LONG_VACATION_TOTAL_DAY | double | LONG_VACATION_TOTAL_DAY |  |
| SICK_LEAVE_DAY_WITHOUT_PREGNANCY | double | SICK_LEAVE_DAY_WITHOUT_PREGNANCY |  |
| FTE_WEIGHTED_WORK_DAY_FOR_ABSENTEEISM | double | FTE_WEIGHTED_WORK_DAY_FOR_ABSENTEEISM |  |
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
| ID | string | ID |  |
| WORK_DAY_FOR_ABSENTEEISM_СNT | double | WORK_DAY_FOR_ABSENTEEISM_СNT |  |
| WORK_DAYS_PER_MONTH_YEAR_CNT | double | WORK_DAYS_PER_MONTH_YEAR_CNT |  |
| FTE_WEIGHTED_WORK_DAYS_PER_MONTH_YEAR_CNT | double | FTE_WEIGHTED_WORK_DAYS_PER_MONTH_YEAR_CNT |  |
| IS_EXIST_VIVA_INFO | boolean | IS_EXIST_VIVA_INFO |  |
| IS_FIRED | boolean | IS_FIRED |  |
| FIRED_UNIT_CNT | int64 | FIRED_UNIT_CNT |  |
| EMPLOYEE_UNIT_AVERAGE | double | EMPLOYEE_UNIT_AVERAGE |  |
| FULL_NAME | string | FULL_NAME |  |
| LONG_VACATION_BY_MAIN_POSITION | double | LONG_VACATION_BY_MAIN_POSITION |  |
| LONG_VACATION_TOTAL_DAY_BY_MAIN_POSITION | double | LONG_VACATION_TOTAL_DAY_BY_MAIN_POSITION |  |
| VACATION_RESERVE | double | VACATION_RESERVE |  |
| VACATION_RESERVE_BY_MAIN_POSITION | double | VACATION_RESERVE_BY_MAIN_POSITION |  |
| NO_VACATION_DURATION_BY_MAIN_POSITION | int64 | NO_VACATION_DURATION_BY_MAIN_POSITION |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| POSITION | string | POSITION |  |
| DISMISSAL_DATE | dateTime | DISMISSAL_DATE |  |
| ORDER_NUM_BY_RISK | int64 | ORDER_NUM_BY_RISK |  |
| HIERARCHY_LEVEL | int64 | HIERARCHY_LEVEL |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | DIVISION_PERSON_ID | `dim_Person` | PERSON_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |

## Пов'язані міри

Усього: **26**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 9

**Здоров'я та благополуччя:** [PP.% днів відпустки в робочі дні](../measures/pp-dniv-vidpustky-v-robochi-dni.md) · [PP.Абсентеїзм](../measures/pp-absenteizm.md) · [PP.Дні відпустки](../measures/pp-dni-vidpustky.md) · [PP.Залишок відпустки](../measures/pp-zalyshok-vidpustky.md) · [PP.Кількість відпусток](../measures/pp-kilkist-vidpustok.md) · [PP.Кількість довгих відпусток](../measures/pp-kilkist-dovhykh-vidpustok.md) · [PP.Лікарняні](../measures/pp-likarniani.md) · [PP.Середня тривалість відпустки](../measures/pp-serednia-tryvalist-vidpustky.md) · [PP.Середня тривалість лікарняного](../measures/pp-serednia-tryvalist-likarnianoho.md)

### [Group Profile](../report/group-profile.md) — 15

**Інші візуали:** [GP.Доля співробітників команди з наявними відпустками понад 10 днів](../measures/gp-dolia-spivrobitnykiv-komandy-z-naiavnymy-vidpustkamy-ponad-10-dniv.md) · [GP.Плинність (%)](../measures/gp-plynnist.md) · [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md)

**Версія 1:** [GP.Доля співробітників команди з наявними відпустками понад 10 днів](../measures/gp-dolia-spivrobitnykiv-komandy-z-naiavnymy-vidpustkamy-ponad-10-dniv.md) · [GP.Плинність (%)](../measures/gp-plynnist.md) · [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md)

**Версія 2 › Ризики та фокуси уваги:** [GP.Рівень coaching (1:1), год/міс](../measures/gp-riven-coaching-1-1-hod-mis.md)

**Здоров'я та благополуччя:** [5AC.Коефіцієнт абсентеїзму](../measures/5ac-koefitsiient-absenteizmu.md) · [AC.Відсоток днів відпустки в робочі дні](../measures/ac-vidsotok-dniv-vidpustky-v-robochi-dni.md) · [AC.Доля співробітників з відпустками понад 10 днів](../measures/ac-dolia-spivrobitnykiv-z-vidpustkamy-ponad-10-dniv.md) · [AC.Лідер за невикористаними днями відпустки](../measures/ac-lider-za-nevykorystanymy-dniamy-vidpustky.md) · [AC.Лідер за часом без відпустки](../measures/ac-lider-za-chasom-bez-vidpustky.md) · [AC.Середня кількість днів використаної відпустки](../measures/ac-serednia-kilkist-dniv-vykorystanoi-vidpustky.md) · [AC.Середня кількість днів невикористаної відпустки](../measures/ac-serednia-kilkist-dniv-nevykorystanoi-vidpustky.md) · [AC.Середня кількість лікарняних на співробітника](../measures/ac-serednia-kilkist-likarnianykh-na-spivrobitnyka.md) · [AC.Середня тривалість відпустки співробітника, днів](../measures/ac-serednia-tryvalist-vidpustky-spivrobitnyka-dniv.md) · [AC.Середня тривалість лікарняного на співробітника](../measures/ac-serednia-tryvalist-likarnianoho-na-spivrobitnyka.md)

### Поза звітом / службові — 2

[PP.Тривалість довгих відпусток](../measures/pp-tryvalist-dovhykh-vidpustok.md) · [PP.Чи виплачено лікарняні від компанії](../measures/pp-chy-vyplacheno-likarniani-vid-kompanii.md)

## Нотатки

_порожньо_
