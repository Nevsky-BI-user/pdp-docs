# PP.Годин для фокусної роботи (Холдинг)

*тека `Personal_Profile\Viva\Viva Collaboration`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Collaboration` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR __val =
DIVIDE(
	SUM( 'fact_Viva_Metrics'[UNINTERRUPTED_HOUR]),
	SUM( 'fact_Viva_Metrics'[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION])
)

RETURN __val
```

### Джерела даних


Колонки: `UNINTERRUPTED_HOUR`, `WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[UNINTERRUPTED_HOUR]`, `fact_Viva_Metrics[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION]`

### Схема

```mermaid
graph LR
  M["PP.Годин для фокусної роботи (Холдинг)"]
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

**Використовується в:** [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md), [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md), [PP.Годин для фокусної роботи (співробітник)](../measures/pp-hodyn-dlia-fokusnoi-roboty-spivrobitnyk.md)

## Нотатки

_порожньо_
