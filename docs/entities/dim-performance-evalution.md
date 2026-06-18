# dim_Performance_Evalution

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `dim_Performance_Evalution` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| General_Performance_Str_Rate | string | General_Performance_Str_Rate |  |
| order_General_Performance_Desc_Rate | int64 | order_General_Performance_Desc_Rate |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | General_Performance_Str_Rate | `fact_Employee_Performance_Total` | General_Performance_Str_Rate |
| to | General_Performance_Str_Rate | `fact_Gaussian_Curve_Performance` | General_Performance_Str_Rate |
| to | GENERAL_PERFORMANCE_STR_RATE | `fact_Employee_Performance` | General_Performance_Str_Rate |

## Пов'язані міри

Усього: 1.
- [GP.Продуктивність.SVG.Bar chart](../measures/gp-produktyvnist-svg-bar-chart.md)

## Нотатки

_порожньо_
