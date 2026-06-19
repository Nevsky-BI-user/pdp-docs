# fact_OKR_Goals

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_OKR_Goals` |
| Джерела | `DM.R27_fact_OKR_Goals` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Змінити-логіку-визначення-окремих-полів-у-вітрині`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| INIT_DOC_JOB_APPLICATION_ID | string | INIT_DOC_JOB_APPLICATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| INIT_DIVISION_PERSON_ID | string | INIT_DIVISION_PERSON_ID |  |
| INIT_DIVISION_PERSON | string | INIT_DIVISION_PERSON |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| DIVISION_PERSON | string | DIVISION_PERSON |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| FORM_TEMPLATE_ID | string | FORM_TEMPLATE_ID |  |
| FORM_TEMPLATE_NAME | string | FORM_TEMPLATE_NAME |  |
| PLAN_YEAR | int64 | PLAN_YEAR |  |
| PLAN_STATUS | string | PLAN_STATUS |  |
| OKR_OBJECTIVE_ID | string | OKR_OBJECTIVE_ID |  |
| OKR_WEIGHT | double | OKR_WEIGHT |  |
| OKR_AVG_RATE | double | OKR_AVG_RATE |  |
| OKR_COLOR_RATE | string | OKR_COLOR_RATE |  |
| TOTAL_OKR_RATE | double | TOTAL_OKR_RATE |  |
| TOTAL_OKR_COLOR_RATE | string | TOTAL_OKR_COLOR_RATE |  |
| CATEGORY | string | CATEGORY |  |
| IS_POSSIBLE_SUPER_GREEN_OKR | string | IS_POSSIBLE_SUPER_GREEN_OKR |  |
| FILLING_STATUS | string | FILLING_STATUS |  |
| IS_CROSSFUNCTIONAL | string | IS_CROSSFUNCTIONAL |  |
| OKR_DESCRIPTION | string | OKR_DESCRIPTION |  |
| OKR_METRIC_DESCRIPTION | string | OKR_METRIC_DESCRIPTION |  |
| OKR_CHANGE | string | OKR_CHANGE |  |
| IND_BONUS_RATE | double | IND_BONUS_RATE |  |
| CALC_PERFORMANCE_STR_RATE | double | CALC_PERFORMANCE_STR_RATE |  |
| CALC_PERFORMANCE_DESC_RATE | string | CALC_PERFORMANCE_DESC_RATE |  |
| EXEC_DATE | dateTime | EXEC_DATE |  |
| CREATED_DATE | dateTime | CREATED_DATE |  |
| UPDATED_DATE | dateTime | UPDATED_DATE |  |
| MONITORING_START_DATE | dateTime | MONITORING_START_DATE |  |
| MONITORING_END_DATE | dateTime | MONITORING_END_DATE |  |
| MONITORING_END_PLAN_DATE | dateTime | MONITORING_END_PLAN_DATE |  |
| MONITORING_END_FACT_DATE | dateTime | MONITORING_END_FACT_DATE |  |
| MONITORING_LAST_MODIFY_DATE | dateTime | MONITORING_LAST_MODIFY_DATE |  |
| MONITORING_EMPLOYEE_INIT_ID | string | MONITORING_EMPLOYEE_INIT_ID |  |
| CONSENT_START_DATE | dateTime | CONSENT_START_DATE |  |
| CONSENT_END_DATE | dateTime | CONSENT_END_DATE |  |
| CONSENT_END_PLAN_DATE | dateTime | CONSENT_END_PLAN_DATE |  |
| CONSENT_END_FACT_DATE | dateTime | CONSENT_END_FACT_DATE |  |
| CONSENT_LAST_MODIFY_DATE | dateTime | CONSENT_LAST_MODIFY_DATE |  |
| CONSENT_EMPLOYEE_INIT_ID | string | CONSENT_EMPLOYEE_INIT_ID |  |
| OKR_APPROVE_TIME | int64 | OKR_APPROVE_TIME |  |
| OKR_ASSESMENT_TIME | int64 | OKR_ASSESMENT_TIME |  |
| DIRECTION_ON_APPROVAL_DATE | string | DIRECTION_ON_APPROVAL_DATE |  |
| SUB_DIRECTION_ON_APPROVAL_DATE | string | SUB_DIRECTION_ON_APPROVAL_DATE |  |
| DIVISION_PERSON_ON_APPROVAL_DATE | string | DIVISION_PERSON_ON_APPROVAL_DATE |  |
| ORGANIZATION_ON_APPROVAL_DATE | string | ORGANIZATION_ON_APPROVAL_DATE |  |
| HAB_FOR_AGRO_ON_APPROVAL_DATE | string | HAB_FOR_AGRO_ON_APPROVAL_DATE |  |
| POSITION_ON_APPROVAL_DATE | string | POSITION_ON_APPROVAL_DATE |  |
| EMPLOYMENT_TYPE_ON_APPROVAL_DATE | string | EMPLOYMENT_TYPE_ON_APPROVAL_DATE |  |
| POSITION_CATEGORY_DETAIL_ON_APPROVAL_DATE | string | POSITION_CATEGORY_DETAIL_ON_APPROVAL_DATE |  |
| OFFICE_TYPE_ON_APPROVAL_DATE | string | OFFICE_TYPE_ON_APPROVAL_DATE |  |
| WORK_FORMAT_ON_APPROVAL_DATE | string | WORK_FORMAT_ON_APPROVAL_DATE |  |
| PERMANENT_TEMPORARY_ON_APPROVAL_DATE | string | PERMANENT_TEMPORARY_ON_APPROVAL_DATE |  |
| GROUP_AGE_ON_APPROVAL_DATE | string | GROUP_AGE_ON_APPROVAL_DATE |  |
| TENURE_ON_APPROVAL_DATE | string | TENURE_ON_APPROVAL_DATE |  |
| GENDER | string | GENDER |  |
| STATUS_ON_APPROVAL_DATE | string | STATUS_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_1_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_1_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_2_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_2_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_3_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_3_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_4_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_4_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_5_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_5_ON_APPROVAL_DATE |  |
| SUBDIVISION_LVL_6_ON_APPROVAL_DATE | string | SUBDIVISION_LVL_6_ON_APPROVAL_DATE |  |
| HRBP_ON_APPROVAL_DATE | string | HRBP_ON_APPROVAL_DATE |  |
| HEAD_ADMIN_ON_APPROVAL_DATE | string | HEAD_ADMIN_ON_APPROVAL_DATE |  |
| HRBP_ON_ASSESMENT_DATE | string | HRBP_ON_ASSESMENT_DATE |  |
| HEAD_ADMIN_ON_ASSESMENT_DATE | string | HEAD_ADMIN_ON_ASSESMENT_DATE |  |
| LOAD_TIMESTAMP | dateTime | LOAD_TIMESTAMP |  |
| OKR_AVG_RATE_WEIGHTED | double | OKR_AVG_RATE_WEIGHTED |  |
| CALC_PERFORMANCE_DESC_RATE_ORDER | string | CALC_PERFORMANCE_DESC_RATE_ORDER |  |
| OKR_COLOR_RATE_ORDER | string | OKR_COLOR_RATE_ORDER |  |
| OKR_DESCRIPTION_WRAPPED | string | OKR_DESCRIPTION_WRAPPED |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | OKR_OBJECTIVE_ID | `fact_OKR_Key_Results` | OKR_OBJECTIVE_ID |
| from | EXEC_DATE | `dim_Date` | Date |

## Пов'язані міри

Усього: **28**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 8

**Паспортна частина:** [PP.OKR.SVG.Last2Periods](../measures/pp-okr-svg-last2periods.md)

**Результативність та оцінка › OKR:** [PP.SVG.OKR.Загальна оцінка](../measures/pp-svg-okr-zahalna-otsinka.md)

**Результативність та оцінка › OKR.детально:** [PP.OKR.Ціль виконана](../measures/pp-okr-tsil-vykonana.md) · [PP.OKR.Ціль не виконана](../measures/pp-okr-tsil-ne-vykonana.md) · [PP.Частка KR за наявністю змін](../measures/pp-chastka-kr-za-naiavnistiu-zmin.md) · [PP.Частка OKR за кросфункційністю](../measures/pp-chastka-okr-za-krosfunktsiinistiu.md) · [PP.Частка OKR за наявністю змін](../measures/pp-chastka-okr-za-naiavnistiu-zmin.md) · [PP.Частка OKR за типом цілі](../measures/pp-chastka-okr-za-typom-tsili.md)

### [Group Profile](../report/group-profile.md) — 7

**Результативність та оцінка › Оцінка ОКР:** [GP.Результативність.Оцінка OKR.Загальна кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-py.md) · [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-cy.md) · [GP.Результативність.Оцінка OKR.Загальна кількість OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-py.md) · [GP.Результативність.Оцінка OKR.Кількість співробітників з OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-kilkist-spivrobitnykiv-z-okr-cy.md) · [GP.Результативність.Оцінка OKR.Середня кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-kr-py.md) · [GP.Результативність.Оцінка OKR.Середня кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-okr-cy.md) · [GP.Результативність.Оцінка OKR.Середня кількість OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-okr-py.md)

### Поза звітом / службові — 13

[GP.Результативність.Оцінка OKR.Кількість співробітників з OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-kilkist-spivrobitnykiv-z-okr-py.md) · [GP.Результативність.Оцінка OKR.Фільтр деталізації OKR](../measures/gp-rezultatyvnist-otsinka-okr-filtr-detalizatsii-okr.md) · [PP.OKR.Current_user.Загальна  оцінка OKR](../measures/pp-okr-current-user-zahalna-otsinka-okr.md) · [PP.OKR.Current_user.Загальна колірна оцінка OKR](../measures/pp-okr-current-user-zahalna-kolirna-otsinka-okr.md) · [PP.OKR.Current_user.Коефіцієнт індивідуального бонусу](../measures/pp-okr-current-user-koefitsiient-indyvidualnoho-bonusu.md) · [PP.OKR.Current_user.Статус плану](../measures/pp-okr-current-user-status-planu.md) · [PP.OKR.IsCurrentEmployee](../measures/pp-okr-iscurrentemployee.md) · [PP.OKR.Вага OKR](../measures/pp-okr-vaha-okr.md) · [PP.OKR.Загальна колірна оцінка OKR](../measures/pp-okr-zahalna-kolirna-otsinka-okr.md) · [PP.OKR.Загальна оцінка OKR](../measures/pp-okr-zahalna-otsinka-okr.md) · [PP.OKR.Значення OKR](../measures/pp-okr-znachennia-okr.md) · [PP.OKR.Колірна оцінка OKR](../measures/pp-okr-kolirna-otsinka-okr.md) · [PP.Частка OKR за статусом](../measures/pp-chastka-okr-za-statusom.md)

## Нотатки

_порожньо_
