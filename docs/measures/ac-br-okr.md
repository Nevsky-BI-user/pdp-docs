# AC.BR.OKR

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SELECTEDVALUE('fact_Burnout_Indicators'[OKR_RATE_TREND])
```

## Джерела


Колонки: `OKR_RATE_TREND`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

OKR_RATE_TREND → Тренд ОКР; OKR_RATE_TREND → Тренд оцінки OKR

Зміна джерела даних

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників/Деталізація-метрик-в-кейсі-Продуктивність`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[OKR_RATE_TREND]`

## Схема

```mermaid
graph LR
  M["AC.BR.OKR"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
