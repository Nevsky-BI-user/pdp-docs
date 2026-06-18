# fact_Employees_Attributes

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employees_Attributes` |
| Джерела | `DM.vw_R27_fact_Employees_Attributes` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| STATUS_KEY | string | STATUS_KEY |  |
| EMPLOYEE_STATUS | string | EMPLOYEE_STATUS |  |
| POSITION_COMPOSITE | string | POSITION_COMPOSITE |  |
| REPLACED_EMPLOYEE | string | REPLACED_EMPLOYEE |  |
| WORK_SCHEDULE | string | WORK_SCHEDULE |  |
| WORK_SCHEDULE_CLARIFIED | string | WORK_SCHEDULE_CLARIFIED |  |
| MILITARY_SERVICE_PLACE | string | MILITARY_SERVICE_PLACE |  |
| EMPLOYEE_MILITARY_BP | string | EMPLOYEE_MILITARY_BP |  |
| DIVISION_PERSON_PART_TIME_ID | string | DIVISION_PERSON_PART_TIME_ID |  |
| DIVISION_PERSON_PART_TIME | string | DIVISION_PERSON_PART_TIME |  |
| JOB_TITLE_PART_TIME_ID | string | JOB_TITLE_PART_TIME_ID |  |
| JOB_TITLE_PART_TIME | string | JOB_TITLE_PART_TIME |  |
| JOB_TITLE_PART_TIME_AMT | double | JOB_TITLE_PART_TIME_AMT |  |
| PART_TIME_PERIOD | int64 | PART_TIME_PERIOD |  |
| PART_TIME_PAYMENT_SIZE | double | PART_TIME_PAYMENT_SIZE |  |
| CATEGORY_MACHINE_OPERATOR | string | CATEGORY_MACHINE_OPERATOR |  |
| WORK_SHIFT | string | WORK_SHIFT |  |
| EMPLOYMENT_TERM | dateTime | EMPLOYMENT_TERM |  |
| JOB_TITLE_COMPOSITE_VEHICLE_FORMAT | string | JOB_TITLE_COMPOSITE_VEHICLE_FORMAT |  |
| EMLOYEE_VEHICLE_FORMAT | string | EMLOYEE_VEHICLE_FORMAT |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |

## Пов'язані міри

Усього: 3.
- [GP.Опція по авто, % план.SVG](../measures/gp-optsiia-po-avto-plan-svg.md)
- [GP.Опція по авто, % факт.SVG](../measures/gp-optsiia-po-avto-fakt-svg.md)
- [PP.Тип опції по авто](../measures/pp-typ-optsii-po-avto.md)

## Нотатки

_порожньо_
