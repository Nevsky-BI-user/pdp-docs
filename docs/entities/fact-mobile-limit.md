# fact_Mobile_Limit

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Mobile_Limit` |
| Джерела | `DM.vw_R27_fact_Mobile_Limit_PDP` |

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERSON_KEY | string | PERSON_KEY |  |
| PHONE_NUMBER_KEY | string | PHONE_NUMBER_KEY |  |
| PHONE_PACKAGE_KEY | string | PHONE_PACKAGE_KEY |  |
| PHONE_CORP_LIMIT_KEY | string | PHONE_CORP_LIMIT_KEY |  |
| PHONE_NUMBER_PURPOSE_KEY | string | PHONE_NUMBER_PURPOSE_KEY |  |
| PERSON_NAME | string | PERSON_NAME |  |
| PHONE_PACKAGE_NAME | string | PHONE_PACKAGE_NAME |  |
| PHONE_CORP_LIMIT_CODE | string | PHONE_CORP_LIMIT_CODE |  |
| PHONE_CORP_LIMIT_NAME | string | PHONE_CORP_LIMIT_NAME |  |
| PHONE_CORP_LIMIT | int64 | PHONE_CORP_LIMIT |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | PERSON_KEY | `dim_Person` | PERSON_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: **5**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Group Profile](../report/group-profile.md) — 2

**TRS:** [GP.К-ть співробітників, що отримують виплати на мобільний зв’язок](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-mobilnyi-zviazok.md) · [GP.Середні витрати на мобільний зв’язок](../measures/gp-seredni-vytraty-na-mobilnyi-zviazok.md)

### Поза звітом / службові — 3

['GP.Мобільний зв''язок, % факт.SVG'](../measures/gp-mobilnyi-zviazok-fakt-svg.md) · ['PP.Мобільний зв''язок - Корпоративний ліміт'](../measures/pp-mobilnyi-zviazok-korporatyvnyi-limit.md) · ['PP.Мобільний зв''язок - Назва пакету'](../measures/pp-mobilnyi-zviazok-nazva-paketu.md)

## Нотатки

_порожньо_
