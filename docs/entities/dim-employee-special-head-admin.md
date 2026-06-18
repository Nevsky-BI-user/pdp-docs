# dim_Employee_Special_Head_admin

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employee_Special_Head_admin` |
| Джерела | `DM.vw_R27_dim_Employee_Special_Head_Admin` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| EMP_ID | string | EMP_ID |  |
| EMP_POSITION_ID | string | EMP_POSITION_ID |  |
| EMP_UNIT_ID | string | EMP_UNIT_ID |  |
| EMP_ORGANIZATION_ID | string | EMP_ORGANIZATION_ID |  |
| EMP_HEAD_ADMIN_ID | string | EMP_HEAD_ADMIN_ID |  |
| EMP_HEAD_ADMIN_TAX | string | EMP_HEAD_ADMIN_TAX |  |
| EMP_HEAD_ADMIN_EMAIL | string | EMP_HEAD_ADMIN_EMAIL |  |
| EMP_HEAD_ADMIN_POSITION | string | EMP_HEAD_ADMIN_POSITION |  |
| EMP_HEAD_ADMIN_PERSONNEL_UNIT | string | EMP_HEAD_ADMIN_PERSONNEL_UNIT |  |
| EMP_HEAD_ADMIN_LAYER | string | EMP_HEAD_ADMIN_LAYER |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| JOB_TITLE_AMT | double | JOB_TITLE_AMT |  |
| EMPLOYEE_ADMIN_ID | string | EMPLOYEE_ADMIN_ID |  |
| DIVISION_ADMIN_ID | string | DIVISION_ADMIN_ID |  |
| JOB_TITLE_ADMIN_ID | string | JOB_TITLE_ADMIN_ID |  |
| STEP_ADMIN | int64 | STEP_ADMIN |  |
| EMPLOYEE_CODE | string | EMPLOYEE_CODE |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| DIVISION_CODE | string | DIVISION_CODE |  |
| DIVISION_NAME | string | DIVISION_NAME |  |
| JOB_TITLE_CODE | string | JOB_TITLE_CODE |  |
| JOB_TITLE_NAME | string | JOB_TITLE_NAME |  |
| EMPLOYEE_ADMIN_CODE | string | EMPLOYEE_ADMIN_CODE |  |
| EMPLOYEE_ADMIN_NAME | string | EMPLOYEE_ADMIN_NAME |  |
| DIVISION_ADMIN_CODE | string | DIVISION_ADMIN_CODE |  |
| DIVISION_ADMIN_NAME | string | DIVISION_ADMIN_NAME |  |
| JOB_TITLE_ADMIN_CODE | string | JOB_TITLE_ADMIN_CODE |  |
| JOB_TITLE_ADMIN_NAME | string | JOB_TITLE_ADMIN_NAME |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | EMP_HEAD_ADMIN_ID | `fact_Employee_List` | ID |

## Пов'язані міри

—

## Нотатки

_порожньо_
