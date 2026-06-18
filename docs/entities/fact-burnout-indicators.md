# fact_Burnout_Indicators

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `fact_Burnout_Indicators` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| IS_MAIN_POSITION | boolean | IS_MAIN_POSITION |  |
| FIRED_UNIT_CNT | int64 | FIRED_UNIT_CNT |  |
| EMPLOYEE_UNIT_AVERAGE | double | EMPLOYEE_UNIT_AVERAGE |  |
| TURNOVER | double | TURNOVER |  |
| IS_TURNOVER_RISK | string | IS_TURNOVER_RISK |  |
| LAST_YEAR_PERFORMANCE_STR_RATE | string | LAST_YEAR_PERFORMANCE_STR_RATE |  |
| PREV_YEAR_PERFORMANCE_STR_RATE | string | PREV_YEAR_PERFORMANCE_STR_RATE |  |
| LAST_YEAR_PERFORMANCE_DESC_RATE | double | LAST_YEAR_PERFORMANCE_DESC_RATE |  |
| PREV_YEAR_PERFORMANCE_DESC_RATE | double | PREV_YEAR_PERFORMANCE_DESC_RATE |  |
| LAST_YEAR_PERFORMANCE | int64 | LAST_YEAR_PERFORMANCE |  |
| PREV_YEAR_PERFORMANCE | int64 | PREV_YEAR_PERFORMANCE |  |
| PERFORMANCE_RATE_TREND | string | PERFORMANCE_RATE_TREND |  |
| IS_PERFORMANCE_RISK | string | IS_PERFORMANCE_RISK |  |
| OKR_LAST_YEAR_RATE | double | OKR_LAST_YEAR_RATE |  |
| OKR_PREV_YEAR_RATE | double | OKR_PREV_YEAR_RATE |  |
| OKR_LAST_YEAR_COLOR_RATE | string | OKR_LAST_YEAR_COLOR_RATE |  |
| OKR_PREV_YEAR_COLOR_RATE | string | OKR_PREV_YEAR_COLOR_RATE |  |
| LAST_YEAR_OKR_PLAN | int64 | LAST_YEAR_OKR_PLAN |  |
| PREV_YEAR_OKR_PLAN | int64 | PREV_YEAR_OKR_PLAN |  |
| OKR_RATE_TREND | string | OKR_RATE_TREND |  |
| IS_OKR_RISK | string | IS_OKR_RISK |  |
| SALARY_RANGE | string | SALARY_RANGE |  |
| IS_SALARY_RISK | string | IS_SALARY_RISK |  |
| NO_QUALITY_VACATION_MONTHS | int64 | NO_QUALITY_VACATION_MONTHS |  |
| IS_VACATION_RISK | string | IS_VACATION_RISK |  |
| TOTAL_AFTER_HOURS | double | TOTAL_AFTER_HOURS |  |
| WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS | int64 | WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS |  |
| VIVA_OVERWORKING | double | VIVA_OVERWORKING |  |
| IS_VIVA_RISK | string | IS_VIVA_RISK |  |
| IS_TOTAL_RISK | string | IS_TOTAL_RISK |  |
| ID | string | ID |  |
| S_ID | string | S_ID |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| PERIOD | dateTime | PERIOD |  |
| DISMISSAL_DATE | dateTime | DISMISSAL_DATE |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| STATUS_KEY | string | STATUS_KEY |  |
| IS_FIRED | boolean | IS_FIRED |  |
| RETENTION_CASE | string | RETENTION_CASE |  |
| IS_FOCUS_GROUP | string | IS_FOCUS_GROUP |  |
| MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR | double | MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR |  |
| IS_MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR_RISK | string | IS_MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR_RISK |  |
| FULL_NAME | string | FULL_NAME |  |
| TOTAL_RISK_CNT | int64 | TOTAL_RISK_CNT |  |
| VACATION_RESERVE | double | VACATION_RESERVE |  |
| VACATION_RESERVE_BY_MAIN_POSITION | double | VACATION_RESERVE_BY_MAIN_POSITION |  |
| NO_VACATION_DURATION_BY_MAIN_POSITION | int64 | NO_VACATION_DURATION_BY_MAIN_POSITION |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| POSITION | string | POSITION |  |
| ORDER_NUM_BY_RISK | int64 | ORDER_NUM_BY_RISK |  |
| HIERARCHY_LEVEL | int64 | HIERARCHY_LEVEL |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | EMPLOYEE_ID | `dim_Person` | EMPLOYEE_CODE |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | ID |
| from | ORGANIZATION_ID | `dim_Organization` | ORGANIZATION_KEY |
| from | DISMISSAL_DATE | `dim_Date` | Date |

## Пов'язані міри

Усього: **49**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 3

**Паспортна частина:** [PP.SVG.Performance.Last2Periods](../measures/pp-svg-performance-last2periods.md) · [PP.Рік оцінки результативності.Last](../measures/pp-rik-otsinky-rezultatyvnosti-last.md) · [PP.Рік оцінки результативності.Prev](../measures/pp-rik-otsinky-rezultatyvnosti-prev.md)

### [Group Profile](../report/group-profile.md) — 1

**Версія 2 › Ризики та фокуси уваги:** [GP.Ризик втрати працівників (%)](../measures/gp-ryzyk-vtraty-pratsivnykiv.md)

### [Утримання працівників](../report/utrymannia-pratsivnykiv.md) — 18

**Інші візуали:** [AC.BR.OKR](../measures/ac-br-okr.md) · [AC.BR.OKR останній рік](../measures/ac-br-okr-ostannii-rik.md) · [AC.BR.OKR попередній рік](../measures/ac-br-okr-poperednii-rik.md) · [AC.BR.Годин взаємодії з керівником](../measures/ac-br-hodyn-vzaiemodii-z-kerivnykom.md) · [AC.BR.Зарплата вилка](../measures/ac-br-zarplata-vylka.md) · [AC.BR.Кількість звільнених](../measures/ac-br-kilkist-zvilnenykh.md) · [AC.BR.Кількість місяців без якісної відпустки](../measures/ac-br-kilkist-misiatsiv-bez-iakisnoi-vidpustky.md) · [AC.BR.Перепрацювання Viva](../measures/ac-br-perepratsiuvannia-viva.md) · [AC.BR.Плинність (%)](../measures/ac-br-plynnist.md) · [AC.BR.Ризик втрати](../measures/ac-br-ryzyk-vtraty.md) · [AC.BR.Стаж в холдингу (неперервний)](../measures/ac-br-stazh-v-kholdynhu-neperervnyi.md) · [AC.BR.Стаж на посаді (останній)](../measures/ac-br-stazh-na-posadi-ostannii.md) · [AC.BR.ТОР останній рік](../measures/ac-br-tor-ostannii-rik.md) · [AC.BR.ТОР попередній рік](../measures/ac-br-tor-poperednii-rik.md) · [AC.BR.Тренд оцінки результативності (ТОР)](../measures/ac-br-trend-otsinky-rezultatyvnosti-tor.md)

**Filter Pannel:** [AC.Burnout_risk.Застосувати вибір](../measures/ac-burnout-risk-zastosuvaty-vybir.md)

**Таблиці › Звільнені:** [AC.Burnout_Risk.Панель фільтрів.Звільнені](../measures/ac-burnout-risk-panel-filtriv-zvilneni.md)

**Таблиці › Працюючі:** [AC.Burnout_risk.Панель фільтрів.Працюючі](../measures/ac-burnout-risk-panel-filtriv-pratsiuiuchi.md)

### Поза звітом / службові — 27

[AC.Burnout_Risk.c_rows](../measures/ac-burnout-risk-c-rows.md) · [AC.Filter](../measures/ac-filter.md) · [AC.Nav.My_lead_team](../measures/ac-nav-my-lead-team.md) · [AC.Взаємодія з керівником](../measures/ac-vzaiemodiia-z-kerivnykom.md) · [AC.Зарплата (вилки)](../measures/ac-zarplata-vylky.md) · [AC.Кількість місяців без якісної відпустки](../measures/ac-kilkist-misiatsiv-bez-iakisnoi-vidpustky.md) · [AC.Перепрацювання Viva](../measures/ac-perepratsiuvannia-viva.md) · [AC.Плинність (%)](../measures/ac-plynnist.md) · [AC.Ризик](../measures/ac-ryzyk.md) · [AC.Тренд оцінки OKR](../measures/ac-trend-otsinky-okr.md) · [AC.Тренд оцінки результативності](../measures/ac-trend-otsinky-rezultatyvnosti.md) · [AC.Чи є ризик вигорання по плинності?](../measures/ac-chy-ie-ryzyk-vyhorannia-po-plynnosti.md) · [AC.Чи є ризик вигорання по результатам оцінки OKR?](../measures/ac-chy-ie-ryzyk-vyhorannia-po-rezultatam-otsinky-okr.md) · [AC.Чи є ризик вигорання по результатам оцінки результативності?](../measures/ac-chy-ie-ryzyk-vyhorannia-po-rezultatam-otsinky-rezultatyvnosti.md) · [AC.Чи є ризик вигорання через відсутність відпусток?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-vidsutnist-vidpustok.md) · [AC.Чи є ризик вигорання через відсутність спілкування з керівником?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-vidsutnist-spilkuvannia-z-kerivnykom.md) · [AC.Чи є ризик вигорання через перепрацювання?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-perepratsiuvannia.md) · [AC.Чи є ризик вигорання через рівень оплати праці?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-riven-oplaty-pratsi.md) · [AC.Чи є ризик?](../measures/ac-chy-ie-ryzyk.md) · [GP.OKR  попередній рік](../measures/gp-okr-poperednii-rik.md) · [GP.OKR  поточний рік](../measures/gp-okr-potochnyi-rik.md) · [GP.Оцінка результативності попередній рік](../measures/gp-otsinka-rezultatyvnosti-poperednii-rik.md) · [GP.Оцінка результативності поточний рік](../measures/gp-otsinka-rezultatyvnosti-potochnyi-rik.md) · [GP.Рік оцінки результативності.Last](../measures/gp-rik-otsinky-rezultatyvnosti-last.md) · [GP.Рік оцінки результативності.Prev](../measures/gp-rik-otsinky-rezultatyvnosti-prev.md) · [PP.Оцінка результативності попередній рік](../measures/pp-otsinka-rezultatyvnosti-poperednii-rik.md) · [PP.Оцінка результативності поточний рік](../measures/pp-otsinka-rezultatyvnosti-potochnyi-rik.md)

## Нотатки

_порожньо_
