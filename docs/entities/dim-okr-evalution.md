# dim_OKR_Evalution

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `dim_OKR_Evalution` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| CALC_PERFORMANCE_DESC_RATE | string | CALC_PERFORMANCE_DESC_RATE |  |
| ORDER | string | ORDER |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | CALC_PERFORMANCE_DESC_RATE | `fact_Employee_OKR` | CALC_PERFORMANCE_DESC_RATE |
| to | CALC_PERFORMANCE_DESC_RATE | `fact_Gaussian_Curve_OKR` | CALC_PERFORMANCE_DESC_RATE |

## Пов'язані міри

Усього: 1.
- [GP.OKR.SVG.Bar chart](../measures/gp-okr-svg-bar-chart.md)

## Нотатки

_порожньо_
