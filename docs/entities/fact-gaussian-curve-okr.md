# fact_Gaussian_Curve_OKR

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Gaussian_Curve_OKR` |
| Джерела | `DM.R27_fact_OKR_Goals` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| CALC_PERFORMANCE_DESC_RATE | string | CALC_PERFORMANCE_DESC_RATE |  |
| EMPLOYEE_COUNT | int64 | EMPLOYEE_COUNT |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | CALC_PERFORMANCE_DESC_RATE | `dim_OKR_Evalution` | CALC_PERFORMANCE_DESC_RATE |

## Пов'язані міри

Усього: **1**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Group Profile](../report/group-profile.md) — 1

**Інші візуали:** [GP.OKR.SVG.Bar chart](../measures/gp-okr-svg-bar-chart.md)

## Нотатки

_порожньо_
