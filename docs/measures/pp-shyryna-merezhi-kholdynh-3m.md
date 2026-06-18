# PP.Ширина мережі (Холдинг, 3м)

*тека `Personal_Profile\Viva\Viva Networks`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Networks` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
// VAR __val =
// CALCULATE(
//     [PP.Ширина мережі (співробітник, 3м)],
//     REMOVEFILTERS(fact_Metrics))

VAR __val =
DIVIDE(
		SUM('fact_Viva_Metrics'[NETWORK_OUTSIDE_ORGANIZATION]),
		CALCULATE(COUNTROWS('fact_Viva_Metrics'), NOT ISBLANK('fact_Viva_Metrics'[NETWORK_OUTSIDE_ORGANIZATION])))

RETURN __val
```

### Джерела даних


Колонки: `NETWORK_OUTSIDE_ORGANIZATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[NETWORK_OUTSIDE_ORGANIZATION]`

### Схема

```mermaid
graph LR
  M["PP.Ширина мережі (Холдинг, 3м)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

**Використовується в:** [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md), [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md), [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

## Нотатки

_порожньо_
