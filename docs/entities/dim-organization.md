# dim_Organization

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Organization` |
| Джерела | `DM.vw_R27_dim_Organization` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Індивідуальний-профіль-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Паспортна-частина-групового-профілю/Метрики-рекрутингу/ТЗ-на-розробку-вітрин-по-метрикам-рекрутингу`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| ORGANIZATION_CODE | string | ORGANIZATION_CODE |  |
| ORGANIZATION | string | ORGANIZATION |  |
| ORGANIZATION_PARENT | string | ORGANIZATION_PARENT |  |
| ORGANIZATION_DIRECTION | string | ORGANIZATION_DIRECTION |  |
| ORGANIZATION_SECTOR | string | ORGANIZATION_SECTOR |  |
| ORGANIZATION_SEGMENT | string | ORGANIZATION_SEGMENT |  |
| EDRPOU | string | EDRPOU |  |
| IS_GREEN | boolean | IS_GREEN |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | ORGANIZATION_KEY | `fact_Employee_List` | ORGANIZATION_KEY |
| to | ORGANIZATION_ID | `fact_Burnout_Indicators` | ORGANIZATION_KEY |
| to | ORGANIZATION_ID | `fact_Loss_of_Productivity` | ORGANIZATION_KEY |

## Пов'язані міри

—

## Нотатки

_порожньо_
