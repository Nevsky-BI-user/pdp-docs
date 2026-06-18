# AC.BR.Зарплата вилка

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
SELECTEDVALUE('fact_Burnout_Indicators'[SALARY_RANGE])
```

## Джерела


Колонки: `SALARY_RANGE`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

SALARY_RANGE → Зарплата (вилки)

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[SALARY_RANGE]`

## Схема

```mermaid
graph LR
  M["AC.BR.Зарплата вилка"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
