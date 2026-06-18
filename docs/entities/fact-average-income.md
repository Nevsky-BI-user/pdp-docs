# fact_Average_Income

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Average_Income` |
| Джерела | `DM.vw_R27_fact_Average_Income` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| PREV_DIVISION_PERSON_ID | string | PREV_DIVISION_PERSON_ID |  |
| PREV_DIVISION_PERSON_NAME | string | PREV_DIVISION_PERSON_NAME |  |
| CURRENT_DIVISION_PERSON_ID | string | CURRENT_DIVISION_PERSON_ID |  |
| CURRENT_DIVISION_PERSON_NAME | string | CURRENT_DIVISION_PERSON_NAME |  |
| MONTLY_INCOME_WITH_BONUS | double | MONTLY_INCOME_WITH_BONUS |  |
| MONTLY_INCOME_WITHOUT_BONUS | double | MONTLY_INCOME_WITHOUT_BONUS |  |
| IS_INCLUDED_INTO_CALC | int64 | IS_INCLUDED_INTO_CALC |  |
| FTE_EMPLOYEE | double | FTE_EMPLOYEE |  |
| EMP_RECEIPT_DATE | dateTime | EMP_RECEIPT_DATE |  |
| EMP_DISMISSAL_DATE | dateTime | EMP_DISMISSAL_DATE |  |
| STATUS_KEY | string | STATUS_KEY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |

## Пов'язані міри

Усього: **2**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Group Profile](../report/group-profile.md) — 2

**TRS:** [GP.Середній дохід без річного бонуса (за ост. 12 міс)](../measures/gp-serednii-dokhid-bez-richnoho-bonusa-za-ost-12-mis.md) · [GP.Середній дохід з річним бонусом (за ост. 12 міс)](../measures/gp-serednii-dokhid-z-richnym-bonusom-za-ost-12-mis.md)

## Нотатки

_порожньо_
