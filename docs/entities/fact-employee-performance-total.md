# fact_Employee_Performance_Total

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employee_Performance_Total` |
| Джерела | `DM.vw_R27_fact_Employee_Performance_General_PBI` |

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| General_Performance_Str_Rate | string | General_Performance_Str_Rate |  |
| General_Performance_Desc_Rate | double | General_Performance_Desc_Rate |  |
| Performance_Year | int64 | Performance_Year |  |
| Performance_Type | string | Performance_Type |  |
| General_Self_Rate | double | General_Self_Rate |  |
| DIRECTION | string | DIRECTION |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| POSITION_NAME | string | POSITION_NAME |  |
| EMPLOYEE_MANAGER_NAME | string | EMPLOYEE_MANAGER_NAME |  |
| PERFORMENCE_PERIOD | string | PERFORMENCE_PERIOD |  |
| PERFORMANCE_PBI_ORDER | int64 | PERFORMANCE_PBI_ORDER |  |
| ORDER | int64 | ORDER |  |
| PERFORMANCE_STATUS | string | PERFORMANCE_STATUS |  |
| PERFORMANCE_AMPLITUDE | string | PERFORMANCE_AMPLITUDE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| DATE_ID | dateTime | DATE_ID |  |
| General_Self_Str_Rate | string | General_Self_Str_Rate |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | General_Performance_Str_Rate | `dim_Performance_Evalution` | General_Performance_Str_Rate |
| from | EMPLOYEE_ID | `dim_Person` | PERSON_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | DATE_ID | `dim_Date` | Date |

## Пов'язані міри

Усього: **9**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 1

**Результативність та оцінка › Результативність:** [PP.SVG.Оцінка результативності.Total](../measures/pp-svg-otsinka-rezultatyvnosti-total.md)

### [Group Profile](../report/group-profile.md) — 3

**Версія 2 › Індикатори здоров'я команди:** [GP.Продуктивність.Середня оцінка команди.Значення](../measures/gp-produktyvnist-serednia-otsinka-komandy-znachennia.md)

**Результативність та оцінка › Оцінка результативності › Оцінка керівника та самооцінка:** [GP.Результативність.Оцінка результативності.К-ть працівників.Total](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-k-t-pratsivnykiv-total.md)

**Результативність та оцінка › Траекторія результативності:** [GP.Результативність.Оцінка результативності.Середня оцінка.Total](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-serednia-otsinka-total.md)

### Поза звітом / службові — 5

[GP.Продуктивність.Кількість співробітників (Останній період оцінки)](../measures/gp-produktyvnist-kilkist-spivrobitnykiv-ostannii-period-otsinky.md) · [GP.Продуктивність.Останній період оцінки](../measures/gp-produktyvnist-ostannii-period-otsinky.md) · [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md) · [PP.Оцінка результативності.Керівником.Total](../measures/pp-otsinka-rezultatyvnosti-kerivnykom-total.md) · [PP.Оцінка результативності.Самооцінка.Total](../measures/pp-otsinka-rezultatyvnosti-samootsinka-total.md)

## Нотатки

_порожньо_
