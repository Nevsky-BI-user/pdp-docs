# dim_Employee_Special_FinBP

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employee_Special_FinBP` |
| Джерела | `DM.vw_R27_dim_Employee_Special_Head_FinBP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| EMP_ID | string | EMP_ID |  |
| EMP_POSITION_ID | string | EMP_POSITION_ID |  |
| EMP_UNIT_ID | string | EMP_UNIT_ID |  |
| EMP_ORGANIZATION_ID | string | EMP_ORGANIZATION_ID |  |
| EMP_FINBP_ID | string | EMP_FINBP_ID |  |
| EMP_FINBP_TAX | string | EMP_FINBP_TAX |  |
| EMP_FINBP_EMAIL | string | EMP_FINBP_EMAIL |  |
| EMP_FINBP_POSITION | string | EMP_FINBP_POSITION |  |
| EMP_FINBP_PERSONNEL_UNIT | string | EMP_FINBP_PERSONNEL_UNIT |  |
| EMP_FINBP_LAYER | string | EMP_FINBP_LAYER |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| JOB_TITLE_AMT | double | JOB_TITLE_AMT |  |
| EMPLOYEE_FINBP_ID | string | EMPLOYEE_FINBP_ID |  |
| DIVISION_FINBP_ID | string | DIVISION_FINBP_ID |  |
| JOB_TITLE_FINBP_ID | string | JOB_TITLE_FINBP_ID |  |
| STEP_FINBP | int64 | STEP_FINBP |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | EMP_HEAD_FUNCTIONAL_ID | `fact_Employee_List` | ID |

## Пов'язані міри

—

## Нотатки

_порожньо_
