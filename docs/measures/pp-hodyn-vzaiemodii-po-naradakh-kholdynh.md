# PP.Годин взаємодії по нарадах (Холдинг)

*тека `Personal_Profile\Viva\Viva Meetings`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Meetings` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR __val =
DIVIDE(
	SUM( 'fact_Viva_Metrics'[MEETING_HOUR] ),
	SUM( 'fact_Viva_Metrics'[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION] ))

RETURN __val
```

### Джерела даних


Колонки: `MEETING_HOUR`, `WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[MEETING_HOUR]`, `fact_Viva_Metrics[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION]`

### Схема

```mermaid
graph LR
  M["PP.Годин взаємодії по нарадах (Холдинг)"]
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

**Використовується в:** [PP.Годин взаємодії по нарадах (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kadrovyi-pidrozdil.md), [PP.Годин взаємодії по нарадах (напрям)](../measures/pp-hodyn-vzaiemodii-po-naradakh-napriam.md), [PP.Годин взаємодії по нарадах (співробітник)](../measures/pp-hodyn-vzaiemodii-po-naradakh-spivrobitnyk.md)

## Нотатки

_порожньо_
