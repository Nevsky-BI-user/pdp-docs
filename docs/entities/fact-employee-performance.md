# fact_Employee_Performance

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employee_Performance` |
| Джерела | `DM.vw_R27_fact_Employee_Performance_PBI` |

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| DIRECTION | string | DIRECTION |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| POSITION_NAME | string | POSITION_NAME |  |
| EMPLOYEE_MANAGER_NAME | string | EMPLOYEE_MANAGER_NAME |  |
| COMPETENCY_NAME | string | COMPETENCY_NAME |  |
| SALF_RATE | double | SALF_RATE |  |
| OFFICIAL_RATE | double | OFFICIAL_RATE |  |
| PERFORMANCE_YEAR | int64 | PERFORMANCE_YEAR |  |
| PERFORMANCE_TYPE | string | PERFORMANCE_TYPE |  |
| PERFORMENCE_PERIOD | string | PERFORMENCE_PERIOD |  |
| PERFORMANCE_PBI_ORDER | int64 | PERFORMANCE_PBI_ORDER |  |
| ORDER | int64 | ORDER |  |
| GENERAL_PERFORMANCE_STR_RATE | string | GENERAL_PERFORMANCE_STR_RATE |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | GENERAL_PERFORMANCE_STR_RATE | `dim_Performance_Evalution` | General_Performance_Str_Rate |

## Пов'язані міри

Усього: **15**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 1

**Результативність та оцінка › Результативність:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Ініціативність при виконанні завдань:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Автономність при виконанні завдань:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Виконання завдань у встановлені терміни:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Відповідність кількості виконаних завдань функціоналу:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Націленість на отримання результату:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Подолання перешкод при вирішенні проблем:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Прийняття відповідальності за отриманий результат:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

**Результативність та оцінка › Результативність.Детально › Якість результату виконаних завдань:** [PP.SVG.Оцінка результативності](../measures/pp-svg-otsinka-rezultatyvnosti.md)

### [Group Profile](../report/group-profile.md) — 1

**Результативність та оцінка › Оцінка результативності › Результативність.Детально:** [GP.Результативність.Оцінка результативності.К-ть працівників](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-k-t-pratsivnykiv.md)

### Поза звітом / службові — 13

[GP.Результативність.Оцінка результативності.Середня оцінка](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-serednia-otsinka.md) · [PP.Ініціативність при виконанні завдань](../measures/pp-initsiatyvnist-pry-vykonanni-zavdan.md) · [PP.Автономність при виконанні завдань](../measures/pp-avtonomnist-pry-vykonanni-zavdan.md) · [PP.Виконання завдань у встановлені терміни](../measures/pp-vykonannia-zavdan-u-vstanovleni-terminy.md) · [PP.Відповідність кількості виконаних завдань функціоналу](../measures/pp-vidpovidnist-kilkosti-vykonanykh-zavdan-funktsionalu.md) · [PP.Націленість на отримання результату](../measures/pp-natsilenist-na-otrymannia-rezultatu.md) · [PP.Оцінка результативності базова](../measures/pp-otsinka-rezultatyvnosti-bazova.md) · [PP.Оцінка результативності.Керівником](../measures/pp-otsinka-rezultatyvnosti-kerivnykom.md) · [PP.Оцінка результативності.Самооцінка](../measures/pp-otsinka-rezultatyvnosti-samootsinka.md) · [PP.Подолання перешкод при вирішенні проблем](../measures/pp-podolannia-pereshkod-pry-vyrishenni-problem.md) · [PP.Прийняття відповідальності за отриманий результат](../measures/pp-pryiniattia-vidpovidalnosti-za-otrymanyi-rezultat.md) · [PP.Середня оцінка результативності річна](../measures/pp-serednia-otsinka-rezultatyvnosti-richna.md) · [PP.Якість результату виконаних завдань](../measures/pp-iakist-rezultatu-vykonanykh-zavdan.md)

## Нотатки

_порожньо_
