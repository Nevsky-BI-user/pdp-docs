# fact_Employee_History_Position

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employee_History_Position` |
| Джерела | `DM.vw_R27_fact_Employee_History_Position` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| DIVISION_PERSON_NAME | string | DIVISION_PERSON_NAME |  |
| DIRECTION | string | DIRECTION |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| JOB_TITLE_NAME | string | JOB_TITLE_NAME |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| IS_MAIN_POSITION | boolean | IS_MAIN_POSITION |  |
| STATUS_KEY | string | STATUS_KEY |  |
| RECEIPT_DATE | dateTime | RECEIPT_DATE |  |
| DISMISSAL_DATE | dateTime | DISMISSAL_DATE |  |
| DIVISION_PERSON_PART_TIME_ID | string | DIVISION_PERSON_PART_TIME_ID |  |
| JOB_TITLE_PART_TIME_ID | string | JOB_TITLE_PART_TIME_ID |  |
| JOB_TITLE_PART_TIME_AMT | double | JOB_TITLE_PART_TIME_AMT |  |
| PART_TIME_PERIOD | int64 | PART_TIME_PERIOD |  |
| REASON_CHANGE_STATE_CODE | string | REASON_CHANGE_STATE_CODE |  |
| IS_POSITION_CHANGE | boolean | IS_POSITION_CHANGE |  |
| IS_ANNUAL_TARGET_INCOME_CHANGE | boolean | IS_ANNUAL_TARGET_INCOME_CHANGE |  |
| IS_POSITION_CATEGORY_CHANGE | boolean | IS_POSITION_CATEGORY_CHANGE |  |
| IS_SALARY_CHANGE | boolean | IS_SALARY_CHANGE |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| HIERARCHY_LEVEL | string | HIERARCHY_LEVEL |  |
| seniority_LAST_POSITION_HIRE_DATE | int64 | seniority_LAST_POSITION_HIRE_DATE |  |
| seniority_FIRST_HOLDING_HIRE_DATE | int64 | seniority_FIRST_HOLDING_HIRE_DATE |  |
| seniority_LAST_HOLDING_HIRE_DATE | int64 | seniority_LAST_HOLDING_HIRE_DATE |  |
| LAST_HOLDING_HIRE_DATE | dateTime | LAST_HOLDING_HIRE_DATE |  |
| SALARY | double | SALARY |  |
| TARIFF_RATE_TYPE_CODE | string | TARIFF_RATE_TYPE_CODE |  |
| PAYMENT_PLAN_SUM | double | PAYMENT_PLAN_SUM |  |
| BONUS_YEAR_SALARY_CNT | double | BONUS_YEAR_SALARY_CNT |  |
| BONUS_QUARTER_SALARY_CNT | double | BONUS_QUARTER_SALARY_CNT |  |
| BONUS_MONTH_SALARY_CNT | double | BONUS_MONTH_SALARY_CNT |  |
| ANNUAL_TARGET_INCOME | double | ANNUAL_TARGET_INCOME |  |
| MHP_STAR | double | MHP_STAR |  |
| MHP_STAR_DATE | dateTime | MHP_STAR_DATE |  |
| GENERAL_PERFORMANCE_STR_RATE | string | GENERAL_PERFORMANCE_STR_RATE |  |
| GENERAL_PERFORMANCE_DESC_RATE | double | GENERAL_PERFORMANCE_DESC_RATE |  |
| PERFORMANCE_YEAR | int64 | PERFORMANCE_YEAR |  |
| PERFORMANCE_TYPE | string | PERFORMANCE_TYPE |  |
| POSITION_BEGIN | string | POSITION_BEGIN |  |
| DIVISION_BEGIN | string | DIVISION_BEGIN |  |
| EMPLOYEE_MANAGER | string | EMPLOYEE_MANAGER |  |
| IND_BONUS_RATE | double | IND_BONUS_RATE |  |
| CALC_PERFORMANCE_STR_RATE | string | CALC_PERFORMANCE_STR_RATE |  |
| Calc_Performance_Desc_Rate | string | Calc_Performance_Desc_Rate |  |
| PLAN_YEAR | int64 | PLAN_YEAR |  |
| POSITION_ON_OKR_DATE | string | POSITION_ON_OKR_DATE |  |
| DIVISION_PERSON_ON_OKR_DATE | string | DIVISION_PERSON_ON_OKR_DATE |  |
| HEAD_ADMIN_ON_APPROVAL_DATE | string | HEAD_ADMIN_ON_APPROVAL_DATE |  |
| HEAD_ADMIN_ON_ASSESMENT_DATE | string | HEAD_ADMIN_ON_ASSESMENT_DATE |  |
| COLLABORATION_HOUR | double | COLLABORATION_HOUR |  |
| COLLABORATION_SPAN | double | COLLABORATION_SPAN |  |
| MEETING_HOUR | double | MEETING_HOUR |  |
| CONFLICTING_MEETING_HOUR | double | CONFLICTING_MEETING_HOUR |  |
| TOTAL_AFTER_HOURS | double | TOTAL_AFTER_HOURS |  |
| MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR | double | MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR |  |
| MANAGER_COACHING_ONE_TO_ONE_HOUR | double | MANAGER_COACHING_ONE_TO_ONE_HOUR |  |
| WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS | int64 | WORKDAYS_WITHOUT_SICKLEAVES_AND_VACATIONS |  |
| IS_APRIL_SALARY_REVIEW | boolean | IS_APRIL_SALARY_REVIEW |  |
| IS_TECH_POSITION_CHANGE | boolean | IS_TECH_POSITION_CHANGE |  |
| IS_TECH_SALARY_TRANSFER | boolean | IS_TECH_SALARY_TRANSFER |  |
| FlagTag | — | — | так |
| IS_OTHER_EVENT | — | — | так |
| EVENT_LIST | — | — | так |
| ORGANIZATION_NAME | string | ORGANIZATION_NAME |  |
| DIVISION_PERSON_CODE | string | DIVISION_PERSON_CODE |  |
| JOB_TITLE_CODE | string | JOB_TITLE_CODE |  |
| DIVISION_PERSON_PART_TIME_NAME | string | DIVISION_PERSON_PART_TIME_NAME |  |
| JOB_TITLE_PART_TIME_NAME | string | JOB_TITLE_PART_TIME_NAME |  |
| POSITION_BEGIN_NAME | string | POSITION_BEGIN_NAME |  |
| DIVISION_BEGIN_NAME | string | DIVISION_BEGIN_NAME |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: **37**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 30

**Життєвий цикл:** [PP.Бал](../measures/pp-bal.md) · [PP.Бал OKR](../measures/pp-bal-okr.md) · [PP.Бонуси Р/К/М](../measures/pp-bonusy-r-k-m.md) · [PP.Год. взаємодії](../measures/pp-hod-vzaiemodii.md) · [PP.Год. конфліктів](../measures/pp-hod-konfliktiv.md) · [PP.Год. нарад](../measures/pp-hod-narad.md) · [PP.Год. нероб.](../measures/pp-hod-nerob.md) · [PP.Дата події](../measures/pp-data-podii.md) · [PP.Довжина дня](../measures/pp-dovzhyna-dnia.md) · [PP.ЖЦ_Категорія посади](../measures/pp-zhts-katehoriia-posady.md) · [PP.ЖЦ_Напрям](../measures/pp-zhts-napriam.md) · [PP.ЖЦ_Посада](../measures/pp-zhts-posada.md) · [PP.ЖЦ_Піднапрям](../measures/pp-zhts-pidnapriam.md) · [PP.ЖЦ_Підприємство](../measures/pp-zhts-pidpryiemstvo.md) · [PP.Зірка МХП](../measures/pp-zirka-mkhp.md) · [PP.Кадровий підрозділ](../measures/pp-kadrovyi-pidrozdil.md) · [PP.Категорія (Performance)](../measures/pp-katehoriia-performance.md) · [PP.Код посади](../measures/pp-kod-posady.md) · [PP.Код підрозділу](../measures/pp-kod-pidrozdilu.md) · [PP.Колір (OKR)](../measures/pp-kolir-okr.md) · [PP.Колір (Performance)](../measures/pp-kolir-performance.md) · [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md) · [PP.Оклад_detailed](../measures/pp-oklad-detailed.md) · [PP.РЦД](../measures/pp-rtsd.md) · [PP.РЦД_detailed](../measures/pp-rtsd-detailed.md) · [PP.Стаж в холдингу](../measures/pp-stazh-v-kholdynhu.md) · [PP.Стаж на посаді](../measures/pp-stazh-na-posadi.md) · [PP.Суміщення](../measures/pp-sumishchennia.md) · [PP.Тип події](../measures/pp-typ-podii.md) · [PP.Форма оплати](../measures/pp-forma-oplaty.md)

### [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md) — 8

**Інші візуали:** [PP.Год. взаємодії](../measures/pp-hod-vzaiemodii.md) · [PP.Год. конфліктів](../measures/pp-hod-konfliktiv.md) · [PP.Год. нарад](../measures/pp-hod-narad.md) · [PP.ЖЦ_Посада](../measures/pp-zhts-posada.md) · [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md) · [PP.Оклад](../measures/pp-oklad.md) · [PP.Підпис типу події](../measures/pp-pidpys-typu-podii.md) · [PP.РЦД](../measures/pp-rtsd.md)

### Поза звітом / службові — 5

[PP.history_position_maxd](../measures/pp-history-position-maxd.md) · [PP.Коеф. бонусу](../measures/pp-koef-bonusu.md) · [PP.Поточний РЦД](../measures/pp-potochnyi-rtsd.md) · [PP.Приріст_РЦД_detailed](../measures/pp-pryrist-rtsd-detailed.md) · [PP.Підприємство](../measures/pp-pidpryiemstvo.md)

## Нотатки

_порожньо_
