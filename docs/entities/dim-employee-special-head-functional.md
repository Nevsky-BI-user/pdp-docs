# dim_Employee_Special_Head_functional

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employee_Special_Head_functional` |
| Джерела | `DM.vw_R27_dim_Employee_Special_Head_Functional` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| EMP_ID | string | EMP_ID |  |
| EMP_POSITION_ID | string | EMP_POSITION_ID |  |
| EMP_UNIT_ID | string | EMP_UNIT_ID |  |
| EMP_ORGANIZATION_ID | string | EMP_ORGANIZATION_ID |  |
| EMP_HEAD_FUNCTIONAL_ID | string | EMP_HEAD_FUNCTIONAL_ID |  |
| EMP_HEAD_FUNCTIONAL_TAX | string | EMP_HEAD_FUNCTIONAL_TAX |  |
| EMP_HEAD_FUNCTIONAL_EMAIL | string | EMP_HEAD_FUNCTIONAL_EMAIL |  |
| EMP_HEAD_FUNCTIONAL_POSITION | string | EMP_HEAD_FUNCTIONAL_POSITION |  |
| EMP_HEAD_FUNCTIONAL_PERSONNEL_UNIT | string | EMP_HEAD_FUNCTIONAL_PERSONNEL_UNIT |  |
| EMP_HEAD_FUNCTIONAL_LAYER | string | EMP_HEAD_FUNCTIONAL_LAYER |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| JOB_TITLE_AMT | double | JOB_TITLE_AMT |  |
| EMPLOYEE_FUNC_ID | string | EMPLOYEE_FUNC_ID |  |
| DIVISION_FUNC_ID | string | DIVISION_FUNC_ID |  |
| JOB_TITLE_FUNC_ID | string | JOB_TITLE_FUNC_ID |  |
| STEP_FUNC | int64 | STEP_FUNC |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | EMP_HEAD_FUNCTIONAL_ID | `fact_Employee_List` | ID |

## Пов'язані міри

—

## Нотатки

_порожньо_
