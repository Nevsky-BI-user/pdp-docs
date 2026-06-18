# fact_Gaussian_Curve_Performance

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Gaussian_Curve_Performance` |
| Джерела | `DM.R27_fact_Employee_Performance` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам/Змінити-джерело-даних-для-полів-із-оцінкою-результативності`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/ТЗ.-Метрика-Небажана-плинність-(regretted-atrition-ratio)`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| General_Performance_Str_Rate | string | General_Performance_Str_Rate |  |
| EMPLOYEE_COUNT | int64 | EMPLOYEE_COUNT |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | General_Performance_Str_Rate | `dim_Performance_Evalution` | General_Performance_Str_Rate |

## Пов'язані міри

Усього: 1.
- [GP.Продуктивність.SVG.Bar chart](../measures/gp-produktyvnist-svg-bar-chart.md)

## Нотатки

_порожньо_
