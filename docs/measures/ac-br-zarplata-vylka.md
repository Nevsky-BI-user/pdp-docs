# AC.BR.Зарплата вилка

*тека `Analytical Cases\Burnout_Risk\Export`*

## Бізнес-суть

SALARY_RANGE → Зарплата (вилки)

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

[Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Burnout_Indicators'[SALARY_RANGE])
```

### Джерела даних


Колонки: `SALARY_RANGE`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[SALARY_RANGE]`

### Схема

```mermaid
graph LR
  M["AC.BR.Зарплата вилка"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

## Нотатки

_порожньо_
