# PP.Розмір мережі (Холдинг, 3м)

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
//     CALCULATE( 
//         [PP.Розмір мережі (співробітник, 3м)], 
//         REMOVEFILTERS( fact_Metrics )
//     ) 

VAR __val =
DIVIDE(
		SUM('fact_Viva_Metrics'[INTERNAL_NETWORK_SIZE]),
		CALCULATE(COUNTROWS('fact_Viva_Metrics'), NOT ISBLANK('fact_Viva_Metrics'[INTERNAL_NETWORK_SIZE])))

RETURN __val
```

### Джерела даних


Колонки: `INTERNAL_NETWORK_SIZE`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[INTERNAL_NETWORK_SIZE]`

### Схема

```mermaid
graph LR
  M["PP.Розмір мережі (Холдинг, 3м)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — VIVA › Viva
- [Group Profile](../report/group-profile.md) — Viva

## Пов'язані міри

**Використовує:** [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md)

**Використовується в:** [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md), [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md), [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md)

## Нотатки

_порожньо_
