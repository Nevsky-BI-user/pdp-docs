# fact_Repayment_Credit

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Repayment_Credit` |
| Джерела | `DM.vw_R27_fact_Repayment_Credit_PDP` |

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERSON_KEY | string | PERSON_KEY |  |
| CONTRACT_KEY | string | CONTRACT_KEY |  |
| BUDGET_ITEM_LOAN_ID | string | BUDGET_ITEM_LOAN_ID |  |
| PERSON_NAME | string | PERSON_NAME |  |
| CONTRACT_NAME | string | CONTRACT_NAME |  |
| BUDGET_ITEM_CODE | string | BUDGET_ITEM_CODE |  |
| IS_INCOMING | boolean | IS_INCOMING |  |
| ACTION_START_DATE | dateTime | ACTION_START_DATE |  |
| ACTION_END_DATE | dateTime | ACTION_END_DATE |  |
| BASE_DEBT_SUM | double | BASE_DEBT_SUM |  |
| PERCENT_SUM | double | PERCENT_SUM |  |
| LAND_SHARE_CONTRACT_SUM | double | LAND_SHARE_CONTRACT_SUM |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| BUDGET_ITEM_NAME | string | BUDGET_ITEM_NAME |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | PERSON_KEY | `dim_Person` | PERSON_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: 7.
- [GP.Доля команди з позикою на ноутбук (%) (діюча)](../measures/gp-dolia-komandy-z-pozykoiu-na-noutbuk-diiucha.md)
- [GP.Доля команди із позиками](../measures/gp-dolia-komandy-iz-pozykamy.md)
- [GP.К-ть співробітників, що отримали позику на ноутбук (діюча)](../measures/gp-k-t-spivrobitnykiv-shcho-otrymaly-pozyku-na-noutbuk-diiucha.md)
- [GP.Середній розмір позики](../measures/gp-serednii-rozmir-pozyky.md)
- [PP.Дата доступності позики на ноутбук](../measures/pp-data-dostupnosti-pozyky-na-noutbuk.md)
- [PP.Позика (активна).Сума](../measures/pp-pozyka-aktyvna-suma.md)
- [PP.Позика на ноутбук](../measures/pp-pozyka-na-noutbuk.md)

## Нотатки

_порожньо_
