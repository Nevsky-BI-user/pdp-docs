# dim_Permanent_Temporary

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Permanent_Temporary` |
| Джерела | `DM.vw_R27_dim_Permanent_Temporary` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| PERMANENT_TEMPORARY_DETAILS_KEY | string | PERMANENT_TEMPORARY_DETAILS_KEY |  |
| CODE | string | CODE |  |
| NAME | string | NAME |  |
| SORT_NUM | int64 | SORT_NUM |  |
| PERMANENT_TEMPORARY | string | PERMANENT_TEMPORARY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | PERMANENT_TEMPORARY_DETAILS_ID | `fact_Employee_List` | PERMANENT_TEMPORARY_DETAILS_KEY |

## Пов'язані міри

Усього: 1.
- [PP.Трудові умови](../measures/pp-trudovi-umovy.md)

## Нотатки

_порожньо_
