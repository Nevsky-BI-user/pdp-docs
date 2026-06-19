# fact_Employee_OKR

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employee_OKR` |
| Джерела | `DM.R27_fact_OKR_Goals` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Змінити-логіку-визначення-окремих-полів-у-вітрині`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| PLAN_YEAR | int64 | PLAN_YEAR |  |
| CALC_PERFORMANCE_STR_RATE | double | CALC_PERFORMANCE_STR_RATE |  |
| CALC_PERFORMANCE_DESC_RATE | string | CALC_PERFORMANCE_DESC_RATE |  |
| order | int64 | order |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | CALC_PERFORMANCE_DESC_RATE | `dim_OKR_Evalution` | CALC_PERFORMANCE_DESC_RATE |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |

## Пов'язані міри

Усього: **4**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### Поза звітом / службові — 4

[GP.ОКР.Кількість співробітників (Останній період оцінки)](../measures/gp-okr-kilkist-spivrobitnykiv-ostannii-period-otsinky.md) · [GP.ОКР.Останній рік](../measures/gp-okr-ostannii-rik.md) · [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md) · [GP.ОКР.Середня оцінка команди.Значення](../measures/gp-okr-serednia-otsinka-komandy-znachennia.md)

## Нотатки

_порожньо_
