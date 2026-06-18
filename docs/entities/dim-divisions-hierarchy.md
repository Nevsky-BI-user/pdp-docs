# dim_Divisions_Hierarchy

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Divisions_Hierarchy` |
| Джерела | `DM.vw_R27_dim_Divisions_Hierarchy` |

**Вимоги:** `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/Додаткові-вимоги-до-вітрини-Плинність`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| division_id | string | division_id |  |
| division_name | string | division_name |  |
| parent_division_id | string | parent_division_id |  |
| parent_division_name | string | parent_division_name |  |
| Organization_ID | string | Organization_ID |  |
| Organization_name | string | Organization_name |  |
| Org_Div_Parent_Key | string | Org_Div_Parent_Key |  |
| division_hierarchy_list | string | division_hierarchy_list |  |

## Зв'язки

—

## Пов'язані міри

—

## Нотатки

_порожньо_
