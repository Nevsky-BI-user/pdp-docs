# dim_Employee_Special_HRBP

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Employee_Special_HRBP` |
| Джерела | `DM.vw_R27_dim_Employee_Special_Head_HRBP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| EMP_ID | string | EMP_ID |  |
| EMP_POSITION_ID | string | EMP_POSITION_ID |  |
| EMP_UNIT_ID | string | EMP_UNIT_ID |  |
| EMP_ORGANIZATION_ID | string | EMP_ORGANIZATION_ID |  |
| EMP_HRBP_ID | string | EMP_HRBP_ID |  |
| EMP_HRBP_TAX | string | EMP_HRBP_TAX |  |
| EMP_HRBP_EMAIL | string | EMP_HRBP_EMAIL |  |
| EMP_HRBP_POSITION | string | EMP_HRBP_POSITION |  |
| EMP_HRBP_PERSONNEL_UNIT | string | EMP_HRBP_PERSONNEL_UNIT |  |
| EMP_HRBP_LAYER | string | EMP_HRBP_LAYER |  |
| CALC_DATE | dateTime | CALC_DATE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| JOB_TITLE_AMT | double | JOB_TITLE_AMT |  |
| EMPLOYEE_HRBP_ID | string | EMPLOYEE_HRBP_ID |  |
| DIVISION_HRBP_ID | string | DIVISION_HRBP_ID |  |
| JOB_TITLE_HRBP_ID | string | JOB_TITLE_HRBP_ID |  |
| STEP_HRBP | int64 | STEP_HRBP |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | EMP_HRBP_ID | `fact_Employee_List` | ID |

## Пов'язані міри

—

## Нотатки

_порожньо_
